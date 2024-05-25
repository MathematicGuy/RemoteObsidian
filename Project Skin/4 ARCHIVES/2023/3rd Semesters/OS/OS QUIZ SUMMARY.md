(Only Essay Problems)
note: 
a > b (a có kí hiệu b)

---
## METRIC UNITS
Mili -> Micro -> Nano -> Pico (**x10^(-3)** each iteration)
Kilo -> Mega -> Giga -> Tera  (**x10^(3)** each iteration)

**1.12/ Consider a computer system that has cache memory, main memory (RAM) and disk, and the operating system uses virtual memory. It takes 2 nsec to access a word from the cache, 10 nsec to access a word from RAM, and 10 ms to access a word from the disk. If the cache hit rate is 95% and memory hit rate (after a cache miss) is 99%, what is the average time to access a word?*

+ Extract data: **Cache > C, RAM > R, Disk > D, chr, mhr**
+ Fomula:  **Average time = (chr * C) + (1 - chr) * (mhr * R + (1 - mhr) * D)**


**1.11/ An alert reviewer notices a consistent spelling error in the manuscript of an operating systems textbook that is about to go to press. The book has approximately 700 pages, each with 50 lines of 80 characters each. How long will it take to electronically scan the text for the case of the master copy being in each of the levels of memory of Fig. 1-7? For internal**

![[Pasted image 20230921095031.png]]
+ Calc Word count
+ 1 Block scan 1024 chars
Total block needed to scan -> Total_Block =  Word_count / Block
Use ms meter for disk, so that we can convert to sec later.

**Main mem = tổng ký tự * access time**
**Disk với Tape cứ lấy số khối * access time**

**2.3/ computer system has enough room to hold four programs in its main memory. These programs are idle waiting for I/O half the time. What fraction of the CPU time is wasted?**

Key Info: **four program (4), haf the time (0.5)**
fomula: **p ^ n** (% wasted times)


**2-4. A computer has 2 GB of RAM of which the operating system occupies 256 MB. The processes are all 128 MB (for simplicity) and have the same characteristics. If the goal is 99% CPU utilization, what is the maximum I/O wait that can be tolerated?**

Convert GB to MB quantity 
1mb = 1024GB
-> n = total mem/128 (n = total process time )
**CPU utilization = 1 - p^n**


**5. Five batch jobs A through E, arrive at a computer center at almost the same time. They have estimated running times of 10, 6, 2, 4, and 8 minutes. Their (externally determined) priorities are 3, 5, 2, 1, and 4, respectively, with 5 being the highest priority. For each of the following scheduling algorithms, determine the mean process turnaround time. Ignore process switching overhead.
	(a) Round robin.
	(b) Priority scheduling.
	(c) First-come, first-served (run in order 10, 6, 2, 4, 8).
	(d) Shortest job first.
For (a), assume that the system is multiprogrammed, and that each job gets its fair share of the CPU. 
For (b) through (d) assume that only one job at a time runs, until it finishes. All jobs are completely CPU bound.**
Same Goal: Find which running-order optimized the most.

**(a) Round robin.**
*Gọi thời gian chạy (tối đa) cho mỗi chu trình là* **Time Quantum**
**Mỗi chu trình chạy lần lượt. Dù chưa chạy xong cũng phải chuyển thời gian chạy cho chu trình khác.**
VD:
+ **T1 cần 20s để hthanh. T2 cần 5s. Time Quantum là 5.**  
+ **Chạy T1 còn thừa 15s. Do T1 chưa chạy xong đưa vào Queue. Chạy T2, T2 chạy xong**
+ **Do T1 là chu trình duy nhất trong Queue. Tiếp tục chạy T1 cho đến hết.**
*For Round Robin that each job gets its fair share of the CPU* :
(1/2) T1 at the First second: 1/2
(20/2) After the first 20 second, T1 burst. Giving T2 the rest of the CPU
(1/2) T2 at the 21 second
(5/2) After 5 second, T2 Burst. Ending at 26 second total.
To the Average run time is: (26 + 21) / 2 = 47/2 = 23.5 second
#### Cách tính thời gian
- *Completion Time:* Time at which process completes its execution.
- *Turn Around Time:* Time Difference between completion time and arrival time.
- *Turn Around Time = Completion Time – Arrival Time*
- *Waiting Time(W.T):* Time Difference between turn around time and burst time.   
    *Waiting Time = Turn Around Time – Burst Time*

