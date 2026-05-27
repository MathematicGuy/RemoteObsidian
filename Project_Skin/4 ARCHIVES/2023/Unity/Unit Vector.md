```cs
if (Input.GetKeyDown(KeyCode.Space) == true)
{
	// multiply **Time.deltaTime** to update speed by time not by frame.
	rigidBody.velocity = Vector2.up * Unit * Time.deltaTime;
	rigidBody.velocity = Vector3.down * Unit * Time.deltaTime;
	
}

```



### Moving Obj Using its transform 
> Moving with it own Orientation (Child) instead of The Word (Parent) 
![[Pasted image 20230630084730.png]] 

```cs
// Setting new Position relative to its old position
transform.position = new Vector3(1, 0, 0);


// Move Obj by a certain Amounts everytime its Called.
transform.translate(Vector2 translation) 

```

### Direction Vector
> **Unit Vector** is an **1 Direction Vector**.
> Easily control Vector's length. 
![[Pasted image 20230630084202.png]]
>> 5 Units Per Second

##### Predetermined Value
![[Pasted image 20230630084503.png]]

