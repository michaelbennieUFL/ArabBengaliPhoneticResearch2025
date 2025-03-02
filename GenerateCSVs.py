#!/usr/bin/env python

import csv
import os
import re
from TestVocabMaker import generateTestWordList
from NgramAPI import getFrequency,getFrequencyOfMostCommon
import CMUreader
from NeighborCalculator import NeighborCalculator  # Import the neighbor calculator class
from CMUreader import generateCombinedWordsets
import json
from tqdm import tqdm


def generateCSVFiles(word_set, frequency_cache):  # Modified to accept cache
    """
    Generates CSV files with neighborhood density column.
    Accepts and modifies a frequency cache dictionary
    """
    test_results = generateTestWordList(word_set)
    neighbor_calc = NeighborCalculator(word_set)  # Initialize neighbor calculator

    output_dir = "out"
    os.makedirs(output_dir, exist_ok=True)


    distance_cache={}

    for test_type, test_dict in test_results.items():
        csv_filename = os.path.join(output_dir, f"{test_type}.csv")
        with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            # Add NeighborhoodDensity to header
            writer.writerow(["TestedPhoneme", "Word", "Frequency",
                             "ARPAbetTranscription", "NeighborhoodDensity"])
            #for phoneme in tqdm(sorted(test_dict.keys()), desc=f"{test_type} phonemes", leave=False):

            for phoneme in sorted(test_dict.keys()):
                rows = []
                for word_dict in tqdm(test_dict[phoneme],desc=f"{test_type} phonemes| type:{phoneme}", leave=False):
                    word_text = word_dict["word"]
                    transcription = " ".join(word_dict["pronunciation"])

                    # Get or calculate frequency
                    if word_text in frequency_cache:
                        target_word,frequency = frequency_cache[word_text]
                    else:
                        try:
                            if word_text.isupper():
                                target_word,frequency = getFrequencyOfMostCommon(word_text)
                            else:
                                frequency = getFrequency(word_text)
                                target_word =word_text
                        except Exception:
                            frequency = 0.0
                            continue
                        frequency_cache[word_text] = (target_word,frequency)

                    # Calculate neighborhood density (phonemic distance <= 1)
                    pronunciation = word_dict["pronunciation"]

                    if tuple(pronunciation) in distance_cache:
                        density=distance_cache[tuple(pronunciation)]
                    else:
                        neighbors = neighbor_calc.filter_by_phonemic_distance(
                            target_pronunciation=pronunciation,
                            target_distance=1,

                        )
                        density = len(neighbors)
                        distance_cache[tuple(pronunciation)] = density

                    rows.append((phoneme, target_word, frequency, transcription, density))

                # Sort by frequency descending
                rows.sort(key=lambda x: x[2], reverse=True)


                seen_transcriptions = set()
                # Write each row to the CSV file
                for row in rows:
                    transcription = row[3]
                    transcription_hash=re.sub(r'\d', '', transcription)
                    if transcription_hash not in seen_transcriptions:
                        writer.writerow(row)
                        seen_transcriptions.add(transcription_hash) # only keep the most common variant


        print(f"CSV file generated: {csv_filename}")


if __name__ == "__main__":
    # Load frequency cache from file
    cache_file = "frequency_cache.json"
    try:
        with open(cache_file, 'r') as f:
            frequency_cache = json.load(f)
    except FileNotFoundError:
        frequency_cache = {}

    # Parse the CMUdict and generate files
    word_set = generateCombinedWordsets()
    generateCSVFiles(word_set, frequency_cache)

    # Save updated cache to file
    with open(cache_file, 'w') as f:
        json.dump(frequency_cache, f)