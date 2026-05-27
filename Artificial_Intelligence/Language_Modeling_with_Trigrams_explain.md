## Preprocess
#### Mục đích và ý nghĩa
+ @ Đoạn code này nhằm mục đích tiền xử lý dữ liệu văn bản thô bằng cách tách văn bản thành các câu và sau đó tách từng câu thành các token (từ). Việc tokenization này rất quan trọng trong các ứng dụng xử lý ngôn ngữ tự nhiên, bởi nó chuyển đổi văn bản thành dạng dữ liệu có cấu trúc để phục vụ cho các bước phân tích hoặc mô hình ngôn ngữ sau này. Code sử dụng biểu thức chính quy để tăng tốc độ xử lý và multiprocessing để tận dụng hiệu quả đa lõi, đặc biệt hữu ích khi xử lý tập dữ liệu lớn.

#### Chi tiết các bước thực hiện

1. **Nhập các thư viện và tiền biên dịch các mẫu regex:**
    ```python
    from tqdm import tqdm
    import multiprocessing as mp
    import re
    
    # Precompile regex patterns:
    TOKEN_REGEX = re.compile(r"[\w_]+")
    SENT_REGEX = re.compile(r'(?<=[^A-Z].[.?]) +(?=[A-Z])')
    ```
    - **Ý tưởng & Liên hệ:**
        - Trước tiên, ta nhập các thư viện cần thiết:
            - `re` để làm việc với biểu thức chính quy,
            - `tqdm` để hiển thị progress bar, và
            - `multiprocessing` để thực hiện xử lý song song.
        - Sau đó, ta tiền biên dịch hai mẫu regex:
            - `TOKEN_REGEX` nhằm nhận diện các chuỗi ký tự (chữ, số, dấu gạch dưới) dùng cho việc tách từ,
            - `SENT_REGEX` dùng để tách văn bản thành các câu dựa trên dấu câu và khoảng trắng kèm theo chữ hoa.
        - Việc tiền biên dịch giúp tăng hiệu suất vì regex không phải được biên dịch lại mỗi khi sử dụng.
	
2. **Định nghĩa hàm tokenize:**
    ```python
    def tokenize(doc):
        """
        Tokenizes the document by converting to lowercase and extracting words.
        This version uses a precompiled regex, which is faster than nltk.word_tokenize.
        """
        return TOKEN_REGEX.findall(doc.lower())
    ```
    - **Ý tưởng & Liên hệ:**
        - Hàm `tokenize` nhận đầu vào là một chuỗi văn bản (`doc`), chuyển nó về dạng chữ thường để đồng nhất.
        - Sau đó, sử dụng `TOKEN_REGEX.findall()` để tìm tất cả các chuỗi khớp, từ đó trích xuất các token.
    - **Chi tiết hoạt động:**
        - `doc.lower()` đảm bảo rằng việc so sánh không bị phân biệt chữ hoa chữ thường.
        - `TOKEN_REGEX.findall(...)` quét toàn bộ văn bản và trả về danh sách các token, ví dụ như ["this", "is", "a", "sample"].
	
3. **Định nghĩa hàm process_sentence:**
    ```python
    def process_sentence(sent):
        """
        Helper function to tokenize a single sentence.
        """
        return tokenize(sent)
    ```
    - **Ý tưởng & Liên hệ:**
        - Hàm `process_sentence` là một hàm trợ giúp đơn giản, chỉ gọi `tokenize` trên một câu (`sent`).
        - Điều này giúp tích hợp dễ dàng với quá trình xử lý song song, khi mỗi câu sẽ được token hóa riêng biệt.
    - **Chi tiết hoạt động:**
        - Mỗi câu được truyền vào hàm này và kết quả trả về là danh sách các token của câu đó.
	
4. **Xử lý dữ liệu văn bản ban đầu:**
    ```python
    full_text = ". ".join(full_data).replace("\n", ". ")
    ```
    - **Ý tưởng & Liên hệ:**
        - Nếu `full_data` là một danh sách các chuỗi văn bản, ta cần nối chúng thành một chuỗi văn bản duy nhất để xử lý thống nhất.
        - Đồng thời, việc thay thế ký tự xuống dòng (`\n`) bằng dấu chấm và khoảng trắng giúp đảm bảo rằng mỗi dòng mới được coi như kết thúc của một câu.
    - **Chi tiết hoạt động:**
        - `". ".join(full_data)` nối các chuỗi lại với nhau, chèn dấu chấm và khoảng trắng giữa các phần tử.
        - `.replace("\n", ". ")` chuyển đổi các dòng mới thành dấu chấm, giúp regex tách câu hoạt động hiệu quả hơn.
	
5. **Tách văn bản thành các câu:**
    ```python
    sents = SENT_REGEX.split(full_text)
    ```
    - **Ý tưởng & Liên hệ:**
        - Sử dụng mẫu `SENT_REGEX` để phân chia văn bản thành các câu, dựa vào dấu câu kết thúc và khoảng trắng theo sau là chữ hoa.
        - Điều này tạo ra danh sách `sents` với mỗi phần tử là một câu riêng biệt.
    - **Chi tiết hoạt động:**
        - `SENT_REGEX.split(full_text)` cắt chuỗi `full_text` thành các mảnh dựa trên mẫu regex, tạo nên danh sách các câu để xử lý tiếp theo.
	
6. **Tokenization song song sử dụng multiprocessing:**
    ```python
    with mp.Pool() as pool:
        corpus = list(tqdm(pool.imap(process_sentence, sents), total=len(sents), desc="Tokenizing sentences"))
    ```
    - **Ý tưởng & Liên hệ:**
        - Để tăng tốc quá trình tokenization cho nhiều câu, ta sử dụng `multiprocessing.Pool` để xử lý song song.
        - `pool.imap(process_sentence, sents)` áp dụng hàm `process_sentence` cho từng câu trong danh sách `sents`.
    - **Chi tiết hoạt động:**
        - `mp.Pool()` tạo ra một pool các tiến trình, mỗi tiến trình có thể xử lý một phần của danh sách.
        - `tqdm(...)` bọc quanh iterator của `pool.imap` để hiển thị progress bar, cho biết số câu đã được token hóa so với tổng số.
        - Kết quả được chuyển thành danh sách `corpus`, trong đó mỗi phần tử là danh sách token của một câu.
	
7. **In kết quả tokenization:**
    ```python
    print("Tokenization complete. Number of sentences:", len(corpus))
    ```


### Hàm N-Gram
#### Mục đích và ý nghĩa
+ @ Hàm `n_gram(tokens, n)` được thiết kế để tạo danh sách **n-gram** từ một danh sách token. Trong xử lý ngôn ngữ tự nhiên, **n-gram** là một chuỗi gồm _n_ token liên tiếp, đóng vai trò quan trọng trong việc xây dựng các mô hình thống kê ngôn ngữ (như trigram, bigram, v.v.). Mục tiêu là thu thập tất cả các **n-gram** có thể có trong tập token đầu vào để hỗ trợ quá trình huấn luyện hoặc phân tích ngôn ngữ.

#### Chi tiết các bước

