1. Bản phân tích sơ bộ controller users.js:
Dựa trên mã nguồn VueJS đã cung cấp, chúng ta có thể thực hiện phân tích thiết kế sử dụng UML để hiểu cách hệ thống hoạt động và tương tác giữa các thành phần. Dưới đây là một phân tích UML đơn giản bằng tiếng Việt:

### Phân tích UML:

#### 1. Biểu đồ lớp (Class Diagram):
- **UserModel (Người dùng):**
  - Thuộc tính: _id, username, password, email, status
  - Phương thức: Không có
  
#### 2. Biểu đồ use case (Use Case Diagram):
- **Actor (Diễn viên):** Admin/User
- **Các Use Case (Trường hợp sử dụng):**
  1. Xem danh sách người dùng
  2. Tạo người dùng mới
  3. Xem chi tiết người dùng
  4. Vô hiệu hóa người dùng
  5. Xóa người dùng
  6. Cập nhật thông tin người dùng
  
#### 3. Biểu đồ trình tự (Sequence Diagram):
- **Kịch bản 1: Xem danh sách người dùng:**
  - Diễn viên: Admin/User
  - Hệ thống: UserController
  - Hành động:
    - Admin/User gửi yêu cầu để lấy danh sách người dùng.
    - UserController truy vấn tất cả người dùng đang hoạt động từ UserModel.
    - UserController gửi danh sách người dùng lại cho Admin/User.
  
- **Kịch bản 2: Tạo người dùng mới:**
  - Diễn viên: Admin/User
  - Hệ thống: UserController
  - Hành động:
    - Admin/User gửi yêu cầu để tạo người dùng mới với thông tin người dùng.
    - UserController tạo một bản ghi mới của UserModel với thông tin được cung cấp.
    - UserController lưu người dùng mới vào cơ sở dữ liệu.
    - UserController gửi lại dữ liệu người dùng mới đã tạo cho Admin/User.
  
- **Kịch bản 3: Xem chi tiết người dùng:**
  - Diễn viên: Admin/User
  - Hệ thống: UserController
  - Hành động:
    - Admin/User gửi yêu cầu để xem chi tiết của một người dùng cụ thể.
    - UserController truy xuất thông tin người dùng từ UserModel dựa trên ID của người dùng.
    - UserController gửi lại chi tiết người dùng cho Admin/User.
  
- **Kịch bản 4: Vô hiệu hóa người dùng:**
  - Diễn viên: Admin/User
  - Hệ thống: UserController
  - Hành động:
    - Admin/User gửi yêu cầu để vô hiệu hóa một người dùng cụ thể.
    - UserController tìm kiếm và cập nhật trạng thái của người dùng sang "disabled".
    - UserController gửi lại dữ liệu người dùng đã cập nhật cho Admin/User.
  
- **Kịch bản 5: Xóa người dùng:**
  - Diễn viên: Admin/User
  - Hệ thống: UserController
  - Hành động:
    - Admin/User gửi yêu cầu để xóa một người dùng cụ thể.
    - UserController tìm và xóa người dùng từ UserModel dựa trên ID của người dùng.
2. Bản phân tích của controller userController:
### 1. Mô hình dữ liệu (Data Model):

#### AccountModel (Mô hình Tài khoản):
- **Attributes:**
  - userId: String
  - email: String (Unique)
  - password: String
  - username: String
  - refreshToken: String
- **Associations:**
  - None
- **Methods:**
  - None

### 2. Chức năng (Functions):

#### apiLogin:
- **Inputs:**
  - email: String
  - password: String
- **Outputs:**
  - status: Boolean
  - msg: String
  - tokens: Object { accessToken: String, refreshToken: String }
- **Flow:**
  1. Kiểm tra sự tồn tại của email trong cơ sở dữ liệu.
  2. So sánh mật khẩu được cung cấp với mật khẩu đã được băm trong cơ sở dữ liệu.
  3. Nếu đăng nhập hợp lệ, tạo mã thông báo truy cập và làm mới mã thông báo.
  4. Gửi mã thông báo truy cập và làm mới mã thông báo trong cookie của người dùng.

#### apiRegister:
- **Inputs:**
  - email: String
  - password: String
  - username: String
- **Outputs:**
  - msg: String
  - status: Boolean
  - user: Object { email: String, username: String }
