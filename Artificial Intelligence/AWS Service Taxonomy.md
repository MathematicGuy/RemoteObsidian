## **1. Dịch vụ Tính toán (Compute Services)**

- **Amazon EC2 (Elastic Compute Cloud):** Cung cấp máy chủ ảo (instance) có khả năng mở rộng trong cloud.
- **AWS Lambda:** Dịch vụ serverless chạy code theo sự kiện mà không cần quản lý server.
- **Amazon ECS (Elastic Container Service):** Dịch vụ quản lý container có khả năng mở rộng cao, hỗ trợ Docker.
- **AWS Fargate:** Engine serverless cho container, hoạt động với ECS hoặc EKS.
- **AWS Batch:** Cho phép chạy hàng trăm nghìn job batch.
- **Amazon Lightsail:** Cung cấp VPS, storage và networking để triển khai website đơn giản.
- **AWS Outposts:** Chạy dịch vụ AWS tại on-premise, hỗ trợ hybrid cloud.

---

## **2. Dịch vụ Lưu trữ (Storage Services)**

- **Amazon S3 (Simple Storage Service):** Lưu trữ object có khả năng mở rộng cho backup, archive và hosting web tĩnh.
- **Amazon EBS (Elastic Block Store):** Lưu trữ dạng block hiệu năng cao cho EC2.
- **Amazon EFS (Elastic File System):** Hệ thống file NFS có khả năng mở rộng dùng cho AWS và on-premise.
- **Amazon S3 Glacier / Glacier Deep Archive:** Lưu trữ chi phí thấp cho dữ liệu dài hạn.
- **AWS Storage Gateway:** Kết nối hybrid giữa on-premise và cloud storage.
- **AWS Snow Family (Snowball, Snowmobile):** Thiết bị vật lý để migrate dữ liệu lớn (petabyte/exabyte).
- **Amazon EC2 Instance Store:** Lưu trữ tạm thời (ephemeral) gắn trực tiếp vào host.

---

## **3. Dịch vụ Cơ sở dữ liệu (Database Services)**

- **Amazon RDS (Relational Database Service):** Dịch vụ database quan hệ managed (Aurora, MySQL, PostgreSQL, MariaDB, Oracle, SQL Server).
- **Amazon Aurora:** Database quan hệ tương thích MySQL/PostgreSQL, tối ưu cho cloud.
- **Amazon DynamoDB:** NoSQL key-value/document fully managed.
- **Amazon Redshift:** Data warehouse phân tích dữ liệu bằng SQL.
- **Amazon ElastiCache:** Cache in-memory (Redis/Memcached) tăng hiệu năng.
- **Amazon Neptune:** Graph database.
- **Amazon DocumentDB:** Database tương thích MongoDB.

---

## **4. Mạng & Phân phối nội dung (Networking & Content Delivery)**

- **Amazon VPC (Virtual Private Cloud):** Mạng riêng ảo trong AWS.
- **Amazon CloudFront:** CDN toàn cầu, giảm độ trễ khi phân phối nội dung.
- **Amazon Route 53:** DNS scalable và domain registrar.
- **AWS Global Accelerator:** Tăng hiệu năng và availability bằng mạng AWS global.
- **AWS Direct Connect:** Kết nối private từ on-premise đến AWS.
- **AWS VPN (Site-to-Site & Client):** Kết nối mã hóa giữa network và AWS.
- **AWS Transit Gateway:** Hub kết nối nhiều VPC và on-premise.
- **Elastic Load Balancing (ALB, NLB, CLB):** Phân phối traffic đến nhiều target.
- **AWS PrivateLink:** Kết nối private giữa VPC và service mà không ra Internet.

---

## **5. Quản lý, Governance & Billing**

- **AWS Organizations:** Quản lý nhiều account, hỗ trợ consolidated billing.
- **AWS CloudTrail:** Ghi log API và hoạt động user.
- **AWS Config:** Theo dõi cấu hình tài nguyên và compliance.
- **Amazon CloudWatch:** Monitoring và observability (logs, metrics, alarms).
- **AWS Trusted Advisor:** Khuyến nghị tối ưu theo best practices.
- **AWS Budgets:** Thiết lập ngân sách và cảnh báo.
- **AWS Cost Explorer:** Phân tích và dự đoán chi phí.
- **AWS CloudFormation:** Infrastructure as Code.
- **AWS Systems Manager:** Quản lý vận hành tài nguyên tập trung.
- **AWS Personal Health Dashboard / Service Health Dashboard:** Cảnh báo sự cố dịch vụ.
- **AWS Artifact:** Truy cập báo cáo compliance.
- **AWS Control Tower:** Thiết lập môi trường multi-account chuẩn.
- **AWS Well-Architected Tool:** Đánh giá workload theo best practices.

---

## **6. Bảo mật, Identity & Compliance**

- **AWS IAM:** Quản lý truy cập và quyền.
- **AWS Shield / Shield Advanced:** Bảo vệ DDoS.
- **AWS WAF:** Firewall cho web app.
- **Amazon GuardDuty:** Phát hiện mối đe dọa bảo mật.
- **Amazon Macie:** Phát hiện dữ liệu nhạy cảm trong S3 bằng ML.
- **Amazon Inspector:** Đánh giá lỗ hổng bảo mật.
- **AWS KMS:** Quản lý key mã hóa.
- **AWS Secrets Manager:** Quản lý secret (API key, DB credentials).
- **AWS CloudHSM:** Thiết bị HSM chuyên dụng.
- **AWS Certificate Manager (ACM):** Quản lý SSL/TLS.
- **Amazon Cognito:** Authentication & user management.
- **AWS Security Hub:** Tổng hợp cảnh báo bảo mật.

---

## **7. Tích hợp ứng dụng & Developer Tools**

- **Amazon SNS:** Messaging (push notification).
- **Amazon SQS:** Message queue để decouple hệ thống.
- **Amazon SES:** Dịch vụ email.
- **AWS CLI / SDK:** Công cụ lập trình và command line.
- **AWS CodeCommit:** Source control.
- **AWS CodeBuild:** Build code.
- **AWS CodeDeploy / CodePipeline:** CI/CD pipeline.
- **AWS Elastic Beanstalk:** PaaS deploy web app.
- **AWS X-Ray:** Trace request để debug performance.

---

## **8. Phân tích dữ liệu & Machine Learning**

- **Amazon Athena:** Query dữ liệu S3 bằng SQL.
- **Amazon EMR:** Big data processing (Hadoop).
- **Amazon Kinesis:** Xử lý streaming data realtime.
- **Amazon QuickSight:** Business Intelligence.
- **Amazon Rekognition:** Phân tích ảnh/video bằng ML.
- **Amazon Polly:** Text-to-speech.
- **Amazon Transcribe / Translate / Comprehend / Lex:** Speech-to-text, dịch, NLP, chatbot.

---

## **9. Ứng dụng doanh nghiệp & Tương tác khách hàng**

- **Amazon Connect:** Contact center trên cloud.
- **AWS Marketplace:** Chợ phần mềm bên thứ ba.
- **AWS Professional Services / APN:** Đội ngũ tư vấn triển khai cloud.
- **AWS Support Plans:** Các gói hỗ trợ (Basic, Developer, Business, Enterprise), bao gồm **TAM (Technical Account Manager)** và **Support Concierge**.