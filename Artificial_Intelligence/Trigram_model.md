# Import Libary
```python
import os
import pickle
from nltk.lm import KneserNeyInterpolated
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk.tokenize import word_tokenize
```
- **`os`**: Thư viện để làm việc với hệ điều hành, cho phép tương tác với tệp tin và thư mục (ví dụ: mở, lưu, di chuyển tệp tin).
- **`pickle`**: Thư viện để lưu trữ và tải lại các đối tượng Python vào/ra tệp (dùng để lưu mô hình đã huấn luyện).
- **`nltk.lm`**: Thư viện của **NLTK** cung cấp các công cụ để huấn luyện mô hình ngôn ngữ, ở đây ta sử dụng mô hình **Kneser-Ney Interpolated** cho n-gram.
- **`nltk.lm.preprocessing`**: Cung cấp các công cụ xử lý trước cho n-gram (ví dụ: padding câu, chuẩn bị dữ liệu huấn luyện).
- **`nltk.tokenize`**: Dùng để tách từ (tokenize) văn bản thành các từ riêng biệt.

# Download data
```python
!wget -O vn_syllables.txt "https://gist.githubusercontent.com/hieuthi/0f5adb7d3f79e7fb67e0e499004bf558/raw/135a4d9716e49a981624474156d6f247b9b46f6a/all-vietnamese-syllables.txt"
```
+ Sử dụng **wget** để tải một tệp văn bản chứa các âm tiết tiếng Việt từ một URL. Tệp này được lưu thành `vn_syllables.txt` trong thư mục hiện tại.
+ **`vn_syllables.txt`** sẽ chứa danh sách tất cả các âm tiết tiếng Việt, có thể được sử dụng trong quá trình tạo các mô hình n-gram hoặc kiểm tra tính đầy đủ của dữ liệu.

```python
full = []
for dirname, _, filenames in os.walk('/content/Train_Full'):
    for filename in filenames:
        with open(os.path.join("/content", os.path.join(dirname, filename)), 'r', encoding='UTF-16') as f:
            full.append(f.read())
print(len(full))
```
- **`os.walk()`** giúp quét qua toàn bộ thư mục `Train_Full` và đọc các tệp tin văn bản. Các tệp này có thể chứa các đoạn văn bản sẽ được sử dụng trong quá trình huấn luyện mô hình.
- **`open()`** mở tệp với mã hóa **UTF-16** và đọc nội dung vào danh sách `full`.

# Preprocess
## Tiền Xử Lý Dữ Liệu và Tokenization

### Mục đích và ý nghĩa
- Mục đích của đoạn code này là để **chuẩn bị dữ liệu văn bản** cho mô hình ngôn ngữ. Mình sẽ **tách văn bản thành các từ (token)** và loại bỏ **dấu câu** để giúp mô hình dễ dàng hiểu được dữ liệu. Việc này gọi là **tokenization**.
- Sau khi xử lý, mình sẽ có một **corpus** (tập hợp các câu), trong đó mỗi câu sẽ là một danh sách các từ đã được tách và làm sạch. Điều này giúp mô hình không bị nhầm lẫn khi gặp dấu câu hay các ký tự không cần thiết.

### Chi tiết các bước

1. **Hàm tokenize để tách từ và loại bỏ dấu câu**
    ```python
    def tokenize(doc):
        tokens = word_tokenize(doc.lower())
        table = str.maketrans('', '', string.punctuation.replace("_", ""))  # Remove all punctuation
        tokens = [w.translate(table) for w in tokens]
        tokens = [word for word in tokens if word]
        return tokens
    ```
- **Đầu vào**:
	- **`doc`** là một câu hoặc đoạn văn cần phải xử lý.
