![[Untitled.png]]

.cshtml -> Razor syntax: HTLM + C#

+ ? **C# files:** These files contain the source code written in C#. They define the classes, methods, and other logic of your application. In your project, you have:
	- `HomeController.cs`: This file defines the `HomeController` class, which likely contains methods that handle HTTP requests for your web pages.
		
	- `Program.cs`: This file is the entry point of your application. It's responsible for starting the application and configuring the web host.

+ ? **Controllers**: store Function for WebApp


+ ? **Models:** This folder contains the model classes for your application. Model classes represent the data that your application works with. Your project has one model file, `ErrorViewModel.cs`.
	Can be use to store Object which read and write data to the DB. 
![[Pasted image 20240307150905.png]]


+ ? **Data (Optional):** This folder can be used to store data files or database access logic. Your project has a subfolder named `Migrations` which is likely used for database migrations with Entity Framework Core (a popular ORM for .NET).
![[Pasted image 20240307144422.png]]


+ ? **Views:** This folder contains the view templates (HTML files) for your application. Views are responsible for displaying the user interface. Your project has a few subfolders and files within the `Views` folder:
	![[Pasted image 20240307143851.png]]
	
- **Home:** This folder likely contains the view templates for the home page of your application. It has a file named `Index.cshtml`.
- **Shared:** This folder can contain view templates that are shared across multiple controllers or actions. Your project has three shared views:
    - `ViewImports.cshtml`: This file is used to centrally manage view component registrations and other shared data for your views.
    - `ViewStart.cshtml`: This file can be used to define a layout template that is inherited by other views.


**appsettings.json:** This file stores configuration settings for your application, such as connection strings and other environment-specific settings.


