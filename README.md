# **ArabBengaliPhoneticResearch2025**
This repository contains the **testing data** used for an **Arabic/Bengali Phonetic test**. 


---

## **📂 Dataset Structure**
### **Unfiltered Data**
The unfiltered data consists of **all available words** containing each plosive phoneme. The number of words per phoneme varies across test conditions.

| **Test Set Type \ Phoneme**  | **P** | **T** | **K** | **B** | **D** | **G** |
|------------------------------|-------|-------|-------|-------|-------|-------|
| **Plosive Initial**          | 106   | 93    | 148   | 147   | 117   | 54    |
| **Plosive Final**            | 108   | 138   | 192   | 59    | 112   | 54    |
| **VCV Plosive**              | 6     | 27    | 43    | 36    | 49    | 22    |
| **Unaspirated Unvoiced Plosive** | 32  | 71    | 30    | -     | -     | -     |
| **Devoiced Plosive**         | -     | -     | -     | 33    | 133   | 23    |

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
| Tested Allophone | Tested Phoneme | Average Probability *1Million | S.D. Probability *1Million | Average Density | S.D. Density |
|-----------------|---------------|------------------------------|---------------------------|----------------|--------------|
| [b]            | B             | 33.71                        | 54.54                      | 41.40          | 10.86        |
| [d]            | D             | 33.72                        | 50.24                      | 41.40          | 9.57         |
| [g]            | G             | 33.29                        | 73.00                      | 40.80          | 4.20         |
| [kʰ]           | K             | 33.77                        | 57.78                      | 41.47          | 10.52        |
| [pʰ]           | P             | 33.61                        | 56.98                      | 41.33          | 9.78         |
| [tʰ]           | T             | 33.68                        | 58.06                      | 41.33          | 9.25         |

✅ **File Saved**: `final/plosiveInitials.csv`

---

### **Plosive Finals**
| Tested Allophone   | Tested Phoneme   |   Average Probability *1Million |   S.D. Probability *1Million |   Average Density |   S.D. Density |
|--------------------|------------------|---------------------------------|------------------------------|-------------------|----------------|
| [b̚]                | B                |                           13.71 |                        26.73 |             38.53 |           6.27 |
| [d̚]                | D                |                           21.41 |                        18.87 |             44.93 |           9.98 |
| [g̚]                | G                |                            6.29 |                         8.65 |             38.33 |           4.41 |
| [k̚]                | K                |                           20.16 |                        27.01 |             43.73 |           9.94 |
| [p̚]                | P                |                           20.14 |                        32.89 |             43.73 |           8.83 |
| [t̚]                | T                |                           31.88 |                        16.68 |             48.07 |           9.92 |

✅ **File Saved**: `final/plosiveFinals.csv`

---


### **Devoiced Plosive Finals**
| Tested Allophone | Tested Phoneme | Average Probability *1Million | S.D. Probability *1Million | Average Density | S.D. Density |
|-----------------|---------------|------------------------------|---------------------------|----------------|--------------|
| [b̥]           | B             | 0.53                         | 0.82                       | 2.20           | 0.75         |
| [d̥]           | D             | 0.52                         | 0.14                       | 2.20           | 0.75         |
| [g̥]           | G             | 0.53                         | 0.37                       | 2.20           | 0.75         |

✅ **File Saved**: `final/devoicedPlosives.csv`

---

### **VCV Plosive Finals**
| Tested Allophone   | Tested Phoneme   |   Average Probability *1Million |   S.D. Probability *1Million |   Average Density |   S.D. Density |
|--------------------|------------------|---------------------------------|------------------------------|-------------------|----------------|
| VCV_[b]            | B                |                            5.27 |                         3.6  |              22.2 |           7.44 |
| VCV_[d]            | D                |                            6.85 |                        13.56 |              22.2 |           6.62 |
| VCV_[g]            | G                |                            5.47 |                         4.36 |              22.2 |           7.11 |
| VCV_[kʰ]           | K                |                            5.56 |                         6.65 |              22.2 |           6.97 |
| VCV_[pʰ]           | P                |                            5.46 |                         4.89 |              22.2 |           5.71 |
| VCV_[tʰ]           | T                |                            5.58 |                         5.13 |              22.2 |           8.11 |
✅ **File Saved**: `final/vcvPlosiveFinals.csv`

---

### **Unaspirated Unvoiced Plosive Initials**
| Tested Allophone | Tested Phoneme | Average Probability *1Million | S.D. Probability *1Million | Average Density | S.D. Density |
|-----------------|---------------|------------------------------|---------------------------|----------------|--------------|
| [k]            | K             | 5.94                         | 14.20                      | 19.53          | 5.56         |
| [p]            | P             | 5.91                         | 17.11                      | 19.47          | 4.00         |
| [t]            | T             | 5.91                         | 16.26                      | 19.53          | 5.31         |

✅ **File Saved**: `final/unaspiratedUnvoicedPlosiveInitials.csv`

---

