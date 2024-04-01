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

[[Blog WebApp Bugs and Notice]]


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



**TAG DROPDOWN: Connect link to a Tag** 
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
3) Get Data from Web to the Database (BloggieDbContext) 
**Create Action Add to View Add.cshtml page**
```cs
[HttpGet]
public IActionResult Add()
{
	return View();
}
```
+ Use Action HttpsPost to Create/Update datas 
+ Create new Tag to store input datas 
```cs
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
```
+ Add Tag (input datas) to bloggieDbContext 
```cs
	 // get data from tag
	bloggieDbContext.Tags.Add(tag);
	// crucial to save changes
	bloggieDbContext.SaveChanges();

	return View("Add");
}
```
> the code above **Saving Data to Database**
![[Pasted image 20240323110223.png]]

### Read Records From Database
+ ! Remember: Http command are like execute SQL query in 1 Word.
Connect 'Tag Model' to .cshtml and get it List of data
```cs
@model List<MyBlog.Web.Models.Domain.Tag> 
```

Create Table, Extract data from Model with Razor (syntax)
> List of 'Tag Model' represent as 'Model' so we represent each tag using @foreach and extract it data.
```html
<!-- Store and View the List -->
<div class="container py-5">
    <!-- Get Table Datas existed a Model -->
    @if (Model != null && Model.Any())
    {
        <!--Boostrap table -->
        <table class= "table">
            
            <thead>
                <tr>
                    <th>Id</th>
                    <th>Name</th>
                    <th>Display Name</th>
                    <th>Actions</th>
                </tr>
            </thead>

            <tbody>
                <!-- Take the attributes of each Tag Object -->
                @foreach (var tag in Model)
                {
                    <tr>
                        <td>@tag.Id</td>
                        <td>@tag.Name</td>
                        <td>@tag.DisplayName</td>
                    </tr>
                }
            </tbody>
        </table>
    }
    else
    {
        <p>No tags found ! </p>
    }
</div>
```

in AdminTagController we want to use HttpGet for Displaying Purpose. Get Tags table from bloggieDBContext and extract it into a List name tags and return it.
```cs
// DISPLAY Functionality
[HttpGet]
// use to redirect user to the List view 
[ActionName("List")]
public IActionResult List()
{
	// get data from bloggieDbContext
	var tags = bloggieDbContext.Tags.ToList();

	// return data to view
	return View(tags);
}
```



### Update (Edit) Records From Database
We need to Update a Record from the Db. The simpliest solution is to replace user input with the data from the DB. To do that we will have to:
1) Create a Edit Page (Display current Data from bloggieDbContext)
2) Create a Model (get Edited User Input)
3) Replace old with new. (bloggieDbContext data -> editTagRequest data) 


+ ! Displaying Chosen Record Data  
First we Create an HTML Page & Connect bloggieDbContext to Displau chosen Record
```html
<!-- Binding View to EditTagRequest Model -->
@model MyBlog.Web.Models.ViewModels.EditTagRequest
@{

}

<div class="bg-secondary bg-opacity-10 py-2">
    <div class="container">
        <!-- Keep Functionality Different for each Page-->
        <h1 class="display-4">Edit Function - Admin Functionality</h1>
    </div>
</div>
```
Display data & Update Btn
```html
<div class="container py-5">
    <form method="post">
        <!-- Id -->
        <div class="mb-3">
            <label class="form-label">Id</label>
            <!-- asp-for Good send data to the Model and View the Data comming back from the DB ->
              <!-- readonly to prevent user from changing the value -->
            <input type="text" id="id" class="form-control" asp-for="Id" readonly/>
        </div>

        <!-- Name -->
        <div class="mb-3">
            <label class="form-label">Name (Use dashline between words like Potato-Peel)</label>
            <input type="text" id="id" class="form-control" asp-for="Name"/>
        </div>

        <!-- Display Name -->
        <div class="mb-3">
            <label class="form-label">Display Name</label>
            <input type="text" id="id" class="form-control" asp-for="DisplayName"/>
        </div>


        <!-- Update & Delete-->
        <div class="mb-3">
            <div class="d-flex">
                <button type="submit" class="btn btn-dark">Update</button>
            </div>
            
        </div>

    </form>
</div>
```


Add Edit option for each each Record and Display data from the Db using Controller's Action  
```html
<!-- Take the attributes of each Tag Object -->
@foreach (var tag in Model)
{
  <tr>
		<td>@tag.Id</td>
		<td>@tag.Name</td>
		<td>@tag.DisplayName</td>
		
		<!-- Edit Record with Id -->
		<td>
			 <a asp-area="" 
			 asp-controller="AdminTags"
			 asp-action="Edit"
			 asp-route-id="@tag.Id">Edit</a>
		</td>
  </tr>
}
```

+ ! We want to save chosen Data to EditTagRequest Model so we can replace data from Db with it later 
```cs
namespace MyBlog.Web.Models.ViewModels
{
    public class EditTagRequest
    {
        // Create new bc we want to seperate Edit Tag from the List Tag
        // Saving Edit Model data then transfer it to List Model
        public Guid Id { get; set; }
        public string Name { get; set; }
        public string DisplayName { get; set; }
    }
}
```


