from typing import List, Dict, Callable
from functools import partial

from CMUreader import parse_cmudict,generateCombinedWordsets


class NeighborCalculator:
    def __init__(self, word_list: List[Dict[str, List[str]]]):
        # Remove duplicate pronunciations
        self.word_dictionary = self.remove_duplicate_pronunciations(word_list)

    def remove_duplicate_pronunciations(self, word_list: List[Dict[str, List[str]]]) -> List[Dict[str, List[str]]]:
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
            # Convert pronunciation list to tuple for hashing
            pronunciation_tuple = tuple(word_entry["pronunciation"])
            if pronunciation_tuple not in pronunciation_map:
                pronunciation_map[pronunciation_tuple] = word_entry
                unique_words.append(word_entry)

        return unique_words

    def phonemic_distance(self, pronunciation1: List[str], pronunciation2: List[str]) -> int:
        """
        Calculates the Levenshtein distance between two pronunciations.
        Ignores numbers after syllables (e.g., 'EH1' becomes 'EH').

        Args:
            pronunciation1 (List[str]): The first pronunciation to compare.
            pronunciation2 (List[str]): The second pronunciation to compare.

        Returns:
            int: The Levenshtein distance between the two pronunciations.
        """

        # Preprocess pronunciations by removing numbers
        def preprocess(phonemes: List[str]) -> List[str]:
            return [''.join([c for c in phoneme if not c.isdigit()]) for phoneme in phonemes]

        pron1 = preprocess(pronunciation1)
        pron2 = preprocess(pronunciation2)

        # Levenshtein distance algorithm
        m, n = len(pron1), len(pron2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                cost = 0 if pron1[i - 1] == pron2[j - 1] else 1
                dp[i][j] = min(dp[i - 1][j] + 1,  # Deletion
                               dp[i][j - 1] + 1,  # Insertion
                               dp[i - 1][j - 1] + cost)  # Substitution or no cost

        return dp[m][n]

    def filter_by_phonemic_distance(self, target_pronunciation: List[str], target_distance=1,
                                    operator=lambda input, target: input <= target) -> List[Dict[str, List[str]]]:
        """
        Filters words based on their phonemic distance from a target pronunciation.

        Args:
            target_pronunciation (List[str]): The target pronunciation to compare against.
            target_distance (int): The target distance to compare.
            operator (Callable[[int, int], bool]): A comparison operator to determine if the distance meets the criteria.

        Returns:
            List[Dict[str, List[str]]]: A list of words that meet the distance criteria.
        """
        matching_words = []
        for word in self.word_dictionary:
            distance = self.phonemic_distance(word["pronunciation"], target_pronunciation)
            if operator(distance, target_distance):
                matching_words.append(word)
        return matching_words


# Example usage:
if __name__ == "__main__":
    cmudict_path = 'dictionaries/cmudict-0.7b'  # Replace with your actual file path
    word_list = generateCombinedWordsets()

    # Initialize DataFilterer
    filterer = NeighborCalculator(word_list)

    # Example 1: Find words with phonemic distance of 1 from ["B", "EH1"]
    target_pronunciation = ['B', 'EH1', 'V']
    results = filterer.filter_by_phonemic_distance(
        target_pronunciation,
        target_distance=1,
    )

    print("Words with phonemic distance 1 from [\"B\", \"EH1\"]:","Total:",len(results))
    for entry in results:
        print(entry)
    print("Words with phonemic distance 1 from [\"B\", \"EH1\"]:", "Total:", len(results))