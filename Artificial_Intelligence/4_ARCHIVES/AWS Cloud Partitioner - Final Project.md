![[Pasted image 20260420202735.png]]
[source code](https://github.com/undertanker86/Vietnam-Air-Quality-Data-Pipeline)
Lưu ý S3 Bucket - là global service -> **Ko đc đặt tên Bucket giống nhau.**

Data Source -> Ingestion -> Storage (Bronze) -> Processing (Silver) -> Aggregation (Gold) -> Quality Check -> Analytics
+ ! Setup permission/policy for Lambda 
+ ! Data Crawl from BronzeBucket S3
+ ? ask: Data Ingestion (API registration)

**Air Quality Open Data Platform:** https://aqicn.org/data-platform/token-confirm/80b6c597-5c52-430d-aad0-57a2aa27c501

**setup AWS secret key**
![[Pasted image 20260420210932.png]]
```python
# Use this code snippet in your app.
# If you need more information about configurations
# or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developer/language/python/

import boto3
from botocore.exceptions import ClientError


def get_secret():

    secret_name = "WAQI_API_TOKEN"
    region_name = "ap-southeast-2"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    secret = get_secret_value_response['SecretString']

    # Your code goes here.
```
![[Pasted image 20260420210752.png]]

additional role to run Lambda function 
![[Pasted image 20260420211322.png]]

copy arn secret
![[Pasted image 20260420211526.png]]



![[Pasted image 20260420211539.png]]
![[Pasted image 20260420211554.png]]

Policy Name: AllowLambdaGetSecret
-> Create Policy (AllowLambdaSNS2S3) -> Add to Role
	Policy có thể update chậm. Có thể rerun để đảm bảo nó chạy. 
![[Pasted image 20260420212305.png]]
Thiếu quyền thì tạo policy rồi thêm từng quyền cần 1. 
Policy 4th: Write -> PutObject

**Create Schedule (Event Bridge) for Lambda**
**AWS Glue Crawler** craw data from S3 bronze
```python
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
job.commit()
```


Error line 87 - bronze_to_silver_statistics_api
-> chỉnh lại param thành api_raw của `--bronze_table`
![[Pasted image 20260420215853.png]]
-> tương tự chỉnh lại cái bronze_to_silver_statistics_csv.py

![[Pasted image 20260420220108.png]]
historical_air_quality_2021_en_

![[Pasted image 20260420220429.png]]
-> Get/PutObject
-> setrup arn of each bucket for this roles

--bronze_database
--bronze_table
--silver_bucket
--silver_database
--bronze_bucket
--sns_topic_arn
s3://athena-etl-query/


Athena Full Access
![[Pasted image 20260420222459.png]]
Cập nhật data lên gold => tháng chạy 1 lần.

ARN in IAM - arn:aws:s3:::data-pipeline-bronze-ap-dev/*


### Athena Compatibility Fix
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

Policy có thể chèn lên nhau.
Phân các policy riêng biệt cho S3, SNS, etc...