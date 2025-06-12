Dashboard:  http://172.17.155.14:1080/splash.html#

# Bài 1
	1 + 2 Clean dataset: [dataset](wea)
## Data Processing using MapReduce for Weather Data Analysis
MapReduce is a programming model for processing large-scale data in a distributed manner. It consists of **two main phases**:

1. **Mapper Phase** - Processes input data and emits key-value pairs.
2. **Reducer Phase** - Aggregates the results by key.

Let's implement **MapReduce in Python (using Hadoop Streaming)** to analyze weather data.

---

## **Step 1: Setting Up Hadoop and HDFS**

Before running MapReduce, ensure you have **Hadoop installed** and **HDFS configured**.

1. **Check if Hadoop is running**:
    
    ```bash
    jps
    ```
    
    You should see processes like `NameNode`, `DataNode`, `ResourceManager`, etc.
    
2. **Create a directory in HDFS** for input data:
    
    ```bash
    hdfs dfs -mkdir -p /user/hadoop/weather
    ```
    
3. **Upload your weather dataset**:
    
    ```bash
    hdfs dfs -put weather.csv /user/hadoop/weather/
    ```
    

---

**Data Format:** "Data.Precipitation","Date.Full","Date.Month","Date.Week of","Date.Year","Station.City","Station.Code","Station.Location","Station.State","Data.Temperature.Avg Temp","Data.Temperature.Max Temp","Data.Temperature.Min Temp","Data.Wind.Direction","Data.Wind.Speed"

## **Step 2: Writing the MapReduce Code in Python**

We will create two Python scripts:

- **Mapper**: Extracts relevant weather data.
- **Reducer**: Computes monthly temperature and precipitation averages.

### **Mapper (weather_mapper.py)**

This script reads input data and outputs key-value pairs **(Month-Year, Temperature, Rainfall)**.
```python
#!/usr/bin/env python3
import sys
import csv

for line in sys.stdin:
    line = line.strip()
    reader = csv.reader([line])  # Parse CSV row
    fields = next(reader)  # Extract fields

    if fields[0] == "Data.Precipitation":  # Skip header row
        continue

    try:
        date = fields[1]  # Full Date (e.g., 2016-01-03)
        month_year = date[:7]  # Extract "YYYY-MM"
        temp_avg = float(fields[9])  # Avg Temperature
        precipitation = float(fields[0])  # Precipitation

        print(f"{month_year}\t{temp_avg}\t{precipitation}")
    except ValueError:
        continue  # Skip rows with missing or invalid values
```

**Explanation:**
- Reads CSV input from Hadoop Streaming.s
- Extracts `Date.Full`, `Avg Temp`, and `Precipitation`.
- Emits key-value pairs: `month_year \t temp_avg \t precipitation`.

---

### **Reducer (weather_reducer.py)**
This script calculates the **average temperature and total precipitation** per month.
```python
#!/usr/bin/env python3
import sys

current_month = None
temp_sum = 0
rainfall_sum = 0
count = 0

for line in sys.stdin:
    line = line.strip()
    parts = line.split("\t")

    if len(parts) != 3:
        continue

    month, temp, rainfall = parts

    try:
        temp = float(temp)
        rainfall = float(rainfall)
    except ValueError:
        continue

    if current_month == month:
        temp_sum += temp
        rainfall_sum += rainfall
        count += 1
    else:
        if current_month:
            print(f"{current_month}\t{temp_sum/count:.2f}\t{rainfall_sum:.2f}")

        current_month = month
        temp_sum = temp
        rainfall_sum = rainfall
        count = 1

# Print last month's result
if current_month:
    print(f"{current_month}\t{temp_sum/count:.2f}\t{rainfall_sum:.2f}")
```

**Explanation:**

- Reads **mapper output**.
- Aggregates **temperature and precipitation** for each month.
- Outputs `Month-Year \t Avg Temp \t Total Precipitation`.

---

## **Step 3: Running the MapReduce Job in Hadoop**

1. **Download hadoop-streaming.jar**
```sh
wget https://archive.apache.org/dist/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz
```
Extract the file
```sh
tar -xvzf hadoop-3.3.6.tar.gz
```
Copy JAR to Hadoop's tools dir
```sh
cp hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar /usr/local/hadoop/share/hadoop/tools/lib/
```


2. **Run Hadoop Streaming Job**:
    
```bash
hadoop jar /user/hadoop/hadoop-streaming-3.3.6.jar \
	-input /user/hadoop/weather/weather.csv \
	-output /user/hadoop/weather_output \
	-mapper /user/hadoop/weather/weather_mapper.py \
	-reducer /user/hadoop/weather/weather_reducer.py
```
    
3. **Check output results**:
    
    ```bash
    hdfs dfs -ls /user/hadoop/weather_output
    hdfs dfs -cat /user/hadoop/weather_output/part-*
    ```
    

---

## **Step 4: Understanding the Output**

Expected output format:

```
2016-01   38.45   10.5
2016-02   42.30   12.8
...
```

Where:

- `2016-01` = Year-Month
- `38.45` = Average Temperature for the month
- `10.5` = Total Precipitation for the month

---

## **Summary of Steps**

✅ **Step 1:** Upload data to HDFS  
✅ **Step 2:** Create **Mapper** (extract data)  
✅ **Step 3:** Create **Reducer** (aggregate results)  
✅ **Step 4:** Run **Hadoop Streaming Job**  
✅ **Step 5:** View **final output**

This is the **basic MapReduce workflow** for weather data analysis! 🚀 Let me know if you need further clarifications or enhancements!

