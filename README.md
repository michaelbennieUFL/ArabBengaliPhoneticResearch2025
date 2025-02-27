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
| Tested Allophone | Tested Phoneme | Average Probability *1Million | S.D. Probability *1Million | Average Density | S.D. Density |
|-----------------|---------------|------------------------------|---------------------------|----------------|--------------|
| [b̚]           | B             | 13.78                        | 26.70                      | 38.20          | 6.33         |
| [d̚]           | D             | 20.88                        | 18.84                      | 45.13          | 10.09        |
| [g̚]           | G             | 6.25                         | 8.68                       | 38.73          | 4.17         |
| [k̚]           | K             | 19.51                        | 27.19                      | 43.87          | 10.78        |
| [p̚]           | P             | 19.41                        | 33.69                      | 43.93          | 8.35         |
| [t̚]           | T             | 33.56                        | 19.10                      | 50.60          | 6.41         |

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
| Tested Allophone | Tested Phoneme | Average Probability *1Million | S.D. Probability *1Million | Average Density | S.D. Density |
|-----------------|---------------|------------------------------|---------------------------|----------------|--------------|
| VCV_[b]        | B             | 3.79                         | 3.73                       | 22.80          | 9.87         |
| VCV_[d]        | D             | 3.22                         | 1.90                       | 22.80          | 9.93         |
| VCV_[g]        | G             | 3.89                         | 4.30                       | 22.80          | 9.74         |
| VCV_[kʰ]      | K             | 3.78                         | 4.58                       | 22.80          | 9.26         |
| VCV_[pʰ]      | P             | 5.46                         | 4.89                       | 22.20          | 5.71         |
| VCV_[tʰ]      | T             | 3.72                         | 4.98                       | 22.80          | 9.81         |

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

