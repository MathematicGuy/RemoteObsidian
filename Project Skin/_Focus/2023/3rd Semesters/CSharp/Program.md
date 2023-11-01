
### Applied Vietnames
```cs
Console.OutputEncoding = System.Text.Encoding.UTF8; // set encoding UTF-8 cho Console
```

### Declare Array and Connect to DB
```cs
SqlConnection connection = null;
connection = db_lib.MoKetNoi(db_lib.connectionString);
```

### Output Desired Table with SQL Command 
```cs
  if (connection == null)
      Console.WriteLine("Không kết nối được CSDL với xâu kết nối là:" + db_lib.connectionString);
  else
  {


      // Lấy table với "điều kiện" sử dụng Lệnh SQL
      arraySimNgay = db_lib.DocBangSim(connection, "SELECT * FROM Sim WHERE NgayKichHoat = '20/08/2023'");
      Console.WriteLine("\nDanh sách thẻ có ngày kích hoạt là 20/08/2023:");
      // In
      for (int i = 0; i < arraySimNgay.Length; i++)
      {
          Console.WriteLine(arraySimNgay[i].simID + "| " + arraySimNgay[i].soSim + "| " + arraySimNgay[i].ngayKichHoat + "| " + arraySimNgay[i].ngayHetHan + "| " + arraySimNgay[i].KhuyenMai + "| ");
      }
  }
```

### Connect to DB and Run Application
```cs
// Đọc bảng Students
connection = db_lib.MoKetNoi(db_lib.connectionString);
DataTable mangSIM;
mangSIM = db_lib.DocTableSim(connection);
/////////////////////////////////////////////
Console.WriteLine("Nhấn Enter để tiếp tục...");
Console.ReadLine();

// Chạy ứng dụng Windows Forms
Application.EnableVisualStyles();
Application.SetCompatibleTextRenderingDefault(false);


// Tạo đối tượng form chạy Windows Forms
FormTable frm1;
frm1 = new FormTable();
frm1.table_sim = mangSIM;


// Chạy form
Application.Run(frm1);
```

