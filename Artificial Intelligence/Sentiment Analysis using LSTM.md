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
!tar -xvzf /content/aclImdb_v1.tar.gz
```

## Tokenize Text
Trước khi tokenize mình cần đi qua 3 bước là loại bỏ stop word cho ngôn ngữ "english" và loại bỏ các từ không có trong dictionary từ của corpus, để có được hàm này trước tiên mình cần loại bỏ các stop word trong train data và xây dựng bộ vocab chứa các từ trong tập dữ liệu train. 
```python
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
stop_words = list(stop_words)
```

### Build Vocab
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

+ ? Example output ![[Pasted image 20250225193828.png]]

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


# Create and Train LSTM Model

## Create LSTM Class
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


## Train and Evaluate LSTM Model
+ ?  Trước khi huấn luyện, sử dụng CUDA để tăng tốc quá trình huấn luyện qua biến device. Cũng như khai báo siêu tham số learning_rate, cùng với Loss Function, Optimizer. 

### Model Trainning with Early Stopping 
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

### Evaluation on Test Set 
**Tổng quan:**  
Đoạn mã này đánh giá mô hình trên tập kiểm tra. Nó chuyển mô hình sang chế độ đánh giá (eval), thu thập các dự đoán và nhãn thật từ test_dataloader, sau đó sử dụng hàm `classification_report` để in ra báo cáo hiệu năng (với các nhãn "neg" và "pos").

**Các bước chính:**
1. **Chuyển mô hình sang chế độ eval:**
    - `standard_model.eval()` đảm bảo rằng các thành phần như dropout được vô hiệu hóa và không tính toán gradient trong quá trình dự đoán.
    
2. **Tắt tính toán gradient:**
    - Sử dụng `with torch.no_grad():` giúp giảm bộ nhớ sử dụng và tăng tốc quá trình inference.
    
3. **Duyệt qua test_dataloader:**
    - Với mỗi batch, chuyển các câu (texts) sang thiết bị (`device`) của mô hình.
    
4. **Dự đoán:**
    - Tính đầu ra (scores) từ mô hình.
    - Chuyển đổi scores sang numpy array và lấy chỉ số của giá trị lớn nhất theo axis=1 để xác định nhãn dự đoán.
    
5. **Thu thập kết quả:**
    - Lưu các nhãn dự đoán và nhãn thật vào danh sách (`y_true` và `y_pred`) để sau đó đánh giá hiệu năng.
    
6. **In báo cáo phân loại:**
    - Sử dụng `classification_report` từ scikit-learn để hiển thị các chỉ số như precision, recall, f1-score cho từng lớp ("neg" và "pos").


+ ? **Kết Quả:** cho thấy mô hình bị over fitting với loss của validation tăng còn training giảm. Về precision, precision cho negative chỉ ở mức 3%, trong khi precision cho positive ở mức 97%. 
![[Pasted image 20250225161107.png]]
![[Pasted image 20250225161154.png]]
# More Exercise

### 1. Learn about Bidirectional LSTMs and test it
> Bidirectional LSTMs học ngữ cảnh từ trái sang phải và từ phải sang trái rồi ghép chúng lại.

**Standard LSTM:** Xử lý chuỗi đầu vào từ token thứ nhất đến token cuối cùng. Chỉ có ngữ cảnh "quá khứ".
 
**Bidirectional LSTM**: Xử lý chuỗi đầu vào theo 2 hướng: Tiến (đọc từ đầu tới cuối), Lùi (đọc từ cuối tới đầu)

+ ? **Kết Quả**: với cải tiến Bidirectional, kết quả tổng quan cho dự cảm xúc positive và negative tăng rõ rệt. Với validation loss giảm xuống còn 0.6933%.
>Với ngữ cảnh hiểu được từ cả trước và sau của câu, mô hình có thể khái quát nếu một câu là tích cực hay tiêu cực tốt hơn.
![[Pasted image 20250225214446.png]]
>So sánh với LSTM thường, độ chính xác của Bidirectional LSTM cho cảm xúc Negative tăng từ 0.03 lên 0.61 dù độ chính xác cho positive giảm từ 0.97 xuống 0.40. Tóm lại mô hình tổng quan hóa nội dung tốt hơn và cần điều chỉnh tham số để có kết quả tốt hơn.  
![[Pasted image 20250225214335.png]]
+ ! note: Do dropout, mỗi lần huấn luyện model sẽ cho ra 1 kết quả khác nhau.
![[Pasted image 20250225222001.png]]


### 2. Compare this model with previous ML model (SVC, Logistic Regression)

#### SVC
**Tổng quan:**  
Đoạn mã xây dựng một pipeline phân loại văn bản bằng cách chuyển đổi dữ liệu văn bản từ IMDB sang vector đặc trưng sử dụng TF-IDF, sau đó huấn luyện mô hình SVC với kernel tuyến tính. Cuối cùng, nó đánh giá mô hình trên tập test và in ra các chỉ số đánh giá như accuracy và báo cáo phân loại.

**Các bước chính:**

1. **Chuẩn bị dữ liệu:**
    - Lấy dữ liệu train và test từ DataFrame (`train_data` và `test_data`), chuyển cột `text` thành danh sách các văn bản và `sentiment` thành danh sách nhãn.
    
2. **Chuyển đổi văn bản thành vector TF-IDF:**
    - Sử dụng `TfidfVectorizer` với:
        - `max_features=10000`: Giới hạn số lượng đặc trưng.
        - `ngram_range=(1, 2)`: Sử dụng unigrams và bigrams.
        - `stop_words='english'`: Loại bỏ các từ dừng tiếng Anh.
    - Huấn luyện vectorizer trên dữ liệu train và chuyển đổi cả train và test thành ma trận đặc trưng.
    
3. **Tạo mô hình SVC:**
    - Khởi tạo mô hình SVC với kernel tuyến tính (`kernel='linear'`), tham số regularization `C=1.0` và `random_state=42` để đảm bảo tính tái lập.
      
4. **Huấn luyện mô hình:**
    - Huấn luyện SVC trên ma trận TF-IDF của dữ liệu train cùng với nhãn tương ứng.
    
5. **Đánh giá mô hình:**
    - Dự đoán nhãn cho tập test.
    - Tính toán độ chính xác và in báo cáo phân loại sử dụng `classification_report`.

+ ? **Kết quả:** so với LSTM cho bài toán phân loại, SVC có Precision cao rõ rệt. 
	![[Pasted image 20250225161856.png]]
+ $ Nhận xét:
	+ TF-IDF + SVM (đặc biệt với kernel tuyến tính) dễ triển khai và hiệu quả với dữ liệu không quá lớn. TF-IDF dễ bắt được các đặc trưng quan trọng về từ vựng, trong khi SVM thường ít bị ảnh hưởng bởi nhiễu hơn nếu được điều chỉnh hợp lý (như tham số `C`, `max_features`).
		
	+ Mạng LSTM, khi có nhiều tham số (n_layers, hidden_dim lớn, bidirectional, v.v.), thường cần nhiều dữ liệu và quá trình tinh chỉnh (hyperparameter tuning) phức tạp hơn. Nếu chưa tối ưu tốt (về số epoch, batch size, dropout, learning rate…), mô hình dễ bị overfitting hoặc không hội tụ tốt.

+ ? **Kết quả:** so với LSTM cho bài toán phân loại, Logistic Regression có Precision cao rõ rệt. 
![[Pasted image 20250225204917.png]]
+ $ Nhận xét: Logistic Regression giống như SVC, cũng hưởng lợi nhiều tư TF-IDF và trả về độ chính xác ngang ngửa SVC. 

### 3. Add one more LSTM layer

![[Pasted image 20250225214922.png]]
![[Pasted image 20250225233945.png]]



### 4. Implement Attention mechanism to improve the performce.
+ ? **Vấn đề của LSTM trong Tổng hợp ngữ cảnh**: LSTM thường dựa vào trạng thái ẩn cuối cùng hoặc một nhóm đơn giản các trạng thái ẩn trong khi LSTM song hướng tiêu tốn quá nhiều compute power. 
+ $ **Tập trung vào các phần chính:** cơ chế  cho phép mô hình học cách "tập trung" vào các phần có liên quan/quan trọng nhất bằng cách tăng chỉ số weight (W). Trong phân tích tình cảm, những từ như "vui vẻ", "xấu xí" có thể ảnh hưởng nhiều hơn đến ngữ cảnh.

**Tổng quan:**  
Đoạn mã này xây dựng mô hình phân loại văn bản sử dụng LSTM kèm Attention. Mô hình trước tiên biến đổi chuỗi đầu vào thành vector embedding, sau đó trích xuất đặc trưng tuần tự qua LSTM (có thể bidirectional), rồi áp dụng Attention để tổng hợp thông tin quan trọng nhất trong chuỗi. Kết quả cuối được đưa qua lớp fully-connected để dự đoán nhãn.

**1. Attention Module (`Attention` Class):**
- **Mục đích:** Học cách gán trọng số (weights) cho mỗi time step của đầu ra LSTM, giúp mô hình tập trung vào các phần quan trọng nhất.
- **Cách hoạt động:**
    1. Tính điểm chú ý (attention scores) qua một lớp `Linear`.
    2. Chuẩn hóa các điểm này thành xác suất bằng hàm `softmax`.
    3. Tính vector ngữ cảnh (context) bằng cách nhân trọng số chú ý với các đầu ra LSTM.


**2. LSTMAttentionClassifier:**
1. **Embedding:**
    - Chuyển token (chỉ số) thành vector embedding, đồng thời bỏ qua chỉ số padding (nếu có).
    - Áp dụng dropout để giảm overfitting.
      
2. **LSTM:**
    - Tiếp nhận chuỗi embedding, có thể bidirectional và có nhiều tầng (`n_layers`).
    - Trả về `lstm_outputs` chứa đặc trưng cho từng time step.
    
3. **Attention:**
    - Áp dụng module Attention để tóm tắt thông tin toàn chuỗi vào một vector ngữ cảnh duy nhất.
    - Cho phép mô hình tập trung vào các từ quan trọng nhất.
      
4. **Fully-connected (FC):**
    - Vector ngữ cảnh được đưa qua một lớp `Linear` để ra dự đoán cuối cùng (`logits`).
    - Trả về `logits` và trọng số chú ý (attention weights) để phân tích hoặc trực quan hóa.

**3. Huấn luyện và Đánh giá:**
- Chuyển mô hình sang `eval()` để tắt dropout và tính toán gradient.
- Trong vòng lặp test, dự đoán nhãn và thu thập `attn_weights`.
- Lưu ý: Có thể trực quan hóa attention bằng cách lấy `sample_attn` rồi vẽ biểu đồ biểu diễn phân bố trọng số chú ý theo thời gian.


