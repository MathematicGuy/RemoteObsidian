---
annotation-target: BookOS-exercises.pdf
---

**2 MODE**
+ **Kernel mode: điều hành trực tiếp vs phần cứng (bit-0)**
	Cấp thấp -> Gần với phần cứng hơn 
+ **User mode: điều hành với giao diện người dùng (bit-1)**
	 Cấp cao -> gần với người dùng. 

## [[OS Test Review]]


## Memory Abtraction

- Địa chỉ Logic Luôn > Địa chỉ Vật Lý
	Địa chỉ ảo có thể đc chỉ sinh ra. Sau đó trở thành địa chỉ 

Cần nhiều thuật toán để chuyển đổi địa chỉ LOGIC sang VẬT LÝ.
##  Exercise Chapter 3: Memory Management

**physical address**: vị trí thực trong bộ nhớ chính
**logical address**: vị trí độc lập đối với vị trí thực. Có thể là  Kí hiệu, dấu hiệu để
chỉ vị trí thực.
**address space:** là tập hợp các địa chỉ. Giống 1 cái rương, có thể dùng để định bị trong bộ nhớ.
**address tranlation:** ánh xạ từ địa trị này sang (chiếu tới)  1 địa chỉ khác.  
**overlay:**  trong bộ nhớ chỉ giữ lại những lệnh hoặc địa chỉ cần thiết, còn lại sẽ đc giải phóng (dispose)
**swapping:** 1 tiến trình được lưu tạm vào bộ nhớ phụ, sau đó có thể sẽ đc nạp lại vào bộ nhớ chính để tiếp tục quá trình thực thi. 
**external fragmentation:**  
	kích thước cấp pháp bộ nhớ đủ đáp ứng yêu cầu. Tuy nhiên bộ nhớ ko liên tục.
**internal fragmentation:** 
	*vụn vặt bên ngoài* ám chỉ số bộ nhớ còn thừa khi cấp pháp 1 lượng bộ nhớ lớn hơn cần thiết
*-> VD: Cấp khoảng trống 18.464 bytes cho 1 tiến trình yêu cầu 18.462 bytes*
**Hole: một khối nhớ khả dụng** 
-> làm sao để cấp phát bộ nhớ đủ lớn cho 1 tiến trình có độ lớn n.

**3.1**
	10 KB, 4 KB, 20 KB, 18 KB, 7 KB, 9 KB, 12 KB và 15 KB.
	Yêu cầu: (a) -> (b) -> (c)
