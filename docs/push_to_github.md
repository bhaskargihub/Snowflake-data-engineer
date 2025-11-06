# How to push this project to GitHub (step-by-step)

1. Create an empty repo on GitHub named `Snowflake-data-engineer`
2. On your local machine:
   ```bash
   git clone https://github.com/yourusername/Snowflake-data-engineer.git
   cd Snowflake-data-engineer
   # copy files from this project into that folder or set remote to your repo
   git add .
   git commit -m "Initial commit - Snowflake data engineer project"
   git push origin main
   ```
3. If you prefer to push to an existing repo (your repo), change remote:
   ```bash
   git remote add origin https://github.com/bhaskargihub/Snowflake-data-engineer.git
   git push -u origin main
   ```
