+ ! There was an error running the selected code generator: 'Package restore failed. Rolling back package changes for 'HowAboutAnotherJoke•,•
	https://youtu.be/GAKvScju1qA?si=1N-A1_TslssWab0V

ApplicaionDbContext

> Cross-Origin Request Blocked: The Same Origin Policy disallows reading the remote resource at http://heval1st-001-site1.anytempurl.com//GetAllHang. (Reason: CORS header ‘Access-Control-Allow-Origin’ missing). Status code: 401.
+ Refresh/reset SSL key. 
+ This error might happend because you already use this SSL key in another Web site. 1 SSL for 1 Web site only. 

+ ! **The ConnectionString property has not been initialized.** 
> Reason, the connection string in appsetting.json might be wrong or
> + The connection string is right. But the code connect to it is wrong. 
+ ? This code is not the right form. It cause error
```cs
builder.Services.AddDbContext<DataContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("PokemonConnectionString")));
```
+ $ This code is the right form 
```cs
// Add the DB context to the services
builder.Services.AddDbContext<DataContext>(options =>
{
    options.UseSqlServer(builder.Configuration.GetConnectionString("PokemonConnectionString"));
});
```

Unknow Error that are too complex to understand like
+ ! Severity Code Description Project File Line Suppression State Error MSB3027 Could not copy "D:\CMC_UNI\2ndYear\Technology & Web Programming\Learn Web API\PokemonAPI\PokemonAPI\obj\Debug\net8.0\apphost.exe" to "bin\Debug\net8.0\PokemonAPI.exe". Exceeded retry count of 10. Failed. The file is locked by: "PokemonAPI (19268)" PokemonAPI C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Current\Bin\amd64\Microsoft.Common.CurrentVersion.targets 5254
+ $ **Clean Solution** in Visual Studio 2022