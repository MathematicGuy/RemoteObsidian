### Before and After GGUF
![[Pasted image 20260517203259.png | 666]]
![[Pasted image 20260517203321.png | 666]]

**Scale of Savings for Larger Models**
The [savings](https://huggingface.co/blog/wolfram/llm-comparison-test-llama-3) become even more critical with larger models like **Llama 3 70B**: 
- **Native (FP16):** Requires **~140 GB** of VRAM (impossible on single consumer GPUs).
- **GGUF (Q4_K_M):** Fits into **~40 GB**. This makes it possible to run a "GPT-4 class" local model using a Mac Studio or a dual-GPU setup (e.g., two RTX 3090s with NVLink)
 
[Explain GGUF](https://pguso.medium.com/the-gguf-format-explained-making-ai-models-run-anywhere-even-on-your-laptop-30dcb45358da) 
![[Pasted image 20260517203553.png]]

