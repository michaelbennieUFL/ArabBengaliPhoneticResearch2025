import pandas as pd
import re
def load_tsv(file_path):
    """Load a TSV file into a pandas DataFrame."""
    return pd.read_csv(file_path, sep='\t')


def convert_ipa_to_arpabet(ipa_str, ipa_to_arpabet):
    """
    Convert an IPA transcription to ARPAbet notation.

    1. Cleans the input by removing diacritics, brackets, slashes, dashes, and periods.
    2. Segments the IPA transcription into phonemes.
    3. Greedily replaces IPA phonemes with their ARPAbet equivalents.
    4. Ensures proper spacing between phonemes.
    """
    # Step 1: Remove extra characters like brackets, slashes, dashes, and diacritics
    ipa_str = re.sub(r'[ˌˈː.\-/\[\]]', '', ipa_str)
    ipa_str = ipa_str.replace('(ɹ)', '')
    ipa_str = ipa_str.replace(' ', '')

    # Step 2: Tokenize IPA into a list of phonemes using a longest-match greedy algorithm
    tokens = []
    i = 0
    while i < len(ipa_str):
        matched = False
        # Try matching longest phoneme first (3, then 2, then 1 character(s))
        for l in (3, 2, 1):
            if i + l <= len(ipa_str) and ipa_str[i:i + l] in ipa_to_arpabet:
                tokens.append(ipa_to_arpabet[ipa_str[i:i + l]])
                i += l
                matched = True
                break
        if not matched:
            return False
            i += 1  # Skip unrecognized characters

    # Step 3: Ensure single spacing between phonemes
    return ' '.join(tokens).strip()


def process_arpabet_conversion(df):
    """Convert IPA transcriptions in a DataFrame to ARPAbet notation."""

    ipa_to_arpabet = {
        # Vowels (from Wikipedia ARPABET)
        'ɑ': 'AA',  # balm, bot (with father–bother merger)
        'æ': 'AE',  # bat
        'ʌ': 'AH',  # butt
        'ɔ': 'AO',  # caught, story
        'aʊ': 'AW',  # bout
        'ə': 'AH',  # comma; per cmu standards
        'ɚ': 'ER',  # letter, forward; per cmu standards
        'aɪ': 'AY',  # bite
        'ɛ': 'EH',  # bet
        'ɝ': 'ER',  # bird, foreword
        'eɪ': 'EY',  # bait
        'ɪ': 'IH',  # bit
        'ɨ': 'IX',  # roses, rabbit
        'i': 'IY',  # beat
        'oʊ': 'OW',  # boat
        'ɔɪ': 'OY',  # boy
        'ʊ': 'UH',  # book
        'u': 'UW',  # boot
        'ʉ': 'UX',  # dude

        # Consonants (from Wikipedia ARPABET)
        'b': 'B',
        't͡ʃ': 'CH',
        'tʃ': 'CH',
        'd': 'D',
        'ð': 'DH',
        'ɾ': 'DX',
        'l̩': 'EL',  # syllabic l
        'm̩': 'EM',  # syllabic m
        'n̩': 'EN',  # syllabic n
        'f': 'F',
        'ɡ': 'G',
        'h': 'HH',
        'd͡ʒ':'JH',
        'dʒ': 'JH',
        'k': 'K',
        'l': 'L',
        'm': 'M',
        'n': 'N',
        'ŋ': 'NG',
        'p': 'P',
        'ʔ': 'Q',
        'ɹ': 'R',
        's': 'S',
        'ʃ': 'SH',
        't': 'T',
        'θ': 'TH',
        'v': 'V',
        'w': 'W',
        'ʍ': 'WH',
        'j': 'Y',
        'z': 'Z',
        'ʒ': 'ZH',
    }

    convert_ipa_to_arpabet("[/ˈbɐ.ʔon/]", ipa_to_arpabet)


    blocked_sounds=['ʍ','ʔ',"-"]

    arpabet_dict = {}
    for _, row in df.iterrows():
        word = row.iloc[0]
        ipa_transcription = row.iloc[1] if len(row) > 1 else ""  # Get IPA if available
        if ipa_transcription and not any(sub in ipa_transcription for sub in blocked_sounds):
            arpabet_transcription = convert_ipa_to_arpabet(ipa_transcription, ipa_to_arpabet)
            if arpabet_transcription and type(word) is str and word.isalpha():
                arpabet_dict[word] = arpabet_transcription

    return pd.DataFrame(arpabet_dict.items(), columns=["Word", "ARPAbet"])

def save_tsv(df, file_path):
    """Save a DataFrame to a TSV file."""
    df.to_csv(file_path, sep='\t', index=False, header=False)

if __name__ == "__main__":
    # Define file paths
    filtered_tsv_file_path = "dictionaries/EnglishData.txt"
    arpabet_tsv_file_path = "dictionaries/Wiktionary_arpabet.tsv"


    # Load the filtered TSV file
    df = load_tsv(filtered_tsv_file_path)

    # Convert IPA transcriptions to ARPAbet
    arpabet_df = process_arpabet_conversion(df)

    # Save the result to a file
    save_tsv(arpabet_df, arpabet_tsv_file_path)

    # Provide the download link
    print(arpabet_tsv_file_path)
