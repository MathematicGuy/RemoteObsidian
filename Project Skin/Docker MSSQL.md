**Template**
>docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=yourStrong(!)Password" --name server_name -p 1433:1433 -d mcr.microsoft.com/mssql/server:2022-latest


**Example**
>docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=cmcuni" --name meinsql  -p 1433:1433 -d mcr.microsoft.com/mssql/server:2019-latest

+ - e: environment flag
+ EULA - End User License Agreement
+ -p: port number 
	-p: 1433:1433 (port use in container : port use outside the container)
+ -d: detached mod (container use in the background)
+  "mcr.microsoft.com/mssql/server:2022-latest" path to the image
	remember to change mssql server and ubuntu to your version  


```
package com.example.ProjectOne.run;  
  
import org.springframework.data.jdbc.repository.query.Query;  
import org.springframework.data.repository.ListCrudRepository;  
  
import java.util.List;  
  
public interface RunRepository extends ListCrudRepository<Run, Integer> {  
    @Query("SELECT * FROM run WHERE location = :location")  
    List<Run> findAllByLocation(String location);  
}
```
\
```
# using docker we don't need to set up db in application.properties  
services:  
  postgres:  
    image: 'postgres:latest'  
    environment:  
      POSTGRES_DB: ProjectOne  
      POSTGRES_USER: sa  
      POSTGRES_PASSWORD: password  
    ports:  
      - '5432:5432' # docker host port : container port  
#    volumes:  
#      - postgres-data:/va
```