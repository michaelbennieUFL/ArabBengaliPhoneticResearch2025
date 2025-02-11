from typing import List
import re
from typing import List, Dict


def parse_cmudict(file_path, include_non_letter_symbols=False):
    """
    Parses a CMUdict-formatted file and returns a list of dictionaries.

    Each dictionary in the returned list has two keys:
      - 'word': A string representing the word.
      - 'pronunciation': A list of strings, each being a phoneme token.

    Args:
        file_path (str): The path to the CMUdict file.

    Returns:
        List[dict]: A list of dictionaries representing the word entries.
    """
    entries = []
    with open(file_path, 'r', encoding='ISO-8859-1', errors='replace') as f:
        for line in f:
            # Remove any leading/trailing whitespace
            line = line.strip()
            # Skip empty lines or lines that are comments (e.g., header lines)
            if not line or line.startswith(';;;') or line.startswith('#'):
                continue

            # Split the line by whitespace. The first token is the word,
            # the remaining tokens represent the pronunciation.
            tokens = line.split()
            if len(tokens) < 2:
                continue  # Skip lines that don't have both a word and a pronunciation

            word = tokens[0]
            pronunciation = tokens[1:]
            if not include_non_letter_symbols and word.isalpha():
                entries.append({
                    'word': word,
                    'pronunciation': pronunciation
                })
            elif include_non_letter_symbols:
                entries.append({
                    'word': word,
                    'pronunciation': pronunciation
                })
    return entries


def filterByLetterPair(word_list: List[Dict[str, List[str]]],
                       first_set: List[str],
                       second_set: List[str],
                       stress_sensitive: bool = False) -> List[Dict[str, List[str]]]:
    """
    Filters the list of word entries, returning only those words
    that contain a consecutive pair of phonemes where:
      - The first phoneme is in `first_set`
      - The second phoneme is in `second_set`

    If stress_sensitive is False, any digits (0-9) present in the phoneme are removed
    before the comparison.

    Args:
        word_list: A list of dictionaries where each dictionary has a 'pronunciation' key
                   containing a list of phoneme strings.
        first_set: A list of phonemes for the first element in the pair.
        second_set: A list of phonemes for the second element in the pair.
        stress_sensitive: Whether to consider stress markers (digits) in the phonemes.

    Returns:
        A filtered list of word dictionaries that match the letter pair criteria.
    """
    new_word_list = []
    for word in word_list:
        pronunciation = word.get("pronunciation", [])
        # Loop through consecutive pairs of phonemes
        for i in range(len(pronunciation) - 1):
            first_phoneme = pronunciation[i]
            second_phoneme = pronunciation[i + 1]

            # Remove any stress digits if not stress sensitive
            if not stress_sensitive:
                first_phoneme = ''.join([char for char in first_phoneme if not char.isdigit()])
                second_phoneme = ''.join([char for char in second_phoneme if not char.isdigit()])

            # Check if the first phoneme is in first_set and the second in second_set
            if first_phoneme in first_set and second_phoneme in second_set:
                new_word_list.append(word)
                break  # Found a matching pair in this word; no need to check further

    return new_word_list


def filterByLetters(word_list: List[Dict[str, List[str]]], initials: List[str], index=0, stress_sensitive=False) -> List[Dict[str, List[str]]]:
    new_word_list = []
    for word in word_list:
        for initial in initials:
            # Get the pronunciation phoneme at the given index
            phoneme = word['pronunciation'][index]

            # If stress insensitive, remove digits (0-9) from phoneme
            if not stress_sensitive:
                phoneme = ''.join([char for char in phoneme if not char.isdigit()])

            # Compare the phoneme with the initial
            if phoneme == initial:
                new_word_list.append(word)

    return new_word_list

def countSyllables(word:Dict[str, List[str]]) -> int:
    total = 0

    for phoneme in word['pronunciation']:
        if phoneme[-1].isdigit():
            total += 1
    return total

def filterBySyllableCount(word_list: List[Dict[str, List[str]]], count:int, operator=int.__eq__) -> List[Dict[str, List[str]]]:
    new_word_list = []
    for word in word_list:
        if operator(countSyllables(word),count):
            new_word_list.append(word)
    return new_word_list


def countPhonemes(word: Dict[str, List[str]]) -> int:
    return len(word['pronunciation'])

def filterByPhonemeCount(word_list: List[Dict[str, List[str]]], count: int, operator=int.__eq__) -> List[Dict[str, List[str]]]:
    new_word_list = []
    for word in word_list:
        if operator(countPhonemes(word), count):
            new_word_list.append(word)
    return new_word_list

def removeDuplicatePronunciations(word_list: List[Dict[str, List[str]]]) -> List[Dict[str, List[str]]]:
    """
    Removes words that share the same pronunciation, keeping only those with unique pronunciations.

    Args:
        word_list (List[Dict[str, List[str]]]): A list of dictionaries where each dictionary contains:
            - 'word': The word as a string.
            - 'pronunciation': A list of phonemes representing its pronunciation.

    Returns:
        List[Dict[str, List[str]]]: A filtered list containing only words with unique pronunciations.
    """
    pronunciation_map = {}
    unique_words = []

    for word_entry in word_list:
        pronunciation_tuple = tuple(word_entry["pronunciation"])  # Convert list to tuple for hashing
        if pronunciation_tuple not in pronunciation_map:
            pronunciation_map[pronunciation_tuple] = word_entry  # Store the first occurrence

    unique_words = list(pronunciation_map.values())  # Extract unique word entries

    return unique_words

# Example usage:
if __name__ == "__main__":
    cmudict_path = 'cmudict-0.7b'  # Replace with your actual file path
    word_list = parse_cmudict(cmudict_path)

    #all the H sounds
    result=filterByLetters(word_list,["HH"])
    for entry in result[:5]:
        print(entry)


    print("\n\nFInding Some really long Words")
    #search for really long words
    result = filterBySyllableCount(word_list, 9,operator=int.__ge__)
    for entry in result[:5]:
        print(entry)