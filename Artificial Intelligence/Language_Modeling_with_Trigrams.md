## Preprocess
### Hàm Tokenize
Đoạn code trên tiền xử lý dữ liệu văn bản để xây dựng mô hình trigram dự đoán từ tiếng Việt. Quá trình tiền xử lý bao gồm:
- Tách văn bản thành các câu.
- Tách từng câu thành các token (các từ đơn lẻ).
- Loại bỏ các dấu câu không cần thiết.
- Chuẩn bị dữ liệu sạch hơn để mô hình dễ dàng học quy luật và dự đoán từ kế tiếp một cách hiệu quả.
### Chi tiết các bước
1. **Định nghĩa hàm `tokenize(doc)`:**
    - Chuyển văn bản sang chữ thường bằng `doc.lower()`.
    - Tách văn bản thành một danh sách token bằng `word_tokenize(...)`.
    - Tạo bảng dịch (translate table) loại bỏ hầu hết dấu câu (trừ ký tự “_”), sau đó áp dụng lên từng token.
    - Loại bỏ những token trống (nếu có).
    - Kết quả trả về là danh sách các token đã được làm sạch.
	
2. **Tạo chuỗi dữ liệu lớn `full_data`:**
    - `". ".join(full)`: Gộp tất cả các đoạn văn/bản ghi trong `full` thành một chuỗi lớn, các đoạn cách nhau bằng dấu chấm và khoảng trắng.
    - `full_data.replace("\n", ". ")`: Thay các ký tự xuống dòng bằng dấu chấm và khoảng trắng để thống nhất cách ngắt câu.
	
3. **Tách câu bằng biểu thức chính quy:**
    - `re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', full_data)`: Tách chuỗi `full_data` thành danh sách các câu (`sents`) dựa trên quy tắc tìm dấu chấm hoặc chấm hỏi, rồi khoảng trắng, và ký tự tiếp theo in hoa. Điều này giúp chia văn bản thành các câu cơ bản.
	
4. **Tạo `corpus`:**
    - Khởi tạo danh sách rỗng `corpus`.
    - Duyệt qua mỗi câu trong `sents` với vòng lặp kèm `tqdm` (chỉ để theo dõi tiến độ).
    - Gọi hàm `tokenize(sent)` để chuyển từng câu thành danh sách token, sau đó thêm vào `corpus`.

Kết quả cuối cùng là `corpus` – một danh sách các câu, trong đó mỗi câu được biểu diễn dưới dạng một danh sách token đã qua xử lý và làm sạch, sẵn sàng cho bước xây dựng mô hình trigram dự đoán từ.


### Hàm N-Gram
Hàm `n_gram(tokens, n)` được thiết kế để tạo danh sách **n-gram** từ một danh sách token. Trong xử lý ngôn ngữ tự nhiên, **n-gram** là một chuỗi gồm _n_ token liên tiếp, đóng vai trò quan trọng trong việc xây dựng các mô hình thống kê ngôn ngữ (như trigram, bigram, v.v.). Mục tiêu là thu thập tất cả các **n-gram** có thể có trong tập token đầu vào để hỗ trợ quá trình huấn luyện hoặc phân tích ngôn ngữ.

### Chi tiết các bước
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

