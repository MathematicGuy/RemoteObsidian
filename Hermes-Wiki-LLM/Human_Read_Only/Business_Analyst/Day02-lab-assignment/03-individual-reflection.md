# Individual Reflection (của Đinh Nhật Thanh - 2A202600572)

## Đóng góp của em trong nhóm

| Hoạt động | Em đã làm gì? | Kết quả / ảnh hưởng |
|-----------|----------------|----------------------|
| Scan cá nhân | Đưa ra 10 problems thực tế ban đầu và mở rộng lên 15 problems cụ thể về công tác giảng dạy & quản lý khoa học. | Cung cấp cho nhóm một kho bài toán thực tế đa dạng lăng kính, có baseline thời gian và đau thật. |
| Pitch Problem Card | Pitch bài toán soạn MCQ từ slide (#1) với bottleneck nghĩ đáp án nhiễu (40 phút) và lỗi format GIFT (15 phút). | Thuyết phục nhóm chọn candidate này làm đề tài cuối cùng nhờ có workflow rõ và scale impact lớn (điểm số cao nhất nhóm: 35). |
| Challenge bài khác | Challenge bài toán order cơm của Chi về quy mô tác động (scale impact) và bài toán tìm tài liệu của Khánh Toàn về tính cần thiết của AI. | Giúp nhóm loại bỏ các ý tưởng có thể giải quyết đơn giản bằng Rule-based hoặc có giá trị sử dụng hẹp. |
| Gom trùng / cluster | Hỗ trợ nhóm phân nhóm các vấn đề thành 3 cluster lớn: Sinh nội dung, Tổng hợp dữ liệu phi cấu trúc, và Truy xuất thông tin. | Nhóm định hình rõ bức tranh tổng thể trước khi bước vào shortlist. |
| Chọn candidate problem | Cung cấp số liệu baseline và bối cảnh nghiệp vụ giảng viên thật để làm sáng tỏ các lý lẽ trong cuộc thảo luận. | Giúp nhóm đạt đồng thuận nhanh chóng và giải quyết triệt để sự phân vân giữa bài MCQ và bài order. |
| Validation / research | Trực tiếp phỏng vấn nhanh 2 giảng viên đồng nghiệp trong khoa và nghiên cứu các competitor như Quizizz AI, ChatGPT. | Xác nhận khoảng trống thị trường: Chưa có công cụ hỗ trợ tiếng Việt bám sát slide và xuất định dạng GIFT chuẩn. |
| Problem Statement | Soạn thảo Problem Statement v0/v1, trực tiếp định nghĩa success metric thời gian và Likert scale đánh giá chất lượng. | Đưa ra mục tiêu rõ ràng, đo lường được và thiết lập ranh giới boundary bảo mật học thuật chặt chẽ. |
| Rule / Workflow / Agent | Lập luận hạ cấp giải pháp từ Agent xuống Workflow để kiểm soát rủi ro hallucination đề thi. | Nhóm thống nhất phương án an toàn nhất: AI hỗ trợ draft, giảng viên duyệt, Rule export GIFT. |
| Decision | Thiết kế phương án pilot nhỏ nhất (chạy prompt ReAct bán thủ công trên slide thật của em). | Định hình bước đi tiếp theo cụ thể, có tiêu chí Go/Rollback rõ ràng dựa trên evidence thực tế. |

---

## Bảng dùng AI trong reflection

| Phase | Em dùng AI để làm gì? | AI hữu ích ở đâu? | AI sai/hời hợt ở đâu? | Em sửa gì bằng nhận định của mình |
|-------|------------------------|-------------------|----------------------|-----------------------------------|
| Scan | Nhờ AI gợi ý mở rộng danh sách từ 10 lên 15 problems giảng dạy của đại học. | Gợi ý rất tốt 2 bài toán mới: Chấm bài viết tự luận (#12) và Phân tích qualitative feedback cuối kỳ (#14). | AI gợi ý một số bài toán quá rộng và mơ hồ như "tự động soạn giáo án từ zero" – không thực tế. | Em loại bỏ các ý tưởng mơ hồ, chỉ giữ lại các tác vụ có workflow và actor rõ ràng. |
| Problem Card | Nhờ AI phản biện Problem Card #1 và phác thảo ASCII workflow trước/sau. | Giúp làm nổi bật bottleneck nghĩ distractors và lỗi cú pháp. | AI tự tiện gộp bước review và upload làm mất đi ranh giới kiểm soát chất lượng của con người. | Em tách lại bước Human review làm ranh giới an toàn (boundary) bắt buộc trong workflow. |
| Research | Tìm hiểu competitor và tài liệu chuẩn GIFT format. | Trích xuất nhanh thông tin Quizizz, ChatGPT nhưng AI bịa số liệu thống kê thời gian tiết kiệm không nguồn. | AI đưa ra số liệu tiết kiệm thời gian ảo (ví dụ: tiết kiệm 95% thời gian ngay lập tức). | Em tự đi phỏng vấn đồng nghiệp để lấy baseline chuẩn 120-180 phút/tuần của giảng viên Việt Nam. |
| Problem Statement | Nhờ AI tìm kịch bản kiểm thử cho chất lượng đề thi. | Gợi ý tốt về việc sử dụng khảo sát Likert 5 điểm đánh giá độ plausible của đáp án nhiễu. | AI đề xuất tự động đẩy đề lên LMS không qua người duyệt – cực kỳ nguy hiểm nếu AI bịa kiến thức. | Em chặn đứng lại bằng boundary: Giảng viên là chốt chặn cuối cùng, AI không tự upload. |

---

## Câu hỏi mở – Reflection

**Em học được gì khi nghe top 3 problems của các bạn khác?**

Em học được sự tương phản sâu sắc giữa các domain nghiệp vụ. Bài toán của Chi (order đồ ăn trưa) hay Quân (feedback phỏng vấn) có tính thực tế cao và chạm vào cuộc sống hàng ngày của doanh nghiệp. Tuy nhiên, khi đặt lên bàn cân "scale impact", bài toán MCQ của em lại có đòn bẩy lớn hơn rất nhiều về mặt giáo dục: Nó ảnh hưởng trực tiếp đến chất lượng đánh giá của hàng ngàn sinh viên và danh tiếng học thuật của khoa. Điều này củng cố tư duy BA sâu sắc: Chọn bài toán không phải vì nó nghe "cool" hay "dễ làm", mà vì quy mô giá trị (leverage) và chiều sâu điểm đau nó mang lại cho người dùng cuối.

**Nhóm có lúc nào bị solution-first không?**

Có. Trong quá trình thảo luận về AI hypothesis cho bài MCQ, một thành viên đã đề xuất ngay lập tức: *"Dùng Multi-Agent tự lập kế hoạch, tự đọc slide và tự import trực tiếp vào Moodle qua API"*. Nhờ ArchSeed *"If you assume it just works, it's already broken"*, em đã đặt câu hỏi ngược lại: *"Nếu hệ thống tự chạy từ đầu đến cuối và bịa ra một kiến thức sai trong đề thi chính thức, ai sẽ là người chịu trách nhiệm trước nhà trường khi sinh viên khiếu nại?"* Câu hỏi này lập tức kéo cả nhóm về thực tế và giúp định hình lại giải pháp ở mức Workflow có Human-in-the-loop chặt chẽ thay vì một Agent tự trị đầy rủi ro.

**Em có thay đổi ý kiến sau khi bị challenge không?**

Có. Khi Chi challenge em: *"Nếu giảng viên chỉ cần dùng lại ngân hàng đề thi cũ của nhà xuất bản đi kèm sách giáo trình thì AI ra đề mới có thực sự cần thiết không?"*, ban đầu em hơi phòng vệ vì cho rằng slide của em là độc quyền. Nhưng sau đó em nhận ra đây là một câu hỏi cực kỳ sắc bén về non-AI alternative. Em đã bình tĩnh phân tích và điều chỉnh: AI không thay thế ngân hàng đề thi cuối kỳ chuẩn hóa, mà hỗ trợ giảng viên soạn các bộ quiz ôn tập nhanh *bám sát slide bài giảng cập nhật thực tế trên lớp hằng tuần* - nơi ngân hàng đề cũ không thể phủ kịp. Challenge này giúp định vị sản phẩm của nhóm trở nên thực tiễn hơn.

**Em đóng góp gì thật sự vào artifact cuối?**

Là domain expert trực tiếp chịu nỗi đau này, em đóng góp quan trọng nhất ở việc cung cấp chi tiết từng bước workflow thực tế của một giảng viên, giải thích cú pháp GIFT/Aiken, trực tiếp phỏng vấn 2 đồng nghiệp để lấy bằng chứng baseline, và thiết lập ranh giới boundary an toàn học thuật. Sự thực tế từ bối cảnh giảng dạy của em giúp toàn bộ tài liệu nhóm không bị rơi vào tình trạng "nghĩ trong chân không".

**Điều khó nhất khi viết Problem Statement là gì?**

Khó nhất là lượng hóa metric "độ nhiễu chất lượng" của các đáp án distractors. Khác với thời gian (đo bằng phút), tính "hợp lý nhưng sai hoàn toàn" của đáp án nhiễu là một khái niệm định tính. Nhóm đã giải quyết bằng cách thiết lập thang đo Likert 5 điểm để giảng viên đánh giá trực quan chất lượng distractors trong quá trình thử nghiệm, kết hợp với chỉ số phân loại (discrimination index) thu được sau khi sinh viên làm bài thật.

**Nếu làm lại, em sẽ challenge nhóm mạnh hơn ở điểm nào?**

Em sẽ challenge nhóm sâu hơn về phần "Fallback" khi AI liên tục sinh ra kiến thức sai (hallucination) trong đợt thi thật. Nếu giảng viên bận rộn và duyệt ẩu qua vòng lặp ReAct, làm sao hệ thống tự động phát hiện được câu hỏi sai? Lẽ ra chúng em nên thiết kế thêm một module Rule-based đối chiếu từ khóa (keyword validation) dựa trên glossary của môn học trước khi cho phép xuất file GIFT để làm màng lọc an toàn thứ hai.