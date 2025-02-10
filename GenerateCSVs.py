#!/usr/bin/env python

import csv
from TestVocabMaker import generateTestWordList  # your module containing generateTestWordList
from NgramAPI import getFrequency  # your module containing getFrequency
import CMUreader  # assuming this module provides parse_cmudict


def generateCSVFiles(word_set):
    """
    Generates one CSV file for each test type defined by generateTestWordList.

    The CSV file for each test type (e.g., 'plosiveInitials.csv') will have the
    columns:
        TestedPhoneme, Word, Frequency, ARPAbetTranscription

    The rows are organized first by the tested phoneme (alphabetically) and then
    by Frequency (descending).
    """
    test_results = generateTestWordList(word_set)

    # Iterate over each test type (the keys of test_results)
    for test_type, test_dict in test_results.items():
        csv_filename = f"out/{test_type}.csv"
        with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            # Write header row
            writer.writerow(["TestedPhoneme", "Word", "Frequency", "ARPAbetTranscription"])

            # Process each tested phoneme group in alphabetical order
            for phoneme in sorted(test_dict.keys()):
                rows = []
                # Each entry in test_dict[phoneme] is a word dictionary
                for word_dict in test_dict[phoneme]:
                    word_text = word_dict["word"]
                    # Join the list of phonemes to form the ARPAbet transcription
                    transcription = " ".join(word_dict["pronunciation"])
                    try:
                        frequency = getFrequency(word_text)
                    except Exception as e:
                        # If the API call fails, assign frequency as 0.0
                        frequency = 0.0
                    rows.append((phoneme, word_text, frequency, transcription))

                # Sort the rows for this phoneme by Frequency in descending order
                rows.sort(key=lambda x: x[2], reverse=True)

                # Write each row to the CSV file
                for row in rows:
                    writer.writerow(row)

        print(f"CSV file generated: {csv_filename}")


if __name__ == "__main__":
    # Parse the CMUdict to get the original word set
    word_set = CMUreader.parse_cmudict("cmudict-0.7b")
    generateCSVFiles(word_set)