1. **Nhận đầu vào**:
    - `tokens`: Danh sách các token (chuỗi).
    - `n`: Số nguyên cho biết độ dài mỗi n-gram (chẳng hạn `n=3` cho trigram).
	
2. **Khởi tạo danh sách kết quả**:
    - `n_gram_list = []`: Danh sách rỗng để lưu các n-gram.
	
3. **Tạo n-gram**:
    - Lặp qua các vị trí _i_ từ `0` đến `len(tokens) - n + 1`.
    - Mỗi lần lặp, lấy _n_ token liên tiếp từ vị trí _i_ bằng `tokens[i:i+n]`.
    - Chuyển đoạn token đó thành tuple: `tuple(tokens[i:i+n])`.
    - Thêm tuple này vào `n_gram_list`.
	
4. **Trả về kết quả**:
    - Kết thúc vòng lặp, hàm trả về toàn bộ danh sách n-gram (`n_gram_list`).


## 3.1 Get N-gram counts
#### Mục đích và ý nghĩa
+ @ Hàm `get_ngram_counts(corpus, n)` có nhiệm vụ tạo danh sách các từ điển (dictionary), trong đó mỗi từ điển biểu diễn tần suất xuất hiện của i-gram (với i = 1 đến n) trong toàn bộ tập dữ liệu `corpus`. Đây là bước chuẩn bị quan trọng trong quá trình xây dựng mô hình ngôn ngữ thống kê (như bigram, trigram), giúp ta nắm được số lần mỗi i-gram xuất hiện.

### Chi tiết các bước

1. **Khởi tạo danh sách kết quả**
```python
    result = []
```
- `result` sẽ chứa _n_ phần tử (tương ứng với i-gram từ 1 đến n), mỗi phần tử là một từ điển lưu trữ tần suất i-gram.
	
2. **Tính tần suất cho từng i-gram (vòng lặp i)**
    ```python
    for i in range(1, n+1):
        ngram_dict = {}
        ...
        result.append(ngram_dict)
    ```
- Duyệt từ `i = 1` đến `i = n`.
- Với mỗi giá trị `i`, tạo một từ điển `ngram_dict` rỗng để lưu i-gram cùng tần suất của chúng.
- Sau khi xử lý xong i-gram, thêm `ngram_dict` vào `result`.
	
3. **Lặp qua từng câu (tokens) trong `corpus`**
    ```python
    for tokens in tqdm(corpus):
        n_gram_list = n_gram(tokens, n=i)
        ...
    ```
    - Dùng `tqdm` để theo dõi tiến độ khi duyệt qua danh sách các câu.
    - Gọi hàm `n_gram(tokens, n=i)` để tạo danh sách i-gram cho câu hiện tại.
	
4. **Cập nhật tần suất i-gram**
    ```python
    for tmp_n_gram in n_gram_list:
        if tmp_n_gram in ngram_dict:
            ngram_dict[tmp_n_gram] += 1
        else:
            ngram_dict[tmp_n_gram] = 1
    ```
    - Lặp qua từng i-gram (được lưu trong `n_gram_list`).
    - Nếu i-gram đã có trong `ngram_dict`, tăng giá trị đếm lên 1.
    - Nếu chưa, khởi tạo giá trị tần suất bằng 1.
	
5. **Trả về danh sách tần suất i-gram**
    ```python
    return result
    ```
    - Kết thúc vòng lặp, `result` là một danh sách gồm _n_ phần tử, mỗi phần tử là một từ điển chứa tần suất xuất hiện của i-gram trong `corpus`.
    - Kết cấu:
        - `result[0]` chứa tần suất unigram (1-gram).
        - `result[1]` chứa tần suất bigram (2-gram).
        - …
        - `result[n-1]` chứa tần suất n-gram (n-gram).

## 3.2 Next word probability
### Mục đích và ý nghĩa
+ @ Hàm `calc_ngram_prob(context, word)` được dùng để tính **xác suất có điều kiện** (dưới dạng log) của từ `word` dựa trên bối cảnh (`context`). Cụ thể, nó tính xác suất `P(word | w_2, w_1)` trong mô hình **trigram**. Xác suất này giúp chúng ta biết mức độ khả thi khi `word` xuất hiện sau cặp từ `(w_2, w_1)`. Đây là bước quan trọng để mô hình có thể dự đoán từ tiếp theo với ngôn ngữ tiếng Việt (hoặc bất kỳ ngôn ngữ nào) dựa trên các thống kê từ tập dữ liệu.

### Chi tiết các bước
1. **Nhận tham số đầu vào**  
   - `context`: Là một bộ (tuple) chứa 2 từ, `(w_2, w_1)`, đại diện cho bối cảnh (2 từ đứng trước).  
   - `word`: Từ cần tính xác suất xuất hiện tiếp theo.
	
2. **Trích xuất giá trị đếm**  
```python
w_2, w_1 = context
trigram_count = trigram_coll.get((w_2, w_1, word), 0)
bigram_count = bigram_coll.get((w_2, w_1), 0)
```
   - `trigram_count`: Số lần xuất hiện của bộ 3 (w_2, w_1, word) trong ngữ liệu (nếu không có, mặc định 0).  
   - `bigram_count`: Số lần xuất hiện của bộ 2 (w_2, w_1) trong ngữ liệu (nếu không có, mặc định 0).
	
3. **Kiểm tra trigram có tồn tại**  
```python
if trigram_count == 0:
   return float('-inf')
```
   - Nếu `trigram_count` bằng 0, nghĩa là bộ 3 `(w_2, w_1, word)` **chưa hề xuất hiện** trong dữ liệu.  
   - Hàm trả về `float('-inf')`, thể hiện xác suất cực kỳ thấp (log-probability âm vô cùng).
	
4. **Tính toán xác suất (dưới dạng log)**  
```python
prob = math.log(trigram_count) - math.log(bigram_count)
return prob
```
   - Công thức tính log của xác suất có điều kiện:  
$$\log P(\text{word} | w_2, w_1) = \log \Big(\frac{\text{trigram count}}{\text{bigram count}}\Big)
 = \log(\text{trigram count}) - \log(\text{bigram count})$$
   - Kết quả `prob` là giá trị log-probability; giá trị này càng lớn thì xác suất càng cao.


### 3.2.1 Propability with Add-1 smoothing
#### Mục đích và ý nghĩa  
- @ Trong mô hình trigram, ta cần tính xác suất từ tiếp theo dựa vào hai từ trước đó. Hàm này sử dụng kỹ thuật **Add-One Smoothing** (còn gọi là Laplace Smoothing) để tránh xác suất bằng 0 trong trường hợp cặp (bigram) hoặc bộ ba (trigram) chưa từng xuất hiện.
- ? Thay vì để đếm (count) bằng 0 dẫn đến xác suất bằng 0, em cộng thêm 1 vào số đếm của trigram, đồng thời cộng thêm “V” (kích thước từ vựng) vào số đếm bigram khi tính xác suất, rồi lấy log.

---

#### Chi tiết các bước hàm  `calc_ngram_prob_with_add_one`:
1. **Nhận `context` và tách từ**
    - Ta đọc hai từ trong bối cảnh (context) bằng cách: `w1, w2 = context`. Như vậy, `(w1, w2)` chính là cặp từ đi trước.
	
