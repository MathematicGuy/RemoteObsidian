Bian, Yifan, et al. *"Understanding Naturalistic Facial Expressions with Deep Learning and Multimodal Large Language Models."*

- **Bước 1: Tập trung vào khung xương của bài báo**
    - Đọc kỹ phần **Tóm tắt (Abstract)** và **Mở đầu (Introduction)**. Hãy chú ý đến cách tác giả định nghĩa phạm vi của bài tổng quan:
        - _Họ sẽ nói về những gì và không nói về những gì?_
        - _Họ sắp xếp, phân loại các nghiên cứu theo tiêu chí nào?_
          
    - Xem các **tiêu đề chính**. Đây chính là "hệ thống phân loại" (taxonomy) mà tác giả đã dày công xây dựng. Đây là phần giá trị nhất của một bài tổng quan.
      
      
- **Bước 2: Phân tích cấu trúc và các nhánh chính**
    - Đừng cố đọc chi tiết từng phần. Thay vào đó, hãy đọc lướt các mục lớn. Với mỗi mục, hãy trả lời:
        - _Nhóm/phương pháp này giải quyết vấn đề gì?_
        - _Ưu và nhược điểm chính của nó là gì?_
        - _Những bài báo tiêu biểu nào được nhắc đến?_
    - **Đặc biệt chú ý đến các Bảng biểu (Tables) và Hình ảnh (Figures)**. Các bài tổng quan thường có những bảng so sánh các phương pháp hoặc hình vẽ thể hiện dòng thời gian phát triển. Đây là những thông tin đã được cô đọng, rất dễ hiểu.
      
- **Bước 3: Đọc kỹ ở phần cuối**
    - Đọc thật kỹ các phần có tên như **”Conclusion”, “Discussion“, “Future Research Directions“, “Open Challenges“** (Thảo luận, Hướng nghiên cứu tương lai, Thách thức còn bỏ ngỏ).
    - Đây là nơi các tác giả đưa ra nhận định, dự báo về xu hướng.

**Gap:** SOTA model are great but computationally heavy -> election of the most prominent,  
publicly accessible, lightweight, and user-friendly toolboxes that incorporate SOTA models  
suitable for analyzing facial expressions in the wild. 


| Bài báo (Tác giả, Năm) | Vấn đề chính | Phương pháp/Cách tiếp cận | Bộ dữ liệu/Đối tượng | Kết quả nổi bật   | Hạn chế / Thách thức      | Hướng tương lai đề xuất  |
| ---------------------- | ------------ | ------------------------- | -------------------- | ----------------- | ------------------------- | ------------------------ |
| Le A, 2021             | Tối ưu hóa X | Dùng thuật toán ABC       | Dữ liệu mô phỏng     | Tăng hiệu quả 15% | Không chạy thời gian thực | Áp dụng cho dữ liệu thực |

----


**🎯 Mục tiêu chính khi đọc:**
- Hiểu được "bức tranh **tổng quan"** của lĩnh vực.
- Nắm được các **thuật ngữ, định nghĩa cốt lõi.**
- Xác định các **trường phái, phương pháp, hướng nghiên cứu chính.**
- Tìm ra các vấn đề còn bỏ ngỏ **(open problems)** và các **xu hướng tương lai** được các chuyên gia chỉ ra.

**🔍 Cách đọc và trích xuất thông tin:**

- **Bước 1: Tập trung vào khung xương của bài báo**
    - Đọc kỹ phần **Tóm tắt (Abstract)** và **Mở đầu (Introduction)**. Hãy chú ý đến cách tác giả định nghĩa phạm vi của bài tổng quan:
        - _Họ sẽ nói về những gì và không nói về những gì?_
        - _Họ sắp xếp, phân loại các nghiên cứu theo tiêu chí nào?_
    - Xem các **tiêu đề chính**. Đây chính là "hệ thống phân loại" (taxonomy) mà tác giả đã dày công xây dựng. Đây là phần giá trị nhất của một bài tổng quan.
- **Bước 2: Phân tích cấu trúc và các nhánh chính**
    - Đừng cố đọc chi tiết từng phần. Thay vào đó, hãy đọc lướt các mục lớn. Với mỗi mục, hãy trả lời:
        - _Nhóm/phương pháp này giải quyết vấn đề gì?_
        - _Ưu và nhược điểm chính của nó là gì?_
        - _Những bài báo tiêu biểu nào được nhắc đến?_
    - **Đặc biệt chú ý đến các Bảng biểu (Tables) và Hình ảnh (Figures)**. Các bài tổng quan thường có những bảng so sánh các phương pháp hoặc hình vẽ thể hiện dòng thời gian phát triển. Đây là những thông tin đã được cô đọng, rất dễ hiểu.
- **Bước 3: Đọc kỹ ở phần cuối**
    - Đọc thật kỹ các phần có tên như **”Conclusion”, “Discussion“, “Future Research Directions“, “Open Challenges“** (Thảo luận, Hướng nghiên cứu tương lai, Thách thức còn bỏ ngỏ).
    - Đây là nơi các tác giả đưa ra nhận định, dự báo về xu hướng.

**✍️ Bảng ghi chú cho bài tổng quan:**

