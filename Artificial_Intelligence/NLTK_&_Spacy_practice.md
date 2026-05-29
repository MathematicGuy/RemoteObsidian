## Tokenization
>Phần code này demo cách Tokenzation hoạt động corpus sử dụng model pre-trained `punkt_tab` của nltk để tokenizing văn bản thành các câu và từ.

+ @ Tokenization là kỹ thuật tách từ trong NLP, được sử dụng để chuyể đổi văn bản (text) thành các đơn vị nhỏ hơnhơn, được gọi là các tokens. Mỗi token có thể là 1 từ (word tokenization), 1 từ phụ (sub tokenization), 1 ký tự (character tokenization) hoặc thậm chí là 1 câu (sentence tokenization) 

+ ? Tokenize văn bản thành câu.
```python
sentences = nltk.sent_tokenize(corpus)
sentences
```
![[Pasted image 20250306083516.png]]

+ ? Tokenize câu thành các từ sử dụng hàm word_tokenize của nltk
```python
tokens =  []
for sentence in sentences:
  token_list = nltk.word_tokenize(sentence)
  tokens.extend(token_list)

tokens
```
![[Pasted image 20250306083502.png]]

## POS-tagging (Part-of-speech tagging)
+ @ Pos-tagging là quá trình xác định và gán nhãn loại từ (part-of-speech, POS) như danh từ (noun), động từ (verb), tính từ (adjectuve), trạng từ (adverb) cho từng từ trog văn bản. 
![[Untitled 6.png]]

Cài đặt mô hình pre-trained cho Pos-tagging  
```python
nltk.download('averaged_perceptron_tagger_eng')
```

Thực hiện Pos-tagging cho từng token trong tokens
```python
nltk.pos_tag(tokens)
```
![[Pasted image 20250306083444.png]]

## Stemming
+ @ Steamming là 1 kỹ thuật xử lý văn bản trong NLP dùng để biến văn bản trở về trạng thái gốc của nó. (e.g. changing, changed, change -> Chang) 

+ ? Sử dụng thuật toán **Porter stemming** trên biến stemmer bằng module PorterStemmer trong thử viện nltk. Sau đó áp dụng kĩ thuật stemming với mỗi token trong tokens.
```python
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

stem_words = [stemmer.stem(token) for token in tokens]
stem_words
```
![[Pasted image 20250306084914.png]]

# Excercise
+ ? Đọc toàn bộ thẻ html từ url `http://php.net/` 
```python
import urllib.request

response = urllib.request.urlopen('http://php.net/')
html = response.read()
print(html)
```
![[Pasted image 20250306092752.png]]

+ ? Phân tích cú pháp html sử dụng Beautiful Soup rồi trích xuất nội dung văn bản từ cú pháp HTML sử dụng `get_text()` với tham số `strip=True` để loại bỏ các bất cứ khoảng trắng nào trong các đoạn văn bản để giúp nó gọn gàng hơn.
```python
soup = BeautifulSoup(html,"html5lib")
text = soup.get_text(strip=True)
print(text)
```
![[Pasted image 20250306092742.png]]

+ ? Sau đó, trích xuất toàn bộ token trong văn bản với mỗi token là 1 từ được phân tách bởi 1 khoảng trắng sử dụng hàm `split()` của python.
```python
tokens = [t for t in text.split()]
print(tokens)
```
![[Pasted image 20250306092955.png]]

+ ? Hàm `freq` được sử dụng để tính tần suất xuất hiện của mỗi token trong `tokens` bằng cách sử dụng tính chất cặp `key:value` của python dictionary, nếu xuất hiện thì cộng 1 value cho mỗi key là 1 token.   
```python
def freq(tokens):
  token_dict = {}
  for token in tokens:
    if token not in token_dict:
      token_dict[token] = 0
    token_dict[token] += 1
  return token_dict
```
![[Pasted image 20250306093339.png]]

+ ? Hàm `pos_tag_count` sử dụng hàm `pos_tag` của thư viện nltk để xác định và gán nhãn loại từ cho mỗi tokens rồi lưu mỗi nhãn vào 1 danh sách `pos_tag_list`. Sau đó biến `tag` đại diện cho loại từ của từng `word` trong `pos_tag_list` được trích xuất ra để đếm số lượng của từng loại từ bằng tính chất cặp `key:value` của python, nếu xuất tồn tại `tag` thì cộng 1 value cho `key`.    
```python
# calculate the number of each pos-tag in the above paragraph
def pos_tag_count(tokens):
  post_tag_dict = {}
  pos_tag_list = nltk.pos_tag(tokens)
  for pos_tag in pos_tag_list:
    word, tag = pos_tag
    if tag not in post_tag_dict:
      post_tag_dict[tag] = 0
    post_tag_dict[tag] += 1
  return post_tag_dict
```
![[Pasted image 20250306094011.png]]

