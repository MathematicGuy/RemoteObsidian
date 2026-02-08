NL reveals that components like optimizers and attention mechanisms are actually associative memory modules that compress information at different frequencies

**Nested Learning, a new approach to machine learning that views models as a set of smaller, nested optimization problems, each with its own internal workflow**, in order to mitigate or even completely avoid the issue of “catastrophic forgetting”, where learning new tasks sacrifices proficiency on old tasks
	nested optimization problems -> not 1 system, but a system of interconnected (multi-level learning with each level optimized a problem), that are optimized simultaneously. 

Complex **ML model** is actually *a set of coherent, **interconnected optimization problems nested within each other** or running in parallel.* Each of these internal porblems has its own context flow - its own distinct set of infor which it is trying to learn. 

**Deep Learning work by compressing their internal context flows.** allowing to build model with deeper computational depth. 

**Inspiration**
+ Human brain adapts through **neuroplasticity** - a term to describe the remarkable capacity to **change its structure in response to new experiences**, memories and learning. 
+ **Associative memory - the ability to map and recall** one thing based on another (e.g. recalling a name when u see a face, where "name" & "face" are pairs of unrelated items)


In the training process itself, specifically the *backpropagation process*, can be modeled as an *associative meory.* **The model learns to map a given data point to the value of its local error**, serve as a measure of how "Suprising" or unexpected that data point was.  
	
+ ? What does it mean to say "The model learns to map a given data point to the value of its local error"
	*"mapping a data point to its local error"* means the model is actively trying to associate **"This specific input"** with **"The mistake I made on it."**
		By *updating the weight* ($W_{t+1}$), the models is *"storing" the connection between the Specific input data and that "Error" its causes* -> By using the Weight, next time the model sees that data point (Key), it recalls the correction (Value) to adjust its behaviour. 
	-> **Weight store Connection of (Input (Key) -> Error (Value))** in a neural network. 
	
+ ? What "Local Error" mean ? 
		*Local Error is the "measure of suprise"*  (like loglikelihood loss function) -> Thus high loss/error also mean high level of unpredictable/suprise) where the "local" term say this "Error" is calculated the specific error comming back from  from the next layer. 
		
	+ **Low Surprise (Entropy)** -> The predicting datapoint is purfect, gradient (error) is zero ->  nothing to memorize to update.
		   
	+ High Surpise if the prediction is wrong, the gradient is large. 
	
+ @ **The Associative Mapping:** The goal of the training process is to treat the **input (x) as a Key** and this **gradient term ($\nabla$) as a Value**

Nested Learning paradigm *reframe the training process* of an entire deep neural network with backpropagation *as a system of parallel optimization problems* **where each layer learns to map its specific input to its specific 'local surprise signal $\nabla \mathcal{L}$'** making the entire network a collection of these processes. 
![[Pasted image 20260102215707.png | 655]]
	HOPE fills the gap with multiple blocks that update at different **frequencies**:
	**Fast Blocks:** Update every few tokens, capturing immediate context.
	**Medium Blocks:** Update every few thousand tokens.
	**Slow Blocks:** Update over millions of tokens, capturing global trends.
	
The model uses a **"self-referential"** process where it *generates its own learning rates and weight decays, effectively learning how to learn.* 

Treats optimizer as something that can learn from its own memory/history. The optimizer become the learner itself. 

The previous layer refine the next layer, its like having a mind where each layer watching & improve the one below. Just like how human learn, we don't just stop at understanding the information but keep on refining it. 

Titan (base model) - only remember what "suprise & forget the rest", it update infor only in 2 layers and limited to first-order thinking. 

HOPE - the model that learns to learn. *Automatically learns what to keep, what to remember and what to forget.* Example of memory refinement:
+ ? How the Titans model behave ? Also Inspired by the human brain, its prioritize storing its mark as important, in other word, titan remember what is "suprise" and forget what is routine or didn't match it expectation. This make Titan expecially good at remembering unexpected event and information while forget the usual/routine one.
	just like how our brain remember special/unusual event than normal one.  
		
