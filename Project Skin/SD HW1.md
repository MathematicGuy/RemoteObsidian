```ad-todo
Bài tập 5. 
a. SCRUM là 1 phương pháp của quản lý dự án theo tiếp cận Agile?
b. Tại sao SCRUM được ưa chuộng khi quản lý dự án phần mềm nghiệp vụ?
c. Backlog (Product Backlog , Sprint backlog...) là gì trong SCRUM?
d. Sprint là gì trong SCRUM?
e. Khi gán Sprint cho các thành viên có nên để thời gian hoàn thành 1 Sprint quá lâu không? (chẳng hạn hơn 4 tuần)
f. Phải xong các Sprint thì team mới chuyển sang gán Sprint mới? hay vẫn tổ chức buổi họp Sprint Review và Retrospective theo kế hoạch để lập Planning tiếp theo?
```

##### a) SCRUM là 1 phương pháp của quản lý dự án theo tiếp cận Agile?
> Đúng, SCRUM là 1 phương pháp quản lý dự án tiếp cận Agile

##### b) Tại sao SCRUM được ưa chuộng khi quản lý dự án phần mềm nghiệp vụ?
> SCRUM được ưa chuộng bởi gì nó cho phép người dùng:
1) Tính linh hoạt: SCRUM cho phép điều chỉnh nhanh chóng theo yêu cầu thị trường và khách hàng.
	
	Ví dụ: Nếu công ty đang phát triển sản phẩm cung cấp OCR dịch tài liệu tiếng anh sang tiếng việt. Đột nhiên thị trường có Trend cung cấp OCR để đọc hóa đơn sản phẩm, nhóm SCRUM có thể dễ dàng điều chỉnh kế hoạch để thêm, sửa, xóa 1 số features trong sprint tiếp theo.   

2) Tăng cường sự cộng tác: SCRUM khuyến khích sự giao tiếp thường xuyên và cộng tác giữa các thành viên trong nhóm thông qua các buổi họp hàng ngày
	
	Ví dụ: mọi người trong nhóm hiểu trạng thái công việc của nhau, góc nhìn tổng quan dự án và có thể hỗ trợ nhau khi cần thiết.

3) Phản hồi nhanh chóng: Các buổi Sprint Review (đánh giá) và Retrospective (phản hồi dự án) cho phép nhóm nhận phản hồi từ khách hàng và cải thiện quy trình làm việc.
	
	Ví dụ:  Sau mỗi Sprint, nhóm nhận phản hồi từ khách hàng và có thể điều chỉnh sản phẩm ngay lập tức.


4) Tăng cường tính minh bạch: Tất cả thành viên trong nhóm đều có cái nhìn rõ ràng về tiến độ và các vấn đề cần giải quyết thông qua các công cụ quản lý và buổi họp.
	
	Ví dụ: mọi người đều biết chuyện gì đang diễn ra và có thể đưa ra giải pháp kịp thời

##### c) Backlog (Product Backlog , Sprint backlog...) là gì trong SCRUM?
> Backlog (Product Backlog , Sprint backlog...) là  1 danh sách thay đổi các yêu cầu dựa trên nhu cầu khách hàng
+ ! Backlog không phải là 1 to-do list, nó là 1 wish list cho những tính năng, công việc mong muốn có trong sản phẩm. Product Backlog và Sprint Backlog sẽ lấy các công việc từ danh sách Backlog này.
	Ví dụ: danh sách chứa mọi features mong muốn có trong dự án. Những features có thể thực hiện sẽ được lấy ra từ danh sách này. 
	
+ ? **Product Backlog:** Danh sách tất cả các công việc cần hoàn thành để phát triển sản phẩm. Nó bao gồm các yêu cầu tính năng, cải tiến, sửa lỗi, v.v., được sắp xếp theo thứ tự ưu tiên. Coi Product Backlog là 1 List chứa các công việc cần thiết để phát triển 1 sản phẩm.
	Ví dụ:  Product Backlog có thể bao gồm các công việc đang sẽ và đang được làm như là "sửa bug cho tính năng A", "phát triển OCR cho mobile", "CI/CD cho Mobile App", etc..
	
