import csv
from collections import defaultdict
import numpy as np
from typing import Dict, List

from NeighborCalculator import NeighborCalculator
import itertools
from itertools import product, combinations
import math, time, sys
import random
import concurrent.futures

class FilterTestStimuli:
    def __init__(self, csv_path: str):
        self.phoneme_groups = defaultdict(list)
        self.global_frequencies = []
        self.global_densities = []

        with open(csv_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                phoneme = row['TestedPhoneme']
                entry = {
                    'word': row['Word'],
                    'frequency': float(row['Frequency']),
                    'density': float(row["NeighborhoodDensity"]),
                    'TestedPhoneme': row['TestedPhoneme'],
                    'transcription': tuple(row['ARPAbetTranscription'].split()),
                }
                self.phoneme_groups[phoneme].append(entry)
                self.global_frequencies.append(entry['frequency'])
                self.global_densities.append(entry['density'])

        # Calculate global z-scores for normalization
        self.freq_mean = np.mean(self.global_frequencies)
        self.freq_std = np.std(self.global_frequencies)
        self.dens_mean = np.mean(self.global_densities)
        self.dens_std = np.std(self.global_densities)

    def get_candidate_generators(self, size: int, max_items=100):
        """
        Instead of generating all permutations for each phoneme group at once,
        store the truncated list of phonemes along with the desired combination size.
        Each entry in the returned list is a tuple: (phoneme_list, size).
        """
        candidate_generators = []
        for key in self.phoneme_groups.keys():
            phonemes = self.phoneme_groups[key]
            # Convert each entry's values into a list
            phonemes = [list(item.values()) for item in phonemes]
            # Join the transcription tuple into a single string
            for item in phonemes:
                item[-1] = " ".join(item[-1])
            # Truncate to max_items and convert each entry to a tuple
            phonemes = [tuple(item) for item in phonemes[:min(max_items, len(phonemes))]]
            candidate_generators.append((phonemes, size))
        return candidate_generators

    def generate_candidate_for_group(self, phoneme_list, size):
        """
        Randomly generate one candidate combination for a phoneme group.
        Instead of precomputing all combinations, we randomly sample `size` items.
        Now, also compute the standard deviation (sd) for both probability and density.
        """
        # Randomly select a combination of items
        combination = tuple(random.sample(phoneme_list, size))

        # Multiply probability by 10**6 (1 million)
        prob_values = [item[1] * 10 ** 6 for item in combination]
        density_values = [item[2] for item in combination]

        total_probability = sum(prob_values)
        total_density = sum(density_values)

        # Calculate standard deviation using numpy
        sd_probability = np.std(prob_values)
        sd_density = np.std(density_values)

        return {
            "total_probability": total_probability,
            "total_density": total_density,
            "sd_probability": sd_probability,
            "sd_density": sd_density,
            "combination": combination
        }

    def calculate_average_distance_between_items(self, items) -> float:
        """
        Calculates the average Euclidean distance between all pairs of items.
        Each item is expected to be a dictionary with keys:
        - 'total_probability'
        - 'total_density'
        - 'sd_probability'
        - 'sd_density'

        The Euclidean distance now takes into account the standard deviations.
        """
        if len(items) < 2:
            return 0.0

        total_distance = 0
        count = 0

        for item1, item2 in combinations(items, 2):
            p1, d1, sd_p1, sd_d1 = item1["total_probability"], item1["total_density"], item1["sd_probability"], item1[
                "sd_density"]
            p2, d2, sd_p2, sd_d2 = item2["total_probability"], item2["total_density"], item2["sd_probability"], item2[
                "sd_density"]

            # Compute Euclidean distance incorporating standard deviations
            distance = math.sqrt((p1 - p2) ** 2 + ((d1 - d2)/5) ** 2 + ((sd_p1 - sd_p2)/20)** 2 + ((sd_d1 - sd_d2)/20) ** 2)
            distance += (math.log((sd_p1 + sd_p2)+1) + math.log(sd_d1 + sd_d2+1))/100
            distance +=-1/10*math.log(p1 + p2)
            total_distance += distance
            count += 1

        return total_distance / count if count > 0 else 0.0

    def simulated_annealing(self, candidate_generators,
                            initial_temperature=1000,
                            cooling_rate=0.95,
                            iterations=100000,
                            calc_distance_fn=None):
        """
        Uses simulated annealing to search for a near-optimal combination.
        Instead of using precomputed candidates, this method generates a new candidate
        for a given group on the fly.
        """
        if calc_distance_fn is None:
            raise ValueError("A function to calculate the average distance must be provided.")

        # Start with a random candidate (one per phoneme group)
        current_solution = [self.generate_candidate_for_group(phonemes, size)
                            for phonemes, size in candidate_generators]
        current_score = calc_distance_fn(current_solution)
        best_solution = current_solution.copy()
        best_score = current_score
        temperature = initial_temperature

        for i in range(iterations):
            # Copy the current solution and perturb one randomly chosen group
            new_solution = current_solution.copy()
            subset_idx = random.randint(0, len(candidate_generators) - 1)
            phonemes, size = candidate_generators[subset_idx]
            new_solution[subset_idx] = self.generate_candidate_for_group(phonemes, size)
            new_score = calc_distance_fn(new_solution)

            # Accept the new solution if it improves or probabilistically if not
            if new_score < current_score or random.random() < math.exp((current_score - new_score) / temperature):
                current_solution = new_solution
                current_score = new_score
                if new_score < best_score:
                    best_solution = new_solution.copy()
                    best_score = new_score

            temperature *= cooling_rate

        print("Simulated annealing best average distance:", best_score)
        return best_solution, best_score

    def beam_search(self, candidate_generators,
                    beam_width=20,
                    iterations=10000,
                    calc_distance_fn=None,
                    num_threads=16):
        """
        Uses beam search with multithreading to find a near-optimal combination.
        Candidates are generated on the fly for each phoneme group.
        """
        if calc_distance_fn is None:
            raise ValueError("A function to calculate the average distance must be provided.")

        # Initialize the beam with random candidate solutions.
        beam = []
        for _ in range(beam_width):
            sol = [self.generate_candidate_for_group(phonemes, size)
                   for phonemes, size in candidate_generators]
            score = calc_distance_fn(sol)
            beam.append((score, sol))
        beam.sort(key=lambda x: x[0])
        best_score, best_solution = beam[0]

        for it in range(iterations):
            new_candidates = []
            # Generate neighbors by perturbing each group in each beam candidate.
            for score, sol in beam:
                for subset_idx in range(len(candidate_generators)):
                    new_sol = sol.copy()
                    phonemes, size = candidate_generators[subset_idx]
                    new_sol[subset_idx] = self.generate_candidate_for_group(phonemes, size)
                    new_candidates.append(new_sol)

            # Evaluate the candidates in parallel.
            evaluated = []
            with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
                future_to_sol = {executor.submit(calc_distance_fn, candidate): candidate
                                 for candidate in new_candidates}
                for future in concurrent.futures.as_completed(future_to_sol):
                    candidate = future_to_sol[future]
                    try:
                        candidate_score = future.result()
                        evaluated.append((candidate_score, candidate))
                    except Exception as exc:
                        print(f"Candidate evaluation generated an exception: {exc}")

            combined = beam + evaluated
            combined.sort(key=lambda x: x[0])
            beam = combined[:beam_width]

            if beam[0][0] < best_score:
                best_score, best_solution = beam[0]

        print("Beam search best average distance:", best_score)
        return best_solution, best_score

    def select_stimuli(self, n: int = None) -> List[dict]:
        """
        Selects stimuli using both Simulated Annealing and Beam Search,
        compares their performance (both in quality and time), and returns the best solution.
        """
        iterations = 5_00  # local variable to set iterations for both algorithms
        candidate_generators = self.get_candidate_generators(n)

        # Measure time for Simulated Annealing
        start_time_sa = time.time()
        best_solution, best_score = self.simulated_annealing(candidate_generators,
                                                             iterations=iterations*1000,
                                                             calc_distance_fn=self.calculate_average_distance_between_items)
        end_time_sa = time.time()
        sa_time = end_time_sa - start_time_sa

        # Measure time for Beam Search
        start_time_bs = time.time()
        best_solution_beam, best_score_beam = self.beam_search(candidate_generators,
                                                               iterations=iterations,
                                                               calc_distance_fn=self.calculate_average_distance_between_items)
        end_time_bs = time.time()
        bs_time = end_time_bs - start_time_bs

        print(f"Simulated Annealing Time: {sa_time:.2f} seconds")
        print(f"Beam Search Time: {bs_time:.2f} seconds")

        if best_score_beam < best_score:
            return best_solution_beam
        return best_solution

    def validate_balance(self, selected: Dict[str, List[dict]]):
        """Check average frequency and density across groups"""
        freq_stats = []
        dens_stats = []

        for phoneme, items in selected.items():
            freqs = [item['frequency'] for item in items]
            dens = [item['density'] for item in items]
            freq_stats.append((np.mean(freqs), np.std(freqs)))
            dens_stats.append((np.mean(dens), np.std(dens)))

        print("Frequency balance:")
        for (mean, std), phoneme in zip(freq_stats, selected.keys()):
            print(f"{phoneme}: μ={mean:.2e} ±{std:.2e}")

        print("\nDensity balance:")
        for (mean, std), phoneme in zip(dens_stats, selected.keys()):
            print(f"{phoneme}: μ={mean:.2e} ±{std:.2e}")

    def save_solution_to_csv_and_print_table(self, best_solution, filename: str, translationTable: Dict[str, str]):
        """
        Saves the best solution into a CSV file and prints a markdown table summary.

        The CSV will have the columns:
          Tested Allophone, Tested Phoneme, Word, Frequency, Density, Phonemic Length, Transcription

        The markdown table will have the columns:
          Tested Allophone, Tested Phoneme, Average Probability *1Million, S.D. Probability *1Million,
          Average Density, S.D. Density

        Parameters:
          best_solution: List of candidate dictionaries (one per phoneme group) generated by the search.
          filename: The name of the CSV file to save the detailed results.
          translationTable: A dictionary mapping TestedPhoneme to TestedAllophone.
        """
        import csv
        from tabulate import tabulate

        # Write CSV file with detailed candidate rows.
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ["Tested Allophone", "Tested Phoneme", "Word", "Frequency", "Density", "Phonemic Length",
                          "Transcription"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            # best_solution is a list of candidate dictionaries, one per phoneme group.
            for candidate in best_solution:
                for item in candidate["combination"]:
                    # item is expected to be a tuple: (word, frequency, density, TestedPhoneme, transcription)
                    tested_phoneme = item[3]
                    tested_allophone = translationTable.get(tested_phoneme, tested_phoneme)
                    phonemic_length = len(item[4].split())
                    writer.writerow({
                        "Tested Allophone": tested_allophone,
                        "Tested Phoneme": tested_phoneme,
                        "Word": item[0],
                        "Frequency": item[1],
                        "Density": item[2],
                        "Phonemic Length": phonemic_length,
                        "Transcription": item[4]
                    })

        # Build the summary table rows for markdown output.
        summary_rows = []
        for candidate in best_solution:
            # Use the first item from the candidate combination as representative.
            first_item = candidate["combination"][0]
            tested_phoneme = first_item[3]
            tested_allophone = translationTable.get(tested_phoneme, tested_phoneme)
            n_items = len(candidate["combination"])

            # Compute averages (note: total_probability is already scaled by 1e6)
            avg_probability = candidate["total_probability"] / n_items
            avg_density = candidate["total_density"] / n_items

            # Compute standard deviations
            sd_probability = candidate["sd_probability"]
            sd_density = candidate["sd_density"]

            summary_rows.append([
                tested_allophone, tested_phoneme,
                f"{avg_probability:.2f}", f"{sd_probability:.2f}",
                f"{avg_density:.2f}", f"{sd_density:.2f}"
            ])

        headers = [
            "Tested Allophone", "Tested Phoneme",
            "Average Probability *1Million", "S.D. Probability *1Million",
            "Average Density", "S.D. Density"
        ]
        md_table = tabulate(summary_rows, headers=headers, tablefmt="github")

        print("\nMarkdown Table Summary:")
        print(md_table)


def process_plosive_initials():
    """Processes Plosive Initials"""
    print("\n🚀 Starting Plosive Initials Processing...")

    filterer = FilterTestStimuli("out/plosiveInitials.csv")
    print("🔍 Selecting best stimuli for Plosive Initials...")
    best_solution = filterer.select_stimuli(n=20)

    apaPlosiveInitalToTestedAllophoneTable = {
        "P": "[pʰ]",
        "T": "[tʰ]",
        "K": "[kʰ]",
        "B": "[b]",
        "D": "[d]",
        "G": "[g]",
    }

    output_file = "final/plosiveInitials.csv"
    filterer.save_solution_to_csv_and_print_table(best_solution, output_file, apaPlosiveInitalToTestedAllophoneTable)
    print(f"✅ Plosive Initials saved to {output_file}\n")


def process_plosive_finals():
    """Processes Plosive Finals"""
    print("\n🚀 Starting Plosive Finals Processing...")

    filterer = FilterTestStimuli("out/plosiveFinals.csv")
    print("🔍 Selecting best stimuli for Plosive Finals...")
    best_solution = filterer.select_stimuli(n=20)

    apaPlosiveFinalToTestedAllophoneTable = {
        "P": "[p̚]",
        "T": "[t̚]",
        "K": "[k̚]",
        "B": "[b̚]",
        "D": "[d̚]",
        "G": "[g̚]",
    }

    output_file = "final/plosiveFinals.csv"
    filterer.save_solution_to_csv_and_print_table(best_solution, output_file, apaPlosiveFinalToTestedAllophoneTable)
    print(f"✅ Plosive Finals saved to {output_file}\n")


def process_devoiced_plosive_finals():
    """Processes Devoiced Plosive Finals"""
    print("\n🚀 Starting Devoiced Plosive Finals Processing...")

    filterer = FilterTestStimuli("out/devoicedPlosives.csv")
    print("🔍 Selecting best stimuli for Devoiced Plosive Finals...")
    best_solution = filterer.select_stimuli(n=10)

    apaPlosiveDevoicedToTestedAllophoneTable = {
        "B": "[b̥]",
        "D": "[d̥]",
        "G": "[g̥]",
    }

    output_file = "final/devoicedPlosives.csv"
    filterer.save_solution_to_csv_and_print_table(best_solution, output_file, apaPlosiveDevoicedToTestedAllophoneTable)
    print(f"✅ Devoiced Plosive Finals saved to {output_file}\n")


def process_vcv_plosive_finals():
    """Processes VCV Plosive Finals"""
    print("\n🚀 Starting VCV Plosive Finals Processing...")

    filterer = FilterTestStimuli("out/VCVplosive.csv")
    print("🔍 Selecting best stimuli for VCV Plosive Finals...")
    best_solution = filterer.select_stimuli(n=15)

    apaPlosiveVCVToTestedAllophoneTable = {
        "P": "VCV_[pʰ]",
        "T": "VCV_[tʰ]",
        "K": "VCV_[kʰ]",
        "B": "VCV_[b]",
        "D": "VCV_[d]",
        "G": "VCV_[g]",
    }

    output_file = "final/vcvPlosiveFinals.csv"
    filterer.save_solution_to_csv_and_print_table(best_solution, output_file, apaPlosiveVCVToTestedAllophoneTable)
    print(f"✅ VCV Plosive Finals saved to {output_file}\n")


def process_unaspirated_unvoiced_plosive_initials():
    """Processes Unaspirated Unvoiced Plosive Initials"""
    print("\n🚀 Starting Unaspirated Unvoiced Finals Processing...")

    filterer = FilterTestStimuli("out/unaspiratedUnvoicedPlosiveInitials.csv")
    print("🔍 Selecting best stimuli for Unaspirated Unvoiced Plosive Initials...")
    best_solution = filterer.select_stimuli(n=20)

    apaPlosiveUnaspiratedUnvoicedToTestedAllophoneTable = {
        "P": "[p]",
        "T": "[t]",
        "K": "[k]",
    }

    output_file = "final/unaspiratedUnvoicedPlosiveInitials.csv"
    filterer.save_solution_to_csv_and_print_table(best_solution, output_file, apaPlosiveUnaspiratedUnvoicedToTestedAllophoneTable)
    print(f"✅ Unaspirated Unvoiced Plosive Initials saved to {output_file}\n")


import multiprocessing

def main():
    """Main function to execute all processing steps in parallel"""
    processes = [
        multiprocessing.Process(target=process_plosive_finals),
        multiprocessing.Process(target=process_devoiced_plosive_finals),
        multiprocessing.Process(target=process_plosive_initials),
        multiprocessing.Process(target=process_vcv_plosive_finals),
        multiprocessing.Process(target=process_unaspirated_unvoiced_plosive_initials)
    ]

    # Start all processes
    for p in processes:
        p.start()

    # Wait for all processes to complete
    for p in processes:
        p.join()

    print("\n🎉 All processing complete!")

if __name__ == "__main__":
    main()
