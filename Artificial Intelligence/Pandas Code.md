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

---

Describe count, mean, std, min, and value at 25%, 50%, 75% 
```python
iris.describe()
```
![[Pasted image 20250203150852.png]]