+ ? Sprint backlog: Sprint là 1 công việc lớn đc chọn từ những công việc được tạo ra trong Backlog . Mỗi Sprint thường kéo dài từ 1 tới 4 tuần.  Coi Sprint là 1 đầu việc lớn chứa các công việc nhỏ lấy từ Backlog và Sprint này sẽ có deadline từ 1 - 4 tuần.
	
	Ví dụ: Sprint "Thiết Kế" bao gồm 2 công việc "Thiết kế hệ thống và Thiết kế UI/UX". 

##### d) Sprint là gì trong SCRUM? 
> Sprint trong SCRUM là 1 gia đoạn làm việc có thời gian cố định (thường 1-4 tuần), trong Sprint chứa các công việc lấy từ Backlog sẽ đc hoàn thành. Mỗi Sprint bắt đầu với 1 buổi Sprint Planning và kết thúc với Sprint Review(đánh giá) và Sprint Retrospective (phản hồi dự án)

Ví dụ: Nhóm Developer bắt đầu với việc 
	1) Lập kế hoạch (Sprint Planning): Tạo Sprint "Thiết Kế" kéo dài 2 tuần bao gồm 2 công việc "Thiết kế hệ thống và Thiết kế UI/UX".  Rồi tiến hành
	2) Làm các công việc trong Sprint Backlog và kết thúc với việc
	3)  Đánh giá (Sprint Review) và phản hồi (Sprint Retrospective)

##### e) Khi gán Sprint cho các thành viên có nên để thời gian hoàn thành 1 Sprint quá lâu không? (chẳng hạn hơn 4 tuần)
> Khi gán Sprint cho các thành viên không nên để thời gian hoàn thành 1 Sprint quá lâu không (Chẳng hạn hơn 4 tuần) vì Sprint (dịch ra là chạy nước rút) chỉ nên làm trong 1 tới 4 tuần vì:
1) Phản hồi nhanh: Thời gian hoàn thành ngắn giúp nhóm nhận được phản hồi sớm và điều chỉnh nhanh chóng.
	
	Ví dụ: Với Sprint 2 tuần, nhóm có thể nhận đc phản hồi từ khách hàng sau mỗi 2 tuần và kịp thời điều chỉnh sản phẩm tr'c khi Scope bị thay đổi quá nhiều.

2) Dễ quản lý rủi ro: Các Sprint ngắn giúp quả lý rủi ro và tránh công việc bị trì trệ
	
	Ví dụ: Nếu 1 Sprint kéo dài quá 4 tuần, có thể gây mất động lực, quá nhiều thời gian tr'c khi phát hiện vấn đề, có thể gây phí phạm công sức khi đi quá hoặc sai Scope.

3) Phù hợp cho nhóm Lập trình viên mới hoặc nhỏ: Những người mới làm dự án thường phải duy trì việc học song song với làm, việc thu ngắn thời gian hoàn thành từng công việc ép buộc lập trình viên phải áp dụng ngay những kiến thức vừa học giúp tăng tốc tiến độ nhanh chóng. Đồng thời phòng tránh rủi do như phát triển quá đà 1 features mà chưa hiểu rõ, xác định những công việc quan trọng nhất giúp hoàn thành công việc hiệu quả.
	
	Ví dụ: Lập trình viên mới mắc sai lầm là thiết kế quá sâu 1 tính năng mà chưa hiểu rõ tính năng đó có thể tích hợp được vào hệ thống hay ko, nhờ Sprint thời hạn là 1 tuần người đó đã sớm nhận ra sai lầm của mình.