2. **Lấy số lần xuất hiện (count)**
    ```python
    trigram_count = trigram_coll.get(((w1, w2), word), 0)
    bigram_count  = bigram_coll.get(((w1, w2), word), 0)
    ```
    - `trigram_count`: Số lần xuất hiện của bộ ba `(w1, w2, word)`. Nếu chưa có trong dữ liệu, hàm `get` sẽ trả về 0.
    - `bigram_count`: Số lần xuất hiện của cặp `(w1, w2)`.
	
3. **Kiểm tra điều kiện đặc biệt**
    ```python
    if trigram_count == 0 or bigram_count == 0:
        return float('-inf')
    ```
    - Nếu chưa gặp trường hợp nào của bigram hoặc trigram trong ngữ liệu (nghĩa là count = 0), hàm sẽ trả về `-inf` (logarithm của 0). Đây là cách biểu diễn “xác suất bằng 0” trong không gian log.
	
4. **Tính kích thước từ vựng (V)**
    - `V = len(vocab)`: Em xác định độ lớn tập từ vựng. Trong Add-One Smoothing, con số này sẽ được thêm vào số lần đếm bigram trong phần mẫu.
	
5. **Áp dụng công thức Add-One Smoothing**
    ```python
    prob = (trigram_count + 1) / (bigram_count + V)
    return math.log(prob)
    ```
    - Công thức này chia (trigram_count + 1) cho (bigram_count + V).
    - Sau đó, để thuận tiện cho các phép tính xác suất nhỏ, ta trả về `math.log(prob)` thay vì trả về xác suất thô.

Nhờ Add-One Smoothing, mô hình sẽ không bị rơi vào tình huống xác suất 0 khi gặp các n-gram hiếm hoặc hoàn toàn mới. 

### 3.2.2 Stupid backoff
#### Mục đích và ý nghĩa
+ @ Hàm `calc_ngram_prob_with_backoff(context, word)` tính xác suất có điều kiện của một từ dựa trên bối cảnh bằng **thuật toán Stupid Backoff**.
	- Nếu bộ n-gram đầy đủ tồn tại trong dữ liệu, xác suất sẽ được tính trực tiếp từ tần suất xuất hiện của nó.
	- Nếu không, thuật toán sẽ **lùi về mô hình nhỏ hơn** (trigram → bigram → unigram) với một hệ số giảm (`0.4`).
	- Nếu không có dữ liệu nào, xác suất unigram được sử dụng.
	- Hàm sử dụng **bộ nhớ đệm** (`prob`) để tránh tính toán lại những giá trị đã được xử lý trước đó.

#### Chi tiết các bước
1. **Kiểm tra từ ngoài từ vựng**  
	```python
   for token in context:
       if token not in vocab:
           return float('-inf')
   if word not in vocab:
       return float('-inf')
	```
	- Kiểm tra xem từ trong `context` và từ cần tính xác suất (`word`) có trong từ vựng `vocab` hay không.
	- Nếu có bất kỳ từ nào không có trong từ vựng, trả về `-inf` (log-probability bằng 0), nghĩa là không thể tính được xác suất.
	
1. **Kiểm tra và trả về giá trị đã tính toán trước đó**
    ```python
    if word in prob[context]:
        return prob[context][word]
    ```
    - Nếu xác suất của từ `word` đã được tính với bối cảnh `context` trước đó và lưu trong bộ nhớ đệm `prob`, trả lại giá trị đã tính.
    
2. **Trường hợp trigram (bối cảnh gồm 2 từ)**
    ```python
    if len(context) == 2:
        bigram_count = bigram_coll.get(context, 0)
        trigram_count = trigram_coll.get((context[0], context[1], word), 0)
    
        if trigram_count > 0 and bigram_count > 0:
            log_prob = math.log(trigram_count / bigram_count)
        else:
            log_prob = math.log(0.4) + calc_ngram_prob_with_backoff((context[1],), word)
    ```
    - **Bối cảnh trigram** gồm 2 từ trước (`context[0]`, `context[1]`).
    - Nếu trigram `(context[0], context[1], word)` và bigram `(context[0], context[1])` có tồn tại trong dữ liệu, tính xác suất của trigram theo công thức: $$\log P(w \mid w_{i-2}, w_{i-1}) = \log \left( \frac{c(w_{i-2}, w_{i-1}, w)}{c(w_{i-2}, w_{i-1})} \right)$$
    - Nếu không có trigram, lùi về **bigram** với hệ số giảm `0.4` và tính xác suất cho bigram `(context[1], word)`.
    
3. **Trường hợp bigram (bối cảnh gồm 1 từ)**
    ```python
    elif len(context) == 1:
        unigram_count = unigram_coll.get((context[0],), 0)
        bigram_count = bigram_coll.get((context[0], word), 0)
    
        if bigram_count > 0 and unigram_count > 0:
            log_prob = math.log(bigram_count / unigram_count)
        else:
            log_prob = math.log(0.4) + calc_ngram_prob_with_backoff((), word)
    ```
    - **Bối cảnh bigram** gồm 1 từ trước (`context[0]`).
    - Nếu bigram `(context[0], word)` và unigram `(context[0])` có tồn tại trong dữ liệu, tính xác suất của bigram.
    - Nếu không có bigram, lùi về **unigram** với hệ số giảm `0.4` và tính xác suất của từ `word` dựa trên unigram.
	
4. **Trường hợp unigram (không có bối cảnh)**
    ```python
    else:
        count_word = unigram_coll.get((word,), 0)
        if count_word > 0:
            log_prob = math.log(count_word / N)
        else:
            log_prob = float('-inf')
    ```
    - **Bối cảnh unigram**: Khi không có bối cảnh (tức là chỉ tính xác suất của từ `word` một cách độc lập).
    - Nếu từ `word` có xuất hiện trong **unigram collection**, tính xác suất theo công thức: $$\log \left( \frac{c(w)}{N} \right)$$
    - Nếu từ không có trong unigram, trả về `-inf`.
	
5. **Lưu và trả về kết quả**
    ```python
    prob[context][word] = log_prob
    return log_prob
    ```
    - Lưu giá trị `log_prob` tính được vào bộ nhớ đệm `prob` cho bối cảnh `context` và từ `word`.
    - Trả về giá trị log probability của từ `word` dựa trên bối cảnh `context`.
	
+ ? Hàm sử dụng **Stupid Backoff** để tính xác suất có điều kiện cho các từ trong n-gram, và sử dụng mô hình hồi lại (backoff) với hệ số giảm khi không thể tính toán xác suất đầy đủ từ trigram hoặc bigram.


### 3.2.3 Knesser-Ney Smoothing (Only for bigram)
#### Mục đích và ý nghĩa
- @ Hàm `kesser_ney_smoothing(context, word, discount=0.75)` tính xác suất theo phương pháp **Kneser-Ney smoothing** cho mô hình bigram (với bối cảnh là unigram).
- ? Kneser-Ney khắc phục hạn chế của các phương pháp đơn giản như Stupid Backoff và Interpolation (vốn phụ thuộc nhiều vào MLE) bằng cách tận dụng thông tin về số lượng “bối cảnh duy nhất” (unique preceding words) của từ để đánh giá khả năng xuất hiện của từ đó.
- @ Với **Kneser-Ney**, xác suất được phân rã thành hai thành phần chính:
    1. **Phần giảm trừ (discounted)** dựa trên tần suất bigram.
    2. **Phần bù (continuation)** dựa trên số bối cảnh duy nhất mà từ có thể xuất hiện.