- **Flow:**
  1. Kiểm tra sự tồn tại của email trong cơ sở dữ liệu.
  2. Băm mật khẩu và lưu tài khoản mới vào cơ sở dữ liệu.
  3. Trả về thông báo đăng ký thành công và thông tin tài khoản người dùng.

#### apiToken:
- **Inputs:**
  - refreshToken: String
- **Outputs:**
  - status: Boolean
  - msg: String
  - tokens: Object { accessToken: String, refreshToken: String }
- **Flow:**
  1. Lấy mã thông báo làm mới từ yêu cầu người dùng.
  2. Tạo lại mã thông báo truy cập và cập nhật vào cơ sở dữ liệu.
  3. Trả về mã thông báo truy cập mới.

### 3. Biểu đồ lớp (Class Diagram):

![Class Diagram](class_diagram.png)

### 4. Xử lý bảo mật (Security Handling):

- Mật khẩu được băm trước khi lưu vào cơ sở dữ liệu để đảm bảo tính bảo mật.
- Sử dụng mã thông báo JWT để xác thực người dùng và quản lý phiên làm việc.
- Mã thông báo làm mới được sử dụng để tái tạo mã thông báo truy cập sau khi hết hạn.

### 5. Ghi chú:

- Mã thông báo truy cập và làm mới mã thông báo truy cập được sử dụng để xác thực người dùng và duy trì phiên làm việc.
- Quản lý lỗi và xử lý ngoại lệ cần được thực hiện để đảm bảo tính ổn định của hệ thống.
- Các mã thông báo JWT được ký và mã hóa để đảm bảo tính toàn vẹn và bảo mật của dữ liệu.
3. Bản mô tả các API:
API
1. **billToText**: Đây là một endpoint API để xử lý yêu cầu chuyển đổi hóa đơn thành văn bản. Tuy nhiên, trong phiên bản hiện tại, nó chỉ trả về một đối tượng JSON với trạng thái và thông tin.

2. **User**: Endpoint này được sử dụng để lấy danh sách tất cả người dùng từ cơ sở dữ liệu.

3. **apiUploadImage_bill**: Đây là endpoint xử lý yêu cầu tải lên ảnh hóa đơn từ người dùng. Nó thực hiện các bước sau:
   - Tạo một thư mục mới để lưu trữ ảnh hóa đơn nếu thư mục chưa tồn tại.
   - Tải lên các tệp ảnh hóa đơn lên máy chủ và lưu trữ chúng trong thư mục đã tạo.
   - Kết nối đến RabbitMQ để gửi các tệp ảnh vừa tải lên để thực hiện quá trình OCR.
   - Khi nhận được kết quả từ RabbitMQ, nó lưu trữ thông tin về ảnh và trả về kết quả cho người dùng.

4. **apiUploadImage_bill_new**: Tương tự như endpoint `apiUploadImage_bill`, nhưng endpoint này chuyển đổi các ảnh thành dữ liệu base64 trước khi gửi đến RabbitMQ.

5. **apiUploadBillBase64**: Endpoint này chấp nhận các yêu cầu tải lên hóa đơn ở định dạng base64 và thực hiện các bước tương tự như `apiUploadImage_bill_new`.

6. **apiUploadBillFile**: Endpoint này chấp nhận các yêu cầu tải lên hóa đơn dưới dạng tệp và thực hiện các bước tương tự như `apiUploadImage_bill`.

7. **apiUploadBillFileVer2** và **apiUploadBillBase64Ver2**: Đây là hai phiên bản nâng cấp của `apiUploadBillFile` và `apiUploadBillBase64` với các chức năng tương tự, nhưng có thể có một số cải tiến hoặc sửa đổi.

8. **downloadImg** và **download**: Hai endpoint này được sử dụng để tải xuống các tệp ảnh hoặc văn bản đã được xử lý từ máy chủ.



### 1. Class Diagram:

#### a. Các Lớp (Classes):
1. **AccountModel**: Đại diện cho mô hình tài khoản.
2. **BillModel**: Đại diện cho mô hình hóa đơn.
3. **ConvertModel**: Đại diện cho mô hình chuyển đổi.
4. **ImageModel**: Đại diện cho mô hình hình ảnh.
5. **PriceModel**: Đại diện cho mô hình giá.
6. **ReportModel**: Đại diện cho mô hình báo cáo.
7. **ReviewModel**: Đại diện cho mô hình đánh giá.
8. **UserModel**: Đại diện cho mô hình người dùng.