**(b) Priority scheduling.**
Thứ tự chạy được xác định theo thứ tự ưu tiên với số 5 là ưu tiên cao nhất: 

**(c) First-come, first-served (run in order 10, 6, 2, 4, 8).**
(Chạy theo thứ tự, đến tr'c chạy tr'c)

**(d) Shortest job first.**
(Cái nào chạy mất ít thời gian thì chạy tr'c)

## Exercise Chapter 3: Memory Management

![[Pasted image 20230921202948.png]]
**Quét toàn bộ dãy, khối nhớ đc chọn sẽ không đc chọn lại** 

+ **first-fit** : (cái này đáp ứng trước thì ấy tr'c)  **Chọn khối nhớ trống phù hợp đầu tiên (first) kể từ đầu bộ nhớ.**
+ **best-fit** : (chọn cái gần đúng ) 
	**< Chọn khối nhớ trống vừa và nhỏ nhất, tìm kiếm trên toàn bộ nhớ >** 
+ **worst-fit** 
	**< Chọn khối nhớ trống lớn nhất nhất, tìm kiếm trên toàn bộ nhớ >**
+ **next-fit** (tới rồi thì sẽ không quay lại nữa)
	**<Chọn khối nhớ trống phù hợp đầu tiên kể từ vị trí cấp pháp cuối cùng>**

**Disk-defrag** 
	Dồn các ổ cứng còn trống lại cho nó gần nhau hơn (cập nhật nhanh hơn)

![[Pasted image 20230921220811.png]]
**Tìm số hiện tại trong khoảng địa chỉ ảo nào. Khi tìm ra tính địa chỉ vật lý tương ứng.**
*Bên ảo cộng thêm bao nhiêu thì bên vật lý cũng bấy nhiêu*

**(a) Địa chỉ ảo 20 thì địa chỉ vật lý là bao nhiêu?**
**Địa chỉ ảo 20 nằm ở ô đầu tiên (đánh số 2, ô 0k- 4k) theo hình vẽ thì ô này tương ứng với ô (8k-12k) bên địa chỉ vật lý.**
*(0K bên ảo và 8k bên vật lý có giá trị tương ứng là:  8212 (Vì 0K ~ 8K, nên 8K + 20 = ) 

**(b) Địa chỉ ảo 4100 nằm ở ô thứ hai (đánh số 1, ô 4k-8k) theo hình vẽ thì ô này tương ứng với ô (4k-8k) bên địa chỉ vật lý.**
*(Địa chỉ vật lý tương ứng là:  4100(vì 4K ~ 4096. Ít hơn bên ảo 4 đơn bị nên 4096 + 4 = 4100)*

**(c) Địa chỉ ảo 8300 nằm ở ô thứ ba (đánh số 6, ô 8k-12k) theo hình vẽ thì ô này tương ứng với ô (24k-28k) bên địa chỉ vật lý.**
*(8192 là 24576 thì 8300 sẽ là (8300 - 8192 = 108 + 24576 = 24684))*


![[Pasted image 20230921222204.png]]

**Page Replacement Algorithms**
**(a) Thuật toán NRU (Not Recently Used)
*Lấy page chưa được dùng nhiều. cả R, M == 0* -> Page 2

**(b) Thuật toán FIFO (First-In First-Out): dựa vào thời gian quét**
***Dựa vào thời gian Load*** **-> Page 3**

**(c) Thuật toán LRU (Least Recently used): dựa vào lần cuối đc dùng tới ít nhất (last reference)**
	LRU là thuật toán được dùng nhiều nhất ->  thực tế nhất
***Dựa vào Last Ref thấp nhất(reference)*** -> Page 1


**(d) Thuật toán second chance: kết hợp FIFO + NRU**
***Quét lần lượt các Page, Nếu tìm đc Page đạt ĐK R,M == 0 thì lấy. Dừng chạy.***


**4-29. A UNIX file system has 1-KB blocks and 4-byte disk addresses. What is the maximum file size if i-nodes contain 10 direct entries, and one single, double, and triple indirect entry each?**
*Số địa chỉ mà mỗi block có = 1KB / 4byte = 1024byte / 4 byte = 256 byte*
*single indirect = block ^ 1
double indirect = block ^ 2
n indirect = block ^ n*
**Maximum file size = direct entries + single indirect + double indirect + n indirect + ...(if exist)**

**4-32. How large is the block size, if the maximum partition size is 128 MB and the FAT type is FAT-16?**
*FAT -> Tổng số địa chỉ (Block Size) = 2 ^ 16 (KB)*
**Block_size = maximum partition size / block size** (= 128 * 1024 / 65_536 = 2 (KB))

**4-34. Which FAT type is used, if the maximum partition size is 256 MB and the block size is 4KB?**
*2 ^ n. Số mũ n là FAT type: FAT-n*
256 * 1024 = 262_144 / 4 = 65536 (2 ^ 16) => FAT-16

**5.22. Disk requests come in to the disk driver for cylinders 10, 22, 20, 2, 40, 6, and 38, in that order. A seek takes 6 msec per cylinder moved. How much seek time is needed for** 
	**In all cases, the arm is initially at cylinder 20.**

Tính Tổng thời gian đi từ Cylinder này đến Cylinder khác. 
VD: 20 -> 10 = 10
	10 -> 22 = 12
Tổng = 10 + 12 = 22

**(a) First-Come, first served. (Ghi chi tiết)** 
*Cái nào đứng trước thì quét trước*

**(b) Closest cylinder next.**
*(Tại Cylinder hiện tại) Chọn Cylinder có khoảng cách gần nhất* 

**(c) Elevator algorithm (initially moving upward)**
	*Như đi thang máy, Đi lên hết rồi mới đi xuống để đón khách* 

**(d) Modified Elevator algorithm - upward**
	*Chỉ đón khách khi đi lên* (Nếu muốn đón khách thì luon phải xuống tầng dưới cùng)

**5-27. The clock interrupt handler on a certain computer requires 2 msec (including process switching overhead) per clock tick. The clock runs at 60 Hz. What fraction of the CPU is devoted to the clock?**
*60Hz: 1 giây (1000 ms) sẽ dao động 60 lần* 
What fraction of the CPU is devoted to the clock: 2 * (60 / 1000) = 0.12

**5-28. A computer uses a programmable clock in square-wave mode. If a 500 Mhz crystal is used, what should be the value of the holding register to achieve a clock resolution of 
(a) a millisecond (a clock tick once every millisecond)? 
(b) 100 microseconds?
*Ghi nhớ: 1sec = 10^3 milisec = 10^6 micro sec = 10^9 nano sec = 10^12 pico sec* 
*Mhz -> Hz = 10^6*
500 Mhz -> 500 * 10^6 = 5 * 10^8 -> Thời gian xử lý: 1/5 * 10^8 = 2 (ns) (1 Clk Tick)

**(a) a millisecond (a clock tick once every millisecond) ?** 
mili -> ns / 2 
**(b) 100 micro seconds ?**
100 micro -> 100 000 ns / 2 = 50 000

**5-37. Assuming that it takes 10 nsec to copy a byte, how much time does it take to completely rewrite the screen of an 80 character x 25 line text mode memory-mapped screen? What about a 1024 x 768 pixel graphics screen with 24-bit color?**
s -> mili s -> micro s -> ns -> ps

Số Bytes: 80 * 25 = 2000
Time to rewrite screen: 10 * 2000 = 20 000 (ns)

24-bit -> 24 / 8  = 4 bytes
Time to rewrite screen: 4 * 1024 * 768 * 10 = 23 592 960


**5-27. The clock interrupt handler on a certain computer requires 2 msec (including process switching overhead) per clock tick. The clock runs at 60 Hz. What fraction of the CPU is devoted to the clock?**
note that second -> ms : 1 / 1000
clock interrupt on a certain computer requires 2 msec. So in 1 sec it take up: 2 * 60 / 1000 = 0.12 %