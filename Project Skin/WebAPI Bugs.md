+ ! There was an error running the selected code generator: 'Package restore failed. Rolling back package changes for 'HowAboutAnotherJoke•,•
	https://youtu.be/GAKvScju1qA?si=1N-A1_TslssWab0V

ApplicaionDbContext

> Cross-Origin Request Blocked: The Same Origin Policy disallows reading the remote resource at http://heval1st-001-site1.anytempurl.com//GetAllHang. (Reason: CORS header ‘Access-Control-Allow-Origin’ missing). Status code: 401.
+ Refresh/reset SSL key. 
+ This error might happend because you already use this SSL key in another Web site. 1 SSL for 1 Web site only. 

+ ! **The ConnectionString property has not been initialized.** 
> Reason, the connection string in appsetting.json might be wrong or
> + The connection string is right. But the code connect to it is wrong. 
+ ? This code is not the right form. It cause error
```cs
builder.Services.AddDbContext<DataContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("PokemonConnectionString")));
```
+ $ This code is the right form 
```cs
// Add the DB context to the services
builder.Services.AddDbContext<DataContext>(options =>
{
    options.UseSqlServer(builder.Configuration.GetConnectionString("PokemonConnectionString"));
});
```

Unknow Error that are too complex to understand like
+ ! Severity Code Description Project File Line Suppression State Error MSB3027 Could not copy "D:\CMC_UNI\2ndYear\Technology & Web Programming\Learn Web API\PokemonAPI\PokemonAPI\obj\Debug\net8.0\apphost.exe" to "bin\Debug\net8.0\PokemonAPI.exe". Exceeded retry count of 10. Failed. The file is locked by: "PokemonAPI (19268)" PokemonAPI C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Current\Bin\amd64\Microsoft.Common.CurrentVersion.targets 5254
+ $ **Clean Solution** in Visual Studio 2022


```cs
        [HttpPost("CreateHang")]
        public async Task<IActionResult> CreateHang(hang_hoa hangHoa)
        {
            // Validate hangHoa properties
            List<string> errorMessages = new List<string>();

            if (string.IsNullOrWhiteSpace(hangHoa.ten_hang_hoa))
            {
                errorMessages.Add("ten_hang_hoa cannot be null or empty.");
            }

            //if (string.IsNullOrWhiteSpace(hangHoa.ghi_chu))
            //{
            //    errorMessages.Add("ghi_chu cannot be null or empty.");
            //}

            if (hangHoa.ma_hang_hoa < 99 || hangHoa.ma_hang_hoa > 1000)
            {
                errorMessages.Add("ma_hang_hoa must be a 3-digit number.");
            }

            if (hangHoa.so_luong < 0)
            {
                errorMessages.Add("so_luong is too low.");
            }
            if (hangHoa.so_luong.GetType() != typeof(int) || hangHoa.so_luong == null)
            {
                errorMessages.Add("so_luong data type must be a Positive INT");
            }



            // Check if hangHoa.ten_hang_hoa is a valid string
            if (!Regex.IsMatch(hangHoa.ten_hang_hoa, @"^[a-zA-Z\s]*$"))
            {
                errorMessages.Add("ten_hang_hoa must contain only letters and spaces.");
            }

            // Check if hangHoa with the same ma_hang_hoa already exists
            if (context.hangHoa.Any(h => h.ma_hang_hoa == hangHoa.ma_hang_hoa))
            {
                errorMessages.Add("hangHoa with the same ma_hang_hoa already exists.");
            }

            if (errorMessages.Count > 0)
            {
                return BadRequest(new { Thanh_warning_msg = errorMessages });
            }

            context.hangHoa.Add(hangHoa);
            await context.SaveChangesAsync();
            return Ok(new { Thanh_warning_msg = "Hang Hoa added successfully", hangHoa });
        }
```

"Data Source=SQL5113.site4now.net;Initial Catalog=db_aa73dc_product;User Id=db_aa73dc_product_admin;Password=