**Quét toàn bộ dãy** 
Với **first-fit** : (cái này đáp ứng trước thì ấy tr'c) 
	**< Chọn khối nhớ trống phù hợp đầu tiên (first) kể từ đầu bộ nhớ. Bộ nhớ đc chọn sẽ không đc chọn lại >**
(a) 12Kb -> 20Kb 
(b) 10Kb -> 10 Kb (Không chọn 20kb vì A đã đc cấp)
(c) 9Kb  -> 18Kb (Khôg chọn )
Với **best-fit** : (chọn cái gần đúng ) 
	**< Chọn khối nhớ trống vừa và nhỏ nhất, tìm kiếm trên toàn bộ nhớ >** 
	12Kb -> 10Kb -> 9Kb (Vừa với bộ nhớ mà bé nhất, gần đúng) 
với **worst-fit** 
	**< Chọn khối nhớ trống lớn nhất nhất, tìm kiếm trên toàn bộ nhớ >**
	20Kb -> 18Kb -> 15Kb (vừa với bộ nhớ mà có dung lượng lớn nhất)
với **next-fit** (tới rồi thì sẽ không quay lại nữa)
	**<Chọn khối nhớ trống phù hợp đầu tiên kể từ vị trí cấp pháp cuối cùng>**
	 *Duyệt các phần tử trong dãy và lấy từng giá trị cho từng lỗ nhớ 1.*
	 (a) 12Kb -> 20Kb
	(b) 10Kb -> 18Kb (vì 20 đc quét rồi nên bắt đầu quét tiếp từ 18, vì 18 thỏa mãn nên lấy luôn)
	(c) 9Kb -> 9Kb 

**Disk-defrag** 
	Dồn các ổ cứng còn trống lại cho nó gần nhau hơn (cập nhật nhanh hơn)

**3.: tìm địa chỉ vật lý với địa chỉ ảo tương ứng**
	tìm số hiện tại trong khoảng địa chỉ ảo nào. Khi tìm ra tính địa chỉ vật lý tương ứng.  
**(a) Địa chỉ ảo 20 thì địa chỉ vật lý là bao nhiêu?**
Biết 1 ô chứa 4096 địa chỉ
	ô đầu tiên: 0, 1, 2,...20,...4096 giá trị

**Địa chỉ ảo 20 nằm ở ô đầu tiên (đánh số 2, ô 0k- 4k) theo hình vẽ thì ô này tương ứng với ô (8k-12k) bên địa chỉ vật lý.**
ô 8k có giá trị 8192
20 có địa chỉ ảo là 20
=> địa chỉ vật lý tương ứng là:  8212

**Địa chỉ ảo 4100 nằm ở ô thứ hai (đánh số 1, ô 4k-8k) theo hình vẽ thì ô này tương ứng với ô (4k-8k) bên địa chỉ vật lý.**
ô 4k có giá trị 4096
=> địa chỉ vật lý tương ứng là:  4196 (vì 4100 - 4000 = 100)

**Địa chỉ ảo 8300 nằm ở ô thứ ba (đánh số 6, ô 8k-12k) theo hình vẽ thì ô này tương ứng với ô (24k-28k) bên địa chỉ vật lý.**
ô 4k có giá trị 24576 (= 8192 * 3)
vì 8192 tương ứng với 24576 
<=> 8300 tương ứng với 108 + 24576 = 24684 (vì 8300 - 8192 = 108)
=> địa chỉ vật lý tương ứng là:  24684
**(8192 là 24576 thì 8300 sẽ là (8300 - 8192 = 108 + 24576 = 24684))**

**Bài 3.4**
**Page Replacement Algorithms**
**(a) Thuật toán NRU (Not Recently Used),**
*(Đưa 1 thằng ra để đưa 1 thằng khác vào, 0 - ko ưu tiên; 1 - ưu tiên)*
Dựa vào vào các bit R (reference) và bit M (modified), các bit càng bằng 0 thì càng dễ được chọn
-> page 2 sẽ đc chọn làm nạn nhân vì cả hai bit R, M đều = 0 ( page này chưa được dùng)

**(b) Thuật toán FIFO (First-In First-Out): dựa vào thời gian quét**
-> Trang đầu của danh sách sẽ đc thay thế. (như tên gọi)

**LRU là thuật toán được dùng nhiều nhất ->  thực tế nhất**
**(c) Thuật toán LRU (Least Recently used): dựa vào lần cuối đc dùng tới (last reference**)
-> thay thế trang chưa đc dùng lâu nhất. (Ít đc ưu tiên nhất)

**(d) Thuật toán second chance: kết hợp FIFO + NRU**
Điểm yếu: Chạy thằng đc ưu tiên trước. Và phần tử khi lấy ra tr'c mà ko đc ưu tiên sẽ bị cho ra ngoài -> Ko hiệu quả

R = [0; ko ưu tiên], [1; được ưu tiên]
	+ FIFO -> page 3 
		Nếu theo NRU thì page 3 có cả bit R, M đều =  1 -> page 3 đc dùng nhiều  -> ko chọn làm nạn nhân
	+ FIFO -> page 0
		nếu theo page 0 có bit R = 1 ->  Ko đc chọn làm nạn nhân.
	+ FIFO -> page 2
		page 2 có cả bit R, M đều = 0 -> ko được dùng nhiều -> đc chọn làm nạn nhân

Bài 7:
1. $free -m
	![[Pasted image 20230810114846.png]]
1. $cat/proc/meminfo
	see what in the file
2. $vmstat -s
3. $top
4. $htop
5.  "#hmidecode -t 17 "
## [[OS Chap4-FILE SYSTEMS]]


note: Bài thầy chữa sẽ có trong bài thi.
**4-29. A UNIX file system has 1-KB blocks and 4-byte disk addresses. What is the maximum file size if i-nodes contain 10 direct entries, and one single, double, and triple indirect entry each?**
Số địa chỉ mà mỗi block có = 1KB / 4byte = 1024byte / 4 byte = 256 byte
- Địa chỉ trực tiếp (direct): 10
- Địa chỉ gián tiếp 1 mức (single): 256
- Địa chỉ gián tiếp 2 (double): 256^2 = 65_536
- Địa chỉ gián tiếp 3 mức (triple): 256^3 = 16_777_216
- Tổng số địa chỉ = 10 + 256 + 65_536 + 16_777_216 = 16_843_018(KB) ~ 16BG

**4-32. How large is the block size, if the maximum partition size is 128 MB and the FAT type is FAT-16?**
Vì định dạng là FAT-16 -> tổng số địa chỉ = 2 ^ 16 = 65_536 địa chỉ
Mà tổng dụng lượng phân vùng = 128mb 
-> block size = 128mb / 65_536 = 128  * 1024KB / 65_536 = 2(KB)

**4-34. Which FAT type is used, if the maximum partition size is 256 MB and the block size is 4KB?**
Tổng số địa chỉ = 256MB / 4KB = 256 * 1024KB / 4KB = 65_536 -> FAT-16

# 5.2 Disks
![[Pasted image 20230912100637.png]]
> Tìm thông tin được tìm trên cylinder.
+ Seek time: searching time

**5.22. Disk requests come in to the disk driver for cylinders 10, 22, 20, 2, 40, 6, and 38, in that order. A seek takes 6 msec per cylinder moved. How much seek time is needed for** 
	**In all cases, the arm is initially at cylinder 20.**

**(a) First-Come, first served. (Ghi chi tiết)** 
	*Đi từ đầu đến cuối không quan trọng điểm bắt đầu là điểm nào.*
	VD: Bắt đầu từ tầng 20. quay lại tầng 1, đi lên lại. (vẫn điểm bắt đầu là tầng 20 )
20 -> 10 : 10
10 -> 22 : 12
22 -> 20 : 2
20 -> 2   : 18
2 -> 40   : 38
40 -> 6   : 34
6 -> 38   : 32 
Tổng số cylinders = 10 + 12 + 2 + 18 + 38 + 34 + 32 = 146 (số lần )
=> ĐS  = 146 *  6 = 876 (ms)

**(b) Closest cylinder next.**
	*(Tại Cylinder hiện tại) Chọn Cylinder có khoảng cách gần nhất* 
20 -> 22 -> 10 -> 6 -> 2 -> 38 -> 40
Tổng số cylinder: 2 + 12 + 4 + 4 + 36 + 2 = 60 
ĐS: 60 * 6 = 360 (ms)

**(c) Elevator algorithm (initially moving upward)**
	*Giống như khi đi thang máy, Đi lên hết rồi mới xuống đón lần lượt các tầng ở dưới. (Trạng thái đang đi lên)* 
Thang máy đi lên: 20 -> 22 -> 38 -> 40 -> 10 -> 6 -> 2
Tổng số cylinder = 2 + 16 + 2 + 30 + 4 + 4 = 58
ĐS: 58 * 6 = 348 (ms)

**(Bonus) Modified Elevator algorithm - upward**
	*Chỉ đón khách khi đi lên, thang máy đi xuống dưới cùng rồi mới đi lên đón khách*
20 -> 20 -> 22 -> 38 -> 40 -> 2 -> 6 -> 10
Tổng số Cylinder =  + 2 + 16 + 2 + 38 + 4 + 4 = 66
ĐS: 66 * 6  = 396 (ms)

**5-27. The clock interrupt handler on a certain computer requires 2 msec (including process switching overhead) per clock tick. The clock runs at 60 Hz. What fraction of the CPU is devoted to the clock?**

Vì đồng hồ chạy đc 60Hz: 1 giây (1000 ms) sẽ dao động 60 lần. Mà máy tính yêu cầu chạy 2ms / tick 
ĐS = 2 * 60/1000 = 0.12 hay 12%
	Khi làm bài nên đổi về Hz. Vì Hz đổi về giây

**5-28. A computer uses a programmable clock in square-wave mode. If a 500 Mhz crystal is used, what should be the value of the holding register to achieve a clock resolution of 
(a) a millisecond (a clock tick once every millisecond)? 
(b) 100 microseconds?**
*Ghi nhớ: 1sec = 10^3 milisec = 10^6 micro sec = 10^9 nano sec*

Máy tính 500 Mhz hay 500 * 10^6 (Hz) = 5 * 10^8 (Hz)
-> Thời gian xử lý = 1/5 * 10^8(s) = 2 (ns)
(a) A milisecond: 1ms = 10^6 (ns) -> Value = 10^6 / 2 = 500 000 
(b) 100 micro second = 100 * 1000 (ns) = 100 000 (ns) -> Value: 100 000 / 2 = 50 000  

**5-37. Assuming that it takes 10 nsec to copy a byte, how much time does it take to completely rewrite the screen of an 80 character x 25 line text mode memory-mapped screen? What about a 1024 x 768 pixel graphics screen with 24-bit color?**

Mất 10 ns để sao chép một byte dữ liệu, nếu sử dụng:
	->Text mode screen: tổng số byte dữ liệu = 80 * 25 = 2000 (bytes)
	-> Mất 20 000 (ns) hoặc 20 (micro-second)
	-> Graphic mode screen: tổng số bytes dữ liệu = 1024 * 768 * 24/8 = 2 358 296 (bytes) -> 23 592 960 (s) ~ 24 (ms)

# DEADLOCK
*> Máy bị treo, tài nguyên không cấp đc nữa. Không chạy đc, tắt đc.*
> Giải quyết vấn đề Deadlock (Tắc nghẽn)
1. **Mutual Exclusion (loại trừ lẫn nhau)**: Mỗi tài nguyên chỉ 1 người dùng, 1 tiến trình để tránh bị xung đột.
2. **Hold and Waitd:** giữ các tài nguyên không cho 1 tiến  hết
3. **No Preemption:** tài nguyên bị (1 tiến trình) giữ không thể lấy lại
4. **Cicular wait:** tiến trình giữ tài nguyên và chờ tài nguyên của 1 tiến trình khác, tạo thành 1 vòng lặp.

## Phát hiện và Điều chỉnh
+ **E (Hiện có) **
+ **A (Sẵn sàng)**
+ **C (Cấp phát)**
+ **R (Yêu cầu)**
![[Pasted image 20230912112950.png]]
Bước 1: So sánh A vs R. Kiểm tra theo hàng
(2 1 0 0) vs các hàng của R.
	Nếu == thì nghĩa là R3 (row3) trả lại tài nguyên: A' = A + C3 = (2 2 2 0) khôgn bằng thì 
![[Pasted image 20230912113350.png]]
-> R2 xong trả lại tài : C' + C2 = (2 2 2 0) + (2 0 0 1) = (4 2 2 1)
Chạy hết dãy (của ma trận) thì sẽ không còn deadlock

def found(result, c):
	R1 = (a +  c1) 
	R2 = R1 + C2
	R3 = R2 + C1
## Phòng tránh tự động
![[Pasted image 20230912114235.png]]
*So sánh A với từng hàng (theo tiến trình đề bài) trong ma trận Needed rồi cộng A với từng hàng trong ma trận Assigned*
1) A = (1 0 2 0) [so sánh vs các hàng D ma trận Needed (0 0 1 0)]
- D chạy xong: A' = A + (1 1 0 1) = (2 1 2 1) [Cộng D ở ma trận Asssigned (1 1 0 1)]

2) A = (2 1 2 1) [so sánh vs các hàng E trong ma trận Needed (2 1 1 0)]
E chạy xong A' = (2 1 2 1) + (0 0 0 0 ) = (2 1 2 1)

Lặp lại Quá trình ta có  đc A' lần lượt là
![[Pasted image 20230912122318.png]]