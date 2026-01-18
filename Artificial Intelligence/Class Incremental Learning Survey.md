Note: _Preliminary: The process of finding out what there is to find out_. 
**Context**
*In Classical ML*, all training data arrive at the same time.
	In detail, traditional ML assume data distribution is static and IID.

*In Incremental Learning (IL),* training data come in sequence or in number of steps, and the distribution of data shift/ overtime as new data arrived (like real world stream of continous data).
<-> IL is not i.i.d (independent and Identically Distribution - Độc lập và phân phối đồng nhất). *violation of the IID assumption is what leads* to "Catastrophic Forgetting (CF)".
-> Solve CF allow model to continously learn new data no matter their distribution is. 

To understand Class-Incremental Learning better, let go through 3 types of Incremental learning. 
![[Pasted image 20260112142639.png]]
**Class-Incremental Learning**
In [[class-incremental learning]], an algorithm must incrementally learn a set of clearly distinguishable tasks. **After training on each Task, it'll be tested on all of the class it have learned before.** 
	For example, task 1 (10 classes) -> test on 10 classes, continuous trainning on task 2 (10 classes) -> test on 20 classes (10 classes form task 1 + task 2) 
	
Detail Explaination:
	training data come in sequence instances with *each Task doens't contain overlapping class $Y_{b} \cap Y_{b}' = \varnothing$.* After each task, the trained model is evaluated over all seen classes in task $b$ $(Y_{b} = Y_{1} \cup \dots Y_{b})$  CILM aim to fit a model $f(x): X \to Y_{b}$ over all class b.
	. 
	Note: If $Y_{b} \cap Y_{b}' \neq \varnothing$ then it Blurry CIL where old classes emerge in new tasks, this allow model to revision old knowledge ie. classes, which weaken the learning difficulty. 
**Difficulty:** Hardest. Model's params is limited, to learn new object mean to forget old object. The problem is how to minimize the loss of learning new (plasticity) while not forgetting the old task (stability), in other word, how to teach the model learned only what is important.    
**Math:** $f(x) \to Y_\text{all}$​ (where $Y_\text{all}​=Y_{\text{task1}}​ \cup Y_{\text{task2}}$)
**Real-world Example:** Google Photos, it learn to recognize your face at 15 years old, few years later you add a lot animal & people to your Photos gallary, but google photos still need to recognize the 15 years old you instead of other people or animal.   

**Task-Incremental Learning**
Training Task come in sequence like Class-Incremental Learning, **tested classes define only within a specific task.** 
	For example, task 1 have "Bird and Dog" class -> only test for "Bird and Dog" class. task 2 have Tiger and Fish class -> only test on task 2's Tiger and Fish class.  
	
This method often apply *TIL in Multi-Head architecture*, so *each Head classified a different task Domain*:
- **Separate Heads:**
    - **Head 1:** Has 2 output buttons: [Bird, Dog].
    - **Head 2:** Has 2 output buttons: [Tiger, Fish].
	
- **The Switch:** When you give the `Task ID`, you are essentially flipping a switch that **turns off** Head 2. The model literally cannot press the "Tiger" button because that part of the network is deactivated for this inference. 
+ **CIL Comparision:** if CIl also use Multi-Head, all heads would be active at once because it trying to predict all classes it have learned. 
**Difficulty:** Easiest. Because the model already given half the answer bc their search space is much smaller, it don't have to worry about guessing wrong among 100 of classes like CIL. 
**Math:** $f(x,t)$ $\to Y_t$​ (predict label y given input x and task t)
**Real-world Example:** Like how human minimize the problem scope, an Object Detection App with TIL will only search the Plant Domain when you open Plant_Detection feature, so that inference is faster and never accidentally a Plant as a Person (bc no Person include the Plant searching domain). 