## Remove stop words using NLTK.
+ @ Stop-word là những được coi là không quan trọng vì chúng không mang nhiều ý nghĩa và có tần suất xuất hiện thường xuyên trong 1 ngôn ngữ. (e.g. 'the', 'and', 'is', 'an', 'in')

+ ? Để loại bỏ các stop word trong tiếng anh. Trước tiên mình sao chép danh sách tokens thành clean_token để tránh làm biến đổi  tokens.  Rồi tải các stop word từ thư viện nltk để loại bỏ những token trong clean_token trùng với stop word. Cuối cùng mình tính tần suất xuất hiện của các từ còn lại để kiểm chứng sử dụng thư viện `FreqDist` của nltk.
```python
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

clean_tokens = tokens[:] # copy tokens list to clean_token
sr = stopwords.words('english')

for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)

freq = nltk.FreqDist(clean_tokens)

for key,val in freq.items():
    print(str(key) + ':' + str(val))
```
![[Pasted image 20250306110136.png]]


## Tokenization using Spacy

Tải thư viện xử lý ngôn ngữ spacy và thư viện xử lý ngôn ngữ tiếng anh của spacy kích thước nhỏ (i.e. sm) 
```python
!pip install -U spacy
!python -m spacy download en_core_web_sm
```

+ ? Đoạn code dưới đây minh họa 1 cách khác để tokenize sử dụng thư viện spacy tạo ra 1 pipeline `nlp` rỗng `spacy.blank("en")` chỉ bao gồm tokenizer của tiếng anh không bao gồm mô hình khác (e.g. POS tagging, parser, etc..)
```python
import spacy

nlp = spacy.blank("en")

# Process the text
doc = nlp("I like tree kangaroos and narwhals.")

# Print all tokens
for token in doc:
  print(token.text)
```

## Model
+ ? Đoạn code thể hiện cách mình có thể tải mô hình tiếng anh đầy đủ các thành phần gồm Tokenizer, POS Tagging, Parser, NER (Named Entity Recognition) từ `en_core_web_sm`  để xử lý văn bản `text` trong đó 
	+ `en`: tiếng anh
	+ `core`: các thành phần cơ bản của NLP (tokenization, tagging, NER, ...)
	+ `web`: mô hình huấn luyện trên dữ liệu web 
	+ `sm`: small (mô hình nhỏ)
```python
import spacy

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

# Process whole documents
text = ("When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")
doc = nlp(text)
```


## Syntax Analyzing
+ ? Đoạn code dưới đây cho phép mình trích xuất 1 danh sách những cụm danh từ và 1 danh sách gồm các token từ gốc (i.e. lemma) thuộc loại động từ.  
```python
# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
```
+ `doc.noun_chunks` trong đoạn code đầu cho phép mình truy cập thuộc tính của SpaCy object `doc`, tự động trích xuất 1 danh sách chứa cụm danh từ (e.g. `["I", "natural language processing"]`) sau đó được đưa về dạng text sử dụng `chunk.text`. 
	
+ `token.pos_` trong đoạn code thứ 2 cho phép mình truy cập Loại từ của token (e.g. VERB là động từ) rồi trả về hình thái ngữ nghĩa của nó sử dụng `token.lemma_` (e.g. running -> run)

## Entity extraction
+ ? Đoạn code dưới minh họa cách **nhận dạng và trích xuất các thực thể (Named Entity Recognition - NER) từ văn bản** đã được xử lý bởi SpaCy. 
```python
for entity in doc.ents:
    print(entity.text, entity.label_)
```
+ `doc.ents`:
	+ là thuộc tính chứa các thực thể đã được SpaCy phát hiện trong văn bản.
	+ mỗi thực thể đều là 1 cụm từ có ý nghĩa đặc biệt như tên người, tổ chức, địa điểm, etc..  (e.g. cụm từ `["Sebastian", "Thrun"]` có là tên người)
