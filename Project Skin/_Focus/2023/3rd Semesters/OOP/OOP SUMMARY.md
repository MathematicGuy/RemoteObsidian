note: re-check inheritance
get the whole view -> organize the main point -> throughly explain -> get deep 
# Person

interface 
	calculateKPI()

**4 Classes**
*Main*
Person
+ 3 attributes: str(name, gender), int(age)
+ abstract getRole()

*Sub-Classes*
p1 - DECLARATION 
	declare independent value.
	get(), set() -> value as demand. where get return a self-value, set take input parameter as value.   

p2 - SET UP
	class main(str value1, str value2, int value3, etc...)
		call get/set function
		super() -> inherit from its parent class



(inherit, extends from Person)
	TeachingAssistant 
	Lecturer 
(inherit, extend from Lecturer)
	Professor 
		public static int countProfessor = 0

p3 - Override function
	@Override function() 
	note: this function can also be inherit with super()
	Ex: int inherit_an_overrideFunc = super.calculateKPI() 


# Main

*p1 - Debugging by creating Obj*
Enable Vietnames (UTF-8)
```java
public static void main(String[] args)throws UnsupportedEncodingException,IOException,InterruptedException {
  System.setOut(new PrintStream(System.out, true, "UTF-8"));
}
```

**Create new Object by Calling new Class (for testing)**
Class Obj_name1 = new Class(attributes);
or 
Class Obj_name1;
Obj_name1  = new Class(attributes);

**Declare an Array**
```java
ArrayList<Class> array_name =  new ArrayList<Class>()];
array_name.add(Obj_name)
```

*p2 - Declaration*
declare "sc" as  "Scanner" for extracting input from terminal. (by import) 
```java
Scanner sc;
sc = new Scanner(System.in)
new_input = sc.nextline();
```
try-catch 
```java
try{

}catch (Exception e){
	System.out.println("Warning Text !!!");
}
```
Add Input Obj to ArrayList
	take string as input -> Parse String input to Int -> if error, try-catch. 
		Create new Obj with given input
		add new Obj to ArrayList
	Declare Sub-classes independent attributes values
		like employeeID, numberOf...  that each sub-class have




*p3 - Print Results*


"TypeCasting" to get the right ID for each Obj 
Get value of each Object from List(name, age, gender, role) 
	and special value from Obj interface (kpiEvaluator).



*p4 - Input*
(have repeated-pattern)
Convert value. Str to Int with Integer.parseInt()

Indepent function for add 
+ AddLecturer
+ AddProfessor
+ AddTeachingAssistant

try-catch() 
	take input as string. and catch error after convert to int...


*p5 - Call JFrame (after Design java Frame)* 
```java
sc.nextline();
// set JFrame as pf
PersonsFrame pf;
// get ArrayList as data
pf = new PersonsFrame(EmployeeList);

// feedback if ArrayList is empty (null)
if (pf.list_nhanvien == null)
	JOptionPane.showMessageDialog(null,"List sv null");
// set position and visability
pf.setLocationRelativeTo(null);
pf.setVisible(true);
```

# Design 

![[Pasted image 20231002101646.png]]

*p1 - Implement ArrayList as JFrame Table*
**JFrame table take List as Row**

declare ArrayList

**Class Main**
	give ArrayList take JFrame ArrayList input as value

declare new Table model
	set current Model from JFrame as default table model 
declare new Object List (store all ArrayList Obj)

For each Obj from ArrayList, add the Obj attribute to a new Obj List 
	add new Obj List to the Table Model (add new Row to Table Model)


*p2 - Button* 
	todo: optimize btn code

**Search** (Core Btn)
![[Pasted image 20231002102404.png]]

