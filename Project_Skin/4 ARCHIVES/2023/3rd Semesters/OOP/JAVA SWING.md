
![[Pasted image 20230824084225.png]]
## Add Row 
**Table take List as Row**
	**Object store value  as ArrayList (ArrayList - Lists in List)**
> The code snippet you provided is a Python function called **add_row()**. This function takes three arguments: **model, name**, and **train_hours**
> + The **model argument is a list of lists**, where each inner list **represents a row in the data model**
> + Object is list that Store added lists. 
#### code in JAVA SWING
```java
model.addRow(new Object[]{IModel, IName, ITrainHours});
"list in Object[]" -> [['IModel', '100', 'ML'], ['IName', '200','NLP'], ['ITrainHours', '300','CV']]
```
#### simplify code in java
```java
public void addRow(List<List<String>> model, String name, int trainHours) {
  List<String> row = new ArrayList<>();
  row.add(name);
  row.add(String.valueOf(trainHours));
  model.add(row);
}

List<List<String>> model = new ArrayList<>();

addRow(model, "IModel", 100);
addRow(model, "IName", 200);
addRow(model, "ITrainHours", 300);

System.out.println(model);
```


## Select jTable Row 
```java
table.setRowSelectionInterval(0, 0);
```

### .setRowSelectionInterval() (khoảng lựa chọn)

The `setRowSelectionInterval()` method is used to select a range of rows in a `JTable`. Here is an example of how to use this method:

```java
JTable table = new JTable(data, columnNames);
table.setRowSelectionInterval(0, 0); // selects the first row
```

This code creates a new `JTable` object with the specified data and column names. Then, it uses the `setRowSelectionInterval()` method to select the first row of the table. The first argument of this method specifies the starting index of the selection interval, and the second argument specifies the ending index. In this case, both arguments are set to 0, so only the first row is selected.

You can also keep the current selection and simply add additional rows by using this code:

```java
table.getSelectionModel().addSelectionInterval(index0, index1);
```

## Delete TTTTable
```java
jTable1.setModel(new DefaultTableModel(null, new String[]{"Mdel", "Name","Train Hours","Field"}));
```

## Selection UI
### JSpinner
#### Customize Code + getValue()
```java  
jSpinnerHours.setModel(new javax.swing.SpinnerNumberModel(5, 4, 300, 1));
String value = spinner.getValue();

```
> Customize code with Current value, Min value, Max Value, Initial value
- The initial value of the spinner
+ The minimum value of the spinner
- The maximum value of the spinner
- The step size of the spinner
![[Pasted image 20230824095823.png]]


### JComboBox
#### addItem() + removeAllItems() + setSelectedIndex() + getSelectedItem();
```java
import javax.swing.*;

public class SetJComboBoxEmpty {

    public static void main(String[] args) {
        // Create a JComboBox
        JComboBox comboBox = new JComboBox();

        // Add the values "Option 1", "Option 2", and "Option 3" to the JComboBox
        comboBox.addItem("Option 1");
        comboBox.addItem("Option 2");
        comboBox.addItem("Option 3");

        // Clear the items in the JComboBox
        comboBox.removeAllItems();

        // Set the selected index of the JComboBox to -1
        comboBox.setSelectedIndex(-1);  

        // Display the JComboBox
        System.out.println(comboBox.getSelectedItem());
    }
}
```

### JRadioButton
![[Pasted image 20230824090943.png]]
#### isSelected() + setSelected()
```java
// Male by default. Female by Choice
String sex = "Male";
if (jRadioButtonFemale.isSelected()) {
	sex = "Female";
}

// set status
jRadioButtonMale.setSelected(true);
jRadioButtonFemale.setSelected(false);
```


### Faded Button when TextField is Empty
Main
```java
initComponents();
timer.start(); 
```

```java
Timer timer = new Timer(50, new ActionListener(){
	  @Override
	  public void actionPerformed(ActionEvent e) 
	  {
			if (jTextFieldSearch.getDocument().getLength() != 4)
			{
				 jButton_TimKiem.setBackground(Color.lightGray);
				 jButton_TimKiem.setForeground(Color.GRAY);
				 jButton_TimKiem.setEnabled(false);
			}
			else
			{
				 jButton_TimKiem.setBackground(Color.white);
				 jButton_TimKiem.setForeground(Color.black);
				 jButton_TimKiem.setEnabled(true);
			}
	  }
 });
```


## Add Row 
> **model.addRow(new Object [ ] { value1, value2, value3, value4 });**
```java
// make get table model from JFrame table model 
DefaultTableModel model = (DefaultTableModel)jTable1.getModel();

// IModel mean Input Model
String IModel = jTextFieldModel.getText();
String IName = jTextFieldName.getText();

// spinner
Integer ITrainHours = Integer.valueOf(jSpinner_TrainHours.getValue().toString());
// combo box
String IField = jComboBox_Field.getSelectedItem().toString();

model.addRow(new Object[]{IModel, IName, ITrainHours, IField});
```


## Update Row 

#### table_model.setValueAt( Sets_Value, selected_Row , selected_Column);

```java
// Update Row
int selectedRow = jTable1.getSelectedRow();
DefaultTableModel model = (DefaultTableModel) jTable1.getModel();

if (selectedRow > 0){
	// set value for table model 
	// setValueAt(A_Value, Row, Column)
	model.setValueAt(jTextFieldModel.getText(), selectedRow , 0);
	model.setValueAt(jTextFieldName.getText(), selectedRow , 1);
	model.setValueAt(jSpinner_TrainHours.getValue(), selectedRow, 2);
	model.setValueAt(jComboBox_Field.getSelectedItem(), selectedRow, 3);	
}

else{
	JOptionPane.showMessageDialog(null, "Please Select a Bot to Modify");
}
```


## Get Value on MouseClick()
> Get from table model at (row;column) to Input 
#### table_model.getValueAt(selectedRow, selectedColumn)
```java
int selectedRow = jTable1.getSelectedRow();
DefaultTableModel model = (DefaultTableModel) jTable1.getModel();
// TextField
jTextFieldModel.setText(model.getValueAt(selectedRow, 0).toString());
jTextFieldName.setText(model.getValueAt(selectedRow, 1).toString());
// Spinner
jSpinner_TrainHours.setValue(Integer.valueOf(model.getValueAt(selectedRow, 2).toString()));
// ComboBox
jComboBox_Field.setSelectedItem(model.getValueAt(selectedRow, 3).toString());
```



## Tab Order & set Focus
Next Component to be focus on
![[Pasted image 20230905165145.png]]
And Set Focus
```java
.grabFocus();
```

## Display Date In Jtable from JDateChooser
```java
SimpleDateFormat dFormat = new SimpleDateFormat("yyy-MM-dd");
String date = dFormat.format(jDateChooser1.getDate());
DefaultTableModel model = (DefaultTableModel) jTable1.getModel();
model.addRow(new Object[]{date});
```


## Load and Clear Jtable Data
## Set Data
![[Pasted image 20230906202159.png]]
### Show Data
![[Pasted image 20230906202212.png]]

## Clear
![[Pasted image 20230906202241.png]]



## Display JTable Selected Rows To Another JFrame JTabel Using Java