- **Giải thích**:
	- **`word_tokenize(doc.lower())`**: Đầu tiên, mình **chuyển hết các từ thành chữ thường** để tránh việxc phân biệt giữa chữ hoa và chữ thường, rồi tách câu thành các từ nhỏ (gọi là token).
	- **`table = str.maketrans('', '', string.punctuation.replace("_", ""))`**: mình tạo ra một **bảng dịch** để loại bỏ tất cả các dấu câu, chỉ để lại các từ và chữ cái. Bảng này sẽ giúp mình "xóa sổ" dấu câu như dấu chấm, dấu phẩy, dấu hỏi,...
	- **`tokens.translate(table)`**: Áp dụng bảng dịch này lên từng từ trong danh sách để **loại bỏ dấu câu**.
	- **`tokens = [word for word in tokens if word]`**: Sau khi loại bỏ dấu câu, một số từ có thể bị rỗng, nên mình **loại bỏ** những từ đó.
- **Đầu ra**:
	- **`tokens`**: Danh sách các từ sau khi đã loại bỏ dấu câu và chuyển sang chữ thường. Ví dụ, câu `"Tôi thích học."` sẽ thành `['tôi', 'thích', 'học']`.
		
2. **Chuyển toàn bộ dữ liệu thành một chuỗi văn bản lớn**
    ```python
    full_data = ". ".join(full)
    full_data = full_data.replace("\n", ". ")
    ```
- **Đầu vào**:
	- **`full`**: Đây là một danh sách các đoạn văn, mỗi phần tử trong danh sách có thể là một câu hoặc đoạn văn ngắn.
- **Giải thích**:
	- **`". ".join(full)`**: mình nối tất cả các câu trong `full` lại với nhau thành một chuỗi duy nhất, mỗi câu cách nhau bằng dấu chấm và khoảng trắng.
	- **`full_data.replace("\n", ". ")`**: Một số đoạn văn có thể có **dấu xuống dòng** (`\n`), vì vậy mình thay thế những dấu xuống dòng này bằng dấu chấm và khoảng trắng, giúp văn bản trở nên liền mạch hơn.
- **Đầu ra**:
	- **`full_data`**: Một chuỗi văn bản lớn, chứa tất cả các câu từ danh sách `full`, đã được nối lại với nhau và chuẩn hóa.
	    
3. **Tách văn bản thành các câu**
    ```python
    sents = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', full_data)
    ```
- **Đầu vào**:
	- **`full_data`**: Một chuỗi văn bản lớn vừa được chuẩn hóa.
- **Giải thích**:
	- **`re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', full_data)`**: Sử dụng biểu thức chính quy (regular expression) để tách văn bản thành các câu. Biểu thức này tìm dấu chấm hoặc dấu hỏi hoặc dấu chấm than, sau đó là một khoảng trắng và tiếp theo là chữ cái viết hoa để xác định nơi kết thúc câu.
- **Đầu ra**:
	- **`sents`**: Một danh sách chứa các câu đã được tách từ văn bản. Mỗi phần tử trong danh sách là một câu riêng biệt.
		
4. **Tokenize từng câu và lưu vào corpus**
    ```python
    corpus = []
    for sent in tqdm(sents):
        corpus.append(tokenize(sent))
    ```
- **Đầu vào**:
	- **`sents`**: Danh sách các câu đã được tách ra từ văn bản.
- **Giải thích**:
	- **`tqdm(sents)`**: mình dùng `tqdm` để hiển thị **thanh tiến trình** khi xử lý từng câu. Việc này giúp ta dễ dàng theo dõi tiến độ.
	- **`tokenize(sent)`**: Áp dụng hàm `tokenize` cho từng câu trong `sents` để tách câu thành các từ nhỏ và loại bỏ dấu câu.
- **Đầu ra**:
	- **`corpus`**: Danh sách chứa các câu đã được tách thành các từ. Mỗi câu trong `corpus` là một danh sách các từ đã được xử lý, sẵn sàng cho việc huấn luyện mô hình.

# Train model
### Mục đích và ý nghĩa
- Huấn luyện mô hình **Kneser-Ney Interpolated** để dự đoán **n-gram** (trigram ở đây, với `n=3`) từ một bộ **corpus** văn bản.  
- Mô hình được huấn luyện sử dụng thư viện **NLTK**, và kết quả mô hình sau khi huấn luyện được **lưu trữ** dưới dạng tệp pickle để có thể sử dụng lại sau này.

