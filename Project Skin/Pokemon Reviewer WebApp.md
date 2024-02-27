Data Base 
![[Pasted image 20240227204906.png]]

```sql
CREATE TABLE [dbo].[Products]
(
	[Id] INT NOT NULL PRIMARY KEY,
	[CategoryId] INT NOT NULL FOREIGN KEY REFERENCES [dbo].[Categories]([Id])
)
```
The above script will create two tables in the database, Categories and Products. The Products table has a foreign key constraint that references the Categories table. 
The following is an example of how to use the SqlServerDatabase class to execute the script above.
```csharp
using SqlServerDatabase;
class Program
{
    static void Main(string[] args)
    {
        var database = new SqlServerDatabase(@"Data Source=.\SQLEXPRESS;Initial Catalog=MyDatabase;Integrated Security=True");
        var script = new SqlScript(@"Path: dbo.Table.sql");
        database.Execute(script);
    }
}
```
The above script will create the two tables in the database.

### 2. Execute a script with a parameter
The following is an example of how to use the SqlServerDatabase class to execute a script with a parameter.
```csharp
using SqlServerDatabase;
class Program
{
    static void Main(string[] args)
    {
        var database = new SqlServerDatabase(@"Data Source=.\SQLEXPRESS;Initial Catalog=MyDatabase;Integrated Security=True");
        var script = new SqlScript(@"Path: dbo.Table.sql");
        script.Parameters.Add("Name", "MyTable");
        database.Execute(script);
    }
}
```
The above script will create the two tables in the database.

### 3. Execute a script with a parameter and get the result
The following is an example of how to use the SqlServerDatabase class to execute a script with a parameter and get the result.
```csharp
using SqlServerDatabase;
class Program
{
    static void Main(string[] args)
    {
        var database = new SqlServerDatabase(@"Data Source=.\SQLEXPRESS;Initial Catalog=MyDatabase;Integrated Security=True");
        var script = new SqlScript(@"Path: dbo.Table.sql");
        script.Parameters.Add("Name", "MyTable");
        var result = database.ExecuteScalar<int>(script);
    }
}
```
The above script will create the two tables in the database and return the Id of the inserted record.

### 4. Execute a script with a parameter and get the result as a list
The following is an example of how to use the SqlServerDatabase class to execute a script with a parameter and
