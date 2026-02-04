**Preliminaries:**
+ [[Vector Dot Product]]
	same direction - positive
	perpendicular direction - zero
	opposite direction - negative

Thay vì làm Loss khó hơn thì tập trung vài build model dễ kiểm soát hơn vs hàm Loss. 

+ ? Understand Gradient Projection to understand this part:  ![[Pasted image 20260204175352.png | 544]]
+ $ Càng gần Vuông Góc thì Loss càng Thấp ? vì Vuông Góc nghĩa là Gradient Thay Đổi Ít Nhất cho cả 2 Class.  
	Sử dụng DotProduct để tính gần Vuông Góc bao nhiêu %  

Constrain: 
![[Pasted image 20260204180425.png# left ]]
	nằm trong vùng Feasible Region (vùng màu xanh dương) 
	giữ khoảng cách với Current Gradient (mũi tên đỏ)

![[Pasted image 20260204180152.png | 455]]


![[Pasted image 20260204180046.png | 455]]



Goals: 
+ Hiểu Orthogonal Project Loss (OPL)
+ OPL có kết hợp đc với M3 Optimizer hay không ? Có thì có thể tích hợp vào TreeLoRA
+ Ôn kthuc Continual Learning để tối gặp.  