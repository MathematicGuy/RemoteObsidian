![[Pasted image 20230821142456.png]]
Pros: It does the job as long it was Blackout.
Cons: Visual errors when Pasting it to Excel. Need to press to see the real data.

**Prep: Set main file table output to be Single Threaded**
>  [STAThread] at top of the Main program.
![[Pasted image 20230821142742.png]]

> **Thread line setting before** Application.Run(frm1);
```cs
// Make Thread to be Single
System.Threading.Thread.CurrentThread.ApartmentState = System.Threading.ApartmentState.STA;
// Chạy form
Application.Run(frm1);
```


**Button_Code**
```cs
private void exportExcel_Click(object sender, EventArgs e)
{
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
}
```