#### Chi tiết các bước
1. **Kiểm tra từ vựng**
    - Duyệt tất cả các token trong `context` và cả `word`. Nếu có từ nằm ngoài `vocab`, trả về `float('-inf')`.
    
2. **Kiểm tra độ dài của `context`**
    - Mặc định hàm chỉ xử lý **bối cảnh unigram** (tức là bigram). Nếu `len(context) != 1`, trả về `float('-inf')`.
	
3. **Lấy số lần xuất hiện của `context`**
    ```python
    w_prev = context[0]
    count_w_prev = unigram_coll.get((w_prev,), 0)
    ```
    - `count_w_prev`: Số lần xuất hiện của từ `w_prev` trong `unigram_coll`.
    - Nếu `count_w_prev == 0`, trả về `float('-inf')`.
	
4. **Tính toán phần bigram**
    ```python
    count_bigram = bigram_coll.get((w_prev, word), 0)
    first_term = max(count_bigram - discount, 0) / count_w_prev
    ```
    - **`count_bigram`**: Số lần bigram `(w_prev, word)` xuất hiện trong tập dữ liệu.
    - **`first_term`**: Phần Likelihood đã được giảm trừ bởi `discount`. $$\text{first term} = \frac{\max(c(w_{i-1}, w_i) - d, 0)}{c(w_{i-1})}$$
5. **Tính trọng số $\lambda(w_{i-1})$**
    ```python
    unique_followers = sum(1 for w in vocab if bigram_coll.get((w_prev, w), 0) > 0)
    lambda_w_prev = (discount / count_w_prev) * unique_followers
    ```
    - **`unique_followers`**: Số lượng từ khác nhau đi sau `w_prev`.
    - **$\lambda(w_{i-1})$**: Mức độ back-off, tỉ lệ thuận với số từ theo sau `w_prev`, và được chia cho `count_w_prev`.
	
6. **Tính xác suất tiếp diễn ($P_{\text{CONTINUATION}}$)**
    ```python
    unique_preceding = sum(1 for (w_prev_candidate, w_candidate) in bigram_coll if w_candidate == word)
    p_continuation = unique_preceding / total_unique_bigrams
    ```
    - **`unique_preceding`**: Số bối cảnh duy nhất (từ đứng trước) mà `word` có thể xuất hiện.
    - **`total_unique_bigrams`**: Tổng số bigram khác nhau trong `bigram_coll`.
    - Xác suất tiếp diễn (Continuation) được tính bởi công thức: $$P_{CONTINUATION}(w) = \frac{\text{Số bối cảnh duy nhất của } w}{\text{Tổng số bigram duy nhất}}$$
7. **Kết hợp hai thành phần**
    ```python
    return first_term + lambda_w_prev * p_continuation
    ```
    - Xác suất theo Kneser-Ney: $$P_{\text{KN}}(w_i \mid w_{i-1}) = \frac{\max(c(w_{i-1}, w_i) - d, 0)}{c(w_{i-1})} + \lambda(w_{i-1}) \cdot P_{\text{CONTINUATION}}(w_i)$$
    - Kết quả trả về là **xác suất** (không phải log-prob), do phương pháp Kneser-Ney mang tính đệ quy và cần giá trị xác suất thực để tiếp tục tính toán.
	
8. **Các trường hợp ngoại lệ**
    - Nếu bất kỳ bước nào trả về `float('-inf')`, coi như mô hình không có thông tin về bigram hoặc từ mục tiêu.

## 3.3 Possible next words
#### Mục đích và ý nghĩa
- @ Hàm `get_possible_next_words(sentence)` nhằm dự đoán các từ kế tiếp có khả năng xuất hiện sau một câu đã cho.  
- ? Hàm này sử dụng thông tin **trigram** (thông qua `calc_ngram_prob`) để tính xác suất cho mỗi từ trong `vocab` khi đứng sau 2 từ cuối cùng trong câu đầu vào.  
- @ Kết quả là một danh sách các từ khả dĩ kèm theo xác suất, sắp xếp theo thứ tự giảm dần để ta có thể chọn ra từ dự đoán cao nhất hoặc xem một số gợi ý có khả năng xuất hiện kế tiếp.

#### Chi tiết các bước
1. **Tiền xử lý và tách câu**  
   - Áp dụng hàm `tokenize(sentence)` để chuyển câu đầu vào thành danh sách các token.  
   - Kiểm tra độ dài của danh sách token. Nếu ít hơn 2, không đủ bối cảnh để hình thành trigram, hàm trả về danh sách rỗng.
	
2. **Lấy bối cảnh (context) từ 2 token cuối**  
   - Tạo `context` là bộ `(tokens[-2], tokens[-1])`. Đây là cặp từ cuối cùng của câu, đóng vai trò bối cảnh cho mô hình.
	
3. **Tính toán xác suất cho từng từ trong từ vựng**  
   - Duyệt qua mọi từ `word` trong `vocab`.  
   - Gọi `calc_ngram_prob(context, word)` để ước tính xác suất xuất hiện `word` tiếp theo.  
   - Lưu cặp `(word, prob)` vào `candidate_list`.
	
4. **Sắp xếp và trả về danh sách**  
   - Sắp xếp `candidate_list` theo giá trị xác suất (`prob`) giảm dần (`reverse=True`).  
   - Trả về `candidate_list`, trong đó mỗi phần tử gồm `(word, prob)`.  

+ ? Sử dụng hàm này, ta có thể dễ dàng lấy top-n từ tiếp theo có khả năng nhất, hoặc đơn giản là xem từ đứng đầu danh sách để dự đoán từ tiếp theo trong câu.  


## 3.4 Most likely next word
#### Mục đích và ý nghĩa
- @ Hàm `predict_next_word(sentence)` trả về **từ dự đoán** có khả năng cao nhất sẽ xuất hiện tiếp theo trong câu.  
- ? Hàm này dựa trên **danh sách ứng viên** từ `get_possible_next_words(sentence)`, nơi mỗi từ tiềm năng được gán một log-probability theo mô hình trigram.

#### Chi tiết các bước
1. **Lấy danh sách ứng viên**  
   - Gọi `get_possible_next_words(sentence)` để nhận về `candidate_list`.  
   - **`candidate_list`** là một **danh sách** chứa các **cặp** `(word, log_prob)`, đã được sắp xếp giảm dần theo `log_prob`.  
   - Mỗi phần tử mô tả một **từ tiềm năng (`word`)** và **log-probability** của nó theo mô hình trigram.
	
2. **Chọn từ phù hợp nhất**  
   - Kiểm tra nếu `candidate_list` không trống. Nếu không trống, lấy phần tử đầu tiên (chỉ số 0).  
   - **`candidate_list[0][0]`** là **từ** có xác suất (log-prob) cao nhất, được mô hình đánh giá là **ứng viên hàng đầu** để xuất hiện tiếp theo.
	