#### b. Mối Quan Hệ (Relationships):
- **Association**: Có một số sự liên kết giữa các lớp, nhưng chúng không được mô tả rõ ràng trong mã nguồn. Ví dụ: Lớp `UserModel` có thể liên kết với mô hình `AccountModel`.
- **Dependency**: Lớp `ConvertModel` phụ thuộc vào các lớp `ImageModel` và `UserModel` để thực hiện các chức năng của nó.

### 2. Sequence Diagram:
- **apiUploadImage_bill**: Mô tả quy trình tải lên ảnh hóa đơn từ người dùng và sử dụng RabbitMQ để gửi yêu cầu xử lý OCR.
- **apiUploadImage_bill_new**: Tương tự như `apiUploadImage_bill` nhưng sử dụng base64 để truyền dữ liệu.
- **apiUploadBillBase64** và **apiUploadBillBase64Ver2**: Cung cấp các phiên bản tải lên hóa đơn mới với base64.
- **apiUploadBillFile** và **apiUploadBillFileVer2**: Cung cấp các phiên bản tải lên hóa đơn mới với tệp.

### 3. Component Diagram:
- **Upload Component**: Bao gồm các hàm liên quan đến việc tải lên ảnh hoặc tệp hóa đơn và gửi yêu cầu xử lý.
- **RabbitMQ Component**: Đại diện cho RabbitMQ, một hệ thống hàng đợi thông báo được sử dụng để gửi yêu cầu xử lý OCR.
- **Processing Component**: Đại diện cho các máy chủ xử lý OCR, nhận yêu cầu từ RabbitMQ, xử lý và trả kết quả cho ứng dụng.

### 4. Activity Diagram:
- **apiUploadImage_bill**: Mô tả quy trình tải lên ảnh hóa đơn từ người dùng, xử lý và lưu trữ vào cơ sở dữ liệu.
- **apiUploadBillBase64** và **apiUploadBillBase64Ver2**: Mô tả quy trình tải lên hóa đơn bằng cách sử dụng base64 và gửi yêu cầu xử lý OCR.
- **apiUploadBillFile** và **apiUploadBillFileVer2**: Mô tả quy trình tải lên hóa đơn bằng cách sử dụng tệp và gửi yêu cầu xử lý OCR.

### 5. Deployment Diagram:
- **Web Server**: Đại diện cho máy chủ web nơi ứng dụng được triển khai.
- **Database Server**: Đại diện cho máy chủ cơ sở dữ liệu nơi dữ liệu của ứng dụng được lưu trữ.
- **RabbitMQ Server**: Đại diện cho máy chủ RabbitMQ được sử dụng để gửi và nhận yêu cầu xử lý OCR.

### 6. Statechart Diagram:
- Có thể sử dụng để mô tả trạng thái của các đối tượng trong hệ thống, nhưng không có thông tin rõ ràng trong mã nguồn đã cho.

### 7. Use Case Diagram:
- **Use Cases**: Bao gồm các tác vụ như tải lên ảnh hóa đơn, xử lý OCR và lưu trữ kết quả.
4. Phân tích host lên S3

Dưới đây là tài liệu đặc tả cho mã nguồn trong file `s3.js`, bao gồm mô tả chức năng và phân tích UML:

## Tài liệu Đặc tả

### Tên Tài liệu: S3.js - AWS S3 Utility Functions

### Mục đích:
Tài liệu này cung cấp một tập hợp các hàm tiện ích để làm việc với dịch vụ lưu trữ đám mây Amazon S3 (Simple Storage Service). Các hàm trong file `s3.js` cho phép tải tệp lên S3, nhận dữ liệu của tệp từ S3, tính toán kích thước của tệp và chuyển đổi kích thước tệp từ đơn vị bytes sang các đơn vị lớn hơn.

### Phiên bản: 1.0

### Ngày Cập Nhật: {{Ngày Cập Nhật}}

### Tác Giả: {{Tên Tác Giả}}

### Môi Trường:

- Node.js
- AWS SDK

### Nội Dung:

