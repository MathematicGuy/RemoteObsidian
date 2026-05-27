





![[Pasted image 20250318081532.png]]
### 📊 **Phân tích Heatmap của PCA Components**

#### **1️⃣ Ý nghĩa của biểu đồ**

- Biểu đồ này cho thấy **mức độ đóng góp (loadings)** của các feature (`total_spending`, `total_quantity`, `total_orders`, `avg_unitprice`) vào **hai thành phần chính (PC1 & PC2)** sau khi thực hiện PCA.
- Giá trị **màu đỏ đậm** (dương cao) → Feature có ảnh hưởng mạnh đến thành phần PCA đó.
- Giá trị **màu xanh đậm** (âm cao) → Feature có ảnh hưởng mạnh nhưng theo chiều ngược lại.
- Giá trị **gần 0 (màu xanh nhạt)** → Feature ít ảnh hưởng đến PC.

#### **2️⃣ Nhận xét về PCA Components**

🔹 **PC1 (Principal Component 1)**

- **total_spending (0.63)** và **total_quantity (0.63)** → Hai feature này có ảnh hưởng mạnh đến PC1.
- **total_orders (0.44)** → Cũng có đóng góp đáng kể vào PC1.
- **avg_unitprice (-0.0015)** → Gần như không ảnh hưởng đến PC1.

✅ **Kết luận:** PC1 chủ yếu đại diện cho **tổng chi tiêu và tổng số lượng sản phẩm mua**, phản ánh **quy mô mua sắm của khách hàng**.

🔹 **PC2 (Principal Component 2)**

- **avg_unitprice (0.998)** → Feature này có ảnh hưởng **gần như tuyệt đối** lên PC2.
- **total_spending (0.029)**, **total_quantity (0.0084)**, **total_orders (-0.05)** → Ảnh hưởng rất nhỏ đến PC2.

✅ **Kết luận:** PC2 chủ yếu đại diện cho **giá trung bình của sản phẩm (`avg_unitprice`)**, phản ánh **mức giá trung bình của các đơn hàng khách hàng mua**.

#### **3️⃣ Ý nghĩa phương sai của PCA**

📌 **Explained variance ratio:**

- **PC1 chiếm 55.51% tổng phương sai**, tức là nó giữ lại hơn **một nửa thông tin quan trọng** từ dữ liệu gốc.
- **PC2 chiếm 25.03% tổng phương sai**, chủ yếu đại diện cho `avg_unitprice`.
- **Tổng phương sai của PC1 + PC2 là 80.54%**, nghĩa là 2 thành phần này giữ lại **80.54% thông tin từ dữ liệu gốc**, đủ để phân tích mà không mất quá nhiều thông tin.

✅ **Kết luận:** PCA đã giúp giảm chiều dữ liệu từ 4 xuống 2 mà vẫn giữ được **80.54% thông tin quan trọng**, giúp việc phân cụm khách hàng và trực quan hóa dễ dàng hơn.

- **PC1 đại diện cho quy mô chi tiêu của khách hàng (`total_spending`, `total_quantity`)**.
- **PC2 đại diện cho mức giá trung bình của sản phẩm khách hàng mua (`avg_unitprice`)**.
- PCA đã giữ lại **80.54% thông tin quan trọng** với chỉ 2 thành phần, giúp giảm độ phức tạp của dữ liệu.



![[Pasted image 20250318081537.png]]



![[Pasted image 20250318081541.png]]



![[Pasted image 20250318081545.png]]
+ The box represent the median (middle 50%) of the data.
+ The line extending from the box (wiskers) show the range of the data excluding outliers. 
+ Each box divide into 4 part. the bottom part represet the 25% user,  

 
![[box-plot-explained.gif]]
Giá trị nhỏ hơn PC1 thể hiện khách hàng mua hàng có giá trị thấp hơn so vs trung bình.
Giá trị nhỏ hơn PC2 thể hiện khách hàng mua ít hàng vs tổng chi tiêu thấp hơn trung bình.

Râu Đỉnh - giá trị cao nhất
Râu Đáy - giá tị thấp nhất 
Upper Part -> 25% of data is > than this value 
Lower part mean 25% of data < than this value 
Outlier - mean they're less than 3/2 value of the upper-lower quartile 

For example given `[5, 7, 8, 12, 14, 18, 21, 23, 24, 26, 30]`, 
+ Median (middle value) is 18
+ Lower half (before median): `[5, 7, 8, 12, 14]` -> Q1 is 8 (middle)
+ Upper half (after median): `[21, 23, 24, 26, 30]`  -> Q3 is 24. 

IQR (Interquarile range) - between Upper Quartile Q3 and Lower Quartile Q1 calculated by Q3 - Q1 = 16. 

Outlier have 2 bound, upper outlier and lower outlier.
+ The Upper bound define as $Q_{3} + 1.5 \times IQR$. This mean value larger than the `max upper quartile + 1.5 * interquartile range`   are Upper Bound Outlier.  
+ The Lower Bound define as $Q_{1} - 1.5 \times IQR$, this mean values less than the Lower Bound are Lower Bound Outlier.  

