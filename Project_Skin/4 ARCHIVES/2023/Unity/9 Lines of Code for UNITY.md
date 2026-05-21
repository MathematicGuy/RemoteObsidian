
note: Don't use ' ' semi-collin in C#. Only " " double-collin

## Line 1: Variables 

###### (Boxes contain Datas) 
Example: 
-> Fire Ball: Speed, Damage, Particle

Specified: 
+ **Public** -> can be Access in the Anywhere. (Apear inside the Inspector)
+ **Private** -> only in code

Type: String, Int, Float, BOOL

Component:
+ **Rigid Body** -> has physics
+ **Transform** -> just a shape body

## Line 2: GetComponents<>()

###### Object attributes -> Component
Component like: transform, Sprite Renderer, etc. ..

###### Set/Change Component property
```cs
private SpriteRenderer rend; // Set Component Name

private void Start()
{
	// Specify Component between blaket
	rend = GetComponent<SpriteRenderer>(); 
	rend.color = Red // Set Component color to Red 
}
```

## Line 3: Instantiate() 

###### Instantiate Script 
```cs
Instantiate(object to spawn, position, rotation);
```

###### Spawn Game Obj within ours Script
```cs
public GameObject objectToSpawn;

private void Start()
{
	// vector3 -> Z coords;  Quaternion.identity -> no rotation 
	Instantiate(objectToSpawn, Vector3.zero, Quaternion.indentity);
}
```


## Line 4: Destroy()  

###### Destroy Script
```cs
Destroy(object to destroy, life time);
```

## Line 5: Loops

+ For Loop
	```cs
	for(int i = 0; i<3, i++)
	{
		// code to loop...3 times
	}
	```

###### Spawn a lot of Game Object
```cs
public int numberOfCaffeeToSpawn;
public GameObject CoffeeToSpawn;

private void Start()
{
	for (int i = 0; i < numberOfCaffeeToSpawn; i++)
	{
		// Random Position
		Vector3 randomPosition = new Vector3(Random.Range(13, -13),                  Random.Range(6, -9) ));
		
		Instantiate(CoffeeToSpawn, randomPosition, Quaternion.indentity);
	}
}
```

## Line 6: If/Else


##### Different Outcome for 1 Code ![[Pasted image 20230625015029.png]]
```cs
if (condition)
{
	// code runs if condition is true
} else
{
	// code...
}
```


## Line 7: Input.GetAxisRaw()

##### Trigger when Pressing Key

```cs
Input.GetAxisRaw("Horizontal"); // Left & Right Arrow key
Input.GetAxisRaw("Vertical");   // Up & Down Arrow key 
```
0 for not Pressing any.
![[Pasted image 20230625015349.png]]
![[Pasted image 20230625015552.png]]

#### Vector3
```cs
Vector3 name = new Vector3(x,y,z); // z = 0 in 2D Space
```

##### Set Character Movement Direction
note: Time.deltaTime -> FrameRate independents. Effect changes by Time not Frame Rate.  
```cs
Animator anim; // set Animator as anim
public float speed;

private void Start()
{
	anim = GetComponent<Animator>();	
}
private void Update()
{
	// move in X,Y Direction
	Vector3 playerInput = new Vector3(Input.GetAxisRaw("Horizontal"),            Input.GetAxisRaw("Vertical"), 0);
	// Implement movement 
	transform.position = transform.position + playerInput.normalized 
	* speed * Time.deltaTime;
}
```

## Line 8: Vector2.MoveTowards()

#### Move an Object from point A -> B 
```cs
Vector2.MoveTowards(startPos, target, speed);
```

1) Create an Enemy
2) Create Chase (Script) 
##### Chase
```cs
// don't need to care
public class Chase : MonoBehaviour 
{
	public GameObject target;
	public float speed;

	private void Update()
	{
		transform.position = Vector2.MoveTowards(transform.position,               target.transform.position, speed * Time.deltaTime);
	}
}
```

## Line 9: OnTriggerEnter2D() & OnCollisionEnter2D()

note: Collider -> aura surround obj response when collies 
##### Run when object collides
( Whatever put inside the function will run automatically when obj Collided or Touched )
```cs
private void OnTriggerEvent(Collider2D other)
{
	// Run when object collies
}
``` 


#### Check COLLISION TRIGGERED with enemy
[Active whenever there're COLLISION]
```cs 
// Set Blood Effect as effect
public GameObject effect;

// Condition when 2 Object collider Collies
private void OnTriggerEnter2D(Collider2D other)
{
	if (other.tag == 'Enemy')
	{
		Instantiate(effect, transform.position, Quaternion.identity);
		
	}
}

```

#### Check COLLISION with enemy 
[Not Active if Obj have Trigger mode on]
```cs
// Set Blood Effect as effect
public GameObject effect;

// Condition when 2 Object collider Collies
private void OnTriggerEnter2D(Collider2D other)
{
	if (other.tag == 'Enemy')
	{
		Instantiate(effect, transform.position, Quaternion.identity);
		
	}
}

```