1. **uploadFile(file):**
    - Mô tả: Hàm này tải một tệp lên S3.
    - Tham số:
        - `file`: Đối tượng tệp tin được tải lên.
    - Trả về: Promise, cho biết quá trình tải lên đã hoàn thành hoặc không.

2. **getFileStream(fileKey):**
    - Mô tả: Hàm này nhận một khóa của tệp trên S3 và trả về một luồng đọc của tệp.
    - Tham số:
        - `fileKey`: Khóa của tệp trên S3.
    - Trả về: ReadStream, đại diện cho luồng đọc của tệp trên S3.

3. **getFile(fileKey):**
    - Mô tả: Hàm này nhận một khóa của tệp trên S3 và gửi dữ liệu của tệp về client.
    - Tham số:
        - `fileKey`: Khóa của tệp trên S3.
    - Trả về: Không có giá trị trực tiếp, nhưng gửi dữ liệu của tệp về client.

4. **sizeOf(fileKey):**
    - Mô tả: Hàm này nhận một khóa của tệp trên S3 và trả về kích thước của tệp (dạng bytes).
    - Tham số:
        - `fileKey`: Khóa của tệp trên S3.
    - Trả về: Kích thước của tệp dưới dạng bytes.

5. **bytesToSize(bytes):**
    - Mô tả: Hàm này chuyển đổi kích thước từ đơn vị bytes sang các đơn vị lớn hơn (KB, MB, ...).
    - Tham số:
        - `bytes`: Kích thước của tệp dưới dạng bytes.
    - Trả về: Kích thước của tệp được định dạng trong các đơn vị lớn hơn.

### Hướng Dẫn Sử Dụng:
1. Cài đặt các thư viện cần thiết: `npm install aws-sdk`
2. Tạo tệp `.env` và cung cấp các biến môi trường như `AWS_BUCKET_NAME`, `AWS_BUCKET_REGION`, `AWS_ACCESS_KEY`, và `AWS_SECRET_KEY`.
3. Sử dụng các hàm từ file `s3.js` để tương tác với dịch vụ Amazon S3.

## Phân tích UML

### Diagram lớp:

```
+-------------------------------------+
|               s3.js                 |
+-------------------------------------+
| + uploadFile(file)                  |
| + getFileStream(fileKey)            |
| + getFile(fileKey)                  |
| + sizeOf(fileKey)                   |
| + bytesToSize(bytes)                |
+-------------------------------------+
```

Trong đó:
- `uploadFile(file)`: Tải một tệp lên S3.
- `getFileStream(fileKey)`: Nhận luồng đọc của một tệp từ S3.
- `getFile(fileKey)`: Nhận dữ liệu của một tệp từ S3 và gửi về client.
- `sizeOf(fileKey)`: Nhận kích thước của một tệp trên S3.
- `bytesToSize(bytes)`: Chuyển đổi kích thước từ bytes sang đơn vị lớn hơn (KB, MB, ...).

### Mô Tả:

- Mỗi phương thức trong file `s3.js` đều thực hiện một chức năng cụ thể liên quan đến việc làm việc với Amazon S3.
- File `s3.js` cung cấp các hàm tiện ích để tải tệp lên, nhận dữ liệu tệp, tính toán kích thước của tệp và chuyển đổi đơn vị kích thước.
5.Phân tích thiết kế lịch sử số hóa:
Dưới đây là phân tích thiết kế UML cho controller `history.js`:

### Class Diagram:

```
------------------------------------------
|             HistoryController           |
------------------------------------------
| + list(req, res): void                  |
| + create(req, res): void                |
| + read(req, res): void                  |
| + delete(req, res): void                |
| + update(req, res): void                |
| + getHistoryById(req, res, next, id):   |
|   void                                  |
------------------------------------------
```

### Mô tả các phương thức:

1. **list(req, res): void**
   - Mô tả: Phương thức này trả về tất cả các lịch sử có trong cơ sở dữ liệu.
   - Parameters: 
     - `req`: Đối tượng yêu cầu (request).
     - `res`: Đối tượng phản hồi (response).
   - Return: Không có.

2. **create(req, res): void**
   - Mô tả: Phương thức này tạo một lịch sử mới trong cơ sở dữ liệu.
   - Parameters: 
     - `req`: Đối tượng yêu cầu (request) chứa dữ liệu để tạo lịch sử mới.
     - `res`: Đối tượng phản hồi (response).
   - Return: Không có.

