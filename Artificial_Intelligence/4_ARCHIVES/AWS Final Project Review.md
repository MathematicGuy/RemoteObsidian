Link quiz: [https://forms.gle/r6th82mQMwqooATr7](https://forms.gle/r6th82mQMwqooATr7)
![[Pasted image 20260421175848.png]]
Input: `.csv` file, weather_data from Vietnam Weather API (make sure to register to get API key). 

![[Pasted image 20260421175945.png | 688]]
**Create 3 S3 buckets** naming from bronze -> silver -> gold. Throw the raw data to bronze S3 bucket for data processing. 
	note: save S3 buckets `arn` address for setup permission later. Each service in AWS have a `arn` acting as a ID, so you can connect service A->B and setup IAM policies for a service using `arn`. 

**Create data_ingestion lambda func**
Add API key to `aws Secret Manager` -> save secret key arn.
Setup `data_ingestion` in AWS Lambda (roles create automatically upon creating a lambda service) -> create policies that allow Read and Write for S3 to Bucket for `data_ingestion` IAM role -> setup env params in configuration, for weather API by setup its param as Secret Key ARN you save.     
Setup `aws SNS` for sending "lambda func running output" to your gmail -> add AWS SNS to `data_ingestion` lambda function in lambda configuration -> test run Lambda Function to see Lambda output email to our setup Gmail in `aws SNS`. 
Setup `aws EventBridge` to auto-run AWS Lambda `data_ingestion` function every `X` hours, this is for update .csv dataset with new data every morning.
![[Pasted image 20260421193709.png | 344]]

**Setup data crawler** in `aws Glue` to process raw_data from `.csv` file within the S3 Bronze Bucket to AWS Glue so we could start Processing data from Bronze to Sivler then from Silver to Gold. This should create 3 database, each with different tables and schemas. 

There're 3 files to setup in ETL pipeline within `aws Glue` -> `bronze_to_silver_statistic_api`, `bronze_to_silver_statistic_csv` and `sivler_to_gold_analytics`. Create them and setup the parameters base on which service they used.
![[Pasted image 20260421193901.png]]
+ ! These 3 `Glue job` **use 1 IAM role** created by glue -> setup IAM policies that allow read/write/put Object from the 3 S3 buckets (bronze, silver, gold) and SNS service (Publish). 

Finally,
+ setup `quality_data` lambda function to make check data and send warning message if any problem -> allow Put/Read/Write S3, Publish SNS and read Secret Manager permisson in `quality data` IAM roles policies. 
+ setup AWS Athena to query data from `aws Glue` using Athena SQL format.
![[Pasted image 20260421180004.png]]
setup `aws Step Functions`, make sure to `.json` file match the `arn` address of your service. 
![[Pasted image 20260421180027.png | 777]]

---

**Test Athena Query as a DS**
```sql
SELECT
    COUNT(*) AS total_rows,
    SUM(CASE WHEN aqi IS NULL THEN 1 ELSE 0 END) AS null_aqi,
    SUM(CASE WHEN measured_at IS NULL THEN 1 ELSE 0 END) AS null_measured_at,
    SUM(CASE WHEN dominant_pollutant IS NULL THEN 1 ELSE 0 END) AS null_dominant_pollutant,
    SUM(CASE WHEN queried_city IS NULL THEN 1 ELSE 0 END) AS null_queried_city,
    SUM(CASE WHEN aqi < 0 OR aqi > 500 THEN 1 ELSE 0 END) AS aqi_out_of_range,
    ARRAY_AGG(DISTINCT queried_city) AS distinct_cities,
    ARRAY_AGG(DISTINCT source) AS distinct_sources
FROM fact_aqi;


SELECT COUNT(*) AS fresh_rows
FROM fact_aqi
WHERE from_iso8601_timestamp(ingested_at)
      >= current_timestamp - INTERVAL '48' HOUR;


SELECT
    COUNT(*) AS total_stations,
    ARRAY_AGG(DISTINCT queried_city) AS station_cities
FROM dim_station;
```

`ROW_NUMBER` example
```sql
SELECT 
    queried_city, 
    ROW_NUMBER() OVER (
        ORDER BY max_aqi DESC, 
        queried_city ASC -- This is your tie-break
    ) AS aqi_rank, 
    max_aqi
FROM "glue-pipeline-gold-dev"."gold_aqi_daily_summary";
```
without row number
```sql
SELECT
    avg_aqi,
    max_aqi,
    aqi_rank
FROM "glue-pipeline-gold-dev"."gold_aqi_city_ranking"
ORDER BY avg_aqi DESC;
```
-> city with the tie max_sql have different rank e.g. 1,1

Bước freshness check dùng điều kiện ‘ingested_at >= cutoff‘. Khi dữ liệu quá lớn, tối ưu nào là đúng nhất để giảm scan ?
```sql
SELECT COUNT(*) AS fresh_rows
FROM fact_aqi
WHERE from_iso8601_timestamp(ingested_at)
      >= current_timestamp - INTERVAL '48' HOUR;
```
+ ! `from_iso8601_timestamp(ingested_at)` khiến Athena phải đọc toàn bộ bảng và chạy hàm chuyển đổi cho từng dòng một.
+ $ Nếu bảng của bạn được partition (phân vùng) theo thời gian (ví dụ: cột `dt`, `year/month/day`), bạn **bắt buộc** phải đưa các cột partition này vào `WHERE`. Đây là cách duy nhất để Athena bỏ qua hoàn toàn các file cũ.
```sql
SELECT COUNT(*) AS fresh_rows
FROM fact_aqi
WHERE ingested_at >= format_datetime(current_timestamp - INTERVAL '48' HOUR, 'yyyy-MM-dd''T''HH:mm:ss');
```

*Bookmark* in AWS Glue -> *re-run at the previous data processing job* (bookmark job)
*Vì sao gắn `.flag` trong cho `.csv` file trong Glue ?*  
Tránh xử lý dữ liệu dở (Partial Data) trong AWS Glue. Vì Job Bookmark có thể thấy 50 file đã xog và bắt đầu ngay. *Nếu 50 file còn lại cùng 1 batch* thì sẽ bị *mất tính toàn vẹn dữ liệu.*
-> File `.flag` chỉ được ghi sau khi **tất cả** các file CSV của lô đó đã upload thành công

+ ? Compare to `.flag` -> `.flag` help control logic in each specific folder/batch.
+ $ có thể xóa cờ ở một folder nhất định để ép Job xử lý lại vùng đó mà không cần can thiệp vào hệ thống bookmark phức tạp của Glue.

