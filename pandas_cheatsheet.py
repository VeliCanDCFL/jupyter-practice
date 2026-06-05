# Pandas Cheat Sheet — Most Used Functions
# Keep this open as a quick reference!

import pandas as pd
import numpy as np

# ============================================================
# 1. CREATING DATAFRAMES / SERIES
# ============================================================
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})          # from dict of lists
df = pd.DataFrame([[1, 2], [3, 4]], columns=['A', 'B']) # from 2D list
s = pd.Series([1, 2, 3])                                # create Series
pd.read_csv('file.csv')                                  # read CSV
pd.read_excel('file.xlsx')                               # read Excel
pd.read_json('file.json')                                # read JSON
pd.read_sql(query, conn)                                 # read from SQL database
pd.DataFrame.from_dict(data)                             # from dict
pd.date_range('2024-01-01', periods=10, freq='D')      # date range
pd.to_datetime(df['col'])                               # convert to datetime

# ============================================================
# 2. INSPECTING DATA
# ============================================================
df.head(n=5)             # first n rows
df.tail(n=5)             # last n rows
df.info()                # column dtypes, non-null counts, memory
df.describe()            # summary stats (numeric cols)
df.describe(include='all')  # summary stats (all cols)
df.shape                 # (rows, cols) as tuple
df.columns               # column names
df.dtypes                # data types of each column
df.index                 # row index
df.values                # underlying numpy array
df.sample(n=5)           # random sample
df.empty                 # True if DataFrame is empty

# ============================================================
# 3. SELECTING / FILTERING DATA
# ============================================================
df['col']               # single column (Series)
df[['col1', 'col2']]    # multiple columns (DataFrame)
df.loc[row_label, col_label]   # label-based indexing
df.iloc[row_idx, col_idx]      # integer-position indexing
df[df['A'] > 5]         # boolean filter
df[(df['A'] > 5) & (df['B'] < 10)]  # multiple conditions
df.query('A > 5 and B < 10')     # query syntax
df.isin([1, 2, 3])      # check if values are in a list
df[df['col'].between(1, 10)]   # range filter
df.dropna()             # drop rows with any NaN
df.dropna(subset=['A']) # drop rows where 'A' is NaN
df.fillna(0)            # replace NaN with 0
df.fillna({'A': 0, 'B': 1})  # fill different cols differently
df.replace('old', 'new')        # replace values

# ============================================================
# 4. MODIFYING DATAFRAMES
# ============================================================
df['new_col'] = [1, 2, 3]           # add new column
df.drop('col', axis=1)               # drop column
df.drop([0, 1], axis=0)              # drop rows by index
df.rename(columns={'old': 'new'})    # rename columns
df.set_index('col')                  # set column as index
df.reset_index()                      # reset index to default
df.assign(new_col=df['A'] + df['B']) # add column via assign
df.astype({'A': int, 'B': str})      # change dtypes

# ============================================================
# 5. SORTING
# ============================================================
df.sort_values('col')                # sort by column (ascending)
df.sort_values('col', ascending=False)
df.sort_values(['A', 'B'])           # sort by multiple columns
df.sort_index()                      # sort by index

# ============================================================
# 6. GROUPBY / AGGREGATIONS
# ============================================================
df.groupby('col').sum()              # group and sum
df.groupby('col').mean()             # group and mean
df.groupby('col').agg({'A': 'sum', 'B': 'mean'})  # multiple agg
df.groupby('col').size()             # count per group
df.groupby('col').count()            # non-null count per group
df.groupby('col').first() / .last()  # first/last value per group
df.pivot_table(values='A', index='B', columns='C', aggfunc='mean')  # pivot

# ============================================================
# 7. MERGING / JOINING
# ============================================================
pd.merge(df1, df2, on='key')                    # inner join (default)
pd.merge(df1, df2, on='key', how='left')        # left join
pd.merge(df1, df2, on='key', how='right')       # right join
pd.merge(df1, df2, on='key', how='outer')       # outer join
pd.concat([df1, df2])                            # stack vertically (rows)
pd.concat([df1, df2], axis=1)                    # stack horizontally (cols)

