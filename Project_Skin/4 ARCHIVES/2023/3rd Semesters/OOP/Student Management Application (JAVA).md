> **Main Object: Connect to DB and manipulate table with SQL command **

**Run Application from terminal withou Ant:**
	java -jar "D:\CODE\JavaProject\HeavenManager\dist\anagrams.jar"

[[JAVA Project SetUp]]
### Some of my note goes here
Name Obj shorter -> Use vowels as sign:
	Ex: + student -> std. + student Count -> stdCount. + User Interface -> UI
Lesson learned: if it not work -> try again form the start. 
### what I have Learned
Part-1: 
	+ How to Create and Use SQL DB on phpMyAdmin with Netbean (java) (download file -> add to library -> connect DB with NetBean)
	+ Basic Design input, output with Swing
+ Think Simple before going Complecated.

degsin UI
+ Add Score
![[Pasted image 20230815113030.png]]

+ Edit / Delete Score
![[Pasted image 20230815111304.png]]

+ Show Score
![[Pasted image 20230815113635.png]]


![[Pasted image 20230817075255.png]]

Fix-bug: duplicate Student Pưrofile and Score
![[Pasted image 20230818092216.png]]

## 1) Connect phpMyAdmin to Create Data Base

>Name your stup, add tables, etc...
![[Pasted image 20230809081157.png]]

2) Download ( mysql-connector-j-8.1.0.jar) & Active 

> And add it to Library
![[Pasted image 20230809081333.png]]
And Active to the DB 
+ Press Admin to go to phpMyAdmin sites
![[Pasted image 20230814135221.png]]

3) Create Java File and Form (Code inside java file and form) 
>File
![[Pasted image 20230814135329.png]]

>Image folder of choice for UI beautify.
![[Pasted image 20230814134903.png]]

## Connect & Design
### MyConnction (Connect to DB Function) 
Connect to DB with 2 Line of Code. (1 connect to the Driver package, 1 connect to the DB) 
```java
Class.forName("com.mysql.cj.jdbc.Driver");
con = DriverManager.getConnection("jdbc:mysql://localhost:3307/stdmgdb", "root", ""); 
```
> Set "con" as the gate way to the Date Base (connection)
```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;

// using phpMyAdmin
public class MyConnection {
    public static Connection getConnection(){
        Connection con = null; // set connection link to null by Default
        
        try {
            // change deprecated path "com.mysql.jdbc.Driver" to "com.mysql.cj.jdbc.Driver" 
            Class.forName("com.mysql.cj.jdbc.Driver");
            // connect to DB in phphMyAdmin by user name "root" with No password
            con = DriverManager.getConnection("jdbc:mysql://localhost:3307/stdmgdb", "root", "");
        } catch (ClassNotFoundException | SQLException ex) {
            System.out.println(ex.getMessage()); // catch error if not connected
        }        
        return con; // return connection when called
    }
}
```

### Login Form
Desgin architect:
	Login - Cancel
	Password - Username 
		Take input Data and Send it to DB. 
		Checking "user" table data with user input if matched => Open MainForm Frame. 
```java
// get connection 
Connection con = MyConnection.getConnection();
PreparedStatement ps;

// Checking user password 

// Take and Set UserName and Password from DB table and assigned it to TextField
// select all data of username and password in "user" table
ps = con.prepareStatement("SELECT * FROM user WHERE username = ? AND password = ?");

ps.setString(1, jTextField1_UserName.getText());
ps.setString(2, String.valueOf(jPasswordField.getPassword()));

// execute connection
ResultSet rs = ps.executeQuery();
```

> **Code HighLight:** 
> + The prepared statement can insert the user input into the SQL query without concatenating strings, which can prevent SQL injection attacks and improve performance.
> + ? act as an input format  like { } in python.
```java
ps = con.prepareStatement("SELECT * FROM user WHERE username = ? AND password = ?");

ps.setString(1, jTextField1_UserName.getText());
ps.setString(2, String.valueOf(jPasswordField.getPassword()));
``` 

