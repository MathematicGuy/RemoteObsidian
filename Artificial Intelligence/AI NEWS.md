**[META TUNG KIẾN TRÚC MỚI THAY THẾ TOKENIZATION](https://www.facebook.com/share/p/16WBGDh5D6/)**
```ad-note
Tháng 12/24, Bước cùng AI review paper mang tính đột phá của Meta. Công ty này vừa open source kiến trúc mới Byte Latent Transformer (BLT), với tham vọng đặt dấu chấm hết cho tokenization quen thuộc.

BLT: CÁCH MẠNG LLM, ĐẬP TOKENIZATION XÂY MỚI
```

---

[text-2-LoRA](https://github.com/sakanaai/text-to-lora) 
(Increase AI Adaptation - like human (e.g. human eyes dialates for diff lighting enviroment))
+ ! Các LLM sau khi training thì kiến thức bị đóng băng. Muốn bổ sung kiến thức mới hoặc tăng cường cho các ứng dụng cụ thể đòi hỏi phải fine-tune cần nhiều tài nguyên.
	+ $ text-2-LoRA sử dụng meta learns về 1 hypernetwork chấp nhận prompt mô tả nhiệm vụ mong muốn và tạo ra LoRA đặc thù cho nhiệm vụ đó. 	
		Note: T2L có thể mã hóa hàng trăm LoRA Adapters mặc dù quá trình nén bị mất mát thông tin nhưng T2L vẫn duy trì hiệu suất để tinh chỉnh đặc thù cho nhiệm vụ. 
	+ $ Text-2-LoRA tiết kiệm tham số và nó tạo ra LoRA trong 1 bước duy nhất, chi phí thấp hơn, chỉ dựa vào mô tả văn bản về nhiệm vụ. 
[Automatically Build Website or App using MCP](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms)


