[aio code solution](https://drive.google.com/drive/folders/1MICD-AhRGdNnz2B7jVF84kA42wlUxIV1?usp=drive_link)
## Tokenization
**$\to$ Translator between human language and mathematical, computational data.**

But *resource are limited and human languages is limitless*. We need a method to *balance Efficiency and Vocabulary size* (Subword Tokenization). This leading us to 3 tokenizer method:
![[Pasted image 20260416122205.png]]
**Word-level (Too Big)**  tokenize at word-level -> *hard to generalize & adapt* to multiple sequence. 
-> Brute force, have to tokenize every single word. Obvisouly Inefficient.

**Char-level (Too Long, even worst efficiency)** if every letter were a token -> long-range context would be a nighmare compare to word-level.

**Subword-level (Just Right)** - Break down word into Structure. Common words (e.g. the) stay whole/unchange, while rare or complex word like "Quintessential" are broken into meaningful subunits ("quint", "essen", "tial") 
-> The great thing is these *subunits could be reused for a lot of words.* This improve efficiency while preserving vocabulary size.  Kinda like how human learning languages. 

This tokenization method *reveal the structural and semantic nuances of language:*
+ *Morphological Awareness:* subword tokens often represent roots, prefixes and suffixes like "un-", "re-" and "-ness" modify a word, allowing the model to generalize meaning.
	
+ *Handling Rare Words/Typos:* by learning word structure instead of the whole word, model can *still understand New Word by breaking it into parts it reognizes.*
	
+ *Efficient Handling of Non-Space Language:* as you know in symbols/character based languages like Chinese, Japanese and Korean every character have its own meaning (unlike English where `a, b,c` alone have no meaning), because each symbol/char added to the characters add a new meaning, we must have a method to destructurelize their language.  
	-> Making subword-level incredibly necessary to identify structure.

![[Pasted image 20260416125022.png | 888]]

### GPT-2 Training Process
1. *Pretraining* (created a reliable backbone with generalized languages) 

2. *Supervised fine-tuning (SFT)* model get fine-tuned with high-quality data with  `prompt - response` or conversation template to *improve Output response (more human) and ability for In-Context Learning.* - 

3. *Alignment tunning* - model get fine-tune using RLHF (Reinforcement Learning with Human Feedback) and DPO (Direct Preference Optimiation) to *improve Understadability, Safetiness and fit with user need more.*

```ad-note
**Compare different between Pretraining vs SFT vs Aligment/Preference tunning**

---

**Dữ liệu pretraining:** Đây là các văn bản thô, chưa được gắn nhãn theo cấu trúc hội thoại hay chỉ dẫn.

*Ví dụ:* “Thơ ngũ ngôn là một thể thơ truyền thống. Mỗi câu thường gồm năm tiếng.
Thể thơ này thường được dùng để diễn tả cảm xúc ngắn gọn, cô đọng...”

---

**Dữ liệu SFT:** Đây là dữ liệu có cấu trúc đầu vào - đầu ra rõ ràng.

*Đầu vào:* “Hãy làm một bài thơ 5 chữ miêu tả cảnh mùa thu.”
*Đầu ra mục tiêu:* “Mùa thu lá vàng rơi / Gió đưa hương cốm mới / Mây trôi ngang
lưng trời / Nắng chiều êm dịu vợi.”

---

**Dữ liệu alignment / preference tuning:** Đây là dữ liệu thể hiện sự ưu tiên tương đối giữa nhiều câu trả lời cho cùng một yêu cầu.

*Prompt:* “Làm thơ 5 chữ về ánh trăng.”
*Chosen:* Một bài thơ đúng chủ đề, đúng 5 chữ, diễn đạt mạch lạc và giàu hình ảnh.
*Rejected:* Một câu trả lời lạc đề, sai số chữ trong câu, hoặc chuyển sang giải thích khái niệm thiên văn thay vì làm thơ.
```

## GPT-2 Poem Generation

### Data Preprocessing (from [Wikitext](https://youtu.be/cI73FgY4aSc?si=o1_UXXTTivcNoiWK))
Wikitext params dictionary structure
```python
params = {
    "action": "query",      # Required: Query for data
    "format": "json",      # Output format
    "titles": "Main Page",  # The title of the page to fetch
    "prop": "revisions",   # Get revisions of the page
    "rvprop": "content",   # Specifically, the content (wikitext)
    "rvslots": "main",     # Defines the slot containing the text
    "formatversion": "2"   # Easier JSON parsing structure
}
```
Example Request:
```python
import requests

URL = "https://en.wikipedia.org/w/api.php"
params = {
    "action": "query",
    "format": "json",
    "titles": "Python_(programming_language)",
    "prop": "revisions",
    "rvprop": "content",
    "rvslots": "main",
    "formatversion": "2"
}

response = requests.get(URL, params=params)
data = response.json()

# Accessing the wikitext
wikitext = data['query']['pages'][0]['revisions'][0]['slots']['main']['content']
print(wikitext)
```
Key Parameters for Wikitext
- **`titles`** or **`pageids`**: Defines which page to retrieve.
- **`prop=revisions`** & **`rvprop=content`**: These must be used together to get the raw text.
- **`rvslots=main`**: Mandatory for modern MediaWiki versions that support multiple slots.
- **`formatversion=2`**: Modernizes the JSON ouput, cleaner to parse than version 1.

---

+ ! Chú ý hàm regex nào nên Ưu Tiên đứng tr'c và hàm nào Đứng Sau. Phòng khi hàm regex 1 xóa mất patterns của hàm regex 2.  

**Quy trình làm sạch:**
- Xóa HTML comments, thẻ `<ref>`, và các HTML tags khác.
- Xóa bảng wiki (`{|...|}`), template (`{{...}}`), và image/file links.
- Giữ lại text trong các wikilink nội bộ (`[[...]]`).
- Chuyển headers `==...==` thành text thuần, xóa list prefix (`*`, `#`, `;`, `:`).
- Cắt bỏ các section cuối thường là tham khảo/liên kết ngoài.
- Chuẩn hóa khoảng trắng và dòng trống.

```python
# --- Regex Patterns & Hằng số dùng cho việc làm sạch Wikitext ---
import re

# Giữ nguyên pattern gốc của script
_PATTERNS = [
    (re.compile(r"<!--.*?-->", re.DOTALL), ""),
    (re.compile(r"<ref[^>]*/\s*>", re.IGNORECASE), ""),
    (re.compile(r"<ref[^>]*>.*?</ref>", re.DOTALL | re.IGNORECASE), ""),
    (re.compile(r"<(div|span|small|big|b|i|u|s|br|p|table|tr|th|td|ul|ol|li|dl|dt|dd|sub|sup|blockquote|nowiki|code|pre|gallery|imagemap|timeline|score|syntaxhighlight|source|poem|section|indicator|templatestyles|hiero|math|chem)[^>]*>", re.IGNORECASE), " "),
    (re.compile(r"</[a-z]+>", re.IGNORECASE), " "),
    (re.compile(r"<[^>]+>"), ""),
]

_MARKUP = re.compile(r"'''|''|----+")
_MAGIC = re.compile(r"__[A-Z_]+__")
_WHITESPACE = re.compile(r"[ \t]+")
_NEWLINES   = re.compile(r"\n{3,}")
_HEADERS = re.compile(r"^=+\s*(.+?)\s*=+\s*$", re.MULTILINE)
_EMPTY_HEADERS = re.compile(r"^=+\s*=+\s*$", re.MULTILINE)
_LIST_PREFIX = re.compile(r"^([*#;:]+)\s?", re.MULTILINE)
_TERMINAL_SECTION_RE = re.compile(
    r"^\s*=+\s*("
    r"Tham\s+kh\u1ea3o|Ch\u00fa\s+th\u00edch|Ghi\s+ch\u00fa|Li\u00ean\s+k\u1ebft\s+ngo\u00e0i"
    r"|Xem\s+th\u00eam|Th\u01b0\s+m\u1ee5c|\u0110\u1ecdc\s+th\u00eam|Ngu\u1ed3n\s+tham\s+kh\u1ea3o"
    r"|Ch\u00fa\s+gi\u1ea3i|Ghi\s+ch\u00fa\s+v\u00e0\s+tham\s+kh\u1ea3o"
    r"|References?|External\s+links?|See\s+also|Notes?|Bibliography|Further\s+reading"
    r")\s*=+\s*$",
    re.IGNORECASE | re.MULTILINE,
)
```