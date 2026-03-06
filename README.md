🏃‍♂️ Marathon Performance & Boston Qualification Analysis (2024)

📌 Project Overview
This project provides a comprehensive end-to-end data analysis of global marathon results from 2024. The primary goal is to identify patterns in runner performance and determine which races offer the highest probability of achieving a Boston Marathon Qualification (BQ).

The analysis covers 188,794 runners across multiple international marathons, excluding outliers and data inconsistencies.

Source: Boston Marathon Qualifiers Dataset (Kaggle) https://www.kaggle.com/datasets/runningwithrock/boston-marathon-qualifiers-dataset?select=Results.csv

🛠️ Tech Stack
Python (Pandas): ETL process, data cleaning, and feature engineering.

SQL (PostgreSQL): Data modeling and advanced analytical querying.

Power BI: Interactive 3-page dashboard with advanced DAX measures and custom tooltips.

📈 Key Business Insights & Findings
1. The "Boston Gap" (Global KPIs)
Global BQ Rate: Only 9.55% of runners achieved the qualification standard.

Average Finish Time: 4.60 hours.

Participation: The data shows a significant gender gap with 109,533 male vs 59,689 female participants.

2. Race Selection Strategy: Volume vs. Probability
The Volume King: London Marathon is the largest "BQ factory," producing 8,870 qualifiers (nearly 50% of the global total in this dataset).

The Smart Bet: For runners seeking the highest probability, Jack and Jill Downhill Marathon leads with a 30.24% BQ Rate, followed by Carmel (20.81%) and Houston (17.41%).

The "Trap" Races: Massive events like Marathon Pour Tous (Paris) and Itabashi City had a 0% BQ Rate, likely due to their recreational or non-competitive nature.

3. The "Endurance Plateau" (Demographics)
Age is just a number: Runners in the 40-44 bracket perform at the exact same level (4.53 hrs average) as those Under 35.

Performance Decay: Significant performance decline only begins after age 50-54, where average times jump from 4.66 hrs to over 6 hrs in older brackets.

4. Geographical Footprint
Top 5 countries by qualifying volume: UK, USA, Spain, Canada, and Italy.

Mexico (MX) ranks in the global Top 10 with 203 qualifiers.

📂 Project Structure
data/: Contains raw and processed CSV files.

scripts/python/: ETL script for data cleaning and BQ logic.

scripts/sql/: SQL queries for exploratory data analysis.

dashboard/: The .pbix file and dashboard screenshots.

🧹 Data Cleaning Highlights (ETL)
Converted finish times from seconds to decimal hours for better visualization.

Outlier Removal: Identified and removed "Flash" runners (Finish = 0) which represented timing chip errors.

Data Consistency: Corrected geographical mapping errors (e.g., Soviet Union 'SU' codes mapped incorrectly by GIS tools).

Exclusion Criteria: Excluded the Boston Marathon itself to avoid biasing the "Qualification Rate" metrics.


This dashboard serves as a strategic tool for competitive runners to choose their next race based on data-driven probabilities rather than brand popularity alone.
