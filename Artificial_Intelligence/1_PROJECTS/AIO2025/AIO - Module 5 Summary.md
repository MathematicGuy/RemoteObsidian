[google collab]([https://drive.google.com/drive/folders/1kPdxT_TLiQReYJjSfPlKj8P7tBNPcQPB?usp=sharing](https://drive.google.com/drive/folders/1kPdxT_TLiQReYJjSfPlKj8P7tBNPcQPB?usp=sharing))

Explain definition + example

slide should have: Example + visualization 
>listener should focus on understanding not visualizing

bias (kind of like  epsilon): handle unexpected value.

LeakyReLU: solve gradient vanishing 

note: I should ask more question. e.g. what the purpose of hidden layers, what does it do.
	Hidden layer -> help NN understand data in more detail.

Fomula + fomula domain 

cải tiến ReLU để giải quyết vấn đề: bảo lưu giá trị < 0.

zero_grad: dùng để reset đạo hàm.
+ $ Purpose: Giúp chỉ xét đạo hàm trong 1 khoảng mong muốn.
+ & Why: The optimization step would consider the sum of gradients from all previous iterations, which could lead to incorrect updates. 
+ ? Ex: Suppose you're training a model in batches:
	1. At each batch, you compute the gradients using `backward()`.
	2. Before computing the next batch, you use `zero_grad()` to clear the old gradients. This ensures that the optimizer updates the parameters using only the current batch's gradients, not a mixture of past and present gradients.
+ $ Prevent Gradient vanishing/exploding (if hidden layers is too large)

1st vs 2nd derivative for gradient vanishing/exploding, explain why too small/large gradient are useless. 

tuyến tính: 1 đường thẳng
phi tuyến tính: không thẳng. 
	Một số hàm phi tuyến có thể chỉ tăng hoặc giảm, nhưng theo cách không đều (không thẳng)
+ ? vd: phi tuyến tính là **một cách thay đổi đầu ra không tỷ lệ tuyến tính với đầu vào**. 
- **Tăng/giảm dần**: Hàm số mũ, hàm logarit.
- **Thay đổi nhiều chiều hướng**: Hàm sóng (lượng giác), hàm đa thức bậc cao, v.v.

## Learning Rate and Initialize Weight
Mục đích của 3 cái khởi tạo Random, Kaiming, **Xavier (khởi tạo mặc định)** là để xem xét tính overfit or underfit của từng kiểu activation function. Tổng quản hơn là để test các cấu trúc khác nhau của mô hình. 
+ $ Sử dụng phân phối thống kê để khởi tạo weight model thường sẽ tốt hơn.
Note: học nhanh quá -> overfitting. loss plot should converge slowly.

### Optimizer: Adam
**RMSProp + Moment**: 
1st term: tối ưu LR
2nd term: tối ưu hướng của vector m

Adamw (1 cải tiến của adam đc dùng hiện nay) 
	giống adam nhưng đánh thêm trọng số

+ $ Optimizer giúp hàm Loss càng thoải càng tốt. 
+ ? Bài toán càng phức tạp thì dùng activation func càng phức tạp.  

