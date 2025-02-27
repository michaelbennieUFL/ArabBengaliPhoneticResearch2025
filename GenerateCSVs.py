#!/usr/bin/env python

import csv
import os

from TestVocabMaker import generateTestWordList
from NgramAPI import getFrequency
import CMUreader
from NeighborCalculator import NeighborCalculator  # Import the neighbor calculator class


def generateCSVFiles(word_set):
    """
    Generates CSV files with neighborhood density column.
    New columns: TestedPhoneme, Word, Frequency, ARPAbetTranscription, NeighborhoodDensity
    """
    test_results = generateTestWordList(word_set)
    frequency_cache = {}
    neighbor_calc = NeighborCalculator(word_set)  # Initialize neighbor calculator

    output_dir = "out"
    os.makedirs(output_dir, exist_ok=True)

    for test_type, test_dict in test_results.items():
        csv_filename = os.path.join(output_dir, f"{test_type}.csv")
        with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            # Add NeighborhoodDensity to header
            writer.writerow(["TestedPhoneme", "Word", "Frequency",
                             "ARPAbetTranscription", "NeighborhoodDensity"])

            for phoneme in sorted(test_dict.keys()):
                rows = []
                for word_dict in test_dict[phoneme]:
                    word_text = word_dict["word"]
                    transcription = " ".join(word_dict["pronunciation"])

                    # Get or calculate frequency
                    if word_text in frequency_cache:
                        frequency = frequency_cache[word_text]
                    else:
                        try:
                            frequency = getFrequency(word_text)
                        except Exception:
                            frequency = 0.0
                        frequency_cache[word_text] = frequency

                    # Calculate neighborhood density (phonemic distance <= 1)
                    pronunciation = word_dict["pronunciation"]
                    neighbors = neighbor_calc.filter_by_phonemic_distance(
                        target_pronunciation=pronunciation,
                        target_distance=1
                    )
                    density = len(neighbors)

                    rows.append((phoneme, word_text, frequency, transcription, density))

                # Sort by frequency descending
                rows.sort(key=lambda x: x[2], reverse=True)


                seen_transcriptions = set()
                # Write each row to the CSV file
                for row in rows:
                    transcription = row[3]
                    if transcription not in seen_transcriptions:
                        writer.writerow(row)
                        seen_transcriptions.add(transcription) # only keep the most common variant


        print(f"CSV file generated: {csv_filename}")


if __name__ == "__main__":
    # Parse the CMUdict to get the original word set
    word_set = CMUreader.parse_cmudict("cmudict-0.7b")
    generateCSVFiles(word_set)
