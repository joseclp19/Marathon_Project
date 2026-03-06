import pandas as pd
import datetime

# 1. Load 2024 Data
print("Cargando archivo de 2024...")
df_results = pd.read_csv("Results_2024.csv", low_memory=False) 
df_bq = pd.read_csv("BQStandards.csv")

# Ensure 'Finish' is numeric to be able to search for 0
df_results['Finish'] = pd.to_numeric(df_results['Finish'], errors='coerce')

# Identify races that have at least one runner with Finish == 0
races_with_zero = df_results[df_results['Finish'] == 0]['Race'].unique()
print(f"Carreras eliminadas por tener corredores 'Flash': {races_with_zero}")

# Filter the DataFrame to remove the ENTIRE race if it's in that list
df_results = df_results[~df_results['Race'].isin(races_with_zero)]

# 2. Remove Boston Marathon
df_results = df_results[~df_results['Race'].str.contains("Boston", case=False, na=False)]

# 3. Force the 'Age' column to be numeric
print("Limpiando edades...")
df_results['Age'] = pd.to_numeric(df_results['Age'], errors='coerce')

# 4. Create age brackets
bins = [0, 34, 39, 44, 49, 54, 59, 64, 69, 74, 79, 120]
labels = ['Under 35', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80 and Over']
df_results['Age Bracket'] = pd.cut(df_results['Age'], bins=bins, labels=labels, right=True)

# 5. Merge with Boston standards
print("Cruzando con estándares de Boston...")
df_master = pd.merge(df_results, df_bq, on=['Gender', 'Age Bracket'], how='left')

# 6. Determine qualification (BQ)
df_master['BQ_Qualifier'] = df_master['Finish'] <= df_master['Standard']

# 7. Format times
print("Formateando tiempos...")
df_master['Finish_Time'] = pd.to_timedelta(df_master['Finish'], unit='s')
df_master['Finish_Time_Str'] = df_master['Finish_Time'].apply(
    lambda x: str(datetime.timedelta(seconds=x.total_seconds())) if pd.notnull(x) else '00:00:00'
)

# 8. Final Cleaning of Null Values
df_master['City'] = df_master['City'].fillna('Unknown')
df_master['State'] = df_master['State'].fillna('Unknown')

# 9. Export
output_file = "Results_2024_Clean_BQ.csv"
df_master.to_csv(output_file, index=False)
print(f"¡Listo! Archivo guardado como: {output_file}")