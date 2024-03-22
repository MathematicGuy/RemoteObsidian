**Project Setup**
	
1. **New Project:**
    - Open Visual Studio and click "Create a new project".
    - Search for "ASP.NET Core Web App (Model-View-Controller)" and click Next.
    - Name your project (e.g., "MyBlogApp") and choose a suitable location. Click Next.
    - Select an appropriate .NET version (check video for recommended version). Choose "Individual User Accounts" for authentication if you want a user login system. Click "Create"

**Database Setup (Entity Framework)**
	
2. **Data Models:**
    
    - Create a `Models` folder in your project.
    - Add classes to represent your data:
        - `Post.cs`: (id, title, body, dateCreated, ...etc.)
        - `Tag.cs`: (id, name, displayName)
3. **Database Context:**
    
    - Create a new class (e.g., `BlogDbContext.cs`) in your `Models` folder (or a separate `Data` folder)
    - Make it inherit from `DbContext`.
    - Add `DbSet` properties for each model:
        ```cs
        public DbSet<Post> Posts { get; set; }
        public DbSet<Tag> Tags { get; set; }
        ```
	
- **Connect to Database:**
    
    - Install `Microsoft.EntityFrameworkCore.SqlServer` NuGet package.
    - Add your database connection string in `appsettings.json`.
    - In `Startup.cs`, in the `ConfigureServices` method, add:
        ```cs
        services.AddDbContext<BlogDbContext>(options =>
            options.UseSqlServer(Configuration.GetConnectionString("MyBlogApp")));
        ```
	
4. **Create Migrations:**
    
    - Open Package Manager Console (Tools -> NuGet Package Manager -> Package Manager Console)
    - Run `Add-Migration InitialCreate`
    - Run `Update-Database`

**Controllers**
	
5. **Posts Controller:**
    
    - Right-click the `Controllers` folder -> Add -> Controller -> MVC Controller with views, using Entity Framework
    - Select `Post` as your model class, `BlogDbContext` as your data context class. Name it `PostsController`.
6. **Tag Controller:**
    
    - Repeat step 6 for your `Tag` model, naming it `TagsController`.

**Views**
	
7. **Modify Layout:**
    
    - Edit `_Layout.cshtml` (in `Views/Shared`) to add navigation links for your blog, admin area, etc.
8. **Implement Views:**
    
    - The scaffolding should have created basic views under `Views/Posts` and `Views/Tags`. Customize these for listing posts, creating new posts, editing, deleting, adding/managing tags, etc.

**Additional Features (Refer to the video for more specifics)**

- **User Authentication/Authorization:** If you chose "Individual User Accounts" during setup, you'll have a basic login/registration system.
- **Rich Text Editor:** Consider integrating a rich-text editor (like TinyMCE or similar) for post creation.
- **Tag Management:** Implement tag assignment to posts from your admin area.

**Testing and Deployment**

- **Thorough Testing:** Test as you build each feature.
- **Deployment:** Choose a hosting provider suitable for ASP.NET Core applications (Azure, AWS, or others).