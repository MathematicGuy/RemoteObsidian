Risk Trigger (when it happend)
Probility (can this happend or not)
Impact (how this effect the PJ)
Response Owner - who is responsible for initiating the response


Chất Lượng 
+ Sản xuất
+ Bán hàng
+ Logistics 
+ CSKH

Quy Trình -> 
Risk
 + Nhận diện rủi ro
 + Đánh giá
 + Ứng phó

PM (là ng cuối cùng chju trách nhiệm về đảm bảo c/luong)
Quality Assurance (đảm bảo chất lượng)
	hệ thống, quy trình để kiểm soát chất lượng dự án.
Quality Control 
	Quality control requires the company to create an environment where management and employees strive for perfection.

Standard
+ cusomter
+ legal
	- có hợp lệ trong luật nhà nước?

Lập kế hoạch chất lượng
Tiêu chuẩn -> thế nào là chất lượng, 
Để đảm bảo chất lượng cần làm gì?
-> nguồn cung, thiết bị, tuyển dụng và đào tạo pha chế, công thức.

VD: 
> Ngon, Không gian đẹp, Nhân viên thân thiện, Chi Phí

Promt
```md
I want you to create a excel fomula to calculate the Risk Rating on G2 base on Likelihood on E2 and Impact on F2
H, H = H
H, M = H
H, L = M

M, H = H
M, M = M
M, L = L

L, H = M
L, M = M
L, L = L
```




```excel
=IF(OR(AND(E6="H", F6="U"), AND(E6="M", F6="U")), "Hết Cứu", LOOKUP(E6&F6, 
{"HH", "HM", "HL", "MH", "MM", "ML", "LU", "LH", "LM", "LL"},
{"High", "High", "Medium", "High", "Medium", "Low", "High", "Medium", "Medium", "Low"}))
```

```
	{"HH", "HM", "HL", "MH", "MM", "ML", "LU", "LH", "LM", "LL"},
		{"High", "High", "Medium", "High", "Medium", "Low", "High", "Medium", "Medium", "Low"}))
```

```excel
=IF(
OR(
	AND(E6="H", F6="U"), AND(E6="M", F6="U")), "Hết Cứu", 
	LOOKUP(E6&F6, {"HH", "HM", "HL"}, {"High", "High", "Medium"}),
	LOOKUP(E6&F6, {"MH", "MM", "ML"}, {"High", "High", "Medium"})
	LOOKUP(E6&F6, {"LU", "LH", "LM", "LL"}, {"High", "Medium", "Medium", "Low"})	
	)
```