3. **Xử lý trường hợp không có ứng viên**  
   - Nếu `candidate_list` trống, hàm trả về `None`. Đây là dấu hiệu cho thấy hàm không tìm được từ nào phù hợp (thường do câu quá ngắn hoặc không đủ thông tin về từ vựng).


## 3.5 Generating text
### Mục đích và ý nghĩa
- @ Hàm `generate_text(sentence, n)` **tự động sinh thêm n từ** kế tiếp cho một câu đầu vào.  
- ? Hàm dựa trên **hàm dự đoán từ** (`predict_next_word`) để tìm ra từ khả dĩ xuất hiện kế tiếp, sau đó nối vào câu hiện tại.

### Chi tiết các bước
1. **Khởi tạo kết quả**  
   - `result = sentence`  
   - **`result`** là **chuỗi** sẽ chứa câu gốc ban đầu, và sẽ được mở rộng dần bằng các từ dự đoán.
	
2. **Vòng lặp sinh từ**  
```python
   for i in range(n):
       next_word = predict_next_word(result)
       ...
```
- Lặp **n lần** (tức sẽ dự đoán và thêm tối đa n từ).
- **`next_word`** là **từ** do hàm `predict_next_word` dự đoán dựa trên nội dung hiện tại của `result`.
	
3. **Xử lý khi không có dự đoán**
    ```python
    if next_word is None:
        break
    ```
    - Nếu mô hình không thể dự đoán từ nào phù hợp, **thoát sớm** khỏi vòng lặp để tránh thêm từ vô nghĩa.
	
4. **Ghép từ dự đoán vào câu**
    ```python
    result += " " + next_word
    ```
    - Thêm khoảng trắng `" "` và **`next_word`** vào cuối chuỗi `result`, mở rộng câu từng bước.
    
5. **Trả về kết quả**
    - Kết thúc vòng lặp hoặc khi mô hình **không** dự đoán được, **trả về** câu được xây dựng trong `result`.

## Perplexity
### Mục đích và ý nghĩa
- @ Hàm `perplexity(corpus)` đo lường **mức độ “bối rối”** mà mô hình ngôn ngữ (ở đây là **trigram**) gặp phải khi dự đoán các từ trong một bộ **corpus**.  
- ? Dựa trên công thức: $$
  PP(W) = \exp\Bigl(-\frac{1}{N}\sum_{i=1}^{N}\log P(w_i \mid w_{i-n+1}, \dots, w_{i-1})\Bigr),
  $$ hàm sẽ tính **trung bình** perplexity trên toàn bộ câu (sentence) trong **corpus**.  
- ? Một giá trị perplexity nhỏ hơn chứng tỏ mô hình dự đoán các từ trong câu tốt hơn, tức khả năng sinh/nghiệm tốt hơn.

### Chi tiết các bước

1. **Khởi tạo biến theo dõi**  
	```python
   total_neg_log_prob = 0.0
   total_count = 0
	```
	- **`total_neg_log_prob`**: Tổng **log probability âm** của các từ được dự đoán.
	- **`total_count`**: Số lượng **token** thật sự được dùng trong tính perplexity (trừ 2 token đầu ở mỗi câu, vì cần ít nhất 2 token để tạo bối cảnh trigram).
	
2. **Duyệt qua mỗi câu trong corpus**
    ```python
    for tokens in corpus:
        if len(tokens) < 3:
            continue
        ...
    ```
    - Mỗi phần tử trong `corpus` là một danh sách token đại diện cho một câu.
    - Nếu câu có ít hơn 3 token, không đủ để hình thành bối cảnh **trigram** ⇒ bỏ qua hoặc xử lý tùy ý.
    
3. **Tính log probability cho từng token (bắt đầu từ vị trí thứ 2)**
    ```python
    for i in range(2, len(tokens)):
        context = (tokens[i-2], tokens[i-1])
        word = tokens[i]
        log_prob = calc_ngram_prob(context, word)
        ...
    ```
    - **`context`**: Bộ 2 token liên tiếp trước đó `(w_{i-2}, w_{i-1})`.
    - **`word`**: Token hiện tại, cần dự đoán xác suất.
    - **`log_prob`**: Giá trị **log** của xác suất $\log P(w_i \mid w_{i-2}, w_{i-1})$.
    
4. **Kiểm tra khả năng dự đoán**
    ```python
    if log_prob == float('-inf'):
        return float('inf')
    ```
    - Nếu `log_prob` bằng `-inf`, nghĩa là xác suất bằng 0, mô hình **không** thể dự đoán → perplexity trở nên vô hạn (`float('inf')`).
    
5. **Cộng dồn log probability âm và đếm token**
    ```python
    total_neg_log_prob += -log_prob
    total_count += (len(tokens) - 2)
    ```
    - Cộng giá trị `-log_prob` vào **`total_neg_log_prob`** để tích lũy.
    - **`total_count`** tăng thêm số lượng token “có bối cảnh trigram” (cụ thể là `len(tokens) - 2`) chỉ sau khi duyệt hết vòng lặp nội bộ.
        - Lưu ý: Có thể đặt lệnh `total_count += (len(tokens) - 2)` ngoài vòng lặp for để tránh cộng lặp lại cho từng token.
        
6. **Tính trung bình và chuyển về không gian xác suất**
    ```python
    if total_count == 0:
        return float('inf')
    avg_neg_log_prob = total_neg_log_prob / total_count
    return math.exp(avg_neg_log_prob)
    ```
    - **`avg_neg_log_prob`**: Giá trị trung bình log probability âm trên tất cả các token dự đoán được.
    - Dùng `math.exp(...)` để đưa giá trị log probability âm **về không gian xác suất**, kết quả chính là **perplexity**.
    
7. **Kết quả perplexity**
    - Giá trị **perplexity** được trả về phản ánh mức độ mô hình “bối rối” khi dự đoán các token trên **corpus**.
    - **Càng thấp** → mô hình dự đoán **càng tốt**.


## Beam-search
### Mục đích và ý nghĩa
- @ **Beam Search** duy trì nhiều “đường đi” (câu) tiềm năng. Tại mỗi vòng lặp, nó mở rộng tất cả các đường đi, sau đó **chỉ giữ lại một số lượng hạn chế** (`num_beam`) các đường đi hứa hẹn nhất (có log-probability cao nhất).
- ?  Hàm `beam_search(sentence, n, num_beam=5)` sinh văn bản bằng cách áp dụng **Beam Search**, thay vì chỉ chọn từ xác suất cao nhất tại mỗi bước (greedy).   
- ? Cách tiếp cận này giúp tránh bị “kẹt” trong một đường đi duy nhất có thể dẫn đến kết quả kém (so với xác suất chuỗi tổng thể).

### Chi tiết các bước

1. **Khởi tạo các beam**  
	```python
   beams = [(sentence, 0.0)]
	```
	- **`beams`** là danh sách các **beam**. Mỗi beam gồm:
	    1. **Câu đã sinh ra** (`beam_sentence`).
	    2. **Tổng log-probability** tích lũy (`beam_score`).
	- Khởi đầu chỉ có một beam: câu gốc `sentence` với điểm số `0.0` (log(1)).
	