![[Pasted image 20230810080427.png]]

> Set Main Form to be Visible and Count its in refer table
```java
// If Login
// If rs is valid then taking nex() action
 if (rs.next()){
	
	  // Main Form 
	  // set MainForm visible to true
	  MainForm mf = new MainForm();
	  mf.setVisible(true);
	  mf.pack();
	  mf.setLocationRelativeTo(null);
	  
	  // Change Label in Form
	  MainForm.jLabel1_UserName.setText("Welcome < "+jTextField1_UserName.getText()+" >");
	  // count total element in refered DB table
	  MainForm.jLabel2_stdCount.setText(" Students Count : " + Integer.toString(MyFunction.countData("student") ));
	  MainForm.jLabel2_crsCount1.setText(" Courses Count : " + Integer.toString(MyFunction.countData("course") ));
	  
	  this.dispose();
```

### MainForm 
>Contain Add Student Button
>	When triggered, Open "AddStudentForm" 
>		If AddStudentForm close  <-> not also dispose MainForm
```java
private void jMenuItem1AddStudentActionPerformed(java.awt.event.ActionEvent evt) {                                                     
  // Open Add Student Form
  System.out.println("Redirect to Form >> Add Student >>");
				  
  // set MainForm visible to true when Btn Pressed
  AddStudentForm addstd = new AddStudentForm();
  addstd.setVisible(true);
  addstd.pack();
  addstd.setLocationRelativeTo(null);
  // Avoid parralel dispose of Main & AddStudent Form 
  addstd.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
}       
```
>+ Student Count are Already Updated at LoginForm 
![[Pasted image 20230810082215.png]]

### Question mark in SQL
Question mark index start from 1.
So if you want to access third value of DB table -> 3 is its index.
```java
ps = con.prepareStatement("INSERT INTO student(firstName, lastName, sex, birth, phone, address) VALUES (?,?,?,?,?,?)");
// set value to the 2rd prepare statement
ps.setString(2, lastName)
```
### Student (Object) 
> **With these datas do this do that**
> => Act as an Object which taken input Data. And Capaple of Doing certain action with its.
#### Insert/Delete/Update Obj (student) by demand Function 
>  + Handle new Student Insertion, Deletion & Update by input using Switch-Case or If/Else
```java
public void insertUpdateDeleteStudent(char operation, Integer id, String fName, String lName,
  String sex, String bdate, String phone, String address) {

  Connection con = MyConnection.getConnection();
  PreparedStatement ps;

  // i for insert
  // Caution: ' ' for char " " for String
  if (operation == 'i') {
		try {
			 // if want to get data from DB table. Must goes use 'con' as a conenctor
			 ps = con.prepareStatement("INSERT INTO student(firstName, lastName, sex, birth, phone, address) VALUES (?,?,?,?,?,?)");
			 ps.setString(1, fName);
			 ps.setString(2, lName);
			 ps.setString(3, sex);
			 ps.setString(4, bdate);
			 ps.setString(5, phone);
			 ps.setString(6, address);
		
			 if (ps.executeUpdate() > 0) {
				  JOptionPane.showMessageDialog(null, "New Student Address");
			 }

		} catch (SQLException ex) {
			 Logger.getLogger(student.class.getName()).log(Level.SEVERE, null, ex);
		}
  }
}
```

**conclusion:**
> Set value statement don't need to be inline ( 1,2,3,4,5... ). Also don't need to fill in all column. Only update the forth or the third value is fine.
	![[Pasted image 20230814142603.png]]

#### Fill Table with "student" table data  

