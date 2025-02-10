import CMUreader

def generateWordCategoryLists():
    category_dict = {
        "Consonants_Stops": ["P", "T", "K", "B", "D", "G"],
        "Consonants_All": [
            "B", "CH", "D", "DH", "F", "G", "HH", "JH", "K", "L",
            "M", "N", "NG", "P", "R", "S", "SH", "T", "TH", "V",
            "W", "Y", "Z", "ZH"
        ],
        "Consonants_Stops_Unvoiced": ["P", "T", "K"],
        "Consonants_S": ["S"],
        "Vowels_Monophthong": ["AA", "AE", "AH", "AO", "AX", "AXR", "EH", "ER", "IH", "IX", "IY", "UH", "UW", "UX"],
        "Vowels_Uncentralized_NonMid": ["AA", "AE", "AW", "AY", "EY", "IH", "IY", "OW", "OY", "UH", "UW"]
    }

    category_dict["Vowels_Monophthong_Uncentralized_NonMid"] = list(
        set(category_dict["Vowels_Monophthong"]) & set(category_dict["Vowels_Uncentralized_NonMid"])
    )

    category_dict["Consonants_Unvoiced"] = [
        "P", "T", "K",
        "F", "S", "SH", "TH",
        "CH", "HH"
    ]


    category_dict["Consonants_Stops_Voiced"] = list(
        set(category_dict["Consonants_Stops"]) - set(category_dict["Consonants_Stops_Unvoiced"]))

    return category_dict

def generatePlosiveInitalTests(word_set) -> dict:
    wordCategoryList = generateWordCategoryLists()
    all_plosive_initals = {}

    for plosive in wordCategoryList["Consonants_Stops"]:
        plosive_initals = CMUreader.filterByLetters(word_set, [plosive])
        plosive_initals = CMUreader.filterByLetters(plosive_initals, wordCategoryList["Consonants_All"], index=-1)
        plosive_initals = CMUreader.filterByLetters(plosive_initals, wordCategoryList["Vowels_Monophthong_Uncentralized_NonMid"], index=-2)
        plosive_initals = CMUreader.filterBySyllableCount(plosive_initals, 1, int.__eq__)
        all_plosive_initals[plosive] = plosive_initals

    return all_plosive_initals

def generatePlosiveFinalsTests(word_set) -> dict:
    wordCategoryList = generateWordCategoryLists()
    all_plosive_finals = {}

    for plosive in wordCategoryList["Consonants_Stops"]:
        plosive_finals = CMUreader.filterByLetters(word_set, [plosive], index=-1)
        plosive_finals = CMUreader.filterByLetters(plosive_finals, wordCategoryList["Consonants_All"], index=0)
        plosive_finals = CMUreader.filterByLetters(plosive_finals, wordCategoryList["Vowels_Monophthong_Uncentralized_NonMid"], index=-2)
        plosive_finals = CMUreader.filterBySyllableCount(plosive_finals, 1, int.__eq__)
        all_plosive_finals[plosive] = plosive_finals

    return all_plosive_finals


def generateUnvoicedAfterSTests(word_set) -> dict:
    wordCategoryList = generateWordCategoryLists()
    all_unvoiced_plosives_after_s = {}

    for plosive in wordCategoryList["Consonants_Stops_Unvoiced"]:
        unvoiced_plosives_after_s = CMUreader.filterByLetters(word_set, wordCategoryList["Consonants_S"], index=0)
        unvoiced_plosives_after_s = CMUreader.filterByLetters(unvoiced_plosives_after_s, [plosive], index=1)
        unvoiced_plosives_after_s = CMUreader.filterByLetters(unvoiced_plosives_after_s, wordCategoryList["Consonants_All"], index=-1)
        unvoiced_plosives_after_s = CMUreader.filterByLetters(unvoiced_plosives_after_s, wordCategoryList["Vowels_Monophthong_Uncentralized_NonMid"], index=-2)
        unvoiced_plosives_after_s = CMUreader.filterBySyllableCount(unvoiced_plosives_after_s, 1, int.__eq__)
        all_unvoiced_plosives_after_s[plosive] = unvoiced_plosives_after_s

    return all_unvoiced_plosives_after_s


def generateDevoicedTests(word_set) -> dict:
    wordCategoryList = generateWordCategoryLists()
    all_devoiced_plosives = {}


    unvoiced_non_plosives=list(
        set(wordCategoryList["Consonants_Unvoiced"]) - set(wordCategoryList["Consonants_Stops"]))


    for plosive in wordCategoryList["Consonants_Stops_Voiced"]:

        devoiced_plosives = CMUreader.filterBySyllableCount(word_set, 2, int.__eq__)
        devoiced_plosives=CMUreader.filterByLetterPair(devoiced_plosives,[plosive],unvoiced_non_plosives)
        all_devoiced_plosives[plosive] = devoiced_plosives

    return all_devoiced_plosives

def generateTestWordList(word_set):
    result_sets = {
        # "devoicedPlosives": generateDevoicedTests(word_set),
        "unaspiratedUnvoicedPlosiveInitials": generateUnvoicedAfterSTests(word_set),
        "plosiveInitials": generatePlosiveInitalTests(word_set),
        "plosiveFinals": generatePlosiveFinalsTests(word_set),
    }

    # Print the results for Plosive Starts
    print("\nPlosive Initial Tests:")
    for plosive, words in result_sets["plosiveInitials"].items():
        print(f"{plosive}: {len(words)} words")

    # Print the results for Plosive Finals
    print("\nPlosive Final Tests:")
    for plosive, words in result_sets["plosiveFinals"].items():
        print(f"{plosive}: {len(words)} words")

    # Print the results for Unaspirated Plosives
    print("\nUnaspirated Unvoiced Plosive Tests:")
    for plosive, words in result_sets["unaspiratedUnvoicedPlosiveInitials"].items():
        print(f"{plosive}: {len(words)} words")

    # # Print the results for Devoiced Plosives
    # print("\nDevoiced Plosive Tests:")
    # for plosive, words in result_sets["devoicedPlosives"].items():
    #     print(f"{plosive}: {len(words)} words")


    return result_sets

if __name__ == "__main__":
    word_categories = generateWordCategoryLists()
    print("\nGenerated Vowel Category (Monophthong Uncentralized Non-Mid):")
    print(word_categories["Vowels_Monophthong_Uncentralized_NonMid"])

    original_word_set = CMUreader.parse_cmudict("cmudict-0.7b")
    result = generateTestWordList(original_word_set)
