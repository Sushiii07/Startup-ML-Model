import pandas as pd

df = pd.read_csv('50_Startups.csv')

# Check for NULL values
print(pd.isnull(df))

# OR

# In the below method we can see number of entries matches number of non-null values
# Therefore, number of NULL values is 0
print(df.info())

# Removing rows containing any NULL values
df2 = df.dropna()

# Check for duplicated values
print(df2.duplicated())
# Number of duplicated values
print("Number of duplicate rows =", df2.duplicated().sum())

# Removing duplicate rows (if any)
df.drop_duplicates(inplace=True)
# "inplace" rewrites te data the data in the same dataset and not create a separate dataset (like I did when creating "df2").

# Final Data
print(df2)