2. **Vòng lặp sinh từ**
    ```python
    for _ in range(n):
        new_beams = []
        ...
    ```
    - Lặp tối đa **n lần** để sinh thêm `n` token mới.
    - **`new_beams`** sẽ tạm chứa các beam mở rộng từ vòng lặp hiện tại.
    
3. **Mở rộng mỗi beam hiện có**
    ```python
    for beam_sentence, beam_score in beams:
        candidate_list = get_possible_next_words(beam_sentence)
        ...
    ```
    - **`candidate_list`**: Danh sách `(word, log_prob)` sắp xếp theo log-prob giảm dần.
    - Mỗi beam cũ được nới rộng thêm **tất cả ứng viên** tiềm năng.
	
4. **Xử lý trường hợp không có ứng viên**
    ```python
    if not candidate_list:
        new_beams.append((beam_sentence, beam_score))
        continue
    ```
    
    - Nếu không tìm được từ tiếp theo, beam vẫn được giữ nguyên (không mở rộng), để không mất thông tin.
	
5. **Tạo beam mở rộng**
    ```python
    for word, log_prob in candidate_list:
        new_sentence = beam_sentence + " " + word
        new_score = beam_score + log_prob
        new_beams.append((new_sentence, new_score))
    ```
    
    - **`new_sentence`**: Câu mới sau khi thêm **`word`** vào cuối câu cũ.
    - **`new_score`**: Tổng log-probability mới = log-prob cũ (`beam_score`) + log-prob ứng viên (`log_prob`).
	
6. **Chọn lọc beam tốt nhất**
    ```python
    if not new_beams:
        break
    new_beams.sort(key=lambda x: x[1], reverse=True)
    beams = new_beams[:num_beam]
    ```
    - Nếu **`new_beams`** trống, không thể mở rộng thêm, kết thúc sớm.
    - **Sắp xếp** `new_beams` theo **log-probability** giảm dần, chỉ **giữ lại** `num_beam` beam đứng đầu.
    
7. **Trả về kết quả**
    ```python
    return beams[0][0] if beams else sentence
    ```
    - Sau khi hoàn tất hoặc đạt đủ vòng lặp, **trả về** câu tốt nhất (đứng đầu trong `beams`) làm kết quả cuối cùng.
    - Nếu `beams` trống (trường hợp đặc biệt), trả về câu gốc.


## 3.6 Generating more text
### Mục đích và ý nghĩa
- @ **`sample_next_word(sentence)`**: Thay vì luôn chọn từ có **log-probability** cao nhất, hàm này sẽ **lấy mẫu ngẫu nhiên** (random sampling) một từ từ danh sách ứng viên, dựa trên **xác suất** của chúng.  
- @ **`generate_text(sentence, n, mode='top'|'random')`**: Mở rộng hàm sinh văn bản, cho phép chọn chế độ:
  1. `"top"`: Chọn **từ có log-probability cao nhất** (giống `predict_next_word`).  
  2. `"random"`: Chọn **từ có xác suất được lấy mẫu** theo `sample_next_word`.

### Chi tiết các bước 

1. **Lấy danh sách ứng viên**  
   ```python
   candidate_list = get_possible_next_words(sentence)
   candidate_list = [(word, log_prob) for word, log_prob in candidate_list if log_prob != float('-inf')]
	```
	- **`candidate_list`**: Kết quả của `get_possible_next_words`, gồm `(word, log_prob)`.
	- Lọc bỏ những ứng viên có `log_prob` bằng `-inf`, bởi chúng tương ứng với xác suất 0.

1. **Kiểm tra danh sách ứng viên**
    ```python
    if not candidate_list:
        return None
    ```
    - Nếu sau khi lọc không còn ứng viên nào, trả về `None`.
	
2. **Chuyển log-prob thành xác suất thường**
    ```python
    words = [word for word, _ in candidate_list]
    weights = [math.exp(log_prob) for _, log_prob in candidate_list]
    ```
    - `math.exp(log_prob)` để đưa `log_prob` về không gian xác suất.
    - **`words`**: Danh sách các từ ứng viên.
    - **`weights`**: Danh sách trọng số (xác suất tương đối) tương ứng với mỗi từ.
	
3. **Lấy mẫu từ**
    ```python
    if sum(weights) == 0:
        return None
    return random.choices(words, weights=weights, k=1)[0]
    ```
    - Nếu tổng trọng số là 0, không có ứng viên khả dĩ ⇒ trả về `None`.
    - Nếu có trọng số dương, dùng `random.choices` để **lấy mẫu một từ** (`k=1`) với xác suất tỷ lệ với `weights`.

#### Hàm `generate_text(sentence, n, mode='top')`
1. **Tham số `mode`**
    ```python
    if mode == 'top':
        next_word = predict_next_word(result)
    elif mode == 'random':
        next_word = sample_next_word(result)
    else:
        raise ValueError("Mode must be either 'top' or 'random'")
    ```
    - **`mode='top'`**: Gọi `predict_next_word`, luôn chọn từ có **log-probability** cao nhất.
    - **`mode='random'`**: Gọi `sample_next_word`, lấy mẫu ngẫu nhiên dựa trên xác suất.
    
2. **Sinh văn bản**
    ```python
    for i in range(n):
        ...
        if next_word is None:
            break
        result += " " + next_word
    return result
    ```
    - Lặp `n` lần để thêm `n` từ.
    - Nếu không thể dự đoán/lấy mẫu (`next_word is None`), dừng sớm.
    - Ghép `next_word` vào `result` để sinh dần một câu dài hơn.

Với tùy chọn `mode='random'`, văn bản thu được sẽ **đa dạng** hơn so với chiến lược chọn từ đứng đầu (greedy), đôi lúc tạo kết quả thú vị nhưng cũng có thể ít “chính xác” hơn so với “top”.


## Language modeling with NLTK

### Khởi Tạo Mô Hình
#### Mục đích và ý nghĩa
- @ Huấn luyện mô hình **Kneser-Ney Interpolated** để dự đoán **n-gram** (trigram ở đây, với `n=3`) từ một bộ **corpus** văn bản.  
- ? Mô hình được huấn luyện sử dụng thư viện **NLTK**, và kết quả mô hình sau khi huấn luyện được **lưu trữ** dưới dạng tệp pickle để có thể sử dụng lại sau này.

####  Chi tiết các bước

1. **Khởi tạo mô hình n-gram**  
   ```python
   vi_model = KneserNeyInterpolated(n)
	```
	- **`vi_model`**: Mô hình **Kneser-Ney Interpolated** với **n=3**, tức là mô hình **trigram**.
	- **Kneser-Ney**: Là phương pháp smoothing cải tiến, giúp xử lý tốt hơn cho những từ chưa xuất hiện trong dữ liệu huấn luyện.
	
2. **Tiền xử lý dữ liệu**
    ```python
    train_data, padded_sents = padded_everygram_pipeline(n, corpus)
    ```
    - **`corpus`**: Là tập văn bản gốc, sẽ được chia thành các n-gram (cả trigram trong trường hợp này).
    - **`train_data`**: Chứa các n-gram đã được chuẩn hóa và chia tách từ dữ liệu.
    - **`padded_sents`**: Là tập các câu đã được **padding** (thêm các token đặc biệt như `<s>` và `</s>`) để xử lý các từ xuất hiện ở đầu và cuối câu.
	
