**URL API**
> https://localhost:7192/api/Home/

**WebAPI**
>https://win9081.site4now.net:8172/MsDeploy.axd?site=sukmadi-001-site1

**Phương thức HTTP**
> https://localhost:7192/api/Home/Calculate?banKinh=10

**Tham số đầu vào**
+ -4 (console output: dientich phai > 0)
+ 222 (trả về dữ liệu phía dưới)

**Dữ liệu trả về**
```json
{
    "dienTich": 154830.25233951936,
    "chuVi": 1394.8671381938682,
}
```

**NuGet Package (important)**
+ Install 4 Swashbuckle package
![[Pasted image 20240304093532.png]]

**Cấu trúc File**
```json
MyProject/
├── Controllers/
│   └── HomeController.cs
├── Models/
├── Views/
├── Models/
├── Views/
├── wwwroot/           
│   ├── css/           
│   ├── js/       
│   └── index.html     
├── appsettings.json
├── Program.cs
└── ... (Các file cấu hình dự án khác)
```

### Ví dụ sử dụng
0) Thêm file Controller có tên là HomeController bên trong file Controller
+ Chọn API Controller 
![[Pasted image 20240304095729.png]]
1) Thêm các thư viện cần thiết cho WebAPI vào file
```cs
using Microsoft.AspNetCore.Mvc; // import library for Web API Controller
using System; // import library for Console, String, etc..
```

2) Kết nối Route và Khai báo API Controller bên trong namespace
```cs
    [Route("api/[controller]/[action]")] // Define the route acess to Actions (function) inside Controller
    [ApiController] // Mark this class as a Controller. (Allow it to automatically activate some feature like check model state, handle errors, etc..)
```
+ Cho HomeController kế thừa tính năng của class Controller 
```cs
public class HomeController : Controller // Inherit from Controller class. Give access to some WebAPI feature like View, etc..
{...}
```


3) Tạo Class CircleData để lấy input/output cho Action
+ ? nên để class get/set ở cuối Controller và cho Action gọi class đó ở trên 
```cs
public class CircleData
{
  public double DienTich { get; set; }
  public double ChuVi { get; set; }
}
```

4) Khai báo trước Action của Controller  [HttpGet] 
+ ! Chú ý: Mọi Hàm bên trong Controller (HomeController) đều được coi là 1 Action. 
```cs
[HttpGet("{banKinh}")] // Say that this action will be called when using HttpGet method with a parameter
```
5) Viết hàm tính bán 
Có 2 hàm đặc biệt cho WebAPI là 
+ ? **BadRequest()** - return HTTP status code 400. Telling the client (Postman, Web, WebAPI) there are error in Send Request. and output the string inside the parameter ().
	Like print but specifically for bug
+ ? Ok() - return HTTP status code 200. Telling it a success
	Like printf but specifically for success run
```cs
// Circle Calculator
public ActionResult<CircleData> Calculate(double banKinh)
{
    // Hàm tính diện tích và chu vi của hình tròn biến bán kính,
    // khi thực hiện kiểm tra bán kính phải > 0 ,
    // nếu đúng thì trả lại diện tích và chu vi của hình tròn,
    // trái lại trả về giá trị báo lỗi.

    if (banKinh <= 0)
    {
        return BadRequest("dientich phai > 0"); // BadRequest output error message ("dientich phai > 0"). Just like print for bug
    }

    double dientich = Math.PI * banKinh * banKinh;
    double chuvi = 2 * Math.PI * banKinh;

    return Ok(new CircleData { DienTich = dientich, ChuVi = chuvi }); // Ok() mean return 200 status code (200 mean success)
}
```

6) Choose GET action & Run the HTTP in POSTMAN 
+ ! **To run any Action** inside the Controller. **Add the Action name after the Controller Name**. (I have **HomeController** so **Home is my Controller Name**)
>Before: https://localhost:7192/api/Home/
>After: https://localhost:7192/api/Home/Calculate

+ ? Add value after ? for parameter input
> https://localhost:7192/api/Home/Calculate?banKinh=222
![[Pasted image 20240304090703.png]]


![[Pasted image 20240314144103.png]]

server: https://win9081.site4now.net:8172/msdeploy.axd?site=sukmadi-001-site1

site-path: sukmadi-001-site1
Destination-ULR: http://sukmadi-001-site1.ktempurl.com/
	pass: 60-dayfreetrial