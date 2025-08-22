[Shannon Entropy Story](https://www.quora.com/What-is-an-intuitive-explanation-of-the-concept-of-entropy-in-information-theory)

![[Pasted image 20241108121850.png]]
Entropy - Measures disorder.
also caleld Shanon Entropy - Measures the uncertainty of a probability distirbution.

Uncertainty mean sth not very predictable. 
+ ? Like 2024 president election (certain, Donal Trump) and the lottery winning number (uncertain).
![[Pasted image 20241108122015.png]]
+ ? **How did one calc the uncertainty and what the unit of uncertainty** even be
  If we look at uncertainty from a diff angle and look uncerstainty at a information standpoint, we could rephrase the question to gain better intuition.
+ $ **How much information (bits), on average, would we need to encode an outcome from the distirbution.** (What we want to proved)
note: the more uncertain you are the more information needed to know the outcome.

![[Pasted image 20241108122449.png]]
With n bits as the prob of an event. 
> The example below show only 1 bit required to send information about the event outcomes: tail 0 or head 1.
![[Pasted image 20241108122616.png]]

Another event, with **8 diffs outcome** so we use **3 bits** because 3 bits is $2^3=8$
![[Pasted image 20241108122727.png]]

For uniform distribution
![[Pasted image 20241108122742.png]]
![[Pasted image 20241108122749.png]]
However we can also show that this formula even holds for **uniform distributions where the number of outcomes is not a power of 2.** 


Assume that we have a distribution with 10 equally likely outcomes four bits give 16 unique states so we could in theory use **four bits to encode every possible outcome** however this is inefficient as it leaves six states left over. **So the average cost to describe a outcome is 4 to 1** (4/1). 
+ ? **Suggestion 1:** To do better we can observe **three separate outcomes and encode the outcomes in groups of three** (e.g. A, A, A) each outcome can be one of ten different states so there are one thousand different possible triples of outcomes ![[Pasted image 20241108123034.png]]
(lý do dùng log mũ 10)
With $2^{10} = 1024$ we can **encode** all 1000 unique states above. What we're saying is that **with 10 bits we can encode three independent outcomes .** However there are **still 24 unused codes.** 
+ $ The **average bits represent an outcome is** 10/3 = 3.333 compare to 4/1= 4 when not seperate to triplet, so it is **more efficient.** 
+ ? Why not use double or more than 3, because **using triples allows us to reach an encoding average closer to the theoretical Shannon entropy value**, achieving greater efficiency. 
	![[Pasted image 20241108143851.png]]
+ ! Though this idea is not completely efficient since we still got 24 unused bits.

**Suggestion 2:** For the **most efficient encoding scheme**, we're looking for the case where $10^{G}= 2^B$ where **$G$ is the possible output can be present using 10 bits.** 
![[Pasted image 20241108142856.png]]
+ ? log conversion  ![[Pasted image 20241108142916.png]]
 

Most distribution is not uniform. But for M outcome (i.e. uniform), each outcome is
![[Pasted image 20241108143004.png]]
+ $ This many needed to encoded the outcome. 
    
>For all M, this is "**the measure of how much information (using binary bits) on average is needed to describe outcomes of a distribution**" it is linked tightly with uncertainty. 
![[Pasted image 20241108143100.png]]
> Since **if we're less certain of an outcome we may need more information to describe.**

---
## Entropy in Short
>**Entropy** is a value represent **Uncertainty**. 
>+ If S = 0, it mean No Suprise -> Certainty about the result/results.
>+ If S = 1, it mean Big Suprise -> Uncertainty about the results.  
![[Pasted image 20250118175824.png]]


### Story of Information Theory: from Morse to Shannon to ENTROPY
At the brink of World War at 1794 (Napoleon)
New invention that can transmit information almost simultaneously.  
**Claude Chappe** -> **encode language for warfare** -> technology that would not be fully resolve for 150 years. 
![[Pasted image 20250812220747.png# left | 333]]
92 symbol encode 92 messages: words, sentences anything the coder desierd.  
- $  But Chappe system go 1 step further instead of coding only 92 primary symbol.  He coded his message into a **set of 2 consecutive symbols.** Which give $92*92=8464$ combination. 
	1 set of **primary** - told the receiver **the page**.  
	1 set for **secondary** - told the **Index of Code on the page** ![[Pasted image 20250812221255.png# left| 500]]
This system would not be resolve for 150 years.>

**Hans Christian Orsted** realize electric current can reflect magnetic needle, use magnet to direct electricity. 
invented **Optical Telegraphy. Electricity** -> being the Age of Electrical Telegraphy. 
![[Pasted image 20250812215721.png# left | 544]]

**Alfred Vail & Morse** found a **way to encode Letter**
	set **Shorter code for more frequent letter and longer code for less frequent letter** -> increase efficient. 
![[Pasted image 20250812220029.png| 544]]

How to automate telegraph ? 
ÉMILE BAUDOT invented an encoding scheme called Bordeaux code. 0
Rather than using a variety set of code, he assigned each letter or number to a fixed 5 bits code, capable of sending 1/32 possibilites. 
![[Pasted image 20250812220407.png# left | 444]]
How ever Baudot code fail to reliazed the redundancy in the information source. Because every letter or number has the same length code (5-bits)

But what **Baudot** give us is th **AUTOMATE**. sending with just a click of the keyboard.  **Provided Instantaneous Global Connectivity.**

But there is
+ No Theory to quantify "INFORMATION", (No definition)
+ No way to find a limit of capacity of the information. (How much a information)
+ No grasp of Noise and Bandwidth.

From 3 possible symbols. Select n consecutive symbols, reference from Chappe system. With **2 consecutive sequence** we got $3*3=9$ possible sequence.  
![[Pasted image 20250812222722.png | 555]]
This would mean **sequence of 4 symbols** would be $3 \times 3 \times 3 \times 3 = 81$ diff symbols. In other word $9^{2}$. THe growthing rate is exponential. 
$3^{5}=  3 \times 3 \times 3 \times 3 \times 3 = 3125$  
  
Consider Chappe's semaphore include 92 possible symbols. For consective selection would give an horrible large number. 
In an Attempt to quantify information, Hartly had observed a monster that grow exponential, that grow out of control. 
![[Pasted image 20250812222405.png| 555]]
For this reason, rather than the raw number of possible sequences, its more sensible to quatify information as its logarithm. 
-> This mean if the number of information go up, information increase linearly, not exponentially. 
![[Pasted image 20250812223542.png| 333]]
Ralph Hartley, the fomula basically say: **Information is the log of all possible sequence** -> this approach count all possible sequences. 

Like languages, there are numerous of ways we can interpret and reorder word and sentences, but only certain of way are chosen. 
![[Pasted image 20250812224520.png| 444]]
this approach count all possible sequences.
 -> Shannon approach consider the likelihood of different sequences occuring. 

**Nguồn gốc của thông tin là gì.** 
He turn the question to the information source and he ask the question where nobody had asked before. **At what rate is the source generated information ?**...this is seperate to asking what capacity a *channel* has. 

Shannon **doesn't see the informatio source as a generator of symbols but a statical process,** each new symbol generated is not independent of the previous symbols. When we count sequences, some are more likely than others. 

Some sentence are use more frequent but some sentence are never occur at all. This can be easily observe in human language, there are numbers of way we can rearrange word, but only a small subset of this combination are commonly used.

Shannon introduce a new perspective, one that considered the Likelyhood of different sequences occuring. Then model a the information source as a Markov process...

Markov Process -> a complex web of interconnected states that transition between each other randomly but according to set probabilistic rules. 
	If this was a language, these rules will be dictated by the normal structure of that language.  
![[Pasted image 20250813012320.png| 555]]

But ANY INFORMATION source has this kind of statistical behaviour. It contains patterns, repetition and redundancy. Out of Shannon's machine came symbols. But how can we measure how much information is being generated ? 

Shannon produced an ideas what would become a funcdamental pillar of not just ML, Information theory, data compression, cryptography, AI, economics and neuroscience. His idea is simple:
	"Information is best measured by the Uncertainty result, not just the number of possible choices."


Học Activation Function sẽ bao gồm Taylor's Series, trong Deep Learning chẳng hạn. 

and generating information.
Hes model the information source as  a Markov Process, where the source is represented as a complex web of interconnected states.  ![[Pasted image 20250812225003.png| 344]]
The language is somehow predictable. 
![[Pasted image 20250812230815.png| 555]]




**"The more often a message is repeated, the less information it contains."**
	Less information than the ‘originally contained’ information in the message. But as noise adds its own ‘information’ the amount of information more than likely increases as it is sent repeatedly. The original message ‘melts’.

![[Pasted image 20250812233005.png | 344]]


Thấy Huân thích ông Shannon , nãy mình video tài liệu về Cách Entropy ra đời hay lắm, nó đi từ lịch sử bắt đầu từ Claude Chappe (ko phải Claude Shannon) ông Chappe đặt nền móng cho mã hóa ngôn ngữ vận dụng trong chiến trường thời napoleon. 

- Ban đầu pháp mã hóa thông tin trên 94 ký tự.
+ Chappe System đề xuất cách mã hóa thông bằng 94 * 94 ký tự trong đó 94 thứ 1 là số trang, 94 thứ 2 là index của từ trong trang đó. 
+ **Nhược điểm:** ko truyền đc xa, do họ cắm 1 cây tín hiệu để truyền thông , dg dài 20 cây số sẽ phải cắm vài trăm cái cọc.

Tiếp đến ông **Hans Christian Orsted**, ôg tìm ra cách điều hướng điện sử dụng nam châm -> khởi nguồn cho Thời Đại Điện Báo (truyền thông tin bằng điện)  -> giúp truyền tin xa hơn.

Bây h vấn đề là làm sao để truyền tin hiệu quả. Alfred Vail và Morse (mã Morse đó) phát minh ra cách Mã Hóa Hiệu Quả dựa trên tần suất của từ, nếu dùng nhiều thì mã hóa ít, dùng ít nhiều mã hóa nhiều hơn. 
+ Note: lúc này mã hóa là bấm máy kêu tít tít á, nghĩa là phải bấm mấy lần mới ra 1 từ, đc nên bấm rất CHẬM. 

-> Cần 1 phương pháp để tự động hóa (ôg kế tiếp phát minh ra máy đánh từ bằng tay. typing machine cổ bấm lạch cạnh ấy)

Ôg này tên là Émile Baudot phát minh ra cách mã hóa các ký tự bảng chữ các sử dụng 5 bits. Từ đó phát minh ra máy đánh tay

Vậy là con người đã phát minh ra cách truyền tin hiệu quả vì mọi từ đã đc mã hóa, Nhưng mình:
+ chưa có Lý thuyết để mô tả THÔNG TIN LÀ GÌ ? định nghĩa của nó ???
+ chưa có cách ĐỊNH LƯỢNG THÔNG TIN ? 1 thông tin là bao nhiêu và bao nhiêu cái gì ??? 
+ Thời này con ng chưa mường tượng đc Nhiễu (truyền thông tin sai) và Băng thông (dữ liệu max có thể truyền tải) là gì ? :)) giống như code á, phải bị bug mới biết. CHÚ Ý: Shannon phát minh ra cái Lý thuyết thông tin thì 2 vấn đề Nhiễu vs Băng Thông mới dần trở nên phổ biến, nếu ko muốn nói là tồn tại. 

Lúc này có 2 người đi vào giải quyết vấn đề này:
+ Ralph Hartley: ông này dùng phương pháp brute force, ông này mã hóa thông tin bằng cách Đặt các Ký Hiệu đại diện cho thông tin liền kề nhau. 
Ví dụ: Ký Hiệu A đại diện cho 3 từ Hè, He, Hẻ. Thì ông này đặt A liền kề A: AA 
Như thế ta sẽ có 3 * 3 = 9 từ. Vậy nếu AAA thì sao ? nó sẽ là 3^3 = 9 -> tăng trưởng theo cấp số Nhân. 
+ Chưa kể Tiếng Pháp nó mã hóa 94 từ trong 1 Ký Tự như ở đầu đã nhắc tới (ông Chappe í) Nghĩa là AAAAAA sẽ đại diện cho 94 * 94 * .... * 94 = số TO LẮM KO MỌI NGƯỜI ƠI. -> Nên là ông Hartley sử dụng LOG để Scale thông tin bé hơn và tốc độ tăng trưởng chậm hơn vì log() scale nó tăng 1 cách tuyến tính.
+  Theo ông Hartley thì "THÔNG TIN LÀ LOG CỦA MỌI CHUỖI TỪ TỒN TẠI", có thể hiểu đơn giản là ông này cố mã hóa mọi từ tồn tại trên thế giới theo kiểu đặt A gồm n từ thì AA sẽ đại diện cho n * n từ.

+ Claude Shannon (bố của CNTT): thay vì chỉ mã hóa, ông đặt câu hỏi là "TỐC ĐỘ MÀ THÔNG TIN  ĐƯỢC TẠO RA TỪ NGUỒN NHƯ THẾ NÀO ?" 

Shannon ko nhìn Nguồn Thông tin như 1 hệ thống sinh Ký Hiệu (i.e. mình tự tạo ra) mà nó là 1 Quá Trình Thống Kê. (như TF-IDF á) trong đó Mọi ký hiệu được tạo ra liền kề với nhau phụ thuộc vào nhau (Ví dụ cho sự phụ thuộc : xin - chào thì việc từ chào đc sinh ra sẽ phụ thuộc vào từ xin rất nhiều)
+ Điều này đúng vì trong ngôn ngữ tự nhiên, có rất nhiều Tổ hợp câu nhưng chỉ 1 số nhỏ tổ hợp con trong tổ hợp đó được sử dụng.

Shannon giới thiệu 1 góc nhìn mới, ôg coi Khả Năng xảy ra (likelihood) của các Trình Tự Câu khác nhau  sử dụng mô hình Markov Process, 1 mạng lưới các nodes và cạnh liên kết với nhau và chuyển đổi giữa  nodes -> nodes 1 cách ngẫu nhiên theo Quy Tăc Xác suất đã đặt ra. (Cơ bản là 1 mạng lưới Xác Suất có mỗi từ 1 một nodes)

Tuy Nhiên, mọi Nguồn Thông Tin đều có hành vi Thông Kê này (đúng vì mọi thông tin đều có thể thông kê  include your mom :)))  và có 1 pattern (khuôn mẫu) 