3. **Huấn luyện mô hình**
    ```python
    vi_model.fit(train_data, padded_sents)
    ```
    - Huấn luyện mô hình n-gram **Kneser-Ney** bằng cách sử dụng các **n-gram** từ `train_data` và các câu đã được padding `padded_sents`.
    - Mô hình sẽ học các xác suất có điều kiện giữa các từ dựa trên bối cảnh của chúng.
	
4. **Kiểm tra kích thước của từ vựng**
    ```python
    print(len(vi_model.vocab))
    ```
    - **`vi_model.vocab`** chứa **từ vựng** của mô hình (tất cả các từ đã được thấy trong quá trình huấn luyện).
    - `len(vi_model.vocab)` in ra số lượng từ có trong từ vựng.
	
5. **Lưu mô hình vào tệp**
    ```python
    model_dir = "/content/drive/My Drive/Colab Notebooks/Ngram_model"
    with open(os.path.join(model_dir, 'kneserney_1st_ngram_model.pkl'), 'wb') as fout:
        pickle.dump(vi_model, fout)
    ```
    - Mô hình sau khi huấn luyện sẽ được **lưu lại** dưới dạng tệp pickle (`.pkl`) vào thư mục `model_dir`.
    - Sau khi lưu trữ, mô hình có thể được tải lại sau này để sử dụng mà không cần huấn luyện lại từ đầu.

6. Tải mô hình lên hệ thống từ Drive 
```python
import os

model_dir = "/content/drive/My Drive/Colab Notebooks/Ngram_model"
with open(os.path.join(model_dir, 'kneserney_1st_ngram_model.pkl'), 'rb') as fin: # model train with nltk 3.5
    model_loaded = pickle.load(fin)
```
+ ? **Chú ý:** phiên bản `nltk` khi huấn luyện mô hình phải cùng phiên bản `nltk` lúc tải lên để tránh lỗi không cần thiết. 

### Generate Sent 
#### Mục đích và ý nghĩa
- @ Hàm `generate_sent(model, num_words, pre_words=[])` được thiết kế để sinh ra một câu văn dựa trên mô hình ngôn ngữ n-gram đã được huấn luyện (sử dụng thư viện `nltk.lm.model`).
- ? Ý tưởng của hàm là bắt đầu với một số từ khởi tạo (`pre_words`) và sau đó tiếp tục sinh thêm từ cho đến khi đạt số từ tối đa (`num_words`) hoặc gặp ký hiệu kết thúc câu (`</s>`). Việc sử dụng hàm detokenize giúp chuyển danh sách các token thành một câu văn có cấu trúc chính xác.

#### Chi tiết các bước thực hiện

1. **Khởi tạo nội dung từ các từ ban đầu:**
    ```python
    content = pre_words
    ```
	- Bắt đầu bằng cách gán biến `content` với danh sách các từ khởi tạo (`pre_words`), đây là nền tảng cho câu sẽ được sinh ra.
	- Việc này đảm bảo rằng quá trình sinh từ sẽ dựa vào ngữ cảnh ban đầu đã được cung cấp.

2. **Sinh từ liên tiếp qua vòng lặp:**
    ```python
    for i in range(num_words):
        token = model.generate(1, text_seed=content[-2:])
        if token == '<s>':
            continue
        if token == '</s>':
            break
        content.append(token)
    ```
	- Vòng lặp chạy tối đa `num_words` lần, mỗi lần sinh ra một token mới bằng cách sử dụng hàm `model.generate(1, text_seed=content[-2:])`.
	- **Sử dụng ngữ cảnh:** Ở mỗi bước, hàm sử dụng 2 từ cuối cùng của `content` (`content[-2:]`) làm bối cảnh để dự đoán từ tiếp theo. Điều này giúp duy trì tính liên tục của câu dựa trên mô hình n-gram.
	- **Xử lý ký hiệu đặc biệt:**
		- Nếu token sinh ra là ký hiệu bắt đầu câu (`<s>`), nó sẽ bị bỏ qua với lệnh `continue`, vì không cần lặp lại ký hiệu bắt đầu trong quá trình sinh.
		- Nếu token là ký hiệu kết thúc câu (`</s>`), vòng lặp sẽ dừng lại với lệnh `break`, báo hiệu rằng câu đã hoàn chỉnh.
	- **Cập nhật nội dung:** Các token hợp lệ sau đó được thêm vào danh sách `content`, mở rộng ngữ cảnh cho các bước sinh tiếp theo.
	
3. **Chuyển đổi danh sách token thành câu hoàn chỉnh:**
    ```python
    return detokenize(content)
    ```
	- Sau khi vòng lặp kết thúc, danh sách `content` chứa toàn bộ các token của câu đã sinh ra.
	- Hàm `detokenize` từ `TreebankWordDetokenizer` được sử dụng để chuyển danh sách token thành một chuỗi văn bản liền mạch, đảm bảo định dạng ngữ pháp và khoảng trắng đúng cách.


### Beam Generate Sent
#### Mục đích và ý nghĩa
+ $ **Cải Tiến:** **Pruning Strategies**, **Parallel Computing**, **Memory Optimization**. 
+ @ Hàm `beam_search_generate_sent` mở rộng quá trình sinh câu sử dụng thuật toán Beam Search, cải tiến với các yếu tố như pruning (cắt tỉa các beam kém khả năng), xử lý song song (parallel processing) và tối ưu bộ nhớ. Ý tưởng là tại mỗi bước, ta mở rộng các beam (các câu đang được xây dựng) bằng cách sinh từ mới dựa trên ngữ cảnh của chúng, sau đó sắp xếp và giữ lại các beam có tổng log-probability cao nhất. Các bước dưới đây giải thích chi tiết cách hoạt động của các đoạn code phức tạp và vai trò của các biến liên quan.

#### Chi tiết các bước thực hiện

1. **Xác định ngữ cảnh của beam hiện tại:**
	```python
    context = beam_sentence[-(model.order - 1):] if model.order > 1 else []
    ```
	- **Ý tưởng & Liên hệ:**
		- Dựa trên thứ tự của mô hình n-gram (`model.order`), ta cần sử dụng các từ cuối cùng của câu hiện tại để làm ngữ cảnh cho việc sinh từ tiếp theo.
		- Nếu `model.order` lớn hơn 1, ngữ cảnh được xác định là danh sách con chứa `(model.order - 1)` từ cuối của `beam_sentence`; nếu không, ngữ cảnh sẽ là một danh sách rỗng.
		
	- **Chi tiết hoạt động:**
		- `beam_sentence` là danh sách các từ của beam hiện tại.
		- Biểu thức `beam_sentence[-(model.order - 1):]` lấy các phần tử từ vị trí `-(model.order - 1)` đến hết danh sách, đảm bảo rằng ta lấy đúng số từ cần làm ngữ cảnh.
		- Nếu `model.order` không vượt quá 1, không có ngữ cảnh nào cần lấy, do đó trả về danh sách rỗng (`[]`).
		
