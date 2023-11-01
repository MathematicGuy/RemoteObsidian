(db_lib)

## Properties and Connect
#### Class Properties
```cs
public class Sim
{
	public string simID;
	public string soSim;
	public string ngayKichHoat;
	public string ngayHetHan;
	public string ghiChu;
} // Sim
```

#### Connect to Database
![[Pasted image 20231004111059.png]]

```cs
public static String connectionString = "Server=macbookM5\\SQLEXPRESS;Database=SimThe;User ID=sa;Password=cmcuni;";

public static SqlConnection MoKetNoi(string connectionString)
{
    SqlConnection connection = null;
    
    connection = new SqlConnection(connectionString);
    try
    {
        connection.Open();
        return connection;
    }
    catch
    {
        return null;
    }
}// MoKetNoi
```

#### Read Table with SQL Command 
>**Read SQL Table -> Return an List**
```cs
// create a list
public static List<Sim> ListSim (SqlConnection connection, string sql_command)
{
    List<Sim> listSim = new List<Sim>();
    // invalid value -> the "SELECT * FROM Students" is wrong
    //SqlCommand command = new SqlCommand("SELECT * FROM SimThe", connection);
    SqlCommand command = new SqlCommand(sql_command, connection);
    SqlDataReader reader = command.ExecuteReader();

    while (reader.Read())
    {
        // add data to Object
        Sim ob1 = new Sim();
        ob1.simID = (string)reader["SimID"];
        ob1.soSim = (string)reader["SoSim"];
        ob1.ngayKichHoat = (String)reader["NgayKichHoat"];
        ob1.ngayHetHan = (String)reader["NgayHetHan"];
        ob1.ghiChu = (string)reader["ghiChu"];
        listSim.Add(ob1); // add Obj to list
    }//while

	    // Stop reader
    reader.Close();
    command.Dispose();

    // return Objs list
    return listSim;
}
```

> **Turn List into Array -> Manipulate Array with SQL Commands**
```cs
// Manipulate Table with SQL code. Take (list and SQL Command as Input)
public static Sim[] DocBangSim(SqlConnection connection, string sql_command)
{
	 Sim[] mangSim = ListSim(connection, sql_command).ToArray();

	 return mangSim;
}// DocMangSim
```
Ex:
```cs
//Gọi hàm đọc thông tin sinh viên
arraySim = db_lib.DocBangSim(connection, "SELECT * FROM Sim");
arraySimNgay = db_lib.DocBangSim(connection, "SELECT * FROM Sim WHERE NgayHetHan = '2023-08-14'");
```

#### Insert (Take Parameter as Inserted Value)
```cs
public static void GhiMotSim(SqlConnection connection, string simID, string soSim, string ngayKichHoat, string ngayHetHan, string ghiChu)
{
	string query = "INSERT INTO Sim (SimID, SoSim, NgayKichHoat, NgayHetHan, GhiChu) VALUES (@SimID, @SoSim, @NgayKichHoat, @NgayHetHan, @GhiChu)";
	SqlCommand command = new SqlCommand(query, connection);

	command.Parameters.AddWithValue("@SimID", simID);
	command.Parameters.AddWithValue("@SoSim", soSim);
	command.Parameters.AddWithValue("@NgayKichHoat", ngayKichHoat);
	command.Parameters.AddWithValue("@NgayHetHan", ngayHetHan);
	command.Parameters.AddWithValue("@GhiChu", ghiChu);
	command.ExecuteNonQuery();

	connection.Close();
	connection.Dispose();
}// GhiMotSim
```

#### Edit
```cs
public static void SuaMotSim(SqlConnection connection,string SimID, string SoSim, string GhiChu)
{
	string query = "UPDATE Sim SET SoSim = @SoSim, GhiChu = @GhiChu WHERE SimID = @SimID";
	SqlCommand command = new SqlCommand(query, connection);

	command.Parameters.AddWithValue("@SimID", SimID);
	command.Parameters.AddWithValue("@SoSim", SoSim);
	command.Parameters.AddWithValue("@GhiChu", GhiChu);

	command.ExecuteNonQuery();

	connection.Close();
	connection.Dispose();
}
```

#### Delete
```cs
public static void XoaSim(SqlConnection connection, string m_simID)
{
	string query = "DELETE FROM Sim WHERE SimID = @SimID";
	SqlCommand command = new SqlCommand(query, connection);
	command.Parameters.AddWithValue("@SimID", m_simID);
	command.ExecuteNonQuery();

	connection.Close();
	connection.Dispose();
}// XoaSinhVien
```


#### Hash Map
Để đếm nhanh số đối tượng Sim của mangSim có ngày hết hạn là “20/10/2023” sử dụng cấu trúc dữ liệu HashMap của C# bạn có thể sử dụng đoạn mã sau:
```cs
public static int CountSimWithExpirationDate(Object[] mangSim, string expirationDate)
{
    var hashMap = new Dictionary<Object, int>();

    for (int i = 0; i < mangSim.Length; i++)
    {
        if (mangSim[i].ExpirationDate == expirationDate)
        {
            if (hashMap.ContainsKey(mangSim[i]))
            {
                hashMap[mangSim[i]]++;
            }
            else
            {
                hashMap[mangSim[i]] = 1;
            }
        }
    }

    return hashMap.Count;
}
```
Trong đoạn mã trên, `mangSim` là mảng chứa các đối tượng Sim, `expirationDate` là ngày hết hạn của Sim cần đếm. Hàm `CountSimWithExpirationDate` sẽ trả về số lượng đối tượng Sim có ngày hết hạn là “20/10/2023”.

Bạn có thể gọi hàm này trong chế độ Console hoặc ở form khi nhấn chuột vào 1 nút “Đếm số sim”. Tuy nhiên, để sử dụng được hàm này, bạn cần phải chỉnh sửa lại mã để phù hợp với cấu trúc dữ liệu và thuộc tính của đối tượng Sim trong chương trình của mình


