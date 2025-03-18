#!/usr/bin/env python3
import os
import glob
import pandas as pd
import argparse

# Import functions from TestVocabMaker and CMUreader.
# (These modules should provide the functions as in your original code.)
from TestVocabMaker import (
    generateTestWordList,
    generateCombinedWordsets,
    generateWordCategoryLists,
    load_unique_words,
    filter_cmudict_words,
)
import CMUreader  # used internally by TestVocabMaker functions

def merge_csv_files(csv_dir="final", output_file="final/combined.csv"):
    """
    Merge all CSV files in the given directory into one CSV file.
    """
    csv_files = glob.glob(os.path.join(csv_dir, "*.csv"))
    csv_files.sort()
    if not csv_files:
        print(f"No CSV files found in {csv_dir}.")
        return
    print(f"🔄 Merging CSV files from '{csv_dir}/' into '{output_file}'...")
    dfs = []
    for file in csv_files:
        try:
            df = pd.read_csv(file)
            dfs.append(df)
        except Exception as e:
            print(f"Error reading {file}: {e}")
    if dfs:
        combined_df = pd.concat(dfs, ignore_index=True)
        combined_df.to_csv(output_file, index=False)
        print(f"✅ Merge complete! Output saved as '{output_file}'.")
    else:
        print("No data to merge.")



def generate_test_rows():
    """
    Reads each individual CSV file in the `final` directory:
      - devoicedPlosives.csv
      - plosiveFinals.csv
      - plosiveInitials.csv
      - unaspiratedUnvoicedPlosiveInitials.csv
      - VCVplosive.csv

    Adds the Test Type based on the filename and generates corresponding filler words from generateTestWordList.

    Output CSV columns:
      Tested Allophone, Tested Phoneme, Word, Frequency*100 Million, Density, Phonemic Length, Transcription
    """
    csv_dir = "final"
    input_files = {
        "plosiveInitials": "plosiveInitials.csv",
        "plosiveFinals": "plosiveFinals.csv",
        "devoicedPlosives": "devoicedPlosives.csv",
        "unaspiratedUnvoicedPlosiveInitials": "unaspiratedUnvoicedPlosiveInitials.csv",
        "vcvPlosiveFinals": "vcvPlosiveFinals.csv"
    }

    filler_mapping = {
        "plosiveInitials": "allCVCFillers",
        "plosiveFinals": "allCVCFillers",
        "devoicedPlosives": "allBisyllabicFillers",
        "unaspiratedUnvoicedPlosiveInitials": "allSCVCFillers",
        "vcvPlosiveFinals": "allVCVFillers"
    }

    # Generate filler lists
    word_categories = generateWordCategoryLists()
    original_word_set = generateCombinedWordsets()
    unique_l2_words = load_unique_words("dictionaries/Oxford_3000_5000_AmericanEnglish.txt")
    filtered_word_set = filter_cmudict_words(original_word_set, unique_l2_words)
    test_word_list_dict = generateTestWordList(filtered_word_set)

    for test_type, filename in input_files.items():
        file_path = os.path.join(csv_dir, filename)
        if not os.path.exists(file_path):
            print(f"⚠️ Input file '{file_path}' not found. Skipping.")
            continue

        df = pd.read_csv(file_path)
        df["Test Type"] = test_type  # Explicitly add Test Type column

        filler_key = filler_mapping[test_type]
        filler_list = test_word_list_dict.get(filler_key, {}).get("fillers", [])

        if not filler_list:
            print(f"⚠️ No fillers found for '{filler_key}'. Skipping '{test_type}'.")
            continue

        filler_count = len(filler_list)
        rows = []
        filler_idx = 0

        for idx, row in df.iterrows():
            filler_word = filler_list[filler_idx % filler_count]
            filler_idx += 1

            tested_allophone = row.get("Tested Allophone", "")
            word_val = row.get("Word", "")
            transcription = row.get("Transcription", "")

            new_row = {
                "Tested Allophone": tested_allophone,
                "Tested Phoneme": "FILLER",
                "Word": filler_word["word"].lower(),
                "Frequency*100 Million": "x",
                "Density": "x",
                "Phonemic Length": "x",
                "Transcription": " ".join(filler_word["pronunciation"]),
            }

            rows.append(new_row)

        if rows:
            output_df = pd.DataFrame(rows)
            output_file = os.path.join(csv_dir, f"{test_type}_with_fillers.csv")
            output_df.to_csv(output_file, index=False)
            print(f"✅ '{test_type}' rows saved to '{output_file}' ({len(rows)} rows).")
        else:
            print(f"⚠️ No rows generated for '{test_type}'.")



def clean_files():
    """
    Remove generated files:
    - combined.csv
    - test_rows.csv
    - All files ending with '_with_fillers.csv' in the 'final' directory.
    """
    files_to_remove = [
        "final/combined.csv",
        "final/test_rows.csv",
    ] + glob.glob("final/*_with_fillers.csv")

    for file in files_to_remove:
        if os.path.exists(file):
            print(f"🧹 Removing '{file}'...")
            os.remove(file)
    print("✅ Cleanup complete!")


def main():
    clean_files()
    generate_test_rows()
    merge_csv_files()

if __name__ == "__main__":
    main()