# ============================================================
# 8. STATISTICS & MATH
# ============================================================
df.sum() / .mean() / .median() / .min() / .max()   # column-wise
df.std() / .var() / .count()                        # std, variance, count
df.cumsum() / .cummax() / .cummin()                 # cumulative
df.diff()                                           # difference between rows
df.pct_change()                                     # percentage change

# ============================================================
# 9. STRING OPERATIONS (Series.str)
# ============================================================
df['col'].str.upper()           # uppercase
df['col'].str.lower()           # lowercase
df['col'].str.strip()           # remove whitespace
df['col'].str.contains('pat')   # check substring
df['col'].str.replace('a', 'b')  # replace substring
df['col'].str.split(',')        # split into lists
df['col'].str.len()             # string length
df['col'].str.extract(r'(\d+)') # regex extraction

# ============================================================
# 10. DATE/TIME OPERATIONS (Series.dt)
# ============================================================
df['col'].dt.year   / .month  / .day
df['col'].dt.hour   / .minute / .second
df['col'].dt.dayofweek       # 0=Monday, 6=Sunday
df['col'].dt.day_name()      # e.g. 'Monday'
df['col'].dt.month_name()    # e.g. 'January'
df['col'].dt.to_period('M')  # convert to period
pd.Grouper(freq='D')         # group by day (in groupby)

# ============================================================
# 11. DROPPING / UNIQUE VALUES
# ============================================================
df.drop_duplicates()                  # remove duplicate rows
df.drop_duplicates(subset=['A'])      # remove dupes based on col A
df['col'].unique()                    # unique values in column
df['col'].value_counts()              # count of each unique value
df['col'].nunique()                   # number of unique values

# ============================================================
# 12. APPLYING FUNCTIONS
# ============================================================
df['col'].apply(lambda x: x * 2)          # element-wise function
df.apply(lambda row: row['A'] + row['B'], axis=1)  # row-wise
df.applymap(lambda x: x ** 2)             # element-wise (DataFrame)

# ============================================================
# 13. HANDLING MISSING DATA
# ============================================================
df.isna() / .isnull()          # boolean mask of NaN
df.notna() / .notnull()        # boolean mask of non-NaN
df.dropna()                    # drop rows with NaN
df.fillna(value)               # fill NaN with value
df.interpolate()               # linear interpolation
df['col'].fillna(df['col'].mean())  # fill with column mean

# ============================================================
# 14. WRITING DATA
# ============================================================
df.to_csv('output.csv', index=False)
df.to_excel('output.xlsx', index=False)
df.to_json('output.json')
df.to_sql('table_name', conn, if_exists='replace')
df.to_parquet('output.parquet')

# ============================================================
# 15. USEFUL PATTERN: GROUPBY → AGGREGATE → FILTER
# ============================================================
# Example: Find groups where mean > threshold
result = (df.groupby('category')['value']
          .mean()
          .loc[lambda x: x > 10]
          .reset_index())

# ============================================================
# 16. COMMON PITFALLS
# ============================================================
# Chained assignment warning → use .loc[] instead:
df.loc[df['A'] > 5, 'B'] = 0    # ✅ correct
# df[df['A'] > 5]['B'] = 0       # ❌ may not work (SettingWithCopyWarning)

# Always check dtypes before operations:
df.dtypes

# Reset index after groupby if needed:
df.groupby('col').mean().reset_index()

# ============================================================
# QUICK REFERENCE: INDEXING SYNTAX
# ============================================================
# df['row_label']['col_name']   → chained (avoid)
# df.loc[row_label, col_name]   → by label ✅
# df.iloc[row_idx, col_idx]     → by position ✅
# df.at[row_label, col_name]    → single scalar (fastest) ✅
# df.iat[row_idx, col_idx]      → single scalar (fastest) ✅