### Chi tiết các bước

1. **Khởi tạo mô hình n-gram**  
```python
   vi_model = KneserNeyInterpolated(n)
```
- **`vi_model`**: Mô hình **Kneser-Ney Interpolated** với **n=3**, tức là mô hình **trigram**.
- **Kneser-Ney**: Là phương pháp smoothing cải tiến, giúp xử lý tốt hơn cho những từ chưa xuất hiện trong dữ liệu huấn luyện.
	
1. **Tiền xử lý dữ liệu**
```python
    train_data, padded_sents = padded_everygram_pipeline(n, corpus)
```
- **`corpus`**: Là tập văn bản gốc, sẽ được chia thành các n-gram (cả trigram trong trường hợp này).
- **`train_data`**: Chứa các n-gram đã được chuẩn hóa và chia tách từ dữ liệu.
- **`padded_sents`**: Là tập các câu đã được **padding** (thêm các token đặc biệt như `<s>` và `</s>`) để xử lý các từ xuất hiện ở đầu và cuối câu.
	
2. **Huấn luyện mô hình**
```python
    vi_model.fit(train_data, padded_sents)
```
- Huấn luyện mô hình n-gram **Kneser-Ney** bằng cách sử dụng các **n-gram** từ `train_data` và các câu đã được padding `padded_sents`.
- Mô hình sẽ học các xác suất có điều kiện giữa các từ dựa trên bối cảnh của chúng.
	
3. **Kiểm tra kích thước của từ vựng**
```python
    print(len(vi_model.vocab))
```
- **`vi_model.vocab`** chứa **từ vựng** của mô hình (tất cả các từ đã được thấy trong quá trình huấn luyện).
- `len(vi_model.vocab)` in ra số lượng từ có trong từ vựng.

4. **Lưu mô hình vào tệp**
```python
    model_dir = "/content/drive/My Drive/Colab Notebooks/Ngram_model"
    with open(os.path.join(model_dir, 'kneserney_1st_ngram_model.pkl'), 'wb') as fout:
        pickle.dump(vi_model, fout)
```
- Mô hình sau khi huấn luyện sẽ được **lưu lại** dưới dạng tệp pickle (`.pkl`) vào thư mục `model_dir`.
- Sau khi lưu trữ, mô hình có thể được tải lại sau này để sử dụng mà không cần huấn luyện lại từ đầu.


# Using model to predict accents
## Generate Prediction Sentence
### Mục đích và ý nghĩa
- **Mục đích**: hàm `generate_sent`  **sinh ra một câu hoàn chỉnh** từ mô hình ngôn ngữ n-gram đã được huấn luyện, dựa trên một chuỗi từ ban đầu (seed). Qua đó, ta có thể kiểm tra khả năng dự đoán và sinh từ của mô hình.
- **Ý nghĩa**: Giúp ta hiểu được cách mô hình vận hành khi dự đoán từ tiếp theo dựa trên ngữ cảnh hiện tại, và cách các từ được kết hợp lại để tạo thành một câu có nghĩa.

### Chi tiết các bước
1. **Khởi tạo hàm detokenize**
```python
    from nltk.tokenize.treebank import TreebankWordDetokenizer
    detokenize = TreebankWordDetokenizer().detokenize
```
- **Đầu vào**: Không có đầu vào cụ thể, chỉ cần import thư viện.
- **Đầu ra**: Một hàm `detokenize` dùng để **ghép danh sách các token** (từng từ đã được sinh ra) thành một chuỗi văn bản (câu hoàn chỉnh).
- Thư viện `TreebankWordDetokenizer` cung cấp chức năng chuyển đổi danh sách từ (tokens) thành một câu có định dạng chuẩn (chẳng hạn thêm khoảng trắng giữa các từ).
	