##### f) Phải xong các Sprint thì team mới chuyển sang gán Sprint mới? hay vẫn tổ chức buổi họp Sprint Review và Retrospective theo kế hoạch để lập Planning tiếp theo?
> Nhóm SCRUM nên tổ chức buổi họp Sprint Review và Retrospective theo kế hoạch sau khi hoàn thành mỗi Sprint, bất kể có hoàn thành tất cả các mục tiêu của Sprint hay không vì: 

0) Mục tiêu của Sprint là để đánh giá, phản hồi 1 dự án nhỏ được kéo dài trong 1 khoảng thời gian ngắn nhằm xác định lỗi sớm, phòng tránh rủi ro và tăng cường hiệu quả làm việc. 
	
1) **Sprint Review**: Đánh giá những gì đã hoàn thành trong Sprint và nhận phản hồi từ các bên liên quan.    
    - **Ví dụ**: Nếu một số nhiệm vụ không hoàn thành, nhóm sẽ xem xét và điều chỉnh trong Sprint tiếp theo.
    
2) **Sprint Retrospective**: Nhìn lại quy trình làm việc và tìm cách cải thiện hiệu suất và hiệu quả của nhóm.
    - **Ví dụ**: Nhóm sẽ thảo luận về những gì đã làm tốt, những gì chưa tốt, và đề xuất các cải tiến cho Sprint tiếp theo.
    
3) **Sprint Planning**: Lập kế hoạch cho Sprint tiếp theo, chọn các mục từ Product Backlog vào Sprint Backlog.
    
    - **Ví dụ**: Nhóm sẽ chọn các nhiệm vụ ưu tiên cao từ Product Backlog và lập kế hoạch cho chúng trong Sprint mới.


```ad-todo
Bài tập 6.
a. Ai là người gán Sprint cho team trong SCRUM?
b. Liệt kê các vai trò của Product Owner, Scrum Master, và Development Team trong SCRUM.
```
##### a) Ai là người gán Sprint cho team trong SCRUM?
> Không ai là người tự gán Sprint cho SCRUM. Thay vào đó, team tự tổ chức và quyết định nội dung, công việc của Sprint thông qua buổi Sprint Planning. Buổi Sprint Planning có sự tham gia của toàn bộ SCRUM team, bao gồm Product Owner, Scrum Master và Development Team. Chính Development Team sẽ cam kết với các mục tiêu của Sprint dựa trên các mục trong Product Backlog được Product Owner ưu tiên.

##### b) Liệt kê các vai trò của Product Owner, Scrum Master, và Development Team trong SCRUM.

#### Product Owner

1. **Quản lý Product Backlog**:
    
    - **Ví dụ**: Product Owner tạo và duy trì Product Backlog, đảm bảo rằng nó được ưu tiên theo giá trị kinh doanh và nhu cầu của khách hàng.
2. **Xác định yêu cầu sản phẩm**:
    
    - **Ví dụ**: Product Owner thu thập và xác định các yêu cầu của khách hàng và các bên liên quan.
3. **Đưa ra quyết định về sản phẩm**:
    
    - **Ví dụ**: Product Owner quyết định những tính năng nào sẽ được phát triển và trong thứ tự nào, dựa trên giá trị kinh doanh và phản hồi từ người dùng.
4. **Tương tác với các bên liên quan**:
    
    - **Ví dụ**: Product Owner làm việc với khách hàng, người dùng và các bên liên quan để đảm bảo rằng sản phẩm phát triển đúng hướng.

#### Scrum Master

1. **Hỗ trợ và huấn luyện nhóm SCRUM**:
    
    - **Ví dụ**: Scrum Master giải thích và hỗ trợ nhóm hiểu rõ và áp dụng đúng các nguyên tắc và thực hành của SCRUM.
2. **Loại bỏ trở ngại (Impediments)**:
    
    - **Ví dụ**: Nếu Development Team gặp phải khó khăn trong công việc, Scrum Master sẽ tìm cách loại bỏ những trở ngại này để nhóm có thể làm việc hiệu quả hơn.
