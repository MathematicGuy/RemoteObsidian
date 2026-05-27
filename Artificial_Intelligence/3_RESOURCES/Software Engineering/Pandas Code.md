**Data Frame**
>How .csv data are represent using pandas
```python
{
  'name': ['Alice', 'Bob', 'Charlie'],
  'score': [95, 85, 78]
}
```
>To turn dictionary to dataframe, simply use `pd.DataFrame()`

**Read Files**
- `pd.read_csv('file.csv')` loads CSV files.
- `pd.read_excel('file.xlsx')` loads Excel files (you often need the `openpyxl` or `xlrd` library installed).
- `pd.read_json('file.json')` for JSON.
- There are also methods like `pd.read_sql(...)` for SQL queries.

**Find index** of **max/min value** -> `.idxmax()`, `.idxmin()`
**Find max/min value** -> `max()`, `min()`
	
**Indexing**
>Retrieve data by index
- `df.loc['label_name']` is label-based indexing (looking up by row label or column label) - *loc mean location* 
- `df.iloc[index_range, label_name/label_index]` is integer-based indexing (like standard Python indexing using row number or position) - *iloc mean index location*
+ ? Example `.iloc()`: Accessing first 5 rows of the data frame
	**Method 1:** `df_student[['name', 'score']].head()`
	**Method 2:** `df_student.iloc[0:5, [0, 1]]` where `name` is column 0 and `score` is column 1.


### Indexing
Common usage patterns:
- **Selecting a single row by label:** `df.loc['row_label']`
- **Selecting a single column by label:** `df.loc[:, 'column_label']`
- **Selecting a specific cell by row and column labels:** `df.loc['row_label', 'column_label']`
- **Selecting multiple rows by a list of labels:** `df.loc[['label1', 'label2']]`
- **Selecting multiple columns by a list of labels:** `df.loc[:, ['col1', 'col2']]`
- **Slicing rows by label:** `df.loc['start_label':'end_label']`
- **Slicing columns by label:** `df.loc[:, 'start_column':'end_column']`
- **Conditional selection using a boolean array:** `df.loc[df['column_name'] > value]`

```python
df2 = pd.read_csv(dataset_path, index_col=['Title', 'Year'])
get_cols = df2.loc[(slice(None), 2010), ['Rank', 'Genre']]
get_cols.head()
```
![[Pasted image 20250804163442.png# left |355]]