2. **Định nghĩa hàm generate_sent**
```python
    def generate_sent(model, num_words, pre_words=[]):
        """
        :param model: An ngram language model from `nltk.lm.model`.
        :param num_words: Max no. of words to generate.
        :param random_seed: Seed value for random.
        """
        content = pre_words
        for i in range(num_words):
            token = model.generate(1, text_seed=content[-2:])
            if token == '<s>':
                continue
            if token == '</s>':
                break
            content.append(token)
        return detokenize(content)
```
- **Đầu vào**:
	- **`model`**: Mô hình ngôn ngữ đã được huấn luyện (ví dụ: mô hình n-gram như vi_model) có khả năng dự đoán từ tiếp theo dựa trên ngữ cảnh.
	- **`num_words`**: Số lượng từ tối đa sẽ được sinh thêm sau seed.
	- **`pre_words`**: Một danh sách các từ ban đầu (seed) dùng để khởi đầu quá trình sinh từ.
	
- **Đầu ra**: Một câu hoàn chỉnh (chuỗi văn bản) được sinh ra từ việc nối các token, bao gồm seed ban đầu và các từ được dự đoán thêm bởi mô hình
	
- **Cách hoạt động**:
	- **Khởi tạo chuỗi nội dung**:
		- Biến `content` được khởi tạo bằng danh sách `pre_words`. Đây là phần bắt đầu của câu.
	- **Vòng lặp sinh từ**:
		- Trong mỗi vòng lặp, hàm `model.generate(1, text_seed=content[-2:])` sử dụng **2 từ cuối** của danh sách `content` làm ngữ cảnh để sinh ra **một từ mới**.
		- Nếu từ sinh ra là token bắt đầu câu `'<s>'`, ta bỏ qua (không thêm vào).
		- Nếu từ sinh ra là token kết thúc câu `'</s>'`, quá trình sinh từ dừng lại ngay lập tức.
		- Nếu không, từ đó được thêm vào danh sách `content`.
	- **Ghép các token thành câu hoàn chỉnh**:
		- Sau khi vòng lặp kết thúc (do đạt đủ số từ hoặc gặp token kết thúc), danh sách `content` được chuyển thành một chuỗi văn bản bằng hàm `detokenize`.

3. **Gọi hàm generate_sent để sinh câu**
```python
    generate_sent(vi_model, 10, ["đất", "nước"])
```
- **Đầu vào**:
	- **`vi_model`**: Mô hình ngôn ngữ đã được huấn luyện.
	- **`10`**: Số từ tối đa sẽ được sinh thêm (không tính các từ seed ban đầu).
	- **`["đất", "nước"]`**: Seed ban đầu cho câu, nghĩa là câu sẽ bắt đầu với "đất nước".
- **Đầu ra**:
	- Một câu hoàn chỉnh được tạo ra bởi mô hình, ví dụ như "đất nước ...", thể hiện khả năng dự đoán từ tiếp theo của mô hình dựa trên ngữ cảnh đã cho.
	
- Hàm `generate_sent` sử dụng ngữ cảnh là 2 từ cuối cùng của câu hiện tại để dự đoán từ tiếp theo. Quá trình dừng lại khi đủ số từ yêu cầu hoặc gặp token kết thúc câu.


## Load Model
1. **Chạy mô hình từ  tệp**
```python
import os
import pickle

# Save model
model_dir = "/content/drive/My Drive/Colab Notebooks/Ngram_model"
with open(os.path.join(model_dir, 'kneserney_1st_ngram_model.pkl'), 'rb') as fin:
    model_loaded = pickle.load(fin)

print(len(model_loaded.vocab))
```
- Lấy mô hình được lưu từ trước trong thư mục `model_dir`. 

## Download VN syllables
```python
!wget -O vn_syllables.txt "https://gist.githubusercontent.com/hieuthi/0f5adb7d3f79e7fb67e0e499004bf558/raw/135a4d9716e49a981624474156d6f247b9b46f6a/all-vietnamese-syllables.txt"
```
+ Tải thư viện âm tiết tiếng việt


