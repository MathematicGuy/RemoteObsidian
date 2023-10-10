### Btn Search
```cs
if (this.textboxSoSim.Text.Length == 10 && this.textboxSoSim.Text.All(char.IsDigit))
{
    for (int i = 0; i < dataGridView1.Rows.Count; i++)
    {
        DataGridViewRow row = dataGridView1.Rows[i];
        if (row.Cells["SoSim"].Value == null)
            continue;

        if (row.Cells["SoSim"].Value.ToString() == this.textboxSoSim.Text)
        {
            // Tìm thấy dòng chứa StudentID, di chuyển đến dòng đó
            this.textBox1.Text = dataGridView1.Rows[i].Cells["SimID"].Value.ToString();
            dataGridView1.CurrentCell = row.Cells[1];
            this.textBox3.Text = dataGridView1.Rows[i].Cells["NgayKichHoat"].Value.ToString();
            this.textBox4.Text = dataGridView1.Rows[i].Cells["NgayHetHan"].Value.ToString();
            this.textBox5.Text = dataGridView1.Rows[i].Cells["GhiChu"].Value.ToString();
            allowMouseMove = true;
            return;
        }
    }

    // Không tìm thấy, hiển thị hộp thoại thông báo
    MessageBox.Show("Không tìm thấy Sim có số: " + this.textboxSoSim.Text);
}//if
else if (this.textboxSoSim.Text.Length > 10 || !this.textboxSoSim.Text.All(char.IsDigit))
{
    this.textboxSoSim.Focus();
    MessageBox.Show("Số Sim không hợp lệ");
    Console.Beep();
}
else
{
    MessageBox.Show("Tìm thấy Sim có số: " + this.textboxSoSim.Text);
}

allowMouseMove = true;
```



### Btn Delete
```cs
// Kiểm tra xem có dòng nào đang được chọn trong DataGridView hay không

if (dataGridView1.SelectedRows.Count > 0)
{
    // Lấy dòng đầu tiên đang được chọn trong DataGridView
    DataGridViewRow selectedRow = dataGridView1.SelectedRows[0];

    // Lấy giá trị của cột "StudentID" của dòng được chọn
    string simID_delete = selectedRow.Cells["SimID"].Value.ToString();


    // Xóa dòng đang được chọn khỏi DataGridView
    if (using_datasouce == false)
        dataGridView1.Rows.Remove(selectedRow);
    else
    {
        DataTable table = (DataTable)dataGridView1.DataSource;
        // Tìm vị trí dòng cần xóa trong DataTable
        int rowIndex_delete = -1;
        for (int i = 0; i < table.Rows.Count; i++)
        {
            DataRow row = table.Rows[i];
            if (row["SimID"].ToString() == simID_delete)
            {
                rowIndex_delete = i;
                break;
            }
        }

        // Xóa dòng từ DataTable nếu tìm thấy dòng cần xóa
        if (rowIndex_delete >= 0)
        {
            table.Rows.RemoveAt(rowIndex_delete);
        }
    }
    // Thực hiện xóa sinh viên từ CSDL ở đây với studentIDToDelete
    SqlConnection connection = null;
    connection = db_lib.MoKetNoi(db_lib.connectionString);
    if (connection == null)
    {
        allowMouseMove = true;
        return;
    }//if
    db_lib.XoaSim(connection, simID_delete);
    connection.Close();
    connection.Dispose();
}
else
{
    // Hiển thị thông báo nếu không có dòng nào được chọn
    MessageBox.Show("Vui lòng chọn sinh viên cần xóa.");
}
allowMouseMove = true;
```


### Btn Edit 
```cs
string soSim = this.textBox1.Text;
string simID = this.textBox2.Text;
string ghiChu = this.textBox5.Text;

// Kiểm tra xem sinh viên có trong DataGridView hay không
bool tim_thay = false;
for (int i = 0; i < dataGridView1.Rows.Count; i++)
{
	 DataGridViewRow row = dataGridView1.Rows[i];
	 if (row.Cells["SimID"].Value == null)
		  continue;

	 if (row.Cells["SimID"].Value.ToString() == simID)
	 {
		  // Sửa giá trị của sinh viên trong DataGridView
		  row.Cells["SimID"].Value = simID;
		  row.Cells["SoSim"].Value = soSim;
		  row.Cells["GhiChu"].Value = ghiChu;
		  tim_thay = true;
		  break;
	 }
}

// Nếu sinh viên không tồn tại trong DataGridView, thêm sinh viên mới vào cả DataGridView và cơ sở dữ liệu
if (tim_thay == false)
{
	 allowMouseMove = true;
	 return;
}

// Thực hiện sửa dữ liệu vào bảng Students của CSDL
SqlConnection connection = db_lib.MoKetNoi(db_lib.connectionString);
if (connection == null)
{
	 allowMouseMove = true;
	 return;
}

db_lib.SuaMotSim(connection, simID, soSim, ghiChu);
connection.Close();
connection.Dispose();

allowMouseMove = true;
```


