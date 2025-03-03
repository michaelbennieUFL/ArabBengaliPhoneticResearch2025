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
- **Average Probability (*1 Million)**: The mean probability of the selected stimuli.
- **S.D. Probability (*1 Million)**: The standard deviation of probability.
- **Average Density**: The mean neighborhood density of selected words.
- **S.D. Density**: The standard deviation of neighborhood density.

### **Plosive Initials**
| Tested Allophone   | Tested Phoneme   |   Average Probability *100 Million |   C.V. Probability *100 Million |   Average Density |   C.V. Density |
|--------------------|------------------|------------------------------------|---------------------------------|-------------------|----------------|
| [b]                | B                |                            1604.84 |                            2.42 |             55.85 |           0.28 |
| [d]                | D                |                            1604.84 |                            2.48 |             55.85 |           0.3  |
| [g]                | G                |                            1604.84 |                            3.43 |             55.75 |           0.2  |
| [kʰ]               | K                |                            1604.86 |                            2.82 |             55.8  |           0.28 |
| [pʰ]               | P                |                            1604.84 |                            2.99 |             55.85 |           0.29 |
| [tʰ]               | T                |                            1604.84 |                            1.91 |             55.85 |           0.32 |

✅ **File Saved**: `final/plosiveInitials.csv`

---

### **Plosive Finals**
| Tested Allophone   | Tested Phoneme   |   Average Probability *100 Million |   C.V. Probability *100 Million |   Average Density |   C.V. Density |
|--------------------|------------------|------------------------------------|---------------------------------|-------------------|----------------|
| [b̚]                | B                |                             545.3  |                            3.53 |             53.05 |           0.13 |
| [d̚]                | D                |                             545.2  |                            1.61 |             53.95 |           0.3  |
| [g̚]                | G                |                             548.82 |                            1.26 |             50.5  |           0.23 |
| [k̚]                | K                |                             545.39 |                            2.21 |             54.1  |           0.25 |
| [p̚]                | P                |                             545.4  |                            1.89 |             53.75 |           0.2  |
| [t̚]                | T                |                             545.42 |                            2.55 |             53.8  |           0.36 |

✅ **File Saved**: `final/plosiveFinals.csv`

---


### **Devoiced Plosives**
| Tested Allophone   | Tested Phoneme   |   Average Probability *100 Million |   C.V. Probability *100 Million |   Average Density |   C.V. Density |
|--------------------|------------------|------------------------------------|---------------------------------|-------------------|----------------|
| [b̥]                | B                |                              17.77 |                            1.81 |              2.55 |           0.9  |
| [d̥]                | D                |                              17.77 |                            1.1  |              2.55 |           0.75 |
| [g̥]                | G                |                              17.77 |                            1.6  |              2.55 |           0.34 |

✅ **File Saved**: `final/devoicedPlosives.csv`

---

### **VCV Plosive Finals**
| Tested Allophone   | Tested Phoneme   |   Average Probability *100 Million |   C.V. Probability *100 Million |   Average Density |   C.V. Density |
|--------------------|------------------|------------------------------------|---------------------------------|-------------------|----------------|
| VCV_[b]            | B                |                             108.98 |                            1.46 |             28.6  |           0.38 |
| VCV_[d]            | D                |                             108.98 |                            1.41 |             28.6  |           0.51 |
| VCV_[g]            | G                |                             109.28 |                            2.46 |             27.73 |           0.4  |
| VCV_[kʰ]           | K                |                             108.94 |                            2.22 |             28.6  |           0.37 |
| VCV_[pʰ]           | P                |                             108.74 |                            1.88 |             28.4  |           0.4  |
| VCV_[tʰ]           | T                |                             108.98 |                            1.95 |             28.6  |           0.52 |

✅ **File Saved**: `final/vcvPlosiveFinals.csv`

---

### **Unaspirated Unvoiced Plosive Initials**
| Tested Allophone   | Tested Phoneme   |   Average Probability *100 Million |   C.V. Probability *100 Million |   Average Density |   C.V. Density |
|--------------------|------------------|------------------------------------|---------------------------------|-------------------|----------------|
| [k]                | K                |                              497.1 |                            2.2  |              26.1 |           0.29 |
| [p]                | P                |                              497.1 |                            2.75 |              26.1 |           0.26 |
| [t]                | T                |                              497.1 |                            2.93 |              26.1 |           0.35 |

✅ **File Saved**: `final/unaspiratedUnvoicedPlosiveInitials.csv`

---

