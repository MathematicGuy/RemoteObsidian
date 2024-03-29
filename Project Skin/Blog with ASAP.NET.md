Strategy divide the video into each sections
	Listen super super carefully & Take Note for each section.
+ ! bug maybe cause if I missheard or misunderstood any part.
+ note: Using Bot to rate my documentation and refine it after I finished.

**What we'll Learn & Achieve**

+ CRUD Operations
	+ CRUD (Create, Read, Update and Delete)
+ Seed Initial Data
+ Routing: datas to the DB
+ Repository Pattern
+ Form Submission: get data on page load and how to submit form.
+ Notifications 
+ Bootstrap CSS Framework
+ UI/UX: Consistent, Clean and Responsive
+ Create a Web API Controllers on an MVC application
	+ then invoke API using JS
	+ Use asynchronous throught out the course
+ Use 3rd party Text Editor to create content for our blog application
+ AUthentication& Authorization using Microsoft Identity
	+ Register
	+ Login
	+ Role Based Authorization
	+ Multiple Roles (User, Admin,
	+ SuperAdmin)
	+ Manage Users
+ Features included:
	tag, manage blog (CRUD on blog) and user (CRUD on user)

launchSetting.json
	contain my connection setting

### [[Blog WebApp Project Overview]]


## Project Document

### 1) Model
**DB**
![[Pasted image 20240322123415.png]]
	Blog post (m - m) Tag


Create a Folder Domain which store 2 Entity Models 
![[Pasted image 20240322125650.png]]
BlogPost
```cs
public class BlogPost
{
	public Guid Id { get; set; }
	public string Heading { get; set; }
	public string PageTitle { get; set; }
	public string Content { get; set; }
	public string ShortDescription { get; set; }
	public string FeatureImageIRL { get; set; }
	public string UrlHandle { get; set; }
	public DateTime PublishedDate { get; set; }
	public string Author { get; set; }
	public bool Visible { get; set; }
	
	// create many-to-many relationship between Blogpost table and Tag table
	public ICollection<Tag> Tags { get; set; }
}
```
Tag
```cs
public class Tag
{
  public Guid Id { get; set; }
  public string Name { get; set; }
  public string DisplayName { get; set; }
  
	// create many-to-many relationship between Tag table and Blogpost table
  public ICollection<BlogPost> BlogPosts { get; set; }
}
```
-> Create M-M relationship
? at the end mean Nullable property
![[Pasted image 20240322124900.png]]


### 2) Installing Entity Framwork Packages 
![[Pasted image 20240322125556.png]]


### 3) Creating DbContext Class
![[Pasted image 20240322131155.png]]
> Performing CRUD operations on our database tables using Entity Framework Core

Create Data folder to store DbContext (Database Context)
![[Pasted image 20240322132355.png]]
```cs
// BloggieDbContext Inherit from DbContext
public class BloggieDbContext : DbContext
{
  // Overwrite DbContextOptions with BloggieDbContext
  public BloggieDbContext(DbContextOptions<BloggieDbContext> options) : base(options)
  {
  
  }

  // BlogPost as DbSet
  public DbSet<BlogPost> BlogPosts { get; set; }
  public DbSet<Tag> Tags { get; set; }
}
```

Add ConnectionString into appsetting.json
```cs
{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  },
  "AllowedHosts": "*"
  // our connection string
  "ConnectionStrings": {
    "BloggieDbConnectionString": "Data Source=macbookM5\\SQLEXPRESS;Initial Catalog=BloggieDb;Integrated Security=True;Connect Timeout=30;Encrypt=True;Trust Server Certificate=True;Application Intent=ReadWrite;Multi Subnet Failover=False"
  }
}
```
### 4) Inject DbContext Into Our App
using dependency connection so our application will smartly handle all the connections and instances -> provided data smoothly.

Inject DbConext to tell Program.cs knowing what database it using. 
```cs
// Inject DbConext => (telling which server we're using)
builder.Services.AddDbContext<BloggieDbContext>(options =>
    // paste connection string name inside GetConnectionString()
    options.UseSqlServer(builder.Configuration.GetConnectionString("BloggieDbConnectionString")));
```


### 5) EF Core Migrations
Run this command on Package Manager Console
![[Pasted image 20240322134627.png]]
Add-Migration "Initial Migration"
	Create tables using the Data set "DbSet<Models_name> DbSet_Name {get;set}" from the DbContext file 

Update
	Update all the table and column from Migration Folder to the Database (in the connection string)  

## Section 3: Introduction to MVC: Model View Controllers
![[Pasted image 20240322140005.png]]

## MODEL (represent the data)
```ad-note
A class in C# is used to describe a model. Model objects store data 
retrieved from the database
```

![[Pasted image 20240322140149.png]]
HTML, CSS, JS and a little of C# for Razor syntax

![[Pasted image 20240322140232.png]]


![[Pasted image 20240322140244.png]]

## Tags Controller
> Admin Functionality To Add A Tag

The Folder from View reflect the controller from Controllers folder
![[Pasted image 20240322172915.png]]


**Connect link to a Tag** 
> using asap. 				
> + asp-controller="AdminTags" -> connect to the controller
> + asp-action="Add" -> Action of that controller
```html
<li class="nav-item dropdown">
	 <a class="nav-link dropdown-toggle text-light" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
		  Admin
	 </a>
	 <ul class="dropdown-menu">
		  <li><a class="dropdown-item" 
				asp-area="" 
				asp-controller="AdminTags"
				asp-action="Add">Add Tag</a>
			</li>
	 </ul>
</li>
```


### Submit Forms and Data Binding
> Read Incomming Request using Model Binding
use asp-for=""
1) Create a View Model name "AddTagRequest.cs"
![[Pasted image 20240323104131.png]]
Create Tag to get data from HTML
```cs
public class AddTagRequest
{
  public string Name { get; set; } 
  public string DisplayName { get; set; }
}
```
2) Make a HTML page name "Add" and get input data using View Model's tags  
**Connet the ViewModel to the HTML file**
```cs
@model MyBlog.Web.Models.ViewModels.AddTagRequest  
```
**Get input data using View Model's tags**  
```html
<div class="mb-3">
	<label class="form-label">Name</label>
	<input type="text" class="form-control" value="" id="name" asp-for="Name"/>
</div>

<div class="mb-3">
	<label class="form-label">Display Name</label>
	<input type="text" class="form-control" value="" id="displayName" asp-for="DisplayName"/>
</div>
```
3) Create Add Action in "AdminTagsController"  to transfer data from INPUT to Web API
```cs
[HttpGet]
public IActionResult Add()
{
	return View();
}

// POST: /AdminTags/Add
[HttpPost]
[ActionName("Add")] // if they're not the same Cs still recognized which Add to use (context: compare Add above and Add below)
public IActionResult Add(AddTagRequest addTagRequest)
{
	// Mapping AddTagRequest to Tag 
	var tag = new Tag
	{
		 Name = addTagRequest.Name,
		 DisplayName = addTagRequest.DisplayName,
	};

	 // get data from tag
	bloggieDbContext.Tags.Add(tag);
	// crucial to save changes
	bloggieDbContext.SaveChanges();

	return View("Add");
}
```

### Saving Data to Database
![[Pasted image 20240323110223.png]]


