[Thang Entropy Use Case](https://beryl-freckle-b85.notion.site/AIO2025-B-i-to-n-n-y-c-p-d-ng-c-ML-DL-hay-kh-ng-24e302d8792c80fe8b65dc9a3463148e#24e302d8792c8019badcd3f224927a5e) 
[Sister Ha](https://docs.google.com/document/d/19498-MpoaqOA7ec6-uUYy5MT78V1Is0DZrLmm4M93TM/edit?tab=t.0) 
[Overview of Decision Tree DeepLearningBlog](https://phamdinhkhanh.github.io/deepai-book/ch_ml/DecisionTree.html)

---

## TF-IDF
A Corpus is a dictionary containing word along with their "number of apperance". If the whole these have 3 documents/paragraph in it then the Corpus will include all the word from the 3 docuements and their number of appearance. e.g. `{the: 123, no: 2, yes: 5,...}  `

### TF (Text Frequency) - term / sentence_length
+ $ **TF** is the frequency of any "term" in a given "document".    
	*ideas:* words that appear often in a document should be important - only if they don't appear too often. 
	
-> Increase **IMPORTANCESS of less-frequence** **in a sentence or document.** 

+ $ **IDF** is constant per corpus and    
	*idea:* if a word is too common in a document (like "the", "and", "is") it's less useful for classified the document (what type the document is), IDF down-weights these words. 
	
-> Increase **IMPORTANTNESS of less-frequence word** **in the word corpus** (not just 1 document, but across all document in the corpus) 

With 
+ t as Term (word)
+ d as a single document
+ N total number of document in the corpus
+ $df(t)$ num of docs containing term $t$.

**Term Frequency (TF)**
$$TF(t, d) = \frac{\text{Number of times t appear in d}}{\text{Total number of terms in d}}$$
**Invert Document Frequency (IDF)**
$$IDF(t) = \log\left( \frac{N}{df(t)} \right)$$
Sometime written as to avoid division by zero and ensure positivity:
$$IDF(t) = \log\left(\frac{1 + N}{1 + df(t)} \right) + 1$$

**TF-IDF Scores:**
$$TF-IDF(t, d) = TF(t, d) \times IDF(t)$$

+ ? For example, given 3 short document:
D1: "Bad Alien will rules the bad"
D2: "Dog hate cat"
D3: "Good AI will rules the world"

Let **compare** TF and IDF of **less frequence and frequence word.** 
Appear **more** time:
`TF(bad, D1) = 2 / 6 = 0.3`
`IDF(bad) = ln(3/2) = 0.4` (total number of docs / term frequence)

Appear **less** time:
`TF("Good", D3) = 1 / 6 = 0.166.` 
`IDF("Good") = ln(3/1) = 1.09` (total number of docs / term frequence)

**Compare TF-IDF of both word:**
`TF-IDF(bad) = 0.12`
`TF-IDF(good) = 0.18094`
-> Less frequence word like "good" have higher TF-IDF because its **more distintive.**



## 2. Decision Tree for Classification
### Introduct to GINI
develop by Corrado Gini
Impurity: không thuần khiết

How to measures the **impurity of an Dataset** (tạp chất trong Dateset). **Like Entropy**, **the more bias and imbalance** the dataset is, **the lower GINI is.**
+ **Balance** Dataset, **Hard to Predict** -> **Highest GINI**. e.g. 5 class with the same probability. 
+ **Bias** Dataset, **Easy to Predict** -> **Low GINI.** -> Easier to make Decision.
![[Pasted image 20250813203928.png]]

**Use Case:**  
![[Pasted image 20250813204548.png# left | 544]]
+ @ The main Idea is to Build a Decision such that **GINI decrease as the tree growth.**




**Năm học 2022-2023 - Học kỳ 1**

|STT|Mã học phần|Tên học phần|Số tín chỉ|Điểm hệ 10|Điểm hệ 4|Điểm chữ|
|---|---|---|---|---|---|---|
|1|MATH2002|Đại số tuyến tính|3|7.2|3|B|
|2|CMC3001|Giải tích 1|3|4.5|1|D|
|3|BIT3001|Nhập môn công nghệ thông tin|3|5.6|2|C|
|4|GENE1001|Triết học Mác - Lênin|3|6.5|2.5|C+|
|5|PHYS2001|Vật lý điện - điện tử|3|7.6|3|B|

**Năm học 2022-2023 - Học kỳ 2**

|STT|Mã học phần|Tên học phần|Số tín chỉ|Điểm hệ 10|Điểm hệ 4|Điểm chữ|
|---|---|---|---|---|---|---|
|1|CMC3002|Giải tích 2|3|5.3|1.5|D+|
|2|INFO2006|Kiến trúc máy tính|3|7|3|B|
|3|GENE1002|Kinh tế chính trị Mác - Lênin|2|7.9|3|B|
|4|PROG2004|Lập trình Python|3|7.9|3|B|
|5|INFO3007|Mạng máy tính và truyền thông|3|7.7|3|B|
|6|MATH2005|Toán rời rạc|3|6|2|C|

**Năm học 2022-2023 - Học kỳ 3**

|STT|Mã học phần|Tên học phần|Số tín chỉ|Điểm hệ 10|Điểm hệ 4|Điểm chữ|
|---|---|---|---|---|---|---|
|1|INFO2002|Cấu trúc dữ liệu và giải thuật|3|5.3|1.5|D+|
|2|GENE1003|Chủ nghĩa xã hội khoa học|2|0|0|F|
|3|PROG3001|Lập trình C#|3|9.3|4|A+|
|4|PROG2002|Lập trình hướng đối tượng|3|7.8|3|B|
|5|BIT3003|Nguyên lý hệ điều hành|3|7.8|3|B|
|6|MATH2003|Xác suất thống kê|3|5.9|2|C|

**Năm học 2023-2024 - Học kỳ 1**

|STT|Mã học phần|Tên học phần|Số tín chỉ|Điểm hệ 10|Điểm hệ 4|Điểm chữ|
|---|---|---|---|---|---|---|
|1|GENE1003|Chủ nghĩa xã hội khoa học|2|7.3|3|B|
|2|INFO2005|Công nghệ phần mềm|3|7.3|3|B|
|3|INFO2004|Cơ sở dữ liệu|3|4|1|D|
|4|PROG2001|Cơ sở lập trình|3|8.6|4|A|
|5|PROG2003|Cơ sở lập trình web|3|8.8|4|A|
|6|GENE1010|Giáo dục thể chất cơ bản|1|6.3|0|P|
|7|GENE1005|Tư tưởng Hồ Chí Minh|2|8.2|3.5|B+|

**Năm học 2023-2024 - Học kỳ 2**

|STT|Mã học phần|Tên học phần|Số tín chỉ|Điểm hệ 10|Điểm hệ 4|Điểm chữ|
|---|---|---|---|---|---|---|
|1|INFO3006|An toàn thông tin|3|8.3|3.5|B+|
|2|GENE1012|Bóng chuyền hơi|1|6.4|0|P|
|3|GENE1011|Bóng rổ|1|6.1|0|P|
|4|INFO3011|Các hệ quản trị cơ sở dữ liệu|3|9.1|4|A+|
|5|PROG3005|Công nghệ lập trình web|3|8.6|4|A|
|6|INFO3009|Quản lý dự án công nghệ thông tin|3|7.4|3|B|
|7|INFO3005|Trí tuệ nhân tạo|3|7.4|3|B|

**Năm học 2023-2024 - Học kỳ 3**

|STT|Mã học phần|Tên học phần|Số tín chỉ|Điểm hệ 10|Điểm hệ 4|Điểm chữ|
|---|---|---|---|---|---|---|
|1|INFO3003|Đồ án chuyên ngành|2|7.5|3|B|
|2|INFO3012|Học máy và khai phá dữ liệu|3|7.7|3|B|
|3|PROG3004|Kỹ năng lập trình nâng cao|2|9.2|4|A+|
|4|GENE1006|Pháp luật đại cương|2|8.7|4|A|
|5|PROG3002|Phát triển ứng dụng di động|3|9.5|4|A+|
|6|INFO3004|Triển khai phần mềm|3|9.3|4|A+|

**Năm học 2024-2025 - Học kỳ 1**

|STT|Mã học phần|Tên học phần|Số tín chỉ|Điểm hệ 10|Điểm hệ 4|Điểm chữ|
|---|---|---|---|---|---|---|
|1|GENE1004|Lịch sử Đảng Cộng sản Việt Nam|2|7.4|3|B|
|2|INFO5001|Thực tập nghề nghiệp|10|8|3.5|B+|

**Năm học 2024-2025 - Học kỳ 2**

|STT|Mã học phần|Tên học phần|Số tín chỉ|Điểm hệ 10|Điểm hệ 4|Điểm chữ|
|---|---|---|---|---|---|---|
|1|INFO3002|Giao diện và trải nghiệm người dùng|2|8.5|4|A|
|2|BIGD4001|Học sâu và ứng dụng|3|8.5|4|A|
|3|BIGD4002|Phân tích dữ liệu lớn|3|8|3.5|B+|
|4|BIGD4004|Thị giác máy tính|3|7.8|3|B|
|5|BIGD4003|Xử lý ngôn ngữ tự nhiên|3|8.6|4|A|

**Năm học 2024-2025 - Học kỳ 3**

|STT|Mã học phần|Tên học phần|Số tín chỉ|Điểm hệ 10|Điểm hệ 4|Điểm chữ|
|---|---|---|---|---|---|---|
|1|LSS2001|Khởi nghiệp|3|8.6|4|A|
|2|LSS|Kỹ năng bổ trợ|3|9.4|4|A+|