### Btn Add
```cs
string simID = this.textBox2.Text;
string soSim = this.textBox1.Text;
string ngayKichHoat = this.textBox3.Text;
string ngayHetHan = this.textBox4.Text;
string ghiChu = this.textBox5.Text;

// Kiểm tra xem các trường thông tin đã được nhập đầy đủ hay chưa
if (string.IsNullOrEmpty(simID) || string.IsNullOrEmpty(soSim) || string.IsNullOrEmpty(ngayKichHoat) || string.IsNullOrEmpty(ngayHetHan) || string.IsNullOrEmpty(ghiChu) || !this.textBox1.Text.All(char.IsDigit))
{
    MessageBox.Show("Kiểm tra lại các trường giá trị cần nhập liệu !");
    return;
}//if

// Kiểm tra xem SimID đã tồn tại trong DataGridView hay chưa
for (int i = 0; i < dataGridView1.Rows.Count; i++)
{
    DataGridViewRow row = dataGridView1.Rows[i];
    if (row.Cells["SimID"].Value == null)
        continue;

    if (row.Cells["SimID"].Value.ToString() == simID)
    {
        MessageBox.Show("Đã tồn tại mã sim này");
        allowMouseMove = true;
        return;
    }//if
}//for

if (using_datasouce == true)
{
    DataTable table = (DataTable)dataGridView1.DataSource;
    DataRow newRow = table.NewRow();
    newRow["SimID"] = simID;
    newRow["SoSim"] = soSim;
    newRow["NgayKichHoat"] = ngayKichHoat;
    newRow["NgayHetHan"] = ngayHetHan;
    newRow["GhiChu"] = ghiChu;
    table.Rows.Add(newRow);
    table.AcceptChanges();
}
else
{
    dataGridView1.Rows.Add(simID, soSim, ngayKichHoat, ngayHetHan, ghiChu);
}

// Thêm dữ liệu vào bảng Sim của CSDL

SqlConnection connection = null;
connection = db_lib.MoKetNoi(db_lib.connectionString);
if (connection == null)
{
    allowMouseMove = true;
    return;
}//if
db_lib.GhiMotSim(connection, simID, soSim, ngayKichHoat, ngayHetHan, ghiChu);
connection.Close();
connection.Dispose();

allowMouseMove = true;
```

#### Export Table to CSV/Excel
### Btn Export CSV (.csv)
```cs
using (SqlConnection connection = db_lib.MoKetNoi(db_lib.connectionString))
{
    if (connection == null)
    {
        MessageBox.Show("Không thể kết nối đến cơ sở dữ liệu.");
        return;
    }

    // Lấy dữ liệu từ SQL Server
    DataTable dataTable = db_lib.DocTableSim(connection);

    // Đường dẫn và tên tệp CSV
    string csvFilePath = "SimThe_output.csv";

    // Ghi dữ liệu vào tệp CSV
    using (StreamWriter writer = new StreamWriter(csvFilePath))
    {
        // Ghi tiêu đề (tên cột)
        for (int i = 0; i < dataTable.Columns.Count; i++)
        {
            writer.Write(dataTable.Columns[i].ColumnName);
            if (i < dataTable.Columns.Count - 1)
            {
                writer.Write(",");
            }
        }
        writer.WriteLine();

        // Ghi dữ liệu từ DataTable vào tệp CSV
        foreach (DataRow row in dataTable.Rows)
        {
            for (int i = 0; i < dataTable.Columns.Count; i++)
            {
                writer.Write(row[i].ToString());
                if (i < dataTable.Columns.Count - 1)
                {
                    writer.Write(",");
                }
            }
            writer.WriteLine();
        }
    }

    string location = "SimThe\\bin\\x64\\Debug";
    MessageBox.Show("File Exported To CSV: " + location);
}
```


