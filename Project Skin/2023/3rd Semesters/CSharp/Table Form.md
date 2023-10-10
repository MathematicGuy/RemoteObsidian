### Load Table
```cs
private void FormTable_Load(object sender, EventArgs e)
{
  //row["id"] = reader["id"];
  //row["name"] = reader["name"];
  //row["expire_date"] = reader["expire_date"];
  //row["price"] = reader["price"];
  //row["note"] = reader["note"];

  dataGridView1.Columns.Add("id", "id");
  dataGridView1.Columns.Add("name", "name");
  dataGridView1.Columns.Add("expire_date", "expire_date");
  dataGridView1.Columns.Add("price", "price");
  dataGridView1.Columns.Add("note", "note");

  for (int i = 0; i < table_product.Rows.Count; i++)
  {
		DataRow row = table_product.Rows[i];
		object[] rowData = row.ItemArray; // Lấy dữ liệu từng dòng dưới dạng mảng object
		// Thêm dữ liệu vào DataGridView bằng cách tạo mới hàng và thêm vào DataGridView
		int rowIndex = dataGridView1.Rows.Add(rowData);
  }

  //textBox1.Enabled = false;
  this.textBox1.Focus();
  // Gán sự kiện CellEnter cho DataGridView
}
```


### Cell Mouse Move
> Turn on "dataGridView1_CellMouseMove" -> Send Data back to TextBox
```cs
 private void dataGridView1_CellMouseMove(object sender, DataGridViewCellMouseEventArgs e)
 {
     if (allowMouseMove == false)
         return;

     // Lấy dòng hiện tại khi di chuyển phím mũi tên lên xuống
     DataGridViewRow currentRow = dataGridView1.CurrentRow;
     // Kiểm tra xem có dòng nào đang được chọn hay không
     if (currentRow != null)
     {
         this.textBox1.Text = currentRow.Cells["SoSim"].Value.ToString(); // TextBox SoSim 
     }//if
 }
```
![[Pasted image 20231004104753.png]]



