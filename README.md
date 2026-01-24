# Student Performance and Aptitude Analysis
**The Key English Course Company - Indonesia**

A comprehensive statistical analysis validating course placement effectiveness at The Key English Course Company.

<p align="center">
  <img src="assets/the_key.png" alt="The Key" width="400" />
</p>

## Project Overview
This project presents a rigorous statistical analysis of 150 students across three English course levels (Advanced, Intermediate, Foundation) to validate the effectiveness of The Key's course placement system. The study examines the relationship between aptitude test scores and actual performance to ensure students are placed in appropriate learning environments.

## Research Questions
1. Do students with different performance levels enroll in different course levels?
2. Are there significant differences in aptitude scores across course levels?
3. What is the correlation between aptitude scores and performance?
4. What are the implications for course placement and program quality?

## Repository Contents
```
.
├── README.md                  # This file
├── assets/                    
│   └── the_key.png            # Company logo
├── Final_Analysis.ipynb       # Analysis report
├── Final_Analysis.pdf         # Full analysis report (PDF)
├── data/
│   └── student_combined_data.csv # Dataset
└── requirements.txt           # Python dependencies
```

## Dataset Description

### Sample Characteristics
- **Total Students**: 150
- **Sample Distribution**: 50 students per course level
- **Sampling Method**: Stratified random sampling
- **Data Completeness**: No missing values

### Variables
| Variable | Type | Description | Range |
|----------|------|-------------|-------|
| student_id | Integer | Unique student identifier | 1-150 |
| course_level | Categorical | Course enrollment level | Advanced, Intermediate, Foundation |
| performance_score | Float | Academic achievement score | 1.55 - 3.80 (4-point scale) |
| aptitude_score | Integer | Language aptitude test score | 9 - 97 (max 126) |

## Key Results Summary

### Descriptive Statistics
| Level | Performance Mean | Performance SD | Aptitude Mean | Aptitude SD |
|-------|------------------|----------------|---------------|-------------|
| Advanced | 3.239 | 0.384 | 67.46 | 19.17 |
| Intermediate | 2.518 | 0.392 | 42.74 | 18.28 |
| Foundation | 1.865 | 0.177 | 22.52 | 7.03 |

### ANOVA Results
| Variable | F-statistic | df | p-value | η² (Effect Size) |
|----------|-------------|----|---------|-------------------|
| Performance | 213.43 | (2, 147) | < 0.001*** | 0.744 (Large) |
| Aptitude | 101.17 | (2, 147) | < 0.001*** | 0.579 (Large) |

### Correlation
| Relationship | r | p-value | Interpretation |
|--------------|---|---------|----------------|
| Performance ↔ Aptitude | 0.887 | < 0.001*** | Very Strong Positive |

## Getting Started

### Required Packages
- `pandas>=1.3.0`
- `numpy>=1.21.0`
- `scipy>=1.7.0`
- `matplotlib>=3.4.0`
- `seaborn>=0.11.0`
- `statsmodels>=0.13.0`
- `jupyter>=1.0.0`

### Notebook Structure
The Jupyter notebook (`Final_Analysis.ipynb`) mirrors the PDF report and includes:
1. Chapter 1: Introduction & Data Loading
2. Chapter 2: Data Overview & Quality Checks
3. Chapter 3: Descriptive Statistics
4. Chapter 4: Assumption Testing
5. Chapter 5: ANOVA Analysis
6. Chapter 6: Post-Hoc Tests
7. Chapter 7: Correlation Analysis
8. Chapter 8: Effect Sizes
9. Chapter 9: Visualizations
10. Chapter 10: Summary & Conclusions

Each chapter includes:
- ✅ Complete Python code
- ✅ Detailed explanations
- ✅ Statistical interpretations
- ✅ Visualization outputs
- ✅ Result verification

## Documentation
See `Final_Analysis.pdf` for the full 50-page analysis report with:
- Executive summary
- Detailed methodology
- Comprehensive results
- Practical recommendations
- Glossary of terms

---
*Last Updated: 13 January 2026 | Version: 1.0*
