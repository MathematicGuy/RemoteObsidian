## Why RAG?

The main goal of RAG is to improve the generation outptus of LLMs.

Two primary improvements can be seen as:

1. **Preventing hallucinations** - LLMs are incredible but they are prone to potential hallucination, as in, generating something that _looks_ correct but isn't. RAG pipelines can help LLMs generate more factual outputs by providing them with factual (retrieved) inputs. And even if the generated answer from a RAG pipeline doesn't seem correct, because of retrieval, you also have access to the sources where it came from.

2. **Work with custom data** - Many base LLMs are trained with internet-scale text data. This means they have a great ability to model language, however, they often lack specific knowledge. RAG systems can provide LLMs with domain-specific data such as medical information or company documentation and thus customized their outputs to suit specific use cases.

---
## Where we appiled it ?
Textbook, Research Paper - Mostly PDF paper form.

## Why ?
> To Understand the Model better and Inspect its core functionality. While keeping privacy, and allowing for further customization.


## Key terms
| Term                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Token**                           | 1 đoạn text, VD "life, is good!" có thể chia thành ["life", ",", "is", "good", "!"]. Một token có thể là 1 từ hoàn chỉnh hoặc 1 phần của từ hoặc 1 ký hiệu câu. 1 token ~ 4 ký tự trong Tiếng Anh, 100 token ~ 75 từ. Văn bản được chia thành các token trước khi được chuyển đến LLM.                                                                                                                                                                                                                                                               |
| **Embedding**                       | Chuyển hóa dữ liệu text sang dữ liệu số cho máy có thể đọc. Dữ liệu số thường thuộc kiểu int hoặc là float. VD, "life is good" thành {1232: b'life', 242: b'is', 132: b'good'} dùng Byte pair encoding (mã hóa cặp Byte). Google có thư viện tokenization là  [SentencePiece](https://github.com/google/sentencepiece)                                                                                                                                                                                                                               |
| **Embedding model**                 | Mô hình được thiết kế để nhận dữ liệu đầu vào và đưa ra 1 biểu diễn số. VD, 1 mô hình nhúng văn bản có thể lấy 384 token và biến nó thành 1 vector kích thước 768 (768 hàng). note: 1 thường khác mô hình LLM                                                                                                                                                                                                                                                                                                                                        |
| **Similarity search/vector search** | "Tìm kiếm tương đồng / Tìm kiến vector" nhằm mục đích tìm 2 vector gần nhau trong không gian n chiều. VD, 2 văn bản có chủ đề tương tự sẽ có giá trị các vector gần nhau, trong khi 2 đoạn văn bản về 2 chủ đề khác nhau sẽ có giá trị các vector thấp. (Mình gọi "điểm tương tự" của 2 token là "giá trị các vector")<br><br>Các phép đo điểm tương tự phổ biến là tích vô hướng và độ tương tự cosin.                                                                                                                                              |
| **Large Language Model (LLM)**      | Mô hình học máy được đào tạo sâu có khả năng hiểu và tạo văn bản ngôn ngữ con người.<br><br>Nói sâu hơn, đây là 1 mô hình đc đào tạo để biểu diễn các mẫu (pattern) trong văn bản theo dạng số. 1 LLM sinh sẽ sinh ra 1 chuỗi số khi đc cung cấp 1 chuỗi số (chuỗi số thường là đoạn văn bản sau khi embedding) <br><br>VD: được cung cấp 1 chuỗi văn bản "life is good", 1 LLM có thể tạo ra "I want to play today". Mô hình dự đoán này phụ thuộc nhiều vào dữ liệu Huấn Luyện và Yêu Cầu của người dùng (User Prompt)                             |
| **LLM context window**              | Số Lượng Tokens mà LLM có thể nhận. VD, vào tháng 8 năm 2024 GPT-4o có cửa sổ ngữ cảnh mặc định là 8192 nghìn tokens. (khoảng 96 trang văn bản word). <br><br>Mô hình Gemma-7b-it mình dùng trong dự án (tháng 8 năm 2024) này có cửa sổ ngữ cảnh là 2048 tới 4096 token (24 trang văn bản) <br><br>Cửa sổ ngữ cảnh cao hơn nghĩa là LLM (hoặc RAG pipeline) có thể nhận nhiều thông tin có liên quan hơn để hỗ trợ truy vấn mà không gây ra ảo giác cao.                                                                                            |
| **Prompt**                          | Một thuật ngữ để mô tả đầu vào cho LLM tạo sinh. Ý tưởng của "kỹ thuật nhắc nhở" [prompt engineering](https://www.google.com/url?q=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FPrompt_engineering) là cấu trúc đầu vào dựa trên văn bản (hoặc dựa trên hình ảnh) cho LLM tạo sinh theo 1 cách cự thể để đầu ra được tạo ra là lý tưởng vs người gửi. <br>Kỹ thuật này có thể thực hiện được vì khả năng học trong ngữ cảnh của LLM, tức là nó có thể sử dụng cách biểu diễn ngôn ngữ của mình để phân tích nhắc và nhận ra đầu vào phù hợp có thể là gì. |


### Install requirements
```
pip install -r requirements.txt
```
**Note:** I found I had to install `torch` manually (`torch` 2.1.1+ is required for newer versions of attention for faster inference) with CUDA, see: https://pytorch.org/get-started/locally/
On Windows I used:
```
pip3 install -U torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