## 3.1 N-gram counts
Hàm `get_ngram_counts(corpus, n)` có nhiệm vụ tạo danh sách các từ điển (dictionary), trong đó mỗi từ điển biểu diễn tần suất xuất hiện của i-gram (với i = 1 đến n) trong toàn bộ tập dữ liệu `corpus`. Đây là bước chuẩn bị quan trọng trong quá trình xây dựng mô hình ngôn ngữ thống kê (như bigram, trigram), giúp ta nắm được số lần mỗi i-gram xuất hiện.

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
Hàm `calc_ngram_prob(context, word)` được dùng để tính **xác suất có điều kiện** (dưới dạng log) của từ `word` dựa trên bối cảnh (`context`). Cụ thể, nó tính xác suất `P(word | w_2, w_1)` trong mô hình **trigram**. Xác suất này giúp chúng ta biết mức độ khả thi khi `word` xuất hiện sau cặp từ `(w_2, w_1)`. Đây là bước quan trọng để mô hình có thể dự đoán từ tiếp theo với ngôn ngữ tiếng Việt (hoặc bất kỳ ngôn ngữ nào) dựa trên các thống kê từ tập dữ liệu.

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
- Trong mô hình trigram, ta cần tính xác suất từ tiếp theo dựa vào hai từ trước đó. Hàm này sử dụng kỹ thuật **Add-One Smoothing** (còn gọi là Laplace Smoothing) để tránh xác suất bằng 0 trong trường hợp cặp (bigram) hoặc bộ ba (trigram) chưa từng xuất hiện.
- Thay vì để đếm (count) bằng 0 dẫn đến xác suất bằng 0, em cộng thêm 1 vào số đếm của trigram, đồng thời cộng thêm “V” (kích thước từ vựng) vào số đếm bigram khi tính xác suất, rồi lấy log.

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
Hàm `calc_ngram_prob_with_backoff(context, word)` tính xác suất có điều kiện của một từ dựa trên bối cảnh bằng **thuật toán Stupid Backoff**.
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
- Hàm `kesser_ney_smoothing(context, word, discount=0.75)` tính xác suất theo phương pháp **Kneser-Ney smoothing** cho mô hình bigram (với bối cảnh là unigram).
- Kneser-Ney khắc phục hạn chế của các phương pháp đơn giản như Stupid Backoff và Interpolation (vốn phụ thuộc nhiều vào MLE) bằng cách tận dụng thông tin về số lượng “bối cảnh duy nhất” (unique preceding words) của từ để đánh giá khả năng xuất hiện của từ đó.
- Với **Kneser-Ney**, xác suất được phân rã thành hai thành phần chính:
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
- Hàm `get_possible_next_words(sentence)` nhằm dự đoán các từ kế tiếp có khả năng xuất hiện sau một câu đã cho.  
- Hàm này sử dụng thông tin **trigram** (thông qua `calc_ngram_prob`) để tính xác suất cho mỗi từ trong `vocab` khi đứng sau 2 từ cuối cùng trong câu đầu vào.  
- Kết quả là một danh sách các từ khả dĩ kèm theo xác suất, sắp xếp theo thứ tự giảm dần để ta có thể chọn ra từ dự đoán cao nhất hoặc xem một số gợi ý có khả năng xuất hiện kế tiếp.

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
- Hàm `predict_next_word(sentence)` trả về **từ dự đoán** có khả năng cao nhất sẽ xuất hiện tiếp theo trong câu.  
- Hàm này dựa trên **danh sách ứng viên** từ `get_possible_next_words(sentence)`, nơi mỗi từ tiềm năng được gán một log-probability theo mô hình trigram.

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
- Hàm `generate_text(sentence, n)` **tự động sinh thêm n từ** kế tiếp cho một câu đầu vào.  
- Hàm dựa trên **hàm dự đoán từ** (`predict_next_word`) để tìm ra từ khả dĩ xuất hiện kế tiếp, sau đó nối vào câu hiện tại.

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
- Hàm `perplexity(corpus)` đo lường **mức độ “bối rối”** mà mô hình ngôn ngữ (ở đây là **trigram**) gặp phải khi dự đoán các từ trong một bộ **corpus**.  
- Dựa trên công thức:
  $$
  PP(W) = \exp\Bigl(-\frac{1}{N}\sum_{i=1}^{N}\log P(w_i \mid w_{i-n+1}, \dots, w_{i-1})\Bigr),
  $$
  hàm sẽ tính **trung bình** perplexity trên toàn bộ câu (sentence) trong **corpus**.  
- Một giá trị perplexity nhỏ hơn chứng tỏ mô hình dự đoán các từ trong câu tốt hơn, tức khả năng sinh/nghiệm tốt hơn.

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
- Hàm `beam_search(sentence, n, num_beam=5)` sinh văn bản bằng cách áp dụng **Beam Search**, thay vì chỉ chọn từ xác suất cao nhất tại mỗi bước (greedy).  
- **Beam Search** duy trì nhiều “đường đi” (câu) tiềm năng. Tại mỗi vòng lặp, nó mở rộng tất cả các đường đi, sau đó **chỉ giữ lại một số lượng hạn chế** (`num_beam`) các đường đi hứa hẹn nhất (có log-probability cao nhất).  
- Cách tiếp cận này giúp tránh bị “kẹt” trong một đường đi duy nhất có thể dẫn đến kết quả kém (so với xác suất chuỗi tổng thể).

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
- **`sample_next_word(sentence)`**: Thay vì luôn chọn từ có **log-probability** cao nhất, hàm này sẽ **lấy mẫu ngẫu nhiên** (random sampling) một từ từ danh sách ứng viên, dựa trên **xác suất** của chúng.  
- **`generate_text(sentence, n, mode='top'|'random')`**: Mở rộng hàm sinh văn bản, cho phép chọn chế độ:
  1. `"top"`: Chọn **từ có log-probability cao nhất** (giống `predict_next_word`).  
  2. `"random"`: Chọn **từ có xác suất được lấy mẫu** theo `sample_next_word`.