> 1) Get Data of ( "firstName", "lastName", "phone", "address" ) from "student"  table that have "%text%" init.
> 2) Declare an array (Row) to store student info
> 3) Add student data to Row one by one
> 4) Add Row to my table Model
``` java
public void fillStudentJtable(JTable table, String valueToSearch) {
	  Connection con = MyConnection.getConnection();
	  PreparedStatement ps;
	  try {
			// Get all data in refered column from student table that have %something% init
			ps = con.prepareCall("SELECT * FROM `tableName` WHERE CONCAT(`column1`, `column2`, `column3`, `column4`)LIKE  ?");
			// set ? from %valuetoSearch%. 1 because that the first quesiton mark 
			ps.setString(1, "%" + valueToSearch + "%");

			// execute table with command above 
			ResultSet rs = ps.executeQuery();
			// assign Defualt table model 
			DefaultTableModel model = (DefaultTableModel) table.getModel();
			// set each student Object data as row
			Object[] row;

			// get student info from data base (data present in row)
			while (rs.next()) {
				 // innitialize array length
				 row = new Object[7];
				 // assigned data to row array
				 row[0] = rs.getInt(1); // Id
				 row[1] = rs.getString(2); // Fname
				 row[2] = rs.getString(3); // Lname
				 row[3] = rs.getString(4); // Sex
				 row[4] = rs.getString(5); // Birthdate
				 row[5] = rs.getString(6); // Phone
				 row[6] = rs.getString(7); // Address

				 // add row array to my table model
				 model.addRow(row);
			}

	  } catch (SQLException ex) {
			Logger.getLogger(student.class.getName()).log(Level.SEVERE, null, ex);
	  }
 }
```


### AddStudentForm 
> **Get & Set Student data to DB (phpMyAdmin) 
> 	using student's class function**

#### verify text
> Checking if there any Empty Text Field. BirthDate is after current Date. 
```java
public boolean verifyText() {
	  if (jTextField1_FirstName.getText().equals("")
				 || jTextField1_LastName.getText().equals("")
				 || jTextField_Phone.getText().equals("")
				 || jTextArea_Address.getText().equals("")
				 || jDateChooserBirthDate.getDate() == null) {
			JOptionPane.showMessageDialog(null, "One Or More Empty Field");
			return false;
	  } // choose a Date higher than the current date
	  else if (jDateChooserBirthDate.getDate().compareTo(new Date()) > 0) {
			JOptionPane.showMessageDialog(null, "No Student from the Future are Allowed");
			return false;
	  } // return True by Default if not False
	  else {
			return true;
	  }

 }
```

#### add student
>  Get datas from TextFields and verify it. If true Add student Obj to data base. 
```java
private void jButtonAddStudentActionPerformed(java.awt.event.ActionEvent evt) {                                                
        // Get data from Text Field 
        String fname = jTextField1_FirstName.getText();
        String lname = jTextField1_LastName.getText();
        String phone = jTextField_Phone.getText();
        String address = jTextArea_Address.getText();
        
        // Male by default. Female by Choice
        String sex = "Male";
        if (jRadioButtonFemale.isSelected()) {
            sex = "Female";
        }

        if (verifyText()) {
            // Set & Get date format
            SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");
            String bdate = dateFormat.format(jDateChooserBirthDate.getDate());

				// Create new student Obj with inserted data
            student std = new student();
            std.insertUpdateDeleteStudent('i', null, fname, lname, sex, bdate, phone, address);
            // re-count student after Insert 
            MainForm.jLabel2_stdCount.setText(" Students Count : " + Integer.toString(MyFunction.countData("student")));
        }
    }  
```

> UI
![[Pasted image 20230810082636.png]]


### Manage Student Form
> Modify, Add, Delete Student direct from Data Base (phpMyAdmin)

![[Pasted image 20230810105638.png]]



### AddStudentForm 


## Error & Mistake
### connnection is null (Solved)
**con** not connect to phpAdmin server.
	![[Pasted image 20230809074850.png]]
Diagnosed: Wrong database library package.
Sol: choose correct path. Reason: not paying close attention to vid turtorial.
![[Pasted image 20230809075108.png]]

### Not Suggest Obj in Frame
 Need connecting Obj from other Frame? here the solution
