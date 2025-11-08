# Snowflake Data Masking Project

### Overview
This project demonstrates Dynamic Data Masking in Snowflake using masking policies to protect sensitive employee data (Email and Salary).

### Project Structure
- `sql_scripts/`: SQL setup scripts
- `documentation/`: Project guide (PDF) and diagram
- `README.md`: Quick instructions

### Steps to Run
1. Run SQL scripts in numerical order (use a user with CREATE MASKING POLICY privilege).
2. Test masking behavior by switching roles between `FULL_ACCESS_ROLE` and `LIMITED_ACCESS_ROLE`.

### GitHub Setup
```bash
git init
git add .
git commit -m "Initial commit - Snowflake Data Masking Project"
git branch -M main
git remote add origin https://github.com/<your-username>/snowflake_data_masking_project.git
git push -u origin main
```

### Verification
- FULL_ACCESS_ROLE → Sees actual data
- LIMITED_ACCESS_ROLE → Sees masked or null values
