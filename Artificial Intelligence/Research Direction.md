**Ưu tiên khi tìm đề tài:** Tìm ra **Vấn Đề Chung trong ngành** mà nhóm muốn giải quyết. **Vấn đề thực tế + mới.** Tính áp dụng cao -> tăng khả năng accept vào báo uy tín.
	Mục Tiêu: **code mô hình (Attention + BERT, etc..)**
	
**Ưu tiên khi Nghiên Cứu:** hiểu mô hình + tự code lại được mô hình => cần khi đi xin việc AI Engineer hoặc Researcher. 
	Bth phỏng vấn sẽ đi từ chủ đề quan trọng nhất (i.e. dự án cá nhân, workflow) rồi fallback về chủ đề liên quan tới software. 
(DL - CV + NLP)

### _Paper - Vision-language foundation models for medical imaging: a review of current practices and innovations

**Ideas:** create a VLM + RAG that return a report from given image. In medicine, they merge **imaging and text** to **improve diagnosis, segmentation, and report generation**.

**1. Introduction**
**1.1 History and Trends:**  
Foundation models mark a shift from task-specific deep learning to **generalized, pre-trained systems** using multimodal data.  
→ Key examples: **CLIP**, **DINO** (), **GPT-3**, **PaLM**.  
→ Impact: improved **zero/few-shot learning** and **cross-modal reasoning**.  
→ In healthcare: enhance **EHR analysis, diagnostics, and report automation** (e.g., BioViL, ChatDoctor).


**1.2 Prior Reviews:**  
Summarizes existing literature on CNNs, deep learning, and medical foundation models, noting the need for **interpretability**, **data balance**, and **clinical validation**.

**2. Survey Research Approach**
**Main idea:**  
Outlines how studies were collected and categorized.  
→ Sources: Google Scholar, Arxiv (2020–2024).  
→ *Criteria: applied to radiology (X-Quang), pathology (bệnh lý), ophthalmology (nhãn khoa); with experimental validation.*  
→ Result: 61 papers reviewed.  
→ Organized by *imaging modality and model type (Specialist vs. Generalist VLMs).*

**3. Preliminary Information**
**3.1. Primary Medical Tasks:**  with foundation models support:
- **Classification & zero-shot classification** (e.g., CheXNet).
- **Segmentation** (U-Net).
- **Detection** (MedYOLO).
- **Retrieval** (Lehmann et al.).

MLLM - 
- **VQA** (VQA-Med dataset).
- **Captioning & Report Generation** (TieNet, Jing et al.).  
    → These tasks automate diagnosis, enhance reporting, and boost efficiency.

**3.2. Model Architectures:** three major VLM types:
1. **Encoder-based Cross-Modal Alignment** (e.g., CLIP) – separate encoders align images & text.
2. **Encoder-based Multimodal Attention** (e.g., VisualBERT, SimVLM) – joint encoder learns contextual relationships.
3. **Encoder–Decoder Integration** (e.g., Flamingo, VisualGPT) – generative; useful for **report generation** and **image synthesis**.



**4. Foundation Models in Medical Imaging**
**4.1 Specific Domain Transfer Applications**
Grouped by modality:
- **X-ray:**  
    Models like **DeViDe, MedViLL, RoentGen, XrayGPT** enhance classification, segmentation, and automated reporting.
    
- **CT (Computed Tomography):**  
    **3D-CT-GPT, CT-CLIP, Merlin, ProMISe** focus on 3D understanding and report generation using cross-modal alignment.
    
- **Fundus Imaging:**  
    **RET-CLIP, FairCLIP, VisionUnite** improve retinal disease classification, captioning, and fairness in diagnosis.
    
- **MRI:**  
    **MedBLIP, Med-UniC, FM-ABS** handle volumetric MRI data, multilingual reporting, and low-supervision segmentation.
    
- **Other Imaging (Pathology, Ultrasound, Echocardiography):**  
    **QAP, LLaVA-Ultra, GP-VLS, SkinGEN** extend VLMs to pathology slides, ultrasound diagnostics, surgery, and dermatology.
    
**4.2 Multi-Domain Integrated Applications**
- Models such as **Mammo-CLIP** and **T3D** integrate **multi-modality (X-ray + CT + MRI)** for general medical AI systems.
- Aim: *unifying visual-text understanding across imaging types for holistic diagnosis (chẩn đoán toàn diện).*

![[Pasted image 20251026103103.png]]


Proposes a **unified transformer architecture** for image-text tasks using **Prefix Language Modeling (PrefixLM)** — predicts future tokens conditioned on both image and text prefixes.


**Adapting Vision-Language Foundation Models for Next-Generation Medical Ultrasound Image Analysis (2024)**
Shows performance gains in **disease recognition, image captioning, and VQA**.