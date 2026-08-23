import pandas as pd

#1. Load the raw data
print("Loading raw data...")
df = pd.read_csv("Global_Superstore2.csv", encoding='windows-1252')

# 2. Basic Cleaning: Drop completely empty rows
df = df.dropna(how='all')

# 3. Standardize Column Names (replace spaces with underscores, make lowercase)
df.columns = df.columns.str.replace(' ', '_').str.lower()
df.columns = df.columns.str.replace('-', '_')

# 4. Check for duplicates and drop them
duplicate_count = df.duplicated().sum()
print(f"Found {duplicate_count} duplicate rows. Removing...")
df = df.drop_duplicates()

# 5. Save the clean data
df.to_csv('Superstore_Cleaned.csv', index=False)
print("Data cleaned and saved as 'Superstore_Cleaned.csv'!")