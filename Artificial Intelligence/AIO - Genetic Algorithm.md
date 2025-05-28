source: https://aivietnam.edu.vn/blog/giai-thuat-di-truyen#crossover-lai-gh%C3%A9p

Chúng ta biết rằng bài toán hồi quy có thể giải quyết đc sử dụng giải thuật Gradient Descentd. Song song vs đó cũng có rất nhiều giải thuật có thể giải quyết đc bài toán Linear Regression. 
+ ! Trong thực tế, không phải lúc nào ta cũng biết rõ hàm số, nhiều khi ta chỉ biết được hành vi của hàm đó thông qua quan sát giá trị Đầu ra và Đầu vào. ![[Pasted image 20250527134504.png]]
+ ? Làm sao để chúng ta tìm ra 1 kết quả tối ưu kể cả khi không biết hàm số cụ thể của bài toán là gì ? 

Thuật toán di truyền được lấy cảm hứng từ tự nhiên, nói rằng những cá thể không kịp thích nghi sẽ bị đào thải trong khi cá thể thích nghi tốt vs môi trường sẽ tiếp tục phát triển. 
![[Pasted image 20250527134015.png| 600]]
![[Pasted image 20250527134535.png# |600]]

+ $ Thuật toán di truyền có thể hình dung qua bài toán One-Max. Đây là 1 bài toán tối ưu trong đó mỗi cá thể là 1 chuỗi nhị phân (binary array) gồm 0 và 1. Mục tiêu là tìm ra chuỗi có số lượng bit "1" nhiều nhất, trong đó mỗi cá thể (i.e. chuỗi nhị phân) sẽ được chọn lọc dựa trên số lượng "1" trong chuỗi của mình, thông qua quá trình chọn lọc, đột biến và lai ghép, các cá thể sẽ tiến hóa để đạt đc lời giải tối ưu.   

Cách thức hoạt động của thuật toán di truyền, bắt đầu từ khởi tạo quần thể -> đánh giá độ phù hợp của mỗi  cá thể -> phép toán di truyền như chọn lọc (selection), đột biến (mutation) và lai ghép (crossover). 
![[Pasted image 20250527133727.png]]

### Initialization 
Mỗi ô trong 1 hàng (i.e. bộ gen của 1 cá thể ) đại diện của 1 đặc trưng của gen đó.  
![[Pasted image 20250527135824.png]]

### Fitness Evaluation (Đánh giá độ thích nghi)
Để biết bộ gen có thích nghi tốt vs môi trg hay không, ta cần 1 hàm để đánh giá độ thích nghi gọi là Fitness Evaluation. Để xác định đc côg thức của hàm này là rất khó nên ta cần xem xét cụ thể môi trường xung quanh và các yếu tố cần quan tâm ví dụ như môi trường nhiều cây cao nên độ dài cổ của hươu cao cổ phải tăng hay để sinh tồn "chim ăn chuột" loài con chuột có màu sắc gần vs môi trg sống lâu hơn, phù hợp vs điều kiện sống của chúng. 
![[Pasted image 20250527140031.png]]
Nên ta có thể nói:

1. **Fitness Evaluation** khó để xác định, vì `f(x) = High` nếu trong ngữ cảnh chọn lọc của hươu cao cổ, và `f(x) = Color` nếu là loài chuột -> Cần có 1 ngữ cảnh cụ thể ms có thể xác định đc công thức của hàm này. 
2. **Fitness Evaluation** là 1 hàm đánh giá mức độ thích khi, ta có thể dựa vào giá trị đánh giá để giữ lại các cá thể mạnh và loại trừ các cá thể yếu. ví dụ như hàm bên dưới: ![[Pasted image 20250527141353.png]]
### Selection (Chọc lọc)
Đây là cách chọn lọc ngẫu nhiên trong đó các cá thể sẽ được chọn 1 cách Ngẫu Nhiên (ko loại trừ những cá thể đã đc chọn rồi hay chưa) và so sánh giá trị Fitness (i.e. số lượng bit) để chọn ra cá thể Tinh Anh có số lượng "1" nhiều hơn. Quá trình lặp lại đến khi Selection Pool đầy (i.e. n = 5)

![[Pasted image 20250527142021.png# | 500]]


### Crossover (Lai ghép)
Minh họa 2 nhiễm sắc thể trao đổi chéo cho nhau, nghĩa là 1 phần của nst xanh hoán đổi cho 1 phần của nst cam.
![[Pasted image 20250527145845.png]]
Tham khảo từ trên, ta có thể hoán đổi các ô từ 2 cá thể khác thể nhau, nhưng không chỉ dừng lại ở trao đổi 1 điểm mà có thể nhiều hơn như hình sau:
![[Pasted image 20250527150058.png]]

Để quá trình trao đổi chéo trở nên tự nhiên hơn, nghĩa là có thể xảy ra ở bất cứ ô nào trong 1 cá thể ta có thể sử dụng **Phép Lai Đồng Nhất (Uniform Crossover)**, cụ thể là Hoán đổi 2 ô cùng vụ trí với xác suất cho trước ở mỗi vị trí. Tóm lại, thực hiện **lai ghép 1 cách random.** note: giá trị xác suất $\in [0, 1]$ 
![[Pasted image 20250527150631.png]]

### Mutation (Đột Biến)
+ ? Note: Phương pháp hoán đổi giá trị giống Crossover nhưng chỉ áp dụng biến đổi cho 1 cá thể chứ không phải giữa 2 cá thể như ở Crossover. 
**Mục tiêu:** tạo sự đột biến cho cá thể con mới nhằm tạo ra sự đa dạng trong quần thể và tránh mắc kẹt ở các cực trị cục bộ.  
![[Pasted image 20250527152910.png]]

Ở trên là các ví dụ khi thực hiện đột biến: 
+ *Hình 13*, ở cá thể $x_{1}$ bị đột biến ở các ô màu đỏ, vì bài toán của chúng ta giới hạn ở 2 giá trị 1 và 0 nên giá trị 0 sẽ trở thành 1 và ngược lại. 
+ *Hình 14* giá trị $x_{1}$ ban đầu ở vùng cực đại cực bộ (local) nhờ đột biến đã trở thành $x_{1}'$ và nằm ở vùng cực đại toàn cục (global) giúp quá trình tối đa hóa Fitness đạt kết quả tốt hơn.

+ ? Để mô phỏng quá trình đột biến này, ta thực hiện tương tự như bước Crossover bằng cách chọn ngẫu nhiên các giá trị trong khoảng `[0, 1]` cho các vị trí với 1 threshold với điều kiện thực hiện đột biến ở vị trí có giá trị $x_{1} \underline{} mutation$  thấp hơn threshold $mutation \underline{} rate$. ví dụ là mutation_rate 0.5 sẽ chỉ đột biến những vị trí có giá trị thấp hơn 0.05. 
![[Pasted image 20250527153407.png]]

### Termination (điều kiện dừng)
Các tiêu chí để dừng thuật toán:
1) Đạt số thế hệ tối đa (giống như đạt max epoch khi train model)
2) Đặt ngưỡng Fitness (giống như Early Stop condition khi train model)
3) Không có cải thiện (giống như Early Stop nốt, dừng lại nếu sau n epoch ko có cải thiện.)

## Coding Practice
[Read for Guide](https://aivietnam.edu.vn/blog/giai-thuat-di-truyen#thực-hành)

Fitness Score (like Loss Function)
![[Pasted image 20250527154634.png]]

**Psudo Code**
```python
gene_prob & mutation_prob is the probability for each position of the gene across its length.

define genes as a object using OOP
define elitism = 2 # choosing 2 genes randomly for comparison

Selection -> randomly choosing 2 genes -> pick the one with highest fitness score, if even then pick one of them. 
Crossover -> permute features (i.e. 0 & 1) between 2 genes if their crosover_prob  < crossover_threshold.
Mutation -> permute gene if any gens mutation_prob  < mutation_theshold.
```

