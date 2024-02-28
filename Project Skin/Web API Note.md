![[Pasted image 20240226104005.png]]
To output function result to Web API, we do this
Where the link `https://localhost:7192/api/Home` is what you got provided. And `/GetProductList` let you run function inside it
![[Pasted image 20240226104132.png]]


```cs
    [ApiController]
    [Route("api/[controller]")]
    public class CircleController : ControllerBase
    {
        [HttpGet("calculate")]
        // Hàm tính diện tích và chu vi của hình tròn biến bán kính,
        // khi thực hiện kiểm tra bán kính phải > 0 ,
        // nếu đúng thì trả lại diện tích và chu vi của hình tròn,
        // trái lại trả về giá trị báo lỗi.
        public ActionResult<CircleController> Calculate(double banKinh)
        {
            if (banKinh <= 0)
            {
                return BadRequest("dienTich phai > 0");
            }

            //Console.WriteLine("Chu vi Hinh Tron {0}", dienTich);
            //Console.WriteLine("Dien Tich Hinh Tron {0}", chuVi);
            double dienTich = Math.PI * banKinh * banKinh;
            double chuVi = 2 * Math.PI * banKinh;

            return Ok(new CircleData { DienTich = dienTich, ChuVi = chuVi });
        }
    }


    public class CircleData
    {
        public double DienTich { get; set; }
        public double ChuVi { get; set; }
    }

```

API connect to a json file online and return data inside it.

## Connect the Data Base
1) Get the Connection String from the DB properties
	![[Pasted image 20240228211219.png]]
2) Goes to Solution Explorer -> appsetting.json
	create "ConnectionStrings" and paste the Connection String you get into DefaultConnection 
	![[Pasted image 20240228211301.png]]