## Xử lý Dấu Tiếng Việt và Sinh Biến Thể Có Dấu
### Mục đích và ý nghĩa
- **Mục đích**: Đoạn code này được thiết kế để **loại bỏ các dấu** trong từ tiếng Việt và sau đó **tìm kiếm, sinh ra các biến thể có dấu** của từ đó từ một danh sách các âm tiết tiếng Việt lưu trong tệp `vn_syllables.txt`.
- **Ý nghĩa**: Trong xử lý ngôn ngữ tiếng Việt, dấu có vai trò quan trọng nhưng cũng có thể gây ra nhiều phức tạp. Việc chuyển từ sang dạng không dấu giúp so sánh dễ dàng hơn, và từ đó có thể tái tạo lại các phiên bản có dấu dựa trên một tập dữ liệu chuẩn. Điều này hữu ích cho các ứng dụng như khôi phục dấu hoặc hiệu chỉnh văn bản.

### Chi tiết các bước
- **Đầu vào chung**: Một từ tiếng Việt cần được xử lý, chẳng hạn `"hoang"`.
- **Quá trình**:
    - **Bước 1**: Sử dụng hàm `remove_vn_accent` để chuyển đổi từ thành phiên bản không dấu.
    - **Bước 2**: Hàm `gen_accents_word` mở tệp danh sách âm tiết tiếng Việt, so sánh từng từ (sau khi loại bỏ dấu) với từ đầu vào không dấu, và nếu trùng khớp thì thêm biến thể gốc (có dấu) vào tập hợp kết quả.
- **Đầu ra chung**: Một tập hợp chứa tất cả các biến thể có dấu của từ đầu vào, giúp phục vụ cho các ứng dụng như phục hồi dấu trong văn bản hoặc cải thiện xử lý ngôn ngữ tiếng Việt.
 
1. **Hàm `remove_vn_accent`**
```python
    def remove_vn_accent(word):
        word = re.sub('[áàảãạăắằẳẵặâấầẩẫậ]', 'a', word)
        word = re.sub('[éèẻẽẹêếềểễệ]', 'e', word)
        word = re.sub('[óòỏõọôốồổỗộơớờởỡợ]', 'o', word)
        word = re.sub('[íìỉĩị]', 'i', word)
        word = re.sub('[úùủũụưứừửữự]', 'u', word)
        word = re.sub('[ýỳỷỹỵ]', 'y', word)
        word = re.sub('đ', 'd', word)
        return word
```
- **Đầu vào**:
	- **`word`**: Một từ tiếng Việt, có thể chứa dấu. Ví dụ: `"hoàng"`.
- **Quá trình hoạt động**:
	- Hàm sử dụng **`re.sub`** để thay thế các ký tự có dấu thành phiên bản không dấu tương ứng:
		- Các ký tự như `á, à, ả, ã, ạ, ă, ...` được thay thế bằng chữ `'a'`.
		- Tương tự cho các chữ `e, o, i, u, y` và thay `'đ'` bằng `'d'`.
- **Đầu ra**:
	- Trả về phiên bản của từ đã được **loại bỏ tất cả dấu**, ví dụ từ `"hoàng"` sẽ trở thành `"hoang"`.

2. **Hàm `gen_accents_word`**
```python
    def gen_accents_word(word):
        word_no_accent = remove_vn_accent(word.lower())
        all_accent_word = {word}
        for w in open('vn_syllables.txt').read().splitlines():
            w_no_accent = remove_vn_accent(w.lower())
            if w_no_accent == word_no_accent:
                all_accent_word.add(w)
        return all_accent_word
```
+ **Đầu vào**:
	- **`word`**: Một từ tiếng Việt cần tìm các biến thể có dấu. Ví dụ: `"hoang"`.
