# **ArabBengaliPhoneticResearch2025**
This repository contains the **testing data** used for an **Arabic/Bengali Phonetic test**. 
The final file for the testing stimuli is located at [`final/combined.csv`](https://github.com/michaelbennieUFL/ArabBengaliPhoneticResearch2025/blob/Master/final/combined.csv)

## **Vowels Tested**

| **ARPAbet** | **IPA** | **Example Word** | **Counterpart in Najdi** | **Counterpart in Bengali** |
|------------|--------|----------------|------------------|---|
| **AA**     | /ɑ/    | **"Bob"** | ✔                | ✔ |
| **AE**     | /æ/    | **"bath"** | ❌                | ✔ |
| **IY**     | /i/    | **"beet"** | ✔                | ✔ |
| **EH**     | /ɛ/    | **"bet"** | ✔                | ✔ |
| **UW**     | /u/    | **"booed"** | ✔                | ✔ |
| **UH**     | /ʊ/    | **"book"** | ✔                | ❌  |


---

## **📂 Dataset Structure**
### **Unfiltered Data**
The unfiltered data consists of **all available words** containing each plosive phoneme. The number of words per phoneme varies across test conditions.

| Test Set Type \ Phoneme      | P   | T   | K   | B   | D   | G   |
|------------------------------|-----|-----|-----|-----|-----|-----|
| Plosive Initial              | 151 | 158 | 245 | 214 | 184 | 110 |
| Plosive Final                | 180 | 224 | 309 | 98  | 189 | 106 |
| VCV Plosive                  | 20  | 38  | 59  | 48  | 64  | 31  |
| Unaspirated Unvoiced Plosive | 52  | 109 | 60  | -   | -   | -   |
| Devoiced Plosive             | -   | -   | -   | 63  | 206 | 49  |

### **Filtered Stimuli**
The data was filtered to ensure that **selected stimuli**:
- Have **balanced probability and density distributions**.
- Have **low standard deviation**, ensuring uniformity.
- Represent all phonemes in a controlled manner.

Each table below provides an **aggregate summary** of the selected stimuli.

---

## **📊 Filtered Stimuli Output**
Each dataset contains a markdown table summarizing:
- **Tested Allophone**: The IPA transcription of the tested phoneme in its respective condition.
- **Tested Phoneme**: The original phoneme used in the dataset.
- **Average Probability \*100 Million**: The mean relative probability of the selected stimuli times $$10^8$$.
- **C.V. Probability \*100 Million**: The coefficient of variation of the probability.
- **Average Density**: The mean neighborhood density of selected words.
- **C.V. Density**: The coefficient of variation of the neighborhood density.

### **Plosive Initials**
| Tested Allophone   | Tested Phoneme   |   Average Probability *100 Million |   C.V. Probability *100 Million |   Average Density |   C.V. Density |
|--------------------|------------------|------------------------------------|---------------------------------|-------------------|----------------|
| [b]                | B                |                            2466.86 |                            0.96 |              62.6 |           0.13 |
| [d]                | D                |                            2466.92 |                            1.29 |              62.8 |           0.12 |
| [g]                | G                |                            2466.29 |                            1.63 |              62   |           0.08 |
| [kʰ]               | K                |                            2466.93 |                            1.48 |              62.6 |           0.3  |
| [pʰ]               | P                |                            2466.82 |                            1.12 |              62.6 |           0.05 |
| [tʰ]               | T                |                            2466.93 |                            1.93 |              62.6 |           0.29 |

✅ **File Saved**: `final/plosiveInitials.csv`

---

### **Plosive Finals**
| Tested Allophone   | Tested Phoneme   |   Average Probability *100 Million |   C.V. Probability *100 Million |   Average Density |   C.V. Density |
|--------------------|------------------|------------------------------------|---------------------------------|-------------------|----------------|
| [b̚]                | B                |                             929.02 |                            1.6  |              55   |           0.17 |
| [d̚]                | D                |                             928.92 |                            1.41 |              55.6 |           0.21 |
| [g̚]                | G                |                             929.11 |                            1.05 |              55.2 |           0.11 |
| [k̚]                | K                |                             929.07 |                            1.56 |              55.2 |           0.24 |
| [p̚]                | P                |                             929.06 |                            1.48 |              55.4 |           0.16 |
| [t̚]                | T                |                             929.07 |                            1.34 |              55.8 |           0.13 |

✅ **File Saved**: `final/plosiveFinals.csv`

---


### **Devoiced Plosives**
| Tested Allophone   | Tested Phoneme   |   Average Probability *100 Million |   C.V. Probability *100 Million |   Average Density |   C.V. Density |
|--------------------|------------------|------------------------------------|---------------------------------|-------------------|----------------|
| [b̥]                | B                |                               74.8 |                            0.82 |               4   |           0.77 |
| [d̥]                | D                |                               74.8 |                            0.78 |               4   |           1.14 |
| [g̥]                | G                |                               71.9 |                            0.34 |               2.6 |           0.19 |

✅ **File Saved**: `final/devoicedPlosives.csv`

---

### **VCV Plosive Finals**
| Tested Allophone   | Tested Phoneme   |   Average Probability *100 Million |   C.V. Probability *100 Million |   Average Density |   C.V. Density |
|--------------------|------------------|------------------------------------|---------------------------------|-------------------|----------------|
| VCV_[b]            | B                |                             296.27 |                            1.17 |              42   |           0.2  |
| VCV_[d]            | D                |                             296.57 |                            0.44 |              44.4 |           0.15 |
| VCV_[g]            | G                |                             293.96 |                            1.38 |              37.8 |           0.18 |
| VCV_[kʰ]           | K                |                             296.9  |                            1.17 |              42.2 |           0.32 |
| VCV_[pʰ]           | P                |                             213.78 |                            1.11 |              30.2 |           0.28 |
| VCV_[tʰ]           | T                |                             296.25 |                            1.55 |              42.6 |           0.15 |

✅ **File Saved**: `final/vcvPlosiveFinals.csv`

---

### **Unaspirated Unvoiced Plosive Initials**
| Tested Allophone   | Tested Phoneme   |   Average Probability *100 Million |   C.V. Probability *100 Million |   Average Density |   C.V. Density |
|--------------------|------------------|------------------------------------|---------------------------------|-------------------|----------------|
| [k]                | K                |                            1774.93 |                            0.9  |              29.6 |           0.33 |
| [p]                | P                |                            1775.37 |                            1.45 |              30.2 |           0.06 |
| [t]                | T                |                            1775.14 |                            1.61 |              29.8 |           0.22 |

✅ **File Saved**: `final/unaspiratedUnvoicedPlosiveInitials.csv`

---

