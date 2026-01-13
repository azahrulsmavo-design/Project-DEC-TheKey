# Data Screening Report

## 1. Jumlah Data (Data Volume)
Based on the initial screening of the CSV files:
- **Student Aptitude Data**: 150 rows, 3 columns.
- **Student Performance Data**: 150 rows, 3 columns.
- **Student Combined Data**: 150 rows, 4 columns.

## 2. Karakteristik Data (Data Characteristics)
The datasets consist of the following structure:

### Student Aptitude (`student_aptitude_data.csv`)
- **Columns**: `student_id`, `course_level`, `aptitude_score`.
- **Types**:
    - `student_id`: Integer (Identifier).
    - `course_level`: String/Object (Categorical: Advanced, etc.).
    - `aptitude_score`: Integer (e.g., 72, 90).

### Student Performance (`student_performance_data.csv`)
- **Columns**: `student_id`, `course_level`, `performance_score`.
- **Types**:
    - `performance_score`: Float (e.g., 3.70, 3.65).

### Student Combined (`student_combined_data.csv`)
- Merged dataset containing all fields: `student_id`, `course_level`, `performance_score`, `aptitude_score`.

## 3. Missing Values
- **Student Aptitude**: 0 missing values.
- **Student Performance**: 0 missing values.
- **Student Combined**: 0 missing values.

## Conclusion
The data is clean (no missing values) and consistent in size (150 records) across all files, ready for further analysis.