Titan big limitation are its only learn at 2 levels, store knowledge at level 1 and slightly adjusted it knowledge in level 2. And have fixed update rules like other deep learning model.  
-> This is where **HOPE (Hierarchical Optimizing Processing Ensemble)** come in 
Hope keeps Titans’ “surprise-based memory,” but adds **self-modification**. 

Note: 
Give Visual Example of Nested Learning - explain it a perspective, ie. we see MLP in nested learning perspective. 
+ ? After pre-explain so the have the core ideas what They will need to understand. Dive Deeper 
	Part 1 What is Associate Memory
	Part 2 Momentum as memory for gradient
	Part 3 Titan: A Self-Referential Module with Continuum Memory
	Part 4 CMS & M3 Algorithm
	Part 5 Experiments result 
Note: Used the Nested Learning Author Inforgraphic as slide reference.
Reference Slides: 
+ [Notebook LM very detail slide](https://youtu.be/-Z_EWSw32sA?si=HoDR985QeezQXsUc) - [[NL Slide 1]]
+ [The Author Ali Behrouz  ppt slide](https://www.youtube.com/watch?v=3WqZIja7kdA) - [[NL Slide 2]]


----
## Insights from the Author - [video source](https://www.youtube.com/watch?v=uX12aCdni9Q)
Original DL Perspective see the output. Nested Learning perspective see the learning process. 

The Gradient create by different Architecture can affect the Optimization process -> Cannot use 1 Optimizer for all model. Diff optimization for Diff architecture. 
	e.g. cannot train a transformer using Gradient Descent -> doesn't perform well. The Hessian create by transofmrer is very complicated compare to regular MLP block. 

*New data change the Loss landscape,* so if the model doesn't have long-term memory it can't see the Global landscape to find the optimal solution. 

Used Nested Learning to design more powerful architecture

**Titans**
every components (e.g. LR) is generated by the model itself and it learning end to end.
generate its own value. the value is not a projection of data anymore, it generated by the memory itself. 

----

## Nested Learning Facebook explain
NESTED LEARNING (paper gần đây của Google) hoạt động như thế nào và tại sao lại được gọi là "Attention is all you need 2.0" ?

--------------------------------

Attention là cơ chế cốt lõi nằm sau gần như tất cả các sản phẩm GenAI hiện nay. Vì vậy để được gọi là Attention 2.0 thì phải là một thứ gì đó rất vuýp.

Lần đầu đọc qua thì mình cũng chưa hiểu sao nó được mệnh danh xịn như vậy, chắc do mình ngu ![😅](https://static.xx.fbcdn.net/images/emoji.php/v9/t53/1/16/1f605.png) Giờ có thời gian đọc kĩ hơn và xem các papers liên quan thì cũng hình dung được rõ hơn.

Nested Learning giúp thay đổi cách chúng ta hiểu về Deep Learning trước giờ, chứ nó không phải là phiên bản nâng cấp của Attention hay Transformer.

Bài báo này rất hay, tuy nhiên cũng cần thêm thời gian để xem Nested Learning có thật sự xứng đáng là Attention 2.0 không. Bởi vì tên gọi này được xuất phát từ các trang truyền thông chứ không phải từ chuyên gia trong ngành. Kết quả thí nghiệm thì Nested Learning tốt hơn các baselines khác không quá nhiều. Nếu so với Titans (tiền thân của Nested Learning) thì Nested Learning chỉ nhỉnh hơn 0.7-1.3% accuracy trên các benchmarks.

---- Giải thích đơn giản về Nested Learning ----

![⛓️‍💥](https://static.xx.fbcdn.net/images/emoji.php/v9/tdf/1/16/26d3_200d_1f4a5.png) VẤN ĐỀ

Nếu bạn đã từng finetune một mô hình và thấy nó quên sạch những gì đã được train trước đó, thì đây là 1 vấn đề thường gặp của DL, gọi là catastrophic forgetting (tạm dịch: học trước quên sau). Ví dụ:

- 1 con LLMs đã được pretrain bằng dữ liệu tiếng Anh

- Sau đó bạn finetune nó cho tập dữ liệu tiếng Việt

- Thì đúng là nó sẽ xử lý tiếng Việt giỏi hơn thật, nhưng cái giá phải trả là nó quên luôn phần đã học với tiếng Anh. Chúc mừng bạn! ![🥳](https://static.xx.fbcdn.net/images/emoji.php/v9/t6d/1/16/1f973.png)

Chúng ta đã có nhiều mẹo để giảm thiểu vấn đề này (mẹo thật chứ ko phải mẹo mày bé) như: experience replay, architectural tweaks, PEFT, regularizations, optimizers, ... nhưng chẳng thứ nào thực sự giải quyết được vấn đề gốc.

=> Ta có Nested Learning

![💡](https://static.xx.fbcdn.net/images/emoji.php/v9/t3c/1/16/1f4a1.png) Ý TƯỞNG CHÍNH

Thông thường trong deep learning, chúng ta tách biệt ba thành phần: mô hình (model), thuật toán huấn luyện (optimizer), và dữ liệu (data). Mô hình học các biểu diễn (representations), optimizer chỉ đơn thuần cập nhật trọng số.

Nhưng tác giả kêu không!

Tác giả nhìn neural network dưới góc độ là một hệ thống gồm nhiều bài toán tối ưu lồng vào nhau (nested optimization problems). Mỗi thành phần trong mô hình (từ attention, MLP cho đến momentum của optimizer, ...) được xem như một learner có:

- context flow riêng (dòng thông tin mà nó quan sát)

- tần suất cập nhật riêng (update frequency)

- và do đó là một dạng associative memory học bằng cách nén dòng bối cảnh của chính nó

Những thành phần cập nhật nhanh tạo thành các fast learners, còn các thành phần cập nhật chậm hơn nằm ở các tầng "outer levels". Khi ta sắp xếp tất cả theo tần suất cập nhật, toàn bộ quá trình huấn luyện hiện ra như một hệ thống nhiều tầng học tập ở các time-scales khác nhau, thay vì một vòng tối ưu duy nhất như ta thường nghĩ trong deep learning

Bạn có thể tưởng tượng như này:

Con người chúng ta có thể học một cái gì đó rất nhanh bằng trí nhớ ngắn hạn, hiểu sâu một chủ đề sau vài tuần bằng trí nhớ trung hạn, và nhớ mãi kiến thức nền tảng qua nhiều năm bằng trí nhớ dài hạn. Nested Learning áp dụng cơ chế tương tự:

- các tầng nhanh học lập tức từ ngữ cảnh hiện tại

- các tầng chậm cập nhật ít hơn, giữ lại các kỹ năng và tri thức cốt lõi

=> Nested Learning có thể học thêm mà không phá vỡ kiến thức đã có, giải quyết catastrophic forgetting

![🪄](https://static.xx.fbcdn.net/images/emoji.php/v9/tb5/1/16/1fa84.png) TẠI SAO NESTED LEARNING LẠI QUAN TRỌNG

Cách nhìn này làm thay đổi toàn bộ cách ta hiểu về deep learning. Từ trước đến nay, ta luôn coi:

- mô hình là một cấu trúc kiến trúc cố định

- optimizer chỉ là công cụ cập nhật trọng số

- quá trình huấn luyện là một vòng lặp gradient descent duy nhất

Nested Learning chỉ ra rằng deep learning không hề học theo một tốc độ duy nhất, mà được tạo thành từ nhiều hệ thống học nhỏ bên trong, mỗi hệ thống có:

- bộ nhớ riêng

- thời gian phản ứng riêng

- mục tiêu tối ưu hóa riêng

Góc nhìn này giúp giải thích vì sao LLM có khả năng in-context learning, vì các tầng “nhanh“ đang học theo thời gian thực ngay trong lúc mô hình chạy inference.

Đồng thời nó cũng giải thích vì sao các mô hình hiện tại khó học liên tục: vì phần “học chậm” (slow learners) gần như đóng băng hoàn toàn sau pre-training.

Lúc đọc xong hiểu được rõ hơn 2 vấn đề cảm giác lên đỉnh luôn mọi người ạ ![😆](https://static.xx.fbcdn.net/images/emoji.php/v9/td4/1/16/1f606.png)

![🔑](https://static.xx.fbcdn.net/images/emoji.php/v9/tad/1/16/1f511.png) NESTED LEARNING HOẠT ĐỘNG NHƯ NÀO

Tác giả định nghĩa một khái niệm quan trọng: update frequency, là số lần một thành phần được cập nhật trên mỗi token. Dựa trên tần suất này, toàn bộ mô hình được phân tầng thành:

- Level 1 (nhanh nhất) — attention, momentum, fast learners

- Level 2 — linear projections, FFN

- Level 3 — outer optimizer

- ...

Mỗi level tương ứng với một bài toán tối ưu riêng, có context flow riêng, và gradient flow riêng.

Các thành phần nhanh nén thông tin chi tiết, còn các thành phần chậm nén các xu hướng dài hạn. Nhờ đó:

- mô hình có thể thích ứng ngay lập tức (giống in-context learning)

- mô hình vẫn duy trì trí nhớ lâu dài (long-term storage)

- mô hình có thể học liên tục mà không quên

Cái hay ở đây là Nested Learning không sửa lại kiến trúc neural network hay đề xuất cấu trúc mạng mới, mà nó sửa lại cách ta hiểu mô hình trong DL.

![🤩](https://static.xx.fbcdn.net/images/emoji.php/v9/t58/1/16/1f929.png) 4 ĐÓNG GÓP CHÍNH CỦA PAPER

I. Deep Optimizers: optimizer chính là một memory module

Trong Nested Learning, tác giả xem optimizer là một "associative memory module" (tạm dịch: bộ nhớ nhanh), bởi vì:

- Momentum optimizer: thực chất là một cơ chế ghi nhớ lịch sử gradient (nó lưu lại thông tin của các gradient trước đó và dùng chúng để dự đoán bước đi tiếp theo)

- Adam optimizer: thực chất là bộ nhớ 2 tầng (tầng 1: ghi nhớ hướng trung bình của gradient (giống Momentum), tầng 2: ghi nhớ độ biến thiên của gradient để điều chỉnh bước nhảy)

- Update của momentum chính là một bước mini-optimization, nghĩa là trong mỗi bước train thông thường, có những tối ưu hóa nhỏ xảy ra bên trong.

Nhận ra điều này, tác giả mở rộng theo 3 hướng:

(a) Tăng sức biểu diễn của optimizer:

Thay vì dùng momentum dạng vector/matrix, họ thay bằng MLP. Họ gọi biến thể này là Deep Momentum Gradient Descent (DMGD) (mình thấy ý tưởng này cũng đã gặp tương tự ở 1 số papers khác rồi)

(b) Dùng loss tốt hơn cho tối ưu hóa bên trong optimizer:

Thay vì tối ưu dot-product (dẫn tới Hebbian updates, dễ nhiễu), tác giả dùng L2 regression (nhận định này mình cũng đã từng đọc qua ở 1 số papers khác rồi)

(c) Cho optimizer phi tuyến hóa đầu ra

Tác giả chỉ ra rằng nếu ta áp Newton–Schulz iteration lên momentum, ta thu được một optimizer tương đương với Muon optimizer (2024)

=> Điều này chỉ ra rằng Muon (là 1 optimizer đang rất hot) hóa ra chỉ là một trường hợp đặc biệt của nested memory

II. Self-Modifying Titans — mô hình học cách tự cập nhật chính nó

Tác giả cho rằng mô hình cũng có thể học cách học: nó không chỉ sinh ra output, mà còn sinh ra cả update rule để tự sửa đổi trọng số của chính nó. Ý tưởng này dựa trên kiến trúc Titans (2024), nhưng được làm rõ và mở rộng mạnh hơn dưới góc nhìn Nested Learning.

Ý tưởng chính: mô hình tự tạo ra bản vá lỗi cho chính nó

Trong kiến trúc này, mỗi bước xử lý token sẽ có hai dòng tính toán song song:

1. Dòng dự đoán (prediction path)

- nhận input

- sinh ra output như mô hình thông thường

2. Dòng tự-cập nhật (self-update path)

- nhìn vào trạng thái hiện tại

- sinh ra một "tuỳ chỉnh" (delta-weights)

- áp dụng những thay đổi này vào chính mô hình

- chạy ở tốc độ chậm hơn (slow learner)

Đây là một dạng test-time learning nội bộ, không cần loopy backprop hay fine-tuning.

Self-Modifying Titans có 2 đặc tính mà Transformer bị thiếu:

- Học ngay trong lúc inference (test-time learning): trong mỗi forward pass, mô hình vừa dự đoán vừa tự cập nhật => khả năng thích nghi mạnh hơn

- Không phá vỡ kiến thức cũ: nhờ cơ chế slow/fast learners. Điều này là tiền đề cho continual learning đến từ nội tại bên trong model, chứ không phải đến từ bên ngoài như trước giờ.

III. Continuum Memory System (CMS)

Hiện nay, LLM có 2 dạng memory:

- Short-term memory (context window): bốc hơi ngay khi bạn nhấn enter, không thể tích lũy tri thức theo thời gian

- Long-term memory (model weights): ổn định lâu dài hơn, nhưng bị đóng băng sau pretraining, không thể cập nhật thêm khi chạy inference

Tức là mô hình chỉ sống được trong:

- giây phút hiện tại (context window)

- hoặc quá khứ xa xôi (pre-training)

Còn tất cả những gì diễn ra giữa hai điểm đó đều bị lãng quên.

=> CMS được sinh ra để sửa điều này.

Ý tưởng chính: sử dụng nhiều tầng MLP, mỗi tầng học theo tần suất khác nhau

Thay vì chỉ 1 MLP trong mỗi block (như Transformer), tác giả xây dựng một chuỗi MLP, mỗi MLP:

- có update frequency riêng

- được cập nhật theo những “chunk size” khác nhau

- đại diện cho một mức độ trừu tượng khác nhau

Kiểu như này:

MLP(f1), MLP(f2), …, MLP(fk)

Trong đó:

- f1 = nhanh nhất (cập nhật gần như liên tục)

- fk = chậm nhất (chỉ cập nhật khi đủ thông tin)

Mỗi tầng MLP là một learner ở một level khác nhau, mỗi learner có context flow riêng và gradient flow riêng (không chia sẻ như backprop truyền thống)

IV. HOPE: Kiến trúc hợp nhất Self-Modifying Titans + CMS

HOPE được xây dựng bằng cách kết hợp cơ chế tự sửa đổi (từ Titans) với một hệ thống bộ nhớ liên tục (CMS), và dùng các optimizer sâu (Deep Optimizers) để học các cập nhật này. Để dễ hiểu hơn thì bạn có thể xem HOPE như là một sequence model, có khả năng học liên tục, thích nghi theo thời gian, và không quên kiến thức cũ, ngay cả trong lúc inference.

HOPE có 3 thành phần chính:

1. CMS

- Là xương sống của HOPE, gồm nhiều tầng MLP, mỗi tầng có update frequency khác nhau. Cơ chế của CMS giúp HOPE ko bị quên đi kiến thức cũ như mình đã giải thích ở mục III.

2. Các projection động (dynamic projections)

Khác với Transformer dùng Wq, Wk, Wv cố định, HOPE:

- cập nhật các projection dựa trên context

- cho phép mô hình điều chỉnh cách nó nhìn vào dữ liệu

- giúp long-context reasoning mạnh hơn

Cái dynamic projection này được lấy nguyên từ Titans - nơi key/value/query không cố định mà có thể điều chỉnh theo context.

3. Self-Modification: HOPE tự học cách cập nhật chính nó

Từ Titans, HOPE kế thừa cơ chế tự-cập nhật:

- mô hình sinh ra delta-weights

- áp dụng lên các lớp chậm (slow learners)

- không phải thông qua backprop truyền thống => giúp HOPE học luôn trong lúc inference

4. Deep Optimizer

HOPE không dùng các optimizer kiểu cũ như SGD/Adam, mà dùng Deep Optimizer (DMGD) được giới thiệu ở mục I.

![🔬](https://static.xx.fbcdn.net/images/emoji.php/v9/t7e/1/16/1f52c.png) KẾT QUẢ THỬ NGHIỆM

HOPE vượt qua Transformer++, RetNet, DeltaNet, và vượt cả Samba và Titans (2 kiến trúc rất mạnh hiện nay) trên nhiều benchmarks khác nhau trong NLP. Tuy nhiên performance gap cũng không quá lớn