2. **Sinh từ mới dựa trên ngữ cảnh:**
    ```python
    candidate = model.generate(1, text_seed=context)
    ```
	- **Ý tưởng & Liên hệ:**
		- Dựa vào ngữ cảnh đã xác định, ta sử dụng mô hình ngôn ngữ để sinh ra một từ ứng viên tiếp theo.
		- Đây là bước quan trọng để mở rộng beam hiện tại.
		
	- **Chi tiết hoạt động:**
		- Hàm `model.generate(1, text_seed=context)` yêu cầu mô hình sinh ra 1 từ, sử dụng `context` (là danh sách các từ cuối của câu hiện tại) làm dữ liệu đầu vào cho việc dự đoán.
		- Kết quả trả về là một chuỗi (token) đại diện cho từ được sinh ra.
	
3. **Tính toán điểm số mới cho beam mở rộng:**
	```python
    new_score = beam_score + model.logscore(word, new_sentence[-(model.order - 1):])
	```
	- **Ý tưởng & Liên hệ:**
		- Khi một từ mới được thêm vào beam, ta cần cập nhật tổng log-probability cho beam đó để phản ánh xác suất của toàn bộ câu mới.
		- Việc cộng logscore của từ mới vào `beam_score` giúp tích lũy điểm số từ đầu câu đến từ hiện tại.
		
	- **Chi tiết hoạt động:**
		- `beam_score` là tổng log-probability của câu hiện tại trong beam trước khi mở rộng.
		- `model.logscore(word, new_sentence[-(model.order - 1):])` tính log-probability của từ `word` dựa trên ngữ cảnh mới được tạo thành từ các từ cuối của `new_sentence` (sau khi thêm từ mới).
		- Biểu thức `new_sentence[-(model.order - 1):]` lấy ngữ cảnh cần thiết từ câu mới, đảm bảo tính nhất quán với mô hình n-gram.
		
4. **Mở rộng các beam theo xử lý song song:**
    ```python
    new_beams = []
    if parallel:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = list(executor.map(expand_beam, beams))
        for res in results:
            new_beams.extend(res)
    ```
	- **Ý tưởng & Liên hệ:**
		- Khi có nhiều beam cần mở rộng, ta có thể xử lý song song để tăng tốc độ.
		- Nếu tham số `parallel` là `True`, các beam sẽ được mở rộng cùng lúc bằng cách sử dụng `ThreadPoolExecutor`.
		
	- **Chi tiết hoạt động:**
		- `new_beams = []`: Khởi tạo danh sách rỗng để lưu trữ tất cả các beam mở rộng.
		- `with concurrent.futures.ThreadPoolExecutor() as executor:`: Tạo một executor cho phép chạy các tác vụ song song.
		- `executor.map(expand_beam, beams)` áp dụng hàm `expand_beam` cho mỗi beam trong danh sách `beams`.
		- Kết quả trả về là một iterator chứa danh sách các beam mở rộng cho từng beam gốc.
		- Vòng lặp `for res in results: new_beams.extend(res)` duyệt qua từng kết quả (một danh sách các beam mở rộng) và hợp nhất chúng vào `new_beams`.
		
5. **Sắp xếp các beam theo điểm số và xác định beam tốt nhất:**
```python
    new_beams.sort(key=lambda x: x[1], reverse=True)
    best_score = new_beams[0][1]
```
- **Ý tưởng & Liên hệ:**
	- Sau khi mở rộng, ta cần sắp xếp các beam theo tổng log-probability để xác định beam nào có khả năng cao nhất.
	- Điều này giúp dễ dàng áp dụng các bước cắt tỉa tiếp theo.
	
- **Chi tiết hoạt động:**
	- `new_beams.sort(key=lambda x: x[1], reverse=True)`: Sắp xếp danh sách `new_beams` dựa trên phần tử thứ hai của mỗi tuple (đại diện cho tổng log-probability), theo thứ tự giảm dần.
	- `best_score = new_beams[0][1]`: Lấy điểm số của beam đứng đầu (beam tốt nhất) làm chuẩn để so sánh trong bước cắt tỉa.
	
6. **Cắt tỉa (pruning) các beam không đủ khả năng:**
	```python
    pruned_beams = [beam for beam in new_beams if best_score - beam[1] <= beam_pruning_threshold]
    beams = pruned_beams[:num_beam]
	```
	- **Ý tưởng & Liên hệ:**
		- Để tránh lãng phí tài nguyên cho các beam có khả năng thấp, ta cắt tỉa bỏ các beam có điểm số thấp hơn so với beam tốt nhất vượt quá ngưỡng `beam_pruning_threshold`.
		- Sau đó, chỉ giữ lại một số lượng giới hạn (`num_beam`) beam tốt nhất để tiếp tục mở rộng.
		
	- **Chi tiết hoạt động:**
		- `pruned_beams = [beam for beam in new_beams if best_score - beam[1] <= beam_pruning_threshold]`: Tạo danh sách mới chỉ bao gồm các beam có hiệu số giữa `best_score` và điểm số của beam không vượt quá `beam_pruning_threshold`.
		- `beams = pruned_beams[:num_beam]`: Lấy top `num_beam` beam từ danh sách đã cắt tỉa để sử dụng cho vòng lặp tiếp theo.
		
7. **Lấy câu tốt nhất từ beam cuối cùng:**
	```python
    best_sentence = beams[0][0] if beams else pre_words
    return ' '.join(best_sentence)
	```
	- **Ý tưởng & Liên hệ:**
		- Khi quá trình mở rộng kết thúc (sinh đủ số từ hoặc không còn beam nào khả thi), ta lấy beam đứng đầu – tức là beam có tổng log-probability cao nhất – làm kết quả.
		- Nếu không còn beam nào, trả về câu khởi tạo (`pre_words`).
		
	- **Chi tiết hoạt động:**
		- `beams[0][0]`: Lấy phần đầu của tuple trong beam đầu tiên, đó là danh sách các từ của câu.
		- `' '.join(best_sentence)`: Chuyển danh sách các từ thành một chuỗi văn bản, tạo thành câu hoàn chỉnh với các khoảng trắng phù hợp.

**Tóm lại:**
- **Đầu vào:**
    - `model`: Mô hình ngôn ngữ n-gram từ `nltk.lm.model`.
    - `num_words`, `pre_words`, `num_beam`, `beam_pruning_threshold`, `parallel`: Các tham số điều khiển quá trình sinh từ, số lượng beam và việc xử lý song song.
	
- **Quá trình:**
    - Mỗi beam được mở rộng bằng cách sử dụng ngữ cảnh từ các từ cuối cùng của câu hiện tại.
    - Từ mới được sinh ra dựa trên ngữ cảnh và điểm số của beam được cập nhật dựa trên log-probability của từ đó.
    - Các beam được mở rộng song song (nếu được bật) và sau đó sắp xếp, cắt tỉa dựa trên ngưỡng cho phép.
    - Cuối cùng, câu từ beam tốt nhất được trích xuất và chuyển đổi thành chuỗi văn bản.
	
- **Đầu ra:**
    - Một câu được sinh ra dưới dạng chuỗi, phản ánh khả năng dự đoán của mô hình n-gram với các cải tiến về pruning và xử lý song song.