![[Pasted image 20230809090526.png]]
Sol: Select Need to Connect Obj -> Customized Code -> enable public & static 
![[Pasted image 20230809090653.png]]

### char & string error
![[Pasted image 20230809162606.png]]



### Can't run file, file missing core function
**At first I think it didn't run suddently, all SWING design can't be conencted**
> Solution: Checking if there anything missing like Main. Check CODE HISTORY to go back when there're no Errors
> 	Because Main Support special Function to run file Using SWING.
> 	 => If don't know what it is. Design the file again.
> 	 + Problem found: Missing Main function for table
![[Pasted image 20230810190117.png]]
**Lack the "Look & Feel" package and something else** 
![[Pasted image 20230810191514.png]]


### Unorder Table Form
![[Pasted image 20230811012542.png]]
Solution: Change Default row number to 0
![[Pasted image 20230811014808.png]]


# Sort SQL to jTable
https://youtu.be/trWVSIq-6Mo?si=Uu4vtsDh91M7a4tV

# Bugg
![[Pasted image 20230811021132.png]]



### "id" is null. Cannot Add student Obj to the DB.
![[Pasted image 20230811090540.png]]
diagnoses: Checking Code history.

**Mistake & Reason:** I use UPDATE STUDENT SQL command for  INSERT STUDENT METHOD. 
	![[Pasted image 20230811094755.png]]

**SHOULD BE with no Id Clarify** (because Id already have AUTO_INCREMENT)
![[Pasted image 20230811113812.png]]
```java
ps = con.prepareStatement("INSERT INTO student(firstName, lastName, sex, birth, phone, address) VALUES (?,?,?,?,?,?)");
```
**INSTEAD OF**
```JAVA
ps = con.prepareStatement("UPDATE `student` SET `firstName`= ?,`lastName`= ?,`sex`= ?,`birth`= ?,`phone`= ?,`address`= ? WHERE `id` = ?");
ps.setInt(7,id)
```
### Add Background to JFrame
Set **Layout to Absolute**
+ Get Lable -> Set icon to the Label.
![[Pasted image 20230811143023.png]]

### Error at Score: No value specified for parameter 5
Reason:
**There're 5 parameter (Question mark) while there only 4 values** (`student_id`, `course_id`, `student_score`, `description`)
	ps = con.prepareStatement("INSERT INTO `score`(`student_id`, `course_id`, `student_score`, `description`) VALUES (?,?,?,?,?)");
![[Pasted image 20230815152846.png]]

Fix: reduce the question mark (parameter) to 4 since to match 4 value
	ps = con.prepareStatement("INSERT INTO `score`(`student_id`, `course_id`, `student_score`, `description`) VALUES (?,?,?,?)");
![[Pasted image 20230816215015.png]]

### Illegal start of Expression


### Values type error between Local code &  DB

**Wrong value types.**
![[Pasted image 20230817150029.png]]

firstName should be string
![[Pasted image 20230817145950.png]]




Reasons: Unmatched Key. Key in {} of Object array must be identical to those in DB tables 
![[Pasted image 20230818171446.png]]
![[Pasted image 20230818171502.png]]

### corresponds to your MariaDB server version for the right syntax to use near 'WHERE id= 29' at line 1
Bug near WHERE id=29
> WHen it say near, it mean NEAR. CLOSE YOUR EYES AND LOOK FOR IT.
![[Pasted image 20230818153015.png]]

![[Pasted image 20230818204536.png]]


### Exception in thread "AWT-EventQueue-0" java.lang.NullPointerException: Cannot invoke "javax.swing.JTable.setModel(javax.swing.table.TableModel)" because "ManageStdForm2.jTableStd" is null 
##### *This mean the JTable doesn't exist*
![[Pasted image 20230912180109.png]]
> **Mistake: Count jTable before it even Declare and Initiate** 
![[Pasted image 20230912175757.png]]

**-> Solve: put Count JTable after a new JTable has been created**  