+ **Quá trình hoạt động**:
	1. **Chuẩn hóa từ đầu vào**:
		- **`word.lower()`**: Chuyển từ về chữ thường.
		- **`remove_vn_accent(word.lower())`**: Loại bỏ dấu để lấy phiên bản không dấu của từ, lưu vào biến **`word_no_accent`**.
	2. **Khởi tạo tập hợp các biến thể**:
		- **`all_accent_word = {word}`**: Tập hợp ban đầu chứa từ gốc (theo định dạng ban đầu của nó).
	3. **Tìm kiếm biến thể từ tệp `vn_syllables.txt`**:
		- Mở tệp `vn_syllables.txt` và đọc từng dòng thành danh sách các từ.
		- Với mỗi từ **`w`** trong tệp:
			- Chuyển thành chữ thường và loại bỏ dấu bằng hàm `remove_vn_accent`, lưu kết quả vào **`w_no_accent`**.
			- So sánh **`w_no_accent`** với **`word_no_accent`**. Nếu chúng bằng nhau, có nghĩa là từ `w` là một biến thể có dấu của từ gốc.
			- Thêm từ `w` vào tập hợp **`all_accent_word`**.
	4. **Trả về kết quả**:
		- Hàm trả về tập hợp **`all_accent_word`** chứa tất cả các biến thể của từ đã tìm được.
		
+ **Đầu ra**:  Một tập hợp các biến thể có dấu của từ đầu vào. Ví dụ: với input `"hoang"`, kết quả có thể là:
```python
	{'hoang', 'hoàng', 'hoáng', 'hoãng', 'hoăng', 'hoạng', 'hoảng', ...}
```
 Tập hợp này giúp ta biết tất cả các cách viết có dấu của từ "hoang" theo dữ liệu trong tệp.


## Beam Search cho dự đoán dấu Tiếng Việt
### Mục đích và ý nghĩa
- **Mục đích**: Sử dụng thuật toán beam search để lựa chọn ra các chuỗi từ có dấu tốt nhất dựa trên đầu vào không dấu. Thuật toán này duy trì một tập hợp các khả năng (beam) và ở mỗi bước chỉ giữ lại những chuỗi có tổng logscore cao nhất theo mô hình ngôn ngữ.
- **Ý nghĩa**: Giúp cải thiện quá trình phục hồi dấu tiếng Việt bằng cách không chỉ dựa vào dự đoán đơn lẻ mà còn xét đến ngữ cảnh của cả câu, từ đó đưa ra những lựa chọn có khả năng xuất hiện cao nhất theo mô hình n-gram đã được huấn luyện.
+ **Định nghĩa hàm và tham số đầu vào, đầu ra**
	- **Đầu vào**:
		- **`words`**: Danh sách các từ không dấu cần phục hồi dấu, ví dụ `["ngay", "hom", "qua", ...]`.
		- **`model`**: Mô hình ngôn ngữ n-gram đã được huấn luyện, dùng để tính toán logscore (xác suất dưới dạng logarithm) của các chuỗi từ.
		- **`k`**: Số lượng chuỗi kết quả được giữ lại tại mỗi bước (beam width). Mặc định là 3.
	- **Đầu ra**:
		- Trả về danh sách các tuple, mỗi tuple chứa:
			- Một chuỗi từ (danh sách các từ có dấu) được sinh ra.
			- Tổng logscore của chuỗi đó, cho biết khả năng xuất hiện của chuỗi theo mô hình.

### Chi tiết các bước
- **Đầu vào chung**: Danh sách các từ không dấu (`words`), mô hình ngôn ngữ đã huấn luyện (`model`), và số lượng beam `k`.
- **Quá trình**:
    - Bắt đầu với từ đầu tiên, sinh ra các biến thể có dấu khác nhau.
    - Với từng từ sau, mở rộng các chuỗi hiện có bằng cách thêm các biến thể của từ đó, đồng thời tính toán tổng logscore của chuỗi.
    - Sau mỗi bước, chỉ giữ lại `k` chuỗi có tổng logscore cao nhất.
- **Đầu ra chung**: Danh sách các chuỗi từ (các biến thể có dấu) cùng với điểm số của chúng, giúp ta lựa chọn ra chuỗi có dấu phù hợp nhất cho câu đầu vào