**Domain-incremental learning**
Training come in sequence like CIL and all Tasks have the *same class/label (Dog)* but they're come from *different domain (e.g. Real Life Dog and Cartoon Dog).* 
	For example:
	**Step 1 (Task 1):** You teach the model to recognize **Dogs** vs. **Cats** using **Photographs**.
    _Classes:_ [Dog, Cat]. _Domain:_ Photos.
	.
	 **Step 2 (Task 2):** You teach the model to recognize **Dogs** vs. **Cats** using **Cartoons/Sketches**.
    _Classes:_ [Dog, Cat]. _Domain:_ Cartoons.
    .
	**Step 3 (The Test):** You show the model a **Pencil Sketch** of a Dog.
    - **The Challenge:** You ask: _"Is this a Dog or a Cat?"_
    - **The Options:** Still just **Dog** or **Cat**.
	 
**Difficulty:** Medium. *Model learn on pattern*. But a Sketchy *circle pattern is far different from a furry ball,* except for the round edge -> Hard to Generallize bc the round edged (of the circle & ball) is the only pattern, so the model have *Few pattern to learn*.   
**Math:** $P(X)$ changes (input distribution shifts), but $P(Y | X)$ remains stable (a stop sign is still a stop sign).
**Real-world Example:** Teach the model to predict pedestrian & traffic sign in snowy Norway (Domain 1: Snowy) and pedestrian & pedestrian in sunny England (Domain 2: sunny). 

Bonus: Blurry CIL mean the model get to revision, this mean old classes from old task get added to new task (this call classes overlapping, bc 2 task have the same class), which help mitigates CF. (kind of like replay)

**Detail Example**
![[Pasted image 20260118160950.png]]

| Scenario                    | Intuitive description                                                                                                                                                  | Mapping to learn      |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| Task-incremental learning   | Sequentially learn to solve a number of distinct tasks                                                                                                                 | $f: X \times C \to y$ |
| Domain-incremental learning | Learn to solve the same problem in different contexts                                                                                                                  | $f: X \to y$          |
| Class-incremental learning  | The model sees only X. To get the answer right, it effectively must predict **both** the Context (C or "which task group this belongs to") and the specific label (y). | $f: X \to C \times y$ |
Note: $X$ is the input space, $y$ is the within-context output space and $C$ is the context space. 

---

## Replay
Exempler: a set of hard to predict samples used to re-train (1 tập các mẫu khó dự đoán được đưa vào để train lại để model ôn lại bài). 
	Basically a hard to predict subset from old data put in a memory buffer waiting for re-train -> help model learn old data that its forget.

**(a) Choosen from hard to predict old task (ie. high entropy old task) as exempler to replay.** 
![[Pasted image 20260118174129.png]]

**Làm sao để biết dữ liệu nào có entropy cao ?**
Noise (dữ liệu hỏng)
	Ảnh quá mờ, che khuất
	Label sai
	Model dự đoán kiểu: P(mèo)=0.33, P(chó)=0.34, P(khác)=0.33
	
OOD (out-of-distribution)
	Ảnh không giống dữ liệu train
	Ví dụ:
		train X-ray phổi → gặp ảnh CT○
		train mèo/chó → gặp ảnh hoạt hình○
		--> Model “hoang mang” → entropy cao vì không hiểu gì cả
	
Vì sao không nên replay ?
	Replay noise → làm model học lệch.
	Replay OOD → phá ranh giới đã học.
	

**(b) Detect sample with high Entropy by Augment "high entropy old data":** 
+ $ **Main Idea:** Sau khi Augment thì dữ liệu nào biến đổi nhiều nhất (ie. accuracy giữa các mẫu sau khi  khác nhau nhiều nhất)
+ ? 1 mẫu khó là mẫu dẫn tới Loss cao chỉ với 1 thay đổi nhẹ -> Có thể tính cường độ thay đổi của 1 mẫu sử dụng data Augment và so sánh Entropy của mẫu tr'c và sau khi Augment có thay đổi nhiều không.   
Workflow Chi tiết:
	Augment mẫu cũ -> thực hiện dự đoán trên các mẫu augment -> Tính Mean Accuracy trên các mẫu augment (dùg để tính Entropy) ->  So sánh Entropy của mẫu  vs Entropy trung bình của các mẫu agument (dùng để tính Điểm tương đồng) -> Điểm tương đồng giữa mẫu tr'c và sau khi đc augment (Mutual Information) -> Ranking tìm mẫu có Điểm tương đồng. 