3. **read(req, res): void**
   - Mô tả: Phương thức này trả về một lịch sử cụ thể dựa trên ID.
   - Parameters: 
     - `req`: Đối tượng yêu cầu (request) chứa ID của lịch sử cần truy vấn.
     - `res`: Đối tượng phản hồi (response).
   - Return: Không có.

4. **delete(req, res): void**
   - Mô tả: Phương thức này xóa một lịch sử khỏi cơ sở dữ liệu dựa trên ID.
   - Parameters: 
     - `req`: Đối tượng yêu cầu (request) chứa ID của lịch sử cần xóa.
     - `res`: Đối tượng phản hồi (response).
   - Return: Không có.

5. **update(req, res): void**
   - Mô tả: Phương thức này cập nhật thông tin của một lịch sử dựa trên ID.
   - Parameters: 
     - `req`: Đối tượng yêu cầu (request) chứa ID của lịch sử cần cập nhật và dữ liệu cập nhật.
     - `res`: Đối tượng phản hồi (response).
   - Return: Không có.

6. **getHistoryById(req, res, next, id): void**
   - Mô tả: Middleware này được sử dụng để lấy lịch sử dựa trên ID trước khi thực hiện các phương thức khác.
   - Parameters: 
     - `req`: Đối tượng yêu cầu (request).
     - `res`: Đối tượng phản hồi (response).
     - `next`: Hàm middleware tiếp theo.
     - `id`: ID của lịch sử cần lấy.
   - Return: Không có.
7. Phân tích phần phản hồi của người dùng
Dưới đây là phân tích thiết kế UML cho module phản hồi:

### Class Diagram:

```
------------------------------------------
|          FeedbackController             |
------------------------------------------
| + create(req, res): void               |
------------------------------------------
```

### Mô tả các phương thức:

1. **create(req, res): void**
   - Mô tả: Phương thức này tạo một phản hồi mới và lưu vào cơ sở dữ liệu.
   - Parameters: 
     - `req`: Đối tượng yêu cầu (request) chứa dữ liệu phản hồi.
     - `res`: Đối tượng phản hồi (response).
   - Return: Không có.

### Mô tả:

- **FeedbackController**: Controller này quản lý việc tạo phản hồi mới và lưu vào cơ sở dữ liệu. Đây là một phương thức cơ bản để ghi lại phản hồi từ người dùng.
8. Phân tích phần xác  thực người dùng:

Dưới đây là phân tích thiết kế của phần xác thực người dùng:

### Class Diagram:

```
------------------------------------------
|            AuthController               |
------------------------------------------
| + register(req, res, next): void       |
| + login(req, res, next): void          |
------------------------------------------
```

### Mô tả các phương thức:

1. **register(req, res, next): void**
   - Mô tả: Phương thức này được sử dụng để đăng ký người dùng mới bằng cách tạo một tài khoản người dùng mới trong cơ sở dữ liệu.
   - Parameters: 
     - `req`: Đối tượng yêu cầu (request) chứa thông tin của người dùng mới.
     - `res`: Đối tượng phản hồi (response).
     - `next`: Middleware tiếp theo trong chuỗi middleware Express.
   - Return: Không có.

2. **login(req, res, next): void**
   - Mô tả: Phương thức này được sử dụng để xác thực người dùng bằng cách so sánh email và mật khẩu với dữ liệu trong cơ sở dữ liệu. Nếu thông tin đăng nhập hợp lệ, phương thức sẽ tạo và gửi mã thông báo truy cập (access token) và mã thông báo làm mới (refresh token) cho người dùng.
   - Parameters: 
     - `req`: Đối tượng yêu cầu (request) chứa email và mật khẩu của người dùng cần đăng nhập.
     - `res`: Đối tượng phản hồi (response).
     - `next`: Middleware tiếp theo trong chuỗi middleware Express.
   - Return: Không có.

### Mô tả:

- **AuthController**: Controller này quản lý việc đăng ký và đăng nhập người dùng. Nó sử dụng mã thông báo JWT để xác thực và tạo phiên làm việc cho người dùng.
9. Phân tích phần trang chính:
Dưới đây là phân tích chi tiết hơn về phần main trong ứng dụng, bao gồm cả cấu hình Express, middleware, và cách xử lý lỗi:

