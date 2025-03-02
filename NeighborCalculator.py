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

    # Preprocess pronunciations by removing numbers
    def preprocess(self,phonemes: List[str]) -> List[str]:
        return [''.join([c for c in phoneme if not c.isdigit()]) for phoneme in phonemes]

    def phonemic_distance(self, pronunciation1: List[str], pronunciation2: List[str], max_allowed=float('inf')) -> int:
        pron1 = tuple(self.preprocess(pronunciation1))
        pron2 = tuple(self.preprocess(pronunciation2))

        if len(pron1) < len(pron2):
            return self.phonemic_distance(pron2, pron1, max_allowed)



        previous_row = list(range(len(pron2) + 1))

        for i, p1 in enumerate(pron1):
            current_row = [i + 1]
            min_val = float('inf')
            for j, p2 in enumerate(pron2):
                cost = 0 if p1 == p2 else 1
                current_val = min(
                    previous_row[j + 1] + 1,  # Deletion
                    current_row[j] + 1,  # Insertion
                    previous_row[j] + cost  # Substitution
                )
                current_row.append(current_val)
                min_val = min(min_val, current_val)

            # Early termination check
            if min_val > max_allowed:
                return min_val

            previous_row = current_row

        return previous_row[-1]

    def filter_by_phonemic_distance(self, target_pronunciation, target_distance=1, limit_max_distance=None, operator=lambda i, t: i <= t):
        # Preprocess target once
        preprocessed_target = self.preprocess(target_pronunciation)

        max_distance=float('inf')
        if limit_max_distance is None:
            max_distance = target_distance

        return [word for word in self.word_dictionary
                if self._meets_distance_criteria(word, preprocessed_target,target_distance, max_distance, operator)]

    def _meets_distance_criteria(self, word, target,target_distance, max_distance, operator):
        # Quick length check first
        word_pron = self.preprocess(word['pronunciation'])
        target_word_len = len(target)
        if abs(len(word_pron) - target_word_len) > max_distance*1.1+1:
            return False

        # Calculate with early termination
        actual_distance = self.phonemic_distance(
            word_pron,
            target,
            max_allowed=max_distance
        )
        return operator(actual_distance, target_distance)


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
        limit_max_distance=1,
    )

    print("Words with phonemic distance 1 from [\"B\", \"EH1\"]:","Total:",len(results))
    for entry in results:
        print(entry)
    print("Words with phonemic distance 1 from [\"B\", \"EH1\"]:", "Total:", len(results))