+ ! Get Record attributes with its Id. 
1) Get Record id using 'Guid Id' -> allow to use chosen id as Path
Let get the Tags from bloggieDbContext with our chosen id to save it in a Variable (tag).  
2) using 'FirstOrDefault' to Scan each Record and Chose the first id that match with our chosen id.
3) Save extracted data to a list and return it (to Edit.cshtml)
```cs
[HttpGet]
// Action Name is crucial bc it show What .cshtml file to render
[ActionName("Edit")]
// read Tag by id
public IActionResult Edit(Guid id)
{
	// 1st method 
	//var tag = bloggieDbContext.Tags.Find(id);
	
	// 2nd  method
	// Find tag by id and return the 1st one it found
	var tag = bloggieDbContext.Tags.FirstOrDefault(x => x.Id == id);  

	// Return EditTagRequest Model to the view if tag is not null
	if (tag != null)
	{
		 var editTagRequest = new EditTagRequest
		 {
			  Id = tag.Id,
			  Name = tag.Name,
			  DisplayName = tag.DisplayName
		 };

		 return View(editTagRequest);
	}

	return View(null);
}
```

```ad-summary
To Concluded, Display Db chosen Record data by conencting Db to the HTML pages and transfer record's data through [HttpGet] Edit Action
```


+ ! Now Let Edit the Chosen Record's Data
1) Get Data from 'EditTagRequest Model' as tag 
2) Connect and Get Data from bloggieDbContext as existingTag
3) Replace desired data from existingTag with tag 
4) Return to List Page to see the result
```cs
[HttpPost]
// Action Name is crucial bc it show What .cshtml file to render
[ActionName("Edit")]
// notice: Tag.id != existingTag.id bc Tag.id is from EditTagRequest and existingTag.id is from bloggieDbContext
// Edit - replace the existing tag with new tag data, then save changes
public IActionResult Edit(EditTagRequest editTagRequest)
{
	// tag object - get tag from editTagRequest (data from Edit.cshtml)
	var tag = new Tag
	{
		 Id = editTagRequest.Id,
		 Name = editTagRequest.Name,
		 DisplayName = editTagRequest.DisplayName,
	};

	// existingTag object - get existing tag from bloggieDbContext (Data from Database) 
	var existingTag = bloggieDbContext.Tags.Find(tag.Id);
	
	// replace existing tag with new tag datas
	if (existingTag != null)
	{
		 existingTag.Name = tag.Name;
		 existingTag.DisplayName = tag.DisplayName;

		 // save changes
		 bloggieDbContext.SaveChanges();

		 // show success notification
		 TempData["SuccessMessage"] = "Tag updated successfully!";

		 return RedirectToAction("List", new { id = editTagRequest.Id });
	}

	// show fail notification
	return RedirectToAction("List", new { id = editTagRequest.Id });
}
```
return to List Page with Edited Record Id to show success edited.
```cs
return RedirectToAction("List", new { id = editTagRequest.Id });
```
![[Pasted image 20240401080127.png]]


### 04 - Asynchronous Programming and Repository Pattern

#### Asynchronous Programming
+ ? Async Make WebApp go Vrooooooooooooommmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
![[Pasted image 20240401085241.png]]

#### Repository Pattern
> **Act as a middle man**. 
> Reference example: 
> + **Like in Math**. You save **all your fomular into a Notebook (responsitory)**. So each time you encounter an problem that require the same fomula to solve, you could bring all that juicy fomula from the Notebook (responsitory) out and solve the problem.     
> + Like in Code: act like a Library that responsible for talking to the Db.
![[Pasted image 20240401090131.png]]


**Advantage**:  
+  If u need to do any changes, you only need to do it in only 1 place
+  The Job talking to the Db is all within the responsitory -> very Clean & Tight. better than having `s*x`
![[Pasted image 20240401090142.png]]
 

**Problem & Process of making Repositories**
+ ! Problem: we have to rewrite code that talk to the Db repeatedly -> Want to group all those code together into a file and called it like a function. 
+ $ Solution: Making a **Responsitory** which **include all the code** responsible for **talking to the Db**.
+ ? How this Process work:
	+  1) Make a Interface to hold the function name and definition. (hold unique function)
	+  2) Make a Responsitory to inherit the Interface function (allow implement interface's function as many time as we want)
	+ 3) Replace those duplicated code from the Controller with Reponsity function we just make.
![[Pasted image 20240401090314.png]]
For example, instead of repeating 2 lines 
```cs
await bloggieDbContext.Tags.AddAsync(tag);
await bloggieDbContext.SaveChangesAsync();
```
We just need to call AddAsync(tag). 
![[Pasted image 20240401094221.png]]
```cs
[HttpPost]
public async Task<IActionResult> AddTag(AddTagRequest addTagRequest)
{
	var tag = new Tag
	{
		 Name = addTagRequest.Name,
		 DisplayName = addTagRequest.DisplayName,
	};

	await tagResponsitory.AddAsync(tag);
	return View("Add");
}
```