### Cấu hình Express và Middleware:

1. **require("dotenv").config()**: Sử dụng để load các biến môi trường từ tệp `.env` vào quá trình thực thi của ứng dụng.

2. **createError và các Middleware khác**: 
   - `createError`: Sử dụng để tạo lỗi HTTP với mã và thông báo cụ thể.
   - `express`: Import Express framework.
   - `path`: Module được sử dụng để làm việc với đường dẫn tệp và thư mục.
   - `cookieParser`: Middleware để phân tích cú pháp cookie trong yêu cầu HTTP.
   - `logger`: Middleware để ghi log các yêu cầu HTTP vào console.
   - `bodyParser`: Middleware để phân tích các phần thân của yêu cầu HTTP thành JSON hoặc x-www-form-urlencoded.
   - `cors`: Middleware để xử lý Cross-Origin Resource Sharing (CORS), cho phép truy cập từ các nguồn khác nhau.

3. **Express Setup**:
   - `app`: Tạo một đối tượng Express application.

4. **Cấu hình view engine và static files**:
   - `app.set('views', path.join(__dirname, 'views'))`: Thiết lập thư mục chứa các file view của ứng dụng.
   - `app.set('view engine', 'jade')`: Thiết lập view engine sử dụng cho ứng dụng là Jade (hoặc Pug).
   - `app.use('/upload', express.static('upload'))`: Cung cấp các tệp tĩnh từ thư mục 'upload'.

5. **Cấu hình Middleware và Parsing**:
   - `app.use(cors())`: Sử dụng middleware CORS để cho phép truy cập từ các nguồn khác nhau.
   - `app.use(logger('dev'))`: Sử dụng middleware logger để ghi log các yêu cầu vào console.
   - `app.use(express.json({limit: '50mb'}))`: Middleware để phân tích các yêu cầu có dạng JSON và giới hạn kích thước lên đến 50MB.
   - `app.use(express.urlencoded({ extended: false, limit: '50mb' }))`: Middleware để phân tích các yêu cầu có dạng `x-www-form-urlencoded` và giới hạn kích thước lên đến 50MB.
   - `app.use(cookieParser())`: Middleware để phân tích cú pháp cookie từ yêu cầu HTTP.

### Cấu hình Router:

6. **Router và Endpoint**:
   - `app.use('/', indexRouter)`: Sử dụng router `indexRouter` cho các yêu cầu tại URI root.
   - `app.use('/users', usersRouter)`: Sử dụng router `usersRouter` cho các yêu cầu tại URI '/users'.
   - `app.use('/admin', admimRouter)`: Sử dụng router `admimRouter` cho các yêu cầu tại URI '/admin'.
   - `app.use('/', authRouter)`: Sử dụng router `authRouter` cho các yêu cầu tại URI root.
   - `app.use('/history', HistoryRouter)`: Sử dụng router `HistoryRouter` cho các yêu cầu tại URI '/history'.
- `app.use('/image', imageRouter)`: Sử dụng router `imageRouter` cho các yêu cầu tại URI '/image'.
   - `app.use('/feedback', feedbackRouter)`: Sử dụng router `feedbackRouter` cho các yêu cầu tại URI '/feedback'.

### Xử lý lỗi:

7. **Middleware xử lý lỗi**:
   - Middleware được sử dụng để xử lý lỗi 404 (không tìm thấy) và chuyển tiếp lỗi cho middleware xử lý lỗi sau đó.
   - Middleware này định nghĩa `res.locals.message` và `res.locals.error` để cung cấp thông điệp lỗi và đối tượng lỗi cho các trang lỗi.
   - Trong môi trường phát triển, middleware này render trang lỗi với thông điệp và stack trace của lỗi. Trong môi trường sản xuất, middleware này chỉ trả về lỗi 500 (lỗi máy chủ) mà không cung cấp thông tin cụ thể cho người dùng.

### Mô tả:

- **app**: Đối tượng `express.Application` đại diện cho ứng dụng Express đã được cấu hình và sẵn sàng để chạy. Đối tượng này được xuất ra ngoài để có thể sử dụng trong các file khác trong ứng dụng.