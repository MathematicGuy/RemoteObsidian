
## Object DS
**"Name in String" : value**  
	value can be (str, in boolean, double, etc..) 
```java 
public class EliteBot{
	public String model;
	public String name;
	public int TrainHours;
	public String Field;
}

EliteBot = {
	"model": "F13",
	"name": "Kru",
	"TrainHours": 240,
	"Field": "Medic",
}

```


## ArrayList 
> Has Weird abstract presented Data when printed out
![[Pasted image 20230824152553.png]]
> **Basically a List (but can contain sub_list)** 
The `ArrayList<EliteBot>` is a data structure that can store a collection of EliteBot objects. 
Each EliteBot object has four properties:
	.model
	.name
	.TrainHours
	.Field

The `ArrayList<EliteBot>` can be **visualized** as a **collection of boxes**, each of which **represents an EliteBot object**. The boxes are arranged in a linear order, and **each box contains the four properties of the EliteBot object that it represents.**

For example, the following code creates an ArrayList of EliteBot objects and adds three EliteBot objects to the list:
```java
ArrayList<EliteBot> list = new ArrayList<EliteBot>();

EliteBot bot1 = new EliteBot("F13", "Kru", 240, "Medic");
list.add(bot1);

EliteBot bot2 = new EliteBot("F13.2", "Rot", 299, "Fighter");
list.add(bot2);

EliteBot bot3 = new EliteBot("F13.3", "Mug", 256, "Mentor");
list.add(bot3);
```

###  The list variable now contains three EliteBot objects. Visualize  as follow
```java
[ // array list
	bot1 { 
	  // EliteBot 1
	 "model": "F13",
	 "name": "Kru",
	 "TrainHours": 240,
	 "Field": "Medic"
	},
	
	bot2 { 
	  // EliteBot 2
	 "model": "F13.2",
	 "name": "Rot",
	 "TrainHours": 299,
	 "Field": "Fighter"
	},
	
	bot3 { 
	  // EliteBot 3
	 "model": "F13.3",
	 "name": "Mug",
	 "TrainHours": 256,
	 "Field": "Mentor"
	}
]
```

**extra example**
```java
[ 
	EliteBot1{name='Bot1', health=100, damage=20},
	EliteBot2{name='Bot2', health=150, damage=30},
	EliteBot3{name='Bot3', health=200, damage=40},
]
```

### Access ArrayList 
> Get Items index. Then access Object properties 
> list.get(0) -> Get Object at index 0 (~first Obj)
> 	.model  -> access to model properties inside the Object
```java
b1_model = list.get(0).model; // access it model properties.
b1_name = list.get(0).name; // access it name properties.
b1_TrHrs = list.get(0).TrainHours; // access it TrainHours properties.
b1_Field = list.get(0).Field; // access it Field properties.
```


### Transfer Object to ArrayList Object 
1) Craete an **Objects**
3) Create an **ArrayList Object** with its Length equal to Obj's properties.
```java
  Object rowData[] = new Object[4];
```
4) Add Each Obj properties to each Obj ArrayList slot. Done
```java
for (int  i = 0; i < list.size(); i++){ 
	rowData[0] = list.get(i).model;
	rowData[1] = list.get(i).name;
	rowData[2] = list.get(i).TrainHours;
	rowData[3] = list.get(i).Field;
	
	// add Array date type to table Form
	table_model.addRow(rowData);
	System.out.println(rowData);
}
 
```

**Transform bot1 to bot1_rowData**
```java
bot1 { 
  // EliteBot 1
 "model": "F13",
 "name": "Kru",
 "TrainHours": 240,
 "Field": "Medic"
}

bot1_rowData = [F13, Kru, 240, Medic]
```