Check for Case Sensitive
```java
Pattern p = Pattern.compile("[^a-z0-9 ]", Pattern.CASE_INSENSITIVE);
// return true if "There is a special character" 
Matcher m = p.matcher(jTextFieldSearch.getText());
boolean b = m.find();
```
Response if Obj Exist but Invalid 
```java
// check input length
if (jTextFieldSearch.getText().length() != 4){
	System.out.println(jTextFieldSearch.getText().length());
	JOptionPane.showMessageDialog(new PersonsFrame(list_nhanvien), "Mã nhân sự không hợp lệ, chỉ nhập 4 ký tự");
	jTextFieldSearch.grabFocus();
}
// catch special char
else if (b == true){
	JOptionPane.showMessageDialog(new PersonsFrame(list_nhanvien), "Mã nhân sự không hợp lệ, chỉ nhập chữ số");
	jTextFieldSearch.grabFocus();
}
```
Check if Obj exist or not by ID. If Found -> set focus. showMessageDialog
```java
else{
	// jTextFieldSearch.grabFocus();
	// get Focus on Searched Row
	boolean found = false;
	for (int row=0;row<jTable1.getRowCount();row++){
		 // get Obj value at 0: ID 
		 String ObjID = jTable1.getValueAt(row, 0).toString();
		 if (jTextFieldSearch.getText().equals(ObjID)){
			  jTable1.requestFocus();
			  jTable1.setRowSelectionInterval(row, row);
			  found = true;
			  JOptionPane.showMessageDialog(new PersonsFrame(list_nhanvien),"TÌM THẤY: Họ và tên: " + jTable1.getValueAt(row, 1) + ", Tuổi: " + jTable1.getValueAt(row, 2) + ", Giới tính: " +                  jTable1.getValueAt(row,3) + ", Chức danh: " + jTable1.getValueAt(row, 4), "Thông tin", JOptionPane.INFORMATION_MESSAGE);
			
			  break;
		}
	}	
}                

// Run After Checking all EmployeeId in jTable
if (found == false){
	 JOptionPane.showMessageDialog(this, "Không Tìm Thấy");
}
```



**Exit**
```java
System.exit(0);
```


**Delete** -> Search then Delete
Delete Searched Row
```java
obj.removeRow(row);
```


**Sort (Max/Min)** (by age)
*p1 - SortMax*
+ Take ArrayList as input
+ SortMax(ArrayList)
+ return SortedArrayList

*p2 - addSortedRow(SortedArrayList) to Table*
+ get SortedArrayList from SortMax() 
+ Delete current jtable
+ Create a new ArrayList, JTable
+ Add each Obj as Row to jTable

*p4 - reverted ArrayList*
using backward for loop ( scan from len(ArrayList) to 0 ) 

*p4 - Sort_Min* (reverse SortMax array)
+ Take ArrayList as input
+ ArrayList = SortMax(ArrayList)
+ addSortedRow(reverseArrayList(ArrayList))   .



*p3 - effect*
+ Blur by Default

if "Search Obj exist -> Search btn active" 
Use "ActiceListener" to scan for new Event each 0.5 second
	if conditin met Active Search btn






Export
```java
String fileName = "StdScore.csv";
String filePath = "D:\\CMC_UNI\\CNTT\\Object Oriented Programming\\FileStorage\\"+fileName;
File file = new File(filePath);
try {  
	FileWriter fw = new FileWriter(file);
	BufferedWriter bw = new BufferedWriter(fw);

	bw.write("StudentID, FirstName, LastName, Course, Score\n");
	for (int i = 0; i<jTableShowAll.getRowCount(); i++){ // Row
		 for (int j = 0; j<jTableShowAll.getColumnCount(); j++){ // Coulumn
			  bw.write(jTableShowAll.getValueAt(i, j).toString()+", ");
		 }
		 bw.newLine();
	}
	
	bw.close();
	fw.close();
	try {
		 Desktop.getDesktop().open(new File("D:\\CMC_UNI\\CNTT\\Object Oriented Programming\\FileStorage\\" + fileName));
	} catch (IOException ex) {
		 Logger.getLogger(showScoreForm.class.getName()).log(Level.SEVERE, null, ex);
	}

	
} catch (IOException ex) {
	Logger.getLogger(showScoreForm.class.getName()).log(Level.SEVERE, null, ex);
}
```