### Btn Export to Excel (.xsml)
```cs
System.Threading.Thread.CurrentThread.ApartmentState = System.Threading.ApartmentState.STA;

DataObject copyData = dataGridView1.GetClipboardContent();
if (copyData != null) Clipboard.SetDataObject(copyData);

// connected to Excel app
Microsoft.Office.Interop.Excel.Application xlapp = new Microsoft.Office.Interop.Excel.Application();
// turn Excel visible
xlapp.Visible = true;


Microsoft.Office.Interop.Excel.Workbook xlWbook;
Microsoft.Office.Interop.Excel.Worksheet xlSheet;
object miseddata = System.Reflection.Missing.Value;
xlWbook = xlapp.Workbooks.Add(miseddata);

xlSheet = (Microsoft.Office.Interop.Excel.Worksheet)xlWbook.Worksheets.get_Item(1);
Microsoft.Office.Interop.Excel.Range xlr = (Microsoft.Office.Interop.Excel.Range)xlSheet.Cells[1, 1];
xlr.Select();

xlSheet.PasteSpecial(xlr, Type.Missing, Type.Missing, Type.Missing, Type.Missing, Type.Missing, true);
```



### Btn Exit
```cs
// Đóng form
this.Close();
// Đóng chương trình
Application.Exit();
// Đóng console
Environment.Exit(0);
```


### Btn Count 
#### Count Total Coulumn with corresponding value using HashMap
doc: [C# Java HashMap equivalent - Stack Overflow](https://stackoverflow.com/questions/1273139/c-sharp-java-hashmap-equivalent)
> C# HashMap == Java Dictionary
```cs
public static int CountSimWithExpirationDate(Product[] mangProduct, string expirationDate)
{
    var hashMap = new Dictionary<Object, int>();

    for (int i = 0; i < mangProduct.Length; i++)
    {
        // if the expire_date column in mangProduct == expirationDate
        if (mangProduct[i].expire_date == expirationDate)
        {
            if (hashMap.ContainsKey(mangProduct[i]))
            {
                hashMap[mangProduct[i]]++;
            }
            else
            {
                hashMap[mangProduct[i]] = 1;
            }
        }
    }

    return hashMap.Count;
}
```
#### Call Function (with desire table using SQL Commands)
> **Column with Corresponding value**
```cs
 SqlConnection connection = null;
 connection = db_lib.MoKetNoi(db_lib.connectionString);
 Product[] mangProduct = db_lib.DocBangProduct(connection, "SELECT * FROM Product");
 
 var count = CountSimWithExpirationDate(mangProduct, "20/10/2023");
 MessageBox.Show("Số sản phẩm hết hạn ngày 20/10/2023: " + count);
```


### Sửa "khuyenMai" với "soSim" tương ứng
#### Edit
```cs
public void edit(string soSim, string khuyenMai)
{
    bool tim_thay = false;

    for (int i = 0; i < dataGridView1.Rows.Count; i++)
    {
        DataGridViewRow row = dataGridView1.Rows[i];
        if (row.Cells["SoSim"].Value == null)
            continue;

        if (row.Cells["SoSim"].Value.ToString() == soSim)
        {
            // Sửa giá trị của sinh viên trong DataGridView
            row.Cells["KhuyenMai"].Value = khuyenMai;
            tim_thay = true;
            break;
        }
    }

    // Nếu sinh viên không tồn tại trong DataGridView, thêm sinh viên mới vào cả DataGridView và cơ sở dữ liệu
    if (tim_thay == false)
    {
        allowMouseMove = true;
        Console.Beep();
        return;
    }

    // Edit in Data Base
    SqlConnection connection = db_lib.MoKetNoi(db_lib.connectionString);
    if (connection == null)
    {
        allowMouseMove = true;
        return;
    }

    db_lib.SuaMotSim(connection, soSim, khuyenMai);
    connection.Close();
    connection.Dispose();

    allowMouseMove = true;
}
```
#### Btn Edit
```cs
string soSim = this.textBoxSoSim.Text;
string khuyenMai = this.textBoxKhuyenMai.Text;

// Kiểm tra xem sinh viên có trong DataGridView hay không
if (soSim.Length == 10)
{
    if (khuyenMai.ToLower() == "x" || khuyenMai.ToLower() == "")
    {
        edit(soSim, khuyenMai);
    }
    else{
        Console.Beep();
        textBoxSoSim.Focus();
    }   
}
else{ 
    MessageBox.Show("Số Sim Không Hợp Lệ");
    textBoxSoSim.Focus();
}
```
