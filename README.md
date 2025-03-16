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
| [b]                | B                |                            1477.45 |                            1.21 |              60.4 |           0.37 |
| [d]                | D                |                            1477.33 |                            1.26 |              60.4 |           0.17 |
| [g]                | G                |                            1477.48 |                            1.3  |              60.4 |           0.08 |
| [kʰ]               | K                |                            1477.42 |                            1.19 |              60.2 |           0.22 |
| [pʰ]               | P                |                            1477.47 |                            0.76 |              60   |           0.33 |
| [tʰ]               | T                |                            1477.44 |                            0.82 |              60.4 |           0.17 |

✅ **File Saved**: `final/plosiveInitials.csv`

---

### **Plosive Finals**
| Tested Allophone   | Tested Phoneme   |   Average Probability *100 Million |   C.V. Probability *100 Million |   Average Density |   C.V. Density |
|--------------------|------------------|------------------------------------|---------------------------------|-------------------|----------------|
| [b̚]                | B                |                             905.39 |                            0.71 |              54   |           0.19 |
| [d̚]                | D                |                             905.69 |                            1.04 |              55.2 |           0.1  |
| [g̚]                | G                |                             905.76 |                            0.94 |              55   |           0.11 |
| [k̚]                | K                |                             905.51 |                            1.6  |              55.2 |           0.27 |
| [p̚]                | P                |                             905.74 |                            1.54 |              54.6 |           0.17 |
| [t̚]                | T                |                             905.82 |                            1.23 |              55.2 |           0.14 |

✅ **File Saved**: `final/plosiveFinals.csv`

---


### **Devoiced Plosives**
| Tested Allophone   | Tested Phoneme   |   Average Probability *100 Million |   C.V. Probability *100 Million |   Average Density |   C.V. Density |
|--------------------|------------------|------------------------------------|---------------------------------|-------------------|----------------|
| [b̥]                | B                |                              74.91 |                            0.78 |               2.4 |           0.5  |
| [d̥]                | D                |                              74.91 |                            0.67 |               2.4 |           0.62 |
| [g̥]                | G                |                              71.9  |                            0.34 |               2.6 |           0.19 |

✅ **File Saved**: `final/devoicedPlosives.csv`

---

### **VCV Plosive Finals**
| Tested Allophone   | Tested Phoneme   |   Average Probability *100 Million |   C.V. Probability *100 Million |   Average Density |   C.V. Density |
|--------------------|------------------|------------------------------------|---------------------------------|-------------------|----------------|
| VCV_[b]            | B                |                             387.89 |                            0.77 |              31.4 |           0.52 |
| VCV_[d]            | D                |                             387.39 |                            1.86 |              32.2 |           0.42 |
| VCV_[g]            | G                |                             387.61 |                            0.99 |              31.6 |           0.32 |
| VCV_[kʰ]           | K                |                             386.53 |                            1.04 |              32.2 |           0.35 |
| VCV_[pʰ]           | P                |                             319.52 |                            0.76 |              34.4 |           0.23 |
| VCV_[tʰ]           | T                |                             387.38 |                            1.18 |              31.8 |           0.39 |

✅ **File Saved**: `final/vcvPlosiveFinals.csv`

---

### **Unaspirated Unvoiced Plosive Initials**
| Tested Allophone   | Tested Phoneme   |   Average Probability *100 Million |   C.V. Probability *100 Million |   Average Density |   C.V. Density |
|--------------------|------------------|------------------------------------|---------------------------------|-------------------|----------------|
| [k]                | K                |                            1696.43 |                            0.98 |              26.6 |           0.4  |
| [p]                | P                |                            1696.54 |                            1.38 |              26.6 |           0.31 |
| [t]                | T                |                            1696.4  |                            1.44 |              26.2 |           0.33 |

✅ **File Saved**: `final/unaspiratedUnvoicedPlosiveInitials.csv`

---