3. **Bảo vệ nhóm khỏi sự gián đoạn**:
    
    - **Ví dụ**: Scrum Master bảo vệ Development Team khỏi sự can thiệp không cần thiết từ các bên ngoài để đảm bảo họ có thể tập trung vào công việc.
4. **Tạo điều kiện cho các buổi họp SCRUM**:
    
    - **Ví dụ**: Scrum Master tổ chức và điều hành các buổi họp Daily Standup, Sprint Review, Sprint Retrospective và Sprint Planning.

#### Development Team

1. **Phát triển sản phẩm**:
    
    - **Ví dụ**: Development Team làm việc cùng nhau để hoàn thành các nhiệm vụ được giao trong Sprint Backlog, bao gồm viết mã, kiểm thử và tích hợp.
2. **Tự tổ chức**:
    
    - **Ví dụ**: Development Team tự quản lý công việc của mình mà không cần sự chỉ đạo từ bên ngoài, quyết định cách tốt nhất để hoàn thành các mục tiêu Sprint.
3. **Đảm bảo chất lượng sản phẩm**:
    
    - **Ví dụ**: Development Team chịu trách nhiệm về chất lượng của sản phẩm được giao, bao gồm viết mã sạch, kiểm thử kỹ lưỡng và thực hiện các phương pháp đảm bảo chất lượng.
4. **Cung cấp đầu ra (Increments)**:
    
    - **Ví dụ**: Mỗi Sprint, Development Team tạo ra một phần sản phẩm hoạt động được (Increment) có giá trị gia tăng và có thể được xem xét và sử dụng bởi khách hàng hoặc người dùng.