+ `entity` là các biến được trích xuất từ `doc.ents` trong đó
	+ `entity.text`: là văn bản gốc của thực thể (e.g. `["Sebastian", "Thrun"]` -> `"Sebastian Thrun"`) 
	+ `entity.label_` là nhãn của thực thể bao gồm các nhãn 
		+ `PERSON`: người
		+ `ORG`: tổ chức
		+ `GPE`: viết tắt của Geog-Political Entities đại diện cho tên quốc gia, thành phố, địa điểm địa lý.
		+ `DATE`: Thời gian, ngày tháng
		+ `NORP`: Quốc tịch hoặc nhóm tôn giáo/chính trị

## Exercise (Count total NER in Vietnamese Text)
+ @ **Mục tiêu bài tập:** đếm số lượng của mỗ thực thể trong văn bản tiếng việt được tiền sử xử lý lấy trừ trên web. 
+ ? Đoạn code dưới đây trích xuất văn bản trong thẻ `html` từ  `url` và chuyển đổi nội dung sang cấu trúc dữ liệu dễ trích xuất hơn với  `html.parser` của BeautifulSoup. Rồi tìm mọi thẻ paragraph `p` có class Normal để ghép văn bản trong các thẻ `p` vào `content` để đọc.   
```python
import tqdm
from bs4 import BeautifulSoup, NavigableString, Tag
import requests
url = "https://vnexpress.net/tong-bi-thu-tiep-tuc-doi-moi-quyet-liet-va-toan-dien-4836938.html"
content = requests.get(url).content
soup = BeautifulSoup(content, "html.parser")
content = ""
for p_tag in soup.find_all("p", class_='Normal'):
  content += p_tag.get_text(" ", strip=True) + "\n"
  
content
```

+ ? Vì SpaCy không còn hỗ trợ mô hình xử lý tiếng việt như `vi_core_news_lg` nữa, mình có thể tải 1 thư viện xử lý tiếng việt mới khác là underthesea
```python
pip install underthesea
```
```python
from underthesea import text_normalize, word_tokenize
```

+ ? Trước khi tokenized mình cần loại bỏ các ký tự thừa trong văn bản lấy từ trong thẻ `p` như là ký hiệu xuống dòng `\n` 
```python
normalized_text = text_normalize(content)
normalized_text
```
![[Pasted image 20250306180306.png]]
+ ? Tokenize văn bản 
```python
tokens = word_tokenize(normalized_text)
tokens
```
![[Pasted image 20250306171956.png]]


+ ? Hàm `ner` nhận vào 1 chuỗi văn bản (`content`) sau đó xử lý và trả về kết quả là danh sách các tuple, mỗi tuple tương ứng 1 token (từ) trong câu. Với mỗi tuple có cấu trúc 4 thành phần `(token, POS-tag, chunking-tag, NER-tag)`
	`token`: từ đã được tokenize 
	`POS-tag` nhãn từ loại (Part-of-speech) của từ
	`chunking-tag` nhãn cụm từ (chunking), xác định via trò của từ trong cụm (e.g. NP, VP, PP)
	`NER-tag`: nhãn thực thể, dùng hệ nhãn [BIO](https://datascience.stackexchange.com/questions/63399/what-is-bio-tags-for-creating-custom-ner-named-entity-recognization) (Begin-Interior-Out)
```python
from underthesea import ner

ner_list = ner(content)
ner_list
```
![[Pasted image 20250306172037.png]]

+ ? Biết rằng mỗi tuple trong `ner_list` có cấu trúc 4 thành phần `(token, POS-tag, chunking-tag, NER-tag)`, mình có thể phân loại `token` vào các list `ner_tag` sử dụng tính chất `key:value` và đẩy `token` ở index 0 vào mỗi `ner_tag` ở index 3. Cuối cùng lưu các cặp `ner_tag:token` vào 1 từ điển `ner_tag_dict`  
```python
ner_tag_dict = {}

for element in ner_list:
  word = element[0]
  ner_tag = element[3]
  if ner_tag not in ner_tag_dict:
    ner_tag_dict[ner_tag] = []
  ner_tag_dict[ner_tag].append(word)

for k, v in ner_tag_dict.items():
  print(k, ":", v)
```
![[Pasted image 20250306172024.png]]
+ ? Để đếm số `token` của mỗi `ner_tag`, mình chỉ cần sử dụng module `.item()` của python dict để trích xuất các cặp `ner_tag:token` rồi đếm số lượng `token` sử dụng `len`
```python
for k, v in ner_tag_dict.items():
  print(k, ":", len(v))
```
![[Pasted image 20250306180517.png]]