### Chi tiết các bước
Hàm `sample_next_word(sentence)`

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
- Huấn luyện mô hình **Kneser-Ney Interpolated** để dự đoán **n-gram** (trigram ở đây, với `n=3`) từ một bộ **corpus** văn bản.  
- Mô hình được huấn luyện sử dụng thư viện **NLTK**, và kết quả mô hình sau khi huấn luyện được **lưu trữ** dưới dạng tệp pickle để có thể sử dụng lại sau này.

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

### Generate Sent
#### Mục đích và ý nghĩa
- Hàm `beam_search_generate_sent(model, num_words, pre_words=[], num_beam=5)` sinh ra một câu mới bằng cách sử dụng thuật toán **Beam Search**.  
- Thuật toán **Beam Search** duy trì một số lượng **beam candidates** nhất định, mở rộng từng beam theo các từ tiếp theo và giữ lại các beam có **log-probability** cao nhất.

#### Chi tiết các bước

1. **Khởi tạo các beam**  
   ```python
   beams = [(pre_words, 0.0)]
```

- **`beams`** là danh sách các beam, mỗi beam gồm:
    1. **Câu đã sinh ra** (`beam_sentence`).
    2. **Tổng log-probability** (`beam_score`).
- Mỗi beam bắt đầu với `pre_words` và log-probability là `0.0`.

1. **Mở rộng mỗi beam**
    ```python
    for _ in range(num_words):
        new_beams = []
        ...
    ```
    - Vòng lặp sẽ chạy tối đa `num_words` lần để sinh thêm từ.
    - **`new_beams`** chứa các beam mở rộng trong mỗi bước.
    
2. **Sinh từ tiếp theo cho mỗi beam**
    ```python
    for beam_sentence, beam_score in beams:
        candidate_list = model.generate(1, text_seed=beam_sentence[-(model.order-1):])
    ```
    - Mỗi beam sẽ được mở rộng, tức là cho mỗi `beam_sentence`, gọi `model.generate()` để sinh một từ tiếp theo.
    - **`text_seed=beam_sentence[-(model.order-1):]`** là bối cảnh của câu hiện tại, sử dụng `(n-1)` từ cuối cùng để làm bối cảnh cho mô hình trigram (với `n=3`, ta cần 2 từ cuối làm bối cảnh).
	
3. **Kiểm tra và xử lý khi không có ứng viên**
    ```python
    if not candidate_list:
        new_beams.append((beam_sentence, beam_score))
        continue
    ```
    - Nếu không có từ nào được sinh ra (`candidate_list` trống), beam sẽ tiếp tục mà không thay đổi. Điều này đảm bảo mô hình không bị kẹt khi không có từ khả dĩ nào.
    
4. **Mở rộng beam với các ứng viên**
    ```python
    for word in candidate_list:
        new_sentence = beam_sentence + [word]
        new_score = beam_score + model.logscore(word, new_sentence[-(model.order-1):])
        new_beams.append((new_sentence, new_score))
    ```
    - **Mở rộng beam**: Duyệt qua từng từ trong `candidate_list`, thêm từ vào `beam_sentence` hiện tại để tạo thành một câu mới `new_sentence`.
    - **Cập nhật điểm số**: Tính tổng log-probability của câu mới bằng cách cộng điểm số cũ với log-probability của từ mới (`new_score`).
    
5. **Sắp xếp các beam theo điểm số**
    ```python
    new_beams.sort(key=lambda x: x[1], reverse=True)
    ```
    - Sau khi tất cả các beam được mở rộng, sắp xếp chúng theo **log-probability** giảm dần. Điều này giúp **giữ lại** các beam có xác suất cao nhất.
	
6. **Giữ lại top `num_beam` beam**
    ```python
    beams = new_beams[:num_beam]
    ```
    - **Chỉ giữ lại `num_beam` beam tốt nhất**: Chỉ giữ các beam có điểm số log-probability cao nhất.
	
7. **Dừng nếu không có beam nào**
    ```python
    if not beams:
        break
    ```
    - Nếu sau khi mở rộng các beam mà không còn beam nào khả dĩ (tức `beams` trống), hàm sẽ dừng sớm để tránh vòng lặp vô tận.
	
8. **Trả về câu sinh ra**
    ```python
    best_sentence = beams[0][0]
    return ' '.join(best_sentence)
    ```
    - Sau khi hết vòng lặp hoặc khi đạt đủ số từ cần sinh (`num_words`), **trả về câu tốt nhất** từ beam đứng đầu (với log-probability cao nhất).
    - Câu được trả về dưới dạng chuỗi từ, loại bỏ dấu bắt đầu câu `<s>` nếu có.
