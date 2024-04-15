Data Base 
[[pokemon_review table]]
![[Pasted image 20240227204906.png]]

**API** - sql on top of http. Middle man (links) between application and DB. To be correct an connection string help App communicate with the DB with ease. 

Model (Object) contain properties. As a cat have attributes.

+ ? ICollection represent a private List. A un-editable list. 
+ $ 1 to 1 Relationship
```cs
public class Review
{
  public int Id { get; set; }
  public string Title { get; set; }
  public string Text { get; set; }
  
  // 1-1: one Review can only belong to 1 Reviewer
  public Reviewer Reviewer { get; set; }
  // 1-1: one Review can only be about 1 Pokemon 
  public Pokemon Pokemon { get; set; }
}
```

+ $ 1 to Many Relationship
```cs
public class Owner
{
  public int Id { get; set; }
  public string firstName { get; set; }
  public string lastName{ get; set; }
  public string Gym { get; set; }


  // 1-1
  public Country Country { get; set; } // very elegant
  // 1-M: 1 Owner to Many PokemonOwners (PokemonOwners mean Pokemon side along with Owner)
  public ICollection<PokemonOwner> PokemonOwners { get; set; }
}
```

```cs
public class Pokemon
{
  public int Id { get; set; }
  public string Name { get; set; }    

  public string Color { get; set; }
  public DateTime BirthDate { get; set; }
  
  // 1-M: 1 Pokemon to Many Reviews
  public ICollection<Review> Reviews{ get; set; }
  // 1-M: 1 Pokemon can belong to many categories
  public ICollection<PokemonCategory> PokemonCategories { get; set; }
  // 1-M: 1 Pokemon can belong to many Owners
  public ICollection<PokemonOwner> PokemonOwners { get; set; }
}
```
	
```cs
public class Reviewer
{
  public int Id { get; set; }
  public string firstName { get; set; }
  public string lastName { get; set; }

	// 1-M: 1 Reviewer can have many Review
  public ICollection<Review> Reviews { get; set; }
}
```


```cs
    public class Country
    {
        public int Id { get; set; }
        public string Name { get; set; }
        // M-1: Many Owners to 1 Country 
        public ICollection<Owner> Owners { get; set; }
    }
```


+ $ Many to Many (always have a JOIN)
```cs
public class PokemonCategory
{
  public int PokemonId { get; set; }
  public int CategoryId { get; set; }

  // M-M join table: Many Pokemon to Many Categories
  public Pokemon Pokemon { get; set; }
  public Category Category { get; set; } 
}
```

```cs
public class PokemonOwner
{
  public int PokemonId { get; set; }
  public int OwnerId { get; set; }

  // M-M: Many Pokemon to Many Owners. Pokemon table join Owner table
  public Pokemon Pokemon { get; set; }
  public Owner Owner { get; set; }
}
```

Update Pokemon Dependency
```cs
public class Pokemon
{
	public int Id { get; set; }
	public string Name { get; set; }    
	
	public string Color { get; set; }
	public DateTime BirthDate { get; set; }
	
	// 1-M: 1 Pokemon to Many Reviews
	public ICollection<Review> Reviews{ get; set; }
	// (Pokemon)-(PokemonCategories)-(Category) : 1-M-1
	// 1-M-1 join table: Many Pokemon to Many Categories through PokemonCategories
	// This also mean 1 Pokemon can belong to many Categories
	// And 1 Category can have many Pokemons
	public ICollection<PokemonCategory> PokemonCategories { get; set; }
	// 1-M-1 join table: Many Pokemon to Many Owners through PokemonOwners
	public ICollection<PokemonOwner> PokemonOwners { get; set; }
}
```

#### Nuget package 
+ Microsoft.EntityFrameworkCore 
+ Microsoft.EntityFrameworkCore.Design
+ Microsoft.EntityFrameworkCore.SqlServer
+ Microsoft.EntityFrameworkCore.Tools (for Migration)
+ Swashbuckle.AspNetCore

#### Migration

+ ? **How to Update Model after Migration**
Ex: add 'ghi_chu' property in Product Model.
> Add-Migration "text" -Context [ExampleDbContext]
Then Update the Database
> Update-Database -Context [ExampleDbContext]

 