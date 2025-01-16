Average Income of each Company each years. 
```python
mean_income_yearly = df.groupby(['Company', 'Year'])['Income'].mean().reset_index(name='MeanIncome')
mean_income_yearly
```

Tính Revenue trung bình của từng Company qua các Year
```python
# Ensure the 'Revenue' column is numeric
df['Revenue'] = pd.to_numeric(df['Revenue'], errors='coerce') # convert N.A to NaN

# Group by 'Company' and calculate the mean of 'Revenue'
mean_revenue_yearly = df.groupby(['Company', 'Year'])['Revenue'].mean().reset_index(name='MeanRevenue')

mean_revenue_yearly
```


```python
company_mean = pd.merge(mean_income_yearly, mean_revenue_yearly, on=['Company', 'Year'])

company_mean.head()
```

**Sort by Values**
```python
import pandas as pd

# Sample DataFrame
data = {'Company': ['A', 'B', 'C', 'D'], 'Income': [1000, 2000, 1500, 3000]}
df = pd.DataFrame(data)

# Sort the DataFrame by the 'Income' column in ascending order
sorted_df = df.sort_values(by='Income')

print(sorted_df)
```

