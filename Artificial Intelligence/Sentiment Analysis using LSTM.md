## Preprocessing

### Clean Text
**Tổng quan:**  
Hàm `clean_text(text)` được thiết kế để tiền xử lý văn bản, giúp chuẩn hóa dữ liệu đầu vào cho các mô hình xử lý ngôn ngữ. Hàm thực hiện các bước như loại bỏ thẻ HTML, xóa các ký tự đặc biệt không cần thiết, chuyển đổi toàn bộ văn bản về dạng chữ thường và thay thế các dấu câu bằng dấu cách.

**Các bước thực hiện:**

1. **Loại bỏ thẻ HTML:**  
    Sử dụng biểu thức chính quy `re.sub(r'<.*?>', '', text)` để tìm và xóa tất cả các thẻ HTML trong văn bản. Điều này giúp loại bỏ các định dạng không mong muốn từ dữ liệu gốc.
    
2. **Xóa các ký tự đặc biệt:**
    
    - Loại bỏ ký tự gạch chéo ngược (`\`) bằng cách thay thế chúng bằng chuỗi rỗng.
    - Tương tự, loại bỏ dấu nháy đơn (`'`) và dấu nháy kép (`"`) bằng cách sử dụng các biểu thức chính quy tương ứng.  
        Các bước này giúp loại bỏ những ký tự có thể gây nhiễu cho quá trình xử lý văn bản.
3. **Chuẩn hóa văn bản:**
    
    - Sử dụng `text.strip().lower()` để loại bỏ khoảng trắng thừa ở đầu và cuối chuỗi.
    - Chuyển toàn bộ văn bản sang chữ thường, giúp giảm thiểu sự khác biệt giữa các từ chỉ khác về chữ hoa chữ thường.
4. **Thay thế dấu câu bằng dấu cách:**
    
    - Định nghĩa một chuỗi `filters` chứa các ký tự dấu câu, ký tự tab và ký tự xuống dòng.
    - Tạo một từ điển `translate_dict` ánh xạ mỗi ký tự trong `filters` sang một khoảng trắng.
    - Sử dụng `str.maketrans(translate_dict)` để tạo bản đồ chuyển đổi, sau đó áp dụng `text.translate(translate_map)` nhằm thay thế tất cả các ký tự dấu câu trong văn bản bằng dấu cách.
5. **Trả về văn bản đã được làm sạch:**  
    Cuối cùng, hàm trả về văn bản sau khi đã được xử lý qua tất cả các bước trên.

### Loading IMDB Dataset
**Tổng quan:**  
Hàm `load_train_test_imdb_data(data_dir)` được thiết kế để tải và tiền xử lý dữ liệu IMDB từ thư mục `data_dir`. Dữ liệu được tổ chức thành hai phần riêng biệt: tập huấn luyện (training) và tập kiểm tra (testing). Mỗi review được gán nhãn cảm xúc dưới dạng số (1 cho positive, 0 cho negative) sau khi được làm sạch.

**Các bước thực hiện:**

1. **Khởi tạo Dictionary:**  
    Hàm bắt đầu bằng việc khởi tạo một dictionary có các khóa `"train"` và `"test"`, mỗi khóa lưu trữ một danh sách chứa các cặp dữ liệu dạng `[review, nhãn]`.
    
2. **Gán nhãn và phân loại dữ liệu theo thư mục:**
    
    - Duyệt qua các phân vùng `"train"` và `"test"`.
    - Trong mỗi phân vùng, hàm lặp qua hai thư mục con `"neg"` và `"pos"`.
    - Với mỗi thư mục:
        - Gán nhãn: nếu thư mục là `"pos"` thì `label = 1`, còn nếu là `"neg"` thì `label = 0`.
        - Xác định đường dẫn (path) tới thư mục chứa các file review.
        - Lấy danh sách các file trong thư mục đó.
3. **Đọc, làm sạch và lưu trữ dữ liệu:**
    
    - Với từng file trong danh sách:
        - Mở và đọc nội dung file sử dụng encoding `"utf-8"`.
        - Sử dụng hàm `clean_text()` để làm sạch nội dung review (loại bỏ HTML, ký tự đặc biệt, chuyển về chữ thường, …).
        - Nếu review sau khi làm sạch không rỗng, lưu cặp `[review, label]` vào danh sách tương ứng trong dictionary `data` (cho `"train"` hoặc `"test"`).
4. **Xáo trộn và chuyển đổi dữ liệu sang DataFrame:**
    
    - Sau khi thu thập xong dữ liệu, danh sách của phần `"train"` được xáo trộn để đảm bảo tính ngẫu nhiên.
    - Danh sách này sau đó được chuyển đổi thành một DataFrame của pandas với hai cột: `text` (chứa nội dung review) và `sentiment` (chứa nhãn cảm xúc).
    - Quá trình tương tự được thực hiện đối với phần `"test"`.


### Download IMDb Dataset
```python
!wget https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz
```
```python
!tar -xvzf /content/aclImdb_v1.tar.gz```

### Tokenize Text
Trước khi tokenize mình cần đi qua 3 bước là loại bỏ stop word cho ngôn ngữ "english" và loại bỏ các từ không có trong dictionary từ của corpus, để có được hàm này trước tiên mình cần loại bỏ các stop word trong train data và xây dựng bộ vocab chứa các từ trong tập dữ liệu train. 
```python
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
stop_words = list(stop_words)
```

#### Build Vocab
**Tổng quan:**  
Hàm `build_vocab` xây dựng một danh sách từ (vocabulary) từ corpus bằng cách duyệt qua từng văn bản và tách các từ (token). Nếu từ chưa được thêm, nó sẽ được lưu vào danh sách. Nếu có giới hạn kích thước (`max_vocab_size`), hàm sẽ dừng lại ngay khi đạt giới hạn đó.

**Các bước chính:**
- **Khởi tạo:**  
    Tạo danh sách `vocab_freq` và tập `seen` để theo dõi các từ đã xuất hiện.
    
- **Duyệt và tách từ:**  
    Với mỗi văn bản trong corpus, sử dụng `wordpunct_tokenize` để tách thành các token.
    
- **Xây dựng danh sách:**  
    Nếu token chưa có trong `seen`, thêm vào `vocab_freq` và cập nhật `seen`.  
    Kiểm tra giới hạn kích thước, trả về ngay nếu vượt quá.
    
- **Trả về:**  
    Trả về danh sách các từ đã thu thập được.

#### Remove Out of Vocabulary Word
**Tổng quan:**  
Hàm `remove_OOV_word_1` lọc danh sách các token, loại bỏ stopwords và thay thế các token không có trong từ điển (`vocab`) bằng `<UNK>`. Nếu kết quả cuối cùng rỗng, hàm trả về `None`.

**Các bước chính:**
- **Chuẩn bị:**  
    Chuyển `vocab` và `stop_words` thành tập hợp để kiểm tra nhanh.
    
- **Duyệt qua các token:**
    
    - Bỏ qua token nếu nó nằm trong danh sách stopwords.
    - Nếu token không có trong từ điển, thay thế bằng `<UNK>`.
    - Nếu token có trong từ điển, giữ nguyên token.
- **Trả về:**  
    Trả về danh sách token mới hoặc `None` nếu danh sách trống.

#### Batch Tokenize
+ ? Trước khi Batch Tokenize mình cần khởi tạo 2 dictionary tham chiếu từng token sang index (i.e. id) trong đó index là int.
**Tổng quan:**  
Hàm `batch_tokenize` chuyển đổi một danh sách các câu (danh sách các token) thành danh sách các index số nguyên, dựa trên từ điển ánh xạ token thành index. Đồng thời, nó pad hoặc truncate mỗi câu về độ dài cố định (`max_length`). Nếu `max_length` không được chỉ định, độ dài của câu dài nhất sẽ được sử dụng.

**Các bước chính:**

1. **Xác định độ dài tối đa:**  
    Nếu `max_length` là `None`, hàm tính độ dài của câu dài nhất trong `token_list`.
    
2. **Chuyển đổi token thành index:**  
    Với mỗi câu, từng token được chuyển thành index dựa trên `token_idx_list`. Nếu token không có trong từ điển, giá trị mặc định là `1` (thường là `<UNK>`).
    
3. **Padding hoặc Truncate:**
    
    - Nếu `padding` là `True` và câu ngắn hơn `max_length`, thêm số 0 vào cuối cho đến khi đạt độ dài `max_length`.
    - Nếu câu dài hơn `max_length`, cắt bớt các token vượt quá.
4. **Trả về kết quả:**  
    Trả về danh sách các câu đã được chuyển đổi thành danh sách các index, mỗi câu có độ dài cố định (hoặc không vượt quá `max_length` nếu không padding).


### Create IMDB Dataset Class
**Tổng quan:**  
Class `IMDBDataset` là một custom Dataset kế thừa từ `torch.utils.data.Dataset`, dùng để lưu trữ và truy cập dữ liệu IMDB đã được token hóa cùng với nhãn của chúng. Nó hỗ trợ việc lấy mẫu dữ liệu (sử dụng phương thức `__getitem__`) cho các quá trình huấn luyện mô hình với PyTorch.

**Các bước chính:**

- **Khởi tạo (`__init__`):**  
    Lưu trữ danh sách các câu đã token hóa (`texts`) và danh sách nhãn tương ứng (`labels`).
    
- **Lấy kích thước (`__len__`):**  
    Trả về số lượng mẫu (số câu) trong dataset.
    
- **Lấy mẫu (`__getitem__`):**  
    Trả về cặp dữ liệu gồm: danh sách token của câu và nhãn (chưa chuyển đổi thành ID, vì việc chuyển đổi sẽ được thực hiện trong hàm `collate` sau này).


### Convert Tokens to Tensors
**Tổng quan:**  
Hàm `collate` nhận một batch dữ liệu (danh sách các cặp `(text, label)` từ `Dataset.__getitem__`), chuyển đổi các câu (danh sách token) thành danh sách chỉ số thông qua `batch_tokenize`, rồi chuyển kết quả thành tensor của PyTorch để đưa vào mô hình.

**Các bước chính:**

1. **Tách dữ liệu:**  
    Tách danh sách `batch` thành `texts` (các câu token) và `labels` (nhãn tương ứng).
    
2. **Chuyển token thành chỉ số:**  
    Sử dụng hàm `batch_tokenize` để chuyển đổi các câu thành danh sách chỉ số, đồng thời pad hoặc truncate các câu về độ dài cố định (`max_length`).
    
3. **Chuyển đổi sang tensor:**  
    Chuyển đổi danh sách các chỉ số và nhãn thành các tensor `torch.LongTensor`.
    
4. **Trả về:**  
    Hàm trả về một tuple gồm tensor của các câu (input IDs) và tensor của các nhãn.

### Create DataLoader
**Tổng quan:**  
Đoạn code này tạo các DataLoader cho tập huấn luyện và kiểm tra dữ liệu IMDB. Nó sử dụng class `IMDBDataset` để chứa dữ liệu và hàm `collate` (được tùy chỉnh bằng `partial`) để chuyển đổi từng batch thành tensor với padding và độ dài cố định.

**Các bước chính:**

1. **Định nghĩa cấu hình:**
    
    - `batch_size = 32`: Số mẫu mỗi batch.
    - `max_seq_length = 200`: Độ dài tối đa của câu (padding/truncate).
2. **Tạo Dataset:**
    
    - `train_dataset` và `test_dataset` được khởi tạo từ `IMDBDataset` với các cột `text` và `sentiment`.
3. **Tùy chỉnh hàm collate:**
    
    - Biến `collate_fn_partial` sử dụng `partial` để cố định các tham số cho hàm `collate` như `token_idx_list`, `max_length`, và `padding`. Đảm bảo mỗi batch trong tập train và test được xử lý nhất quán.  
    
4. **Tạo DataLoader:**
    
    - `train_dataloader` và `test_dataloader` được tạo bằng `DataLoader` của PyTorch, sử dụng dataset tương ứng, cấu hình batch, chế độ xáo trộn (shuffle) và hàm collate tùy chỉnh để chuyển đổi dữ liệu thành tensor.


## Create and Train LSTM Model

### Create LSTM Class
**Tổng quan:**  
Lớp `LSTMClassifier` là một mô hình phân loại sử dụng mạng LSTM. Mô hình gồm một lớp embedding chuyển các token thành vector, một hoặc nhiều lớp LSTM (có thể song hướng) để trích xuất đặc trưng từ chuỗi, và một lớp fully-connected cuối cùng để dự đoán nhãn. Ngoài ra, dropout được áp dụng để giảm overfitting.

**Các bước chính:**

1. **Khởi tạo (`__init__`):**
    
    - **Embedding:** Chuyển các token (chỉ số) thành vector có kích thước `embedding_dim`, padding mặc định là 0 qua `pad_idx`.
    - **LSTM:** Xử lý chuỗi embedding với các tham số như `hidden_dim`, `n_layers`, `bidirectional`, và `dropout` (chỉ áp dụng nếu số lớp > 1).
    - **Fully-connected (FC):** Lớp linear nhận đầu ra từ LSTM (nếu song hướng, nhân đôi kích thước ẩn) và chuyển đổi thành `output_dim`.
    - **Dropout:** Áp dụng sau embedding và trên hidden state cuối cùng để giảm overfitting.
	
2. **Forward pass (`forward`):**
    
    - **Embedding & Dropout:** Đầu vào `x` (shape: `[batch_size, seq_len]`) được chuyển thành vector embedding, sau đó áp dụng dropout.
    - **Khởi tạo trạng thái ẩn:** Tạo các tensor `h0` và `c0` với kích thước phù hợp và đưa lên `device`.
    - **LSTM:** Xử lý 
    - chuỗi embedding qua LSTM, trả về output cùng hidden state.
    - **Xử lý hidden state:**
        - Nếu dùng LSTM song hướng, nối hidden state của hai hướng (sử dụng 2 lớp cuối) và áp dụng dropout.
	        note: 2 lớp cuối `hidden[-2, :, :]`  đại diện cho đầu ra của 2 hướng
        - Nếu không song hướng, sử dụng hidden state của lớp cuối cùng.
    - **Fully-connected:** Hidden state cuối cùng được chuyển qua lớp FC để tạo ra dự đoán với kích thước `[batch_size, output_dim]`.


### Train and Evaluate LSTM Model
+ ?  Trước khi huấn luyện, sử dụng CUDA để tăng tốc quá trình huấn luyện qua biến device. Cũng như khai báo siêu tham số learning_rate, cùng với Loss Function, Optimizer. 

#### Model Trainning with Early Stopping 
**Tổng quan:**  
Đoạn code thực hiện quá trình huấn luyện mô hình với cơ chế early stopping. Mô hình được huấn luyện trong mỗi epoch trên tập Training và đánh giá trên tập Testing. Nếu không có cải thiện sau một số epoch nhất định (được định nghĩa bởi `patience`), quá trình huấn luyện sẽ dừng lại sớm.

**Các bước chính:**
- **Khởi tạo:**
    
    - `best_test_loss` được đặt ban đầu là vô cùng (infinity) để đảm bảo bất kỳ giá trị loss nào cũng sẽ lớn hơn.
    - `patience` xác định số epoch chờ đợi nếu không có cải thiện.
    - Các danh sách `train_losses` và `test_losses` để lưu lại loss qua các epoch.
    - `best_model_state` lưu trạng thái mô hình tốt nhất (có loss thấp nhất).
    
- **Vòng lặp huấn luyện:**
    - **Training Phase:**
        - Chuyển mô hình sang chế độ training (`model.train()`).
        - Với mỗi batch trong tập huấn luyện, chuyển dữ liệu sang device (cùng sử dụng CUDA hoặc CPU), thực hiện forward pass, tính loss, backward pass và cập nhật trọng số.
        - Tích lũy loss của epoch và tính trung bình.
          
    - **Validation Phase:**
        - Chuyển mô hình sang chế độ evaluation (`model.eval()`) và tắt tính toán gradient.
        - Tính toán loss trên tập kiểm tra và tính trung bình.
          
- **Kiểm tra Early Stopping:**
    - Nếu loss trên tập kiểm tra cải thiện (nhỏ hơn `best_test_loss`), cập nhật `best_test_loss` và lưu trạng thái mô hình.
    - Nếu không cải thiện, tăng biến đếm `epochs_no_improve` và so sánh với `patience`. Nếu vượt quá, dừng huấn luyện sớm.
      
- **Kết thúc:**
    - Sau khi huấn luyện, nếu có mô hình tốt nhất được lưu, nạp lại trạng thái đó vào mô hình.

#### Evaluation 



## More Exercise

### 1. Learn about Bidirectional LSTMs and test it

### 2. Compare this model with previous ML model (SVC, Logistic Regression)

### 3. Add one more LSTM layer

### 4. Implement Attention mechanism to improve the performce.