```ad-todo
Bài tập 7. Danh sách các vị trí cơ bản trong một dự án phát triển phần mềm nghiệp vụ lớn khi có một user story của khách hàng, bao gồm mô tả chi tiết cho từng vai trò:

1. Project Manager (Quản lý dự án)
Quản lý toàn bộ dự án: Lập kế hoạch, theo dõi tiến độ và đảm bảo dự án hoàn thành đúng hạn.
Điều phối các nguồn lực: Đảm bảo các nguồn lực (nhân lực, tài chính, công nghệ) được sử dụng hiệu quả.
Giao tiếp với các bên liên quan: Đảm bảo thông tin liên lạc thông suốt giữa đội dự án và các bên liên quan.
2. Solution Architect (Kiến trúc sư giải pháp)
Thiết kế kiến trúc tổng thể của hệ thống: Đảm bảo tính nhất quán và khả năng mở rộng.
Lựa chọn công nghệ: Đưa ra quyết định về công nghệ, framework và công cụ phù hợp cho dự án.
Giám sát việc thực hiện: Đảm bảo rằng các thành phần của hệ thống được phát triển theo kiến trúc đã thiết kế.
3. Business Analyst (Chuyên viên phân tích nghiệp vụ)
Phân tích yêu cầu từ khách hàng và người dùng: Thu thập, phân tích và làm rõ các yêu cầu nghiệp vụ.
Lập tài liệu yêu cầu chi tiết: Tạo ra các tài liệu đặc tả yêu cầu phần mềm (SRS), tài liệu phân tích thiết kế (SDD).
Giao tiếp với đội phát triển: Đảm bảo rằng đội phát triển hiểu rõ yêu cầu và mục tiêu của khách hàng.
4. UI/UX Designer (Thiết kế giao diện và trải nghiệm người dùng)
Thiết kế giao diện người dùng: Tạo ra các thiết kế giao diện (wireframes, mockups) dựa trên yêu cầu nghiệp vụ.
Thiết kế trải nghiệm người dùng: Đảm bảo rằng trải nghiệm người dùng (UX) mượt mà và hiệu quả.
Thử nghiệm giao diện: Thu thập phản hồi từ người dùng và điều chỉnh thiết kế để cải thiện UX.
5. Front-End Developer (Lập trình viên giao diện người dùng)
Phát triển giao diện người dùng: Xây dựng các trang web hoặc ứng dụng di động dựa trên thiết kế của UI/UX Designer.
Tương tác với API: Gọi các API từ phía máy chủ để lấy dữ liệu và hiển thị trên giao diện.
Tối ưu hóa hiệu suất: Đảm bảo giao diện người dùng hoạt động nhanh và mượt mà trên các trình duyệt và thiết bị khác nhau.
6. Back-End Developer (Lập trình viên phía máy chủ)
Phát triển các API và logic nghiệp vụ: Xây dựng và duy trì các API, dịch vụ web và logic nghiệp vụ của hệ thống.
Quản lý cơ sở dữ liệu: Thiết kế và tối ưu hóa cơ sở dữ liệu để đảm bảo hiệu suất và tính toàn vẹn dữ liệu.
Bảo mật: Đảm bảo các biện pháp bảo mật được thực hiện để bảo vệ dữ liệu và ngăn chặn các lỗ hổng bảo mật.
7. DevOps Engineer (Kỹ sư DevOps)
Thiết lập và quản lý môi trường phát triển: Cấu hình và quản lý các môi trường phát triển, thử nghiệm và sản xuất.
Tự động hóa triển khai: Thiết lập các quy trình CI/CD để tự động hóa việc xây dựng, kiểm thử và triển khai phần mềm.
Giám sát hệ thống: Giám sát hiệu suất và tính sẵn sàng của hệ thống, xử lý sự cố và tối ưu hóa hệ thống.
h. Quality Assurance (QA) Engineer (Kỹ sư đảm bảo chất lượng)
Kiểm thử phần mềm: Thực hiện các loại kiểm thử STD cho functional, performance, security để đảm bảo chất lượng phần mềm.
Tạo kịch bản kiểm thử: Viết tài liệu kiểm thử phần mềm và thực hiện các kịch bản kiểm thử để kiểm tra các tính năng và chức năng của phần mềm.
Báo cáo lỗi: Ghi nhận và theo dõi các lỗi phát hiện trong quá trình kiểm thử, làm việc với đội phát triển để khắc phục.
8. Chuyên Viên Đào Tạo Sử Dụng (Training Specialist)
Tạo tài liệu hướng dẫn:
+Phát triển tài liệu đào tạo: Bao gồm sách hướng dẫn sử dụng, tài liệu tham khảo, video hướng dẫn và các bài giảng trực tuyến.
+Đảm bảo tài liệu chi tiết và dễ hiểu: Phù hợp với đối tượng người dùng.
Thực hiện các buổi đào tạo:
+Tổ chức buổi đào tạo: Thực hiện các buổi đào tạo trực tiếp hoặc trực tuyến cho người dùng cuối và các bên liên quan.
+Đảm bảo người dùng nắm vững phần mềm: Đảm bảo rằng người dùng có thể thực hiện các tác vụ cần thiết một cách hiệu quả.
Hỗ trợ sau đào tạo:
+Cung cấp hỗ trợ liên tục: Giải đáp thắc mắc và giải quyết các vấn đề phát sinh sau đào tạo.
+Thu thập phản hồi: Cải thiện tài liệu và phương pháp đào tạo dựa trên phản hồi của người dùng.
Đánh giá hiệu quả đào tạo:
+Thực hiện khảo sát và kiểm tra: Đánh giá mức độ hiểu biết và khả năng sử dụng phần mềm của người dùng sau khi đào tạo.
+Điều chỉnh tài liệu và phương pháp: Dựa trên kết quả đánh giá để cải thiện chất lượng đào tạo.

Hãy tự đánh giá định hướng của mình để xem mình phù hợp với vị trí nào?
```