1. **Khởi tạo chuỗi ở bước đầu tiên**
    ```python
    if idx == 0:
       sequences = [([x], 0.0) for x in gen_accents_word(word)]
    ```
	- Với từ đầu tiên trong danh sách `words`, hàm `gen_accents_word(word)` được sử dụng để tạo ra tất cả các biến thể có dấu của từ đó.
	- Mỗi biến thể được lưu thành một tuple: (danh sách chứa biến thể, tổng score ban đầu = 0.0).
	- **Đầu ra**: Một tập hợp ban đầu các chuỗi từ (chỉ chứa từ đầu tiên với các biến thể khác nhau).
	
2. **Mở rộng chuỗi cho các từ còn lại**
    ```python
    else:
       all_sequences = []
       for seq in sequences:
         for next_word in gen_accents_word(word):
           current_word = seq[0][-1]
           try:
               previous_word = seq[0][-2]
               score = model.logscore(next_word, [previous_word, current_word])
           except:
               score = model.logscore(next_word, [current_word])
           new_seq = seq[0].copy()
           new_seq.append(next_word)
           all_sequences.append((new_seq, seq[1] + score))
       all_sequences = sorted(all_sequences, key=lambda x: x[1], reverse=True)
       sequences = all_sequences[:k]
    ```
	- **Với mỗi từ mới trong `words`** (từ thứ hai trở đi), thuật toán mở rộng từng chuỗi đã có:
		- **Duyệt qua mỗi chuỗi `seq` hiện tại** trong `sequences`.
		- Với mỗi chuỗi, dùng hàm `gen_accents_word(word)` để lấy tất cả các biến thể có dấu của từ hiện tại.
	- **Tính logscore cho từ mới**:
		- Lấy từ cuối (`current_word`) của chuỗi hiện tại làm ngữ cảnh.
		- Nếu chuỗi đã có ít nhất 2 từ, lấy cả từ kế cuối (`previous_word`) để tạo ngữ cảnh 2-gram cho việc tính logscore.
		- Sử dụng **`model.logscore(next_word, [previous_word, current_word])`** nếu có đủ ngữ cảnh, hoặc **`model.logscore(next_word, [current_word])`** nếu không có.
		- Logscore được tính ra là điểm số cho từ mới dựa trên ngữ cảnh hiện tại.
	- **Tạo chuỗi mới**:
		- Sao chép chuỗi hiện tại, thêm từ mới vào, và cộng dồn logscore.
		- Thêm chuỗi mới (với tổng logscore cập nhật) vào danh sách `all_sequences`.
	- **Lựa chọn các chuỗi tốt nhất**:
		- Sau khi duyệt hết các khả năng, sắp xếp `all_sequences` theo tổng logscore (giá trị càng cao thì khả năng xuất hiện càng tốt).
		- Chỉ giữ lại `k` chuỗi có điểm số cao nhất cho bước tiếp theo.
	
3. **Trả về kết quả cuối cùng**
    ```python
    return sequences
    ```
	- Sau khi duyệt qua tất cả các từ trong `words`, hàm trả về danh sách `sequences` cuối cùng.
	- **Đầu ra**: Một danh sách các tuple, mỗi tuple gồm một chuỗi từ có dấu và tổng logscore của chuỗi đó. Đây là các chuỗi được xem là có khả năng cao nhất theo mô hình.


### Validate Beam Search Function
>Để kiểm tra thuật toán Beam search đầu tiên ta cần tách câu thành list các chuỗi. Ta gọi hàm beam search để dự đoán dấu câu và sử dụng detokenize để chuyển danh sách các từ trong chuỗi đó thành 1 câu hoàn chỉnh.
```python
from nltk.tokenize.treebank import TreebankWordDetokenizer
detokenize = TreebankWordDetokenizer().detokenize

sentence = "ngay hom qua la ngay bau cư tong thong My"
result = beam_search(sentence.lower().split(), model_loaded) 

print(detokenize(result[0][0])) # convert list of token to a complete sentence
```
```python
	"ngày hôm qua là ngày bầu cử tổng thống mỹ".
```


