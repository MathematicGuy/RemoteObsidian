

```cs
operation = "-"
switch (operation)
{
	case "-":
		MessageBox.Show("Định dạng không hợp lệ")
}
```

```cs
try{

}
catch(FormatException)
{

}
```

```cs
private void exitButton_Click(object sender, EventArgs e)  
        { 
	         // Hiển thị hộp thoại xác nhận thoát 
            DialogResult result = MessageBox.Show("Bạn có chắc chắn muốn thoát không?", "Thoát", MessageBoxButtons.YesNo, MessageBoxIcon.Question);               
  
            if (result == DialogResult.Yes)  
            {  
	            // Đóng ứng dụng nếu người dùng chọn "Có"
                Application.Exit();   
            }  
        }
```
![[Pasted image 20230629135825.png]]
	Text Appear 
	Text Close
	MessageBoxButtons.YesNo
	MessageBoxIcon.Question