| Hạng mục                                   | Nội dung cần trích xuất                                                                                                                                  |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Các nhóm, phương pháp, đối tượng chính** | Vẽ lại sơ đồ cây hoặc gạch đầu dòng các hướng nghiên cứu chính mà tác giả đề xuất.                                                                       |
| **Các định nghĩa quan trọng**              | Ghi lại các thuật ngữ cốt lõi và cách định nghĩa chúng.                                                                                                  |
| **Tóm tắt các hướng tiếp cận**             | Với mỗi hướng, ghi 1-2 câu về bản chất, ưu/nhược điểm.                                                                                                   |
| **Các bài báo/tác giả "kinh điển"**        | Liệt kê các công trình được trích dẫn nhiều lần, được xem là nền móng.                                                                                   |
| **Xu hướng và Thách thức**                 | **(Quan trọng nhất)** Chép lại nguyên văn hoặc tóm tắt các ý trong phần **”Conclusion”, “Discussion“, “Future Research Directions“, “Open Challenges“.** |



Dưới đây là **tóm tắt ngắn gọn, có trích dẫn từ bài báo** cho từng hướng tiếp cận bạn liệt kê — mỗi mục gồm 1–2 câu mô tả bản chất và một câu ngắn nêu ưu / nhược điểm chính. Sau đó mình cho phần **đánh giá & so sánh cụ thể các FER toolboxes** (OpenFace, Affdex, Py-Feat, LibreFace, PyAFAR) theo kiến trúc, dữ liệu huấn luyện và hiệu năng cross-domain — mọi khẳng định đều được dẫn nguồn trong file bạn cung cấp.

---

## Tóm tắt các hướng tiếp cận (1–2 câu + ưu/nhược)

1. **Đánh giá & so sánh FER toolboxes (OpenFace, Affdex, Py-Feat, LibreFace, PyAFAR)**  
    Bản chất: tổng hợp, so sánh các toolboxes “thân thiện người dùng” về chức năng (face detection, AU, emotion), kiến trúc (từ shallow → DNN/ViT) và loại dataset huấn luyện (posed/spontaneous/wild).  
    Ưu/nhược: giúp chọn công cụ phù hợp nhanh chóng (ưu: có GUI/tiện lợi, nhiều package sẵn dùng); nhược: khác biệt về nguồn dữ liệu và việc nhiều SOTA DNN nặng/không mở mã làm khó reproducibility và real-time use.
    
2. **Kết hợp tín hiệu AU/features từ FER toolboxes với ngữ cảnh do MLLMs mô tả → xây dựng _contextualized emotion models_**  
    Bản chất: lấy output định lượng từ AU/feature (từ toolbox) và input mô tả ngữ cảnh (objects, scene, activity) do MLLM sinh ra, rồi hợp nhất để suy luận cảm xúc có giải thích.  
    Ưu/nhược: ưu là inference gần với cách con người suy diễn (tăng độ tin cậy, giải thích được); nhược là cần cơ chế fusing/weighting hợp lý và có thể bị nhiễu nếu MLLM mô tả sai ngữ cảnh.
    
3. **Dùng MLLMs để trích xuất/định lượng biến ngữ cảnh (objects, activities, scenes, speech cues) rồi dùng thông tin này để suy luận cảm xúc có giải thích**  
    Bản chất: MLLM đóng vai “bộ não” đọc ảnh/video (và audio/text) để trả về mô tả ngữ cảnh chi tiết (ví dụ “wedding”, “gun on table”) làm tiền đề cho việc xác định nghĩa cảm xúc.  
    Ưu/nhược: ưu là mô tả ngữ cảnh phong phú, chi tiết giúp phân biệt cảm xúc giống-nhìn nhưng khác-nghĩ; nhược là mô tả có thể oversimplify hoặc bỏ sót vật nhỏ nhưng quyết định (ví dụ một khẩu súng) → hậu quả inference sai.
    
4. **Khai thác few-shot ICL của MLLMs để mở rộng phân loại sang nhãn cảm xúc tinh vi/hiếm (awe, shame, …)**  
    Bản chất: dùng in-context learning (few examples + prompt) để MLLM “áp dụng” vào nhiệm vụ ER mới mà không cần fine-tuning.  
    Ưu/nhược: ưu — giảm mạnh nhu cầu nhãn lớn, cho khả năng mở rộng nhanh (nuanced labels); nhược — ICL cho FER chưa được thí nghiệm sâu, và quality phụ thuộc ví dụ/ prompt.
    
5. **Đối chiếu/đo lường sự tương đồng giữa mô tả cues do MLLMs tạo ra và các AU/FACS do toolkit phát hiện**  
    Bản chất: đo xem MLLM mô tả cue nào có tương đương với AU mã hóa FACS (ví dụ “tightened eyes” ↔ AU6) — để đánh giá MLLM có thể thay thế/tương thích với hệ thống AU hay không.  
    Ưu/nhược: ưu — có thể kiểm chứng tính chính xác giải thích của MLLM; nhược — cần bộ đánh giá chuẩn (metrics) và dữ liệu chú thích song song (MLLM-text vs AU labels) để so sánh.
    
6. **Phát triển annotation multimodal (image/video + textual context + self-report khi có)**  
    Bản chất: xây bộ dữ liệu chú thích đồng thời hình ảnh/video, mô tả ngữ cảnh, và (nếu có thể) self-report để làm ground-truth giàu ngữ cảnh.  
    Ưu/nhược: ưu — tăng độ tin cậy label, giúp training + evaluation contextualized models; nhược — chi phí, công sức cao (annotation phức tạp), cần tool/ protocol chuẩn.
    
7. **Thiết lập benchmarks cross-domain / independent evaluations & pilot datasets**  
    Bản chất: tạo tiêu chuẩn đánh giá đa miền (lab → wild, demographics khác nhau) để kiểm tra generalizability và reproducibility của cả toolboxes và MLLMs.  
    Ưu/nhược: ưu — cung cấp phép đo khách quan cho khái quát hóa; nhược — cần cộng đồng, nguồn lực để chuẩn hóa và duy trì benchmark.
    
