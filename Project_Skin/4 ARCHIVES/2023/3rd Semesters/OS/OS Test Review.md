**1. Consider a computer system that has cache memory, main memory (RAM) and disk, and the operating system uses virtual memory. It takes 2 nsec to access a word from the cache, 10 nsec to access a word from RAM, and 10 ms to access a word from the disk. If the cache hit rate is 95% and memory hit rate (after a cache miss) is 99%, what is the average time to access a word?**

access:
	**C**ache: 2**ns** 
	**R**AM: 10**ns**
	**D**isk: 10**ms** ->  10 000 000**ns** (vì 1ms  = 10^6ns)
**(chr)** cache hit rate: 95% (0.95)
**(mhr)** mem hit rate (after a cache miss): 99% (0.99)

**Fomular**
> **Average time = (chr * C) + (1 - chr) * (mhr * R + (1 - mhr) * D)**
-> (0.95 * 2) + (1 - 0.95) * (0.99 * 10 + (1-0.99) * 1000000)
-> 5002.395 **ns**

hitC + (miss) * (hitR + missD)

>**Unit**: 1s = 10^3 (ms)
>			= 10 ^ 6  (us)
>		= 10 ^ 9 (ns)
>		*Fig 1.7*
>		![[Pasted image 20230720095416.png]]


**2. How long will it take to electronically scan the text for the case of the master copy being in each of the levels of memory of *Fig. 1-7*? For internal storage methods, consider that the access time given is per character, for disk devices assume the time is per block of 1024 characters, and for tape assume the time given is to the start of the data with subsequent access at the same speed as disk access**

total char = 700 * 50 * 80 = 2tr800 characters.
total block = 2_800_000 / 1024 = 2734.375 

(làm tròn lên để đủ dung lượng cho file chạy)
Register -> 2800 000 (ns) or 2.8 (ms)
Cache: -> 5.6 ms (vì gấp 2 lần register)
RAM -> 28 ms
Magnetic disk -> 2735 * 10ms = 27350 (ms) -> 27s
Tape = 27 * 10 ^ 6 = 27 000 000 s

> Price: why the top is expensive: 
>Volatility (mất dữ liệu khi thiếu nguồn điện): phía trên là non-voltility (register, cache, ram), còn disk là volatility.


**3. A computer system has enough room to hold four programs in its main memory. These programs are idle waiting for I/O half the time. What fraction of the CPU time is wasted?**

**Important Fomula**
> **CPU Utilization = 1 - p^n**. 
> trong đó **n là số tiến trình**, 
> ***p %** là thời gian cho I/O*
> -> **p ^ n là % hao phí**
>p = 0,5 và n =4 -> p^n = (0,5)^4 = 0,0625 hay 6,25%


 **4. A computer has 2 GB of RAM of which the operating system occupies 256 MB. The processes are all 128 MB (for simplicity) and have the same characteristics. If the goal is 99% CPU utilization, what is the maximum I/O wait that can be tolerated?**

> 1GB = 1024mb
> 1mb = 1024kb
> 1kb = 1024b
> 1b = 8bits 

8Mbps, 128Mbps. 
 OS occupied 256mb, Processes are 128mb
 Tính n = (2 * 1024 - 256)/128 = 14
	Khi đó 0,99 = 1 - p^14 -> p = (0,01)^(1/14) ~ 0,72 hay 72%.
	**p^n** -> Wasted time.

#### Trong hai bài trên, (p^n) I/O wait time đgl wasted time.  

**5. Five batch jobs A through E, arrive at a computer center at almost the same time. They have estimated running times of 10, 6, 2, 4, and 8 minutes. Their (externally determined) priorities are 3, 5, 2, 1, and 4, respectively, with 5 being the highest priority. For each of the following scheduling algorithms, determine the mean process turnaround time. Ignore process switching overhead.
	(a) Round robin. (6, 8, 10, 2, 4)
	(b) Priority scheduling.
	(c) First-come, first-served (run in order 10, 6, 2, 4, 8).
	(d) Shortest job first.
> Mục đích thuật toán là tối ưu thời gian chạy trước sau giữa các chương trình. (Cái nào bật/tắt trước sẽ tối ưu hơn)

**For (a), assume that the system is multiprogrammed, and that each job gets its fair share of the CPU. 
For (b) through  (d) assume that only one job at a time runs, until it finishes. All jobs are completely CPU bound.*

*For each of the following scheduling algorithms, determine the mean process turnaround time.*
**nên thời gian của Cái chạy sau bị ảnh hương bởi Cái chạy tr'c vì phải quay đầu lại**

**(a) [Round Robin](https://www.geeksforgeeks.org/program-for-round-robin-scheduling-for-the-same-arrival-time/)
**For (a), assume that the system is multiprogrammed, and that each job gets its fair share of the CPU** nghĩa là *Cái nào chạy thì chạy xong mới thôi. Thời gian trung bình thì lấy thời gian Burst (hoàn thành) của 1 chu trình cộng lại là đc*

(total time taken) Task: left-over runtime.
Gọi thời gian chung **Time Quantum là 1**, ta có **round-robin chạy theo thứ tự theo thứ tự giảm xuống (10, 8, 6, 4, 2)** là:
**(10) - For round robin, during the first 10 minutes, each job gets 1/5 of the CPU.
(10) - At the end of the 10 minutes, C finishes. 
(18) - During the next 8 minutes, each job gets 1/4 of the CPU, after which time D finishes.
Then each of the three remaining jobs get 1/3 of the CPU for 6 minutes, until B finishes and so on.**
	The finishing times for the five jobs are 10, 18, 24. 28, 30, for an average of 22.2 minutes.
![[Pasted image 20230923174458.png]]
**A at 30p:** (10/5 + 8/4 + 6/3 + 4/2 + 2/2) = 2 + 2 + 2 + 2 + 2 = 10
#### How to compute below times in Round Robin using a program
- ****Completion Time:**** Time at which process completes its execution.
- ****Turn Around Time:**** Time Difference between completion time and arrival time. ****Turn Around Time = Completion Time – Arrival Time****
- ****Waiting Time(W.T):**** Time Difference between turn around time and burst time.   
    ****Waiting Time = Turn Around Time – Burst Time****


**(b) Priority scheduling.**
(thay 3,5,2,1,4 )
Thứ tự chạy được xác định theo thứ tự ưu tiên với số 5 là ưu tiên cao nhất: 
**3 (A), 5(B), 2(C), 1(D), 4(E)**
**B -> E -> A -> C -> D**
B = 6
E = 6+8=14
A = 14 + 10 = 24
C = 24 + 2 = 26
D = 26 + 4 = 30
-> (6 + 14+24+26+30)/5 = 220


**(c) First-come, first-served (run in order 10, 6, 2, 4, 8).**
A = 10 
B = 16
C = 18
D = 22
E = 30
**(A+B+C+D+E)/5 = 19.2
-> Thứ tự là: A -> B -> C -> D -> E là 19.2**

**d) c ->  d -> b -> e ->  a** 
> thời gian chạy tương ứng: 10 ,6, 2, 4, 8 là (a,b,c,d,e) 
>  vậy c ->  d -> b -> e ->  a 
	Thời gian chạy:
	C : 2
	D = 2 + 4 = 6
	B = 6 + 6 = 12
	E = 12 + 8 = 20
	A = 20 + 10 = 30
		thời gian trung bình: (2 + 6 + 12 + 20 + 30)/5 = 70/5 = 14.






