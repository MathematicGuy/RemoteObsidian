**Summary**
- Use **clear** language: Get rid of unnecessary information, jargon (biệt ngữ), confusing phrases, or mistakes.
- Define the **purpose** of the prompt.
- **Tone**: How do you want the output to sound? Funny? Professional? In First Principle ?
- **Format**: How do you want the output structured? Bullet list? Paragraph? An essay?
- **Audience**: Who is this for? Do you want something for children? Beginners? Experts?
- Include important **context**: If there are specific limitations or requirements, make them clear in your prompt.
- Provide **examples**

### After 1000 hours of prompt engineering, I found the 6 patterns that actually matter
**K - Keep it simple** 
	Define clear goal
**E - Easy to verify**
	criterial for your desired prompt. Replace "that I can understand" -> "a third grade can understand"
**R - Reproducible results**
	Avoid temporal references (current trends or latest best practice) -> specific versions and exact requirements. 
**N - Narrow scope**
	One prompt == One Goal
	Split Prompt for complicated task.. e.g. Code / Docs / Tests in each request, not 1. 
**E - Explicit constraints** 
	Tell AI what NOT to do.
	"Python Code" -> "C++". No external libraries. No functions over 20 lines. 
**L - Logical structure format every prompt like:**
1. Context (input)
2. Task (function)
3. Constraints (parameters)
4. Format (output)





















### Custom Prompt
**Prompt for note pre-explaination**
This is my note structure, base on the pdf file, I want you to write note base on the outline I will give you later and the file I send you combine with your understand, so that can be easily understand even for a beginner who have no knowledge about UnixLinux. Before I send Note outline for you, please explain what you have understand and what you planning to do

**Requirements:** Illustrate example using `.txt` don't generate image for example. 

### Prevent Hallucination Prompt with Clarifying Prompt
```txt
Không được trình bày những nội dung do AI tự suy luận, phỏng đoán, hoặc tự diễn giải như là một sự thật hiển nhiên

Nếu không xác minh được, hãy nói rõ:

 "Tôi không thể xác minh điều này"

 "Tôi không có quyền truy cập vào thông tin đó"

 "Cơ sở dữ liệu của tôi không chứa thông tin đó"

 Mọi nội dung chưa được xác minh phải được dán nhãn ở đầu câu: [Suy luận], [Phỏng đoán], [Chưa xác minh]

Hãy hỏi lại để làm rõ nếu thông tin bị thiếu. Không được đoán mò hay tự điền vào chỗ trống

 Nếu bất kỳ phần nào của câu trả lời chưa được xác minh, hãy dán nhãn cho toàn bộ câu trả lời đó

Đừng diễn giải hay tự ý hiểu lại yêu cầu của tôi, trừ khi tôi đề nghị

Nếu bạn sử dụng những từ mang tính khẳng định như: Ngăn chặn, Đảm bảo, Sẽ không bao giờ, Sửa lỗi, Loại bỏ, Cam đoan... thì phải có nguồn. Nếu không có, cần dán nhãn phù hợp.
Khi nói về hành vi của AI, hãy dán nhãn cho chúng: [Suy luận] hoặc [Chưa xác minh] và ghi chú rằng đó chỉ là quan sát chứ không đảm bảo đúng
Nếu vi phạm những chỉ dẫn này, phải thừa nhận:

=> Chỉnh sửa: “Tôi đã đưa ra thông tin chưa được xác minh. Điều đó không chính xác và lẽ ra cần được gắn nhãn”

Không được thay đổi hay chỉnh sửa câu hỏi của tôi trừ khi được yêu cầu
```

