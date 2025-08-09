1) **Tóm tắt kiến thức (Những phần chính muốn học)**
	Pandas Command + Làm Quizz trước để hiểu tổng quan
	Movie Dataset
	Time Series Dataset
	
2) **Cài đặt thư viện và set-up folder dự án**
3) **Xác định ideas flow và code.**

**What Pandas for ?**
1. Loading the Data  
2. Preparing the Data  
3. Manipulating the Data  
4. Modeling the Data  
5. Analyzing the Data

### Pandas vs Numpy 
1. **CORE TYPES** (in data)
	**Numpy:** accept Homogeneous data type, meaning they only contain 1 dtype) thus offer faster indexing. 
	**Pandas:** accept Heterogeneous data, this mean they can contain multiple dtype) - Series Object data type (Basically python dictionary or a list, its flexible)
	+ ? In short, **Numpy are faster in indexing and performance** for numerical computation but **Pandas are more flexible** which use both integer and labeled indexing.  
```python
>> d = {'a': 1, 'b': ['A', 'B', 'C'], 'c': 3}
>> ser = pd.Series(data=d, index=['a', 'b', 'c'])
>> ser
a   1
b   ['A', 'B', 'C']
c   3
dtype: int64
```

2. **DATA HANDLING:**
	**Numpy** are optimized for performing vectorized/numerical operations 
	**Pandas Series** offer *more functionality for data* malnipulation, alignment, handling missing data and most important time-series.  

3. **INDEXING:**
	A key distinction lies in the **indexing system**: **NumPy arrays** use an **implicitly** (1 type) defined integer index, **suitable for ordered data access**. In contrast, **pandas Series** feature an **explicitly** (multi-types) defined index associated with each element, offering **numeric or label-based indexing for enhanced data manipulation and retrieval flexibility.**
  
4. **PERFORMANCE & MEMORY USAGE** 
	Pandas hold multiple datatype while Numpy hold uniform data type -> Numpy are more memory efficient and performance.

5. **USE CASES**
	**Pandas Seires for Data Processing and Manipulation** especially tabular data like Excel spreadsheets or SQL tables.    
	**Numpy for Task with Processed Data** - Task require high-performace computing and numerical analysis without the need for data manipulation

Data Structures in Python Pandas
![[Pasted image 20250803204245.png]]

**Combine condition pandas**
```python
df[(df['HP'] >= 60) & (df['Type 2'] == 'Poison')]
```

Initialize pd Series with customize index
```python
s = pd.Series([3, -5, 7, 4], index=[‘a’, ‘b’, ‘c’, ‘d’])
```
*![[Pasted image 20250804112330.png]]*