![[Pasted image 20260118175541.png]]
**Ý tưởng cốt lõi** Một mẫu thật sự khó thì: “Chỉ cần thay đổi nhẹ ảnh $\to$ model đổi ý”
	Với 1 ảnh x, tạo nhiều bản:
		crop nhẹ
		rotate vài độ
		thay đổi brightness
		blur nhẹ 
	Cách chọn exemplar
		Chạy model trên tất cả bản augment
		Nếu dự đoán dao động mạnh → mẫu uncertain.

**(c) Greedy Selection - chọn sao cho đa dạng**
**Main Idea:** chọn Gradient khác biệt nhất so với mẫu gốc, bằng cách so sánh Gradient của từng mẫu so với mẫu gốc và loại dần. 
![[Pasted image 20260118182542.png]]
Ý nghĩa trực giác
	Gradient = “nếu học mẫu này, model sẽ bị kéo theo hướng nào”•
	Hai mẫu có gradient giống nhau → học cái này hay cái kia gần như giống hệt•
	Hai mẫu có gradient khác nhau nhiều → học hai “kiểu kiến thức khác nhau”


**(d) Reservoir Sampling** (**CHECK LATER**, *something not right)*
Intuition: Reservoir by nature definition is a natural lake whose outlet has been dammed to control the water level. Bring this ideas to Computer Science, we have memory buffer as the dam (đập thủy điện) and data stream as the water source, in which, a set of old data are selected randomly across timestep store in the memory buffer for replay.

Step by step example: 
Note: Each sample in datastream are add by timestep to the memory buffer (until the buffer is full).
0) If Buffer is empty then add sample by timestep t.
	Else memory buffer is full (*Timestep start at 3*)
At timestep 4 
	sample at index 1 will have P = 3/4 = 0.75 
	sample at index 2 at P = 3/3 = 0.6
	...
	sample at index 4 at P = 3/7 = 0.6
	
1) draw *index* $j \sim \text{Uniform} \{1,...,t\}$ from the datastream. Where the probabity of $j$ in the datastream is Uniform probability (ie. t=4 -> P(t=1,2,3,4) = 1/4). 
2) If index $j$ is smaller than Memory Buffer size, then replace value at timestep $t$  with value at index $j$,   

+ ? When "Discard sample t from the memory buffer", does sample m go back to the Datastream ?
	+ $ if yes, then **memory buffer is limited to the first 3 index. And each value only get replayed one.** -> Prioritize replay only the first task ? 
		If yes then Datastream need to be updated so new data could get at timestep t. This mean Discard sample t will discard a sample from The Datastream. So New data could be replace provide that j < K which is hard enough for Uniform distribution at 1/100. 
	+ if no then all sample in the datastream will shift.
+ ? In Fairness prob, if refer to all sample in memory buffer -> prob for Discard ? if so then the prob for Discard get smaller as time go on.
![[Pasted image 20260118183148.png]]
**Vấn đề**
	Dữ liệu đến liên tục (stream)
	Không biết “task 1 kết thúc ở đâu, task 2 bắt đầu ở đâu”
**Reservoir sampling làm gì ?**
	Giữ bộ nhớ kích thước cố định
	Mỗi mẫu mới có xác suất ngẫu nhiên được giữ
	Mẫu cũ có thể bị thay thế
**Kết quả:**
	Bộ nhớ là mẫu ngẫu nhiên, công bằng theo thời gian•
	Gần như i.i.d. sample toàn bộ stream
	
Note: Task-boundary là TIL (Task-Incremental Learning) vì search domain đc thu hẹp trong 1 task (chỉ test các class ở trong 1 Task nhất định), ngược lại là CIL là ko có Task-Boundary vì nó test trên mọi class đc học mỗi khi train 1 task mới mà ko thu hẹp prediction domain trong task nào.


