# File System
![[Pasted image 20240620175706.png]]

Java - main folder storing others importance folder where you working with.
	In Web MVC (This where M, V and C be store)

## Runnerz Folder (The Processing Section)
**run folder** store 
+ Controller
+ Repository
+ run file (Main File)

**user folder** (Models store here)

## Resources Folder (The Memory Section)
> Ours Database store. You can also create table, insert, edit, delete table manually in here

Is there a CRUD Operation scraffold

# Module 1: Create your Project
Let try by making a simple, file structure
![[Pasted image 20240715154341.png]]
> In run, there are Record Class Run with attribute location as Location Class.

In Traditional way, to would create a class with get set. But with class record, it can provide all of those features with just a few line:
```java
package com.example.ProjectOne.run;  
import java.time.LocalDateTime;  
  
public record Run(  
        // record class is the same as a class of attribute  
        // with getters, setters, equals, hashcode, and toString        Integer id,  
        String title,  
        LocalDateTime startedOn,  
        LocalDateTime completedOn,  
        Integer kilometers,  
        Location location  
) {}
```
Location [[enum class]]
```java
package com.example.ProjectOne.run;  
  
public enum Location {  
    INDOOR, OUTDOOR  
}
```


After that, we just call Run class (having get/set function integrated) in Application Class (our main class) 
```java

public class Application {  
    CommandLineRunner runner(){  
       return args -> {  
          Run run = new Run(1, "First Run", LocalDateTime.now(),  
                    LocalDateTime.now().plusHours(1),  
                13, Location.OUTDOOR);  
  
          log.info("{}", run);  
       };    
    }
}
output >> Run[id=1, title=First run, startedOn=2024-07-15T15:39:33.076377100, completedOn=2024-07-15T16:39:33.076377100, kilometers=13, location=OUTDOOR]
```


# Module 2: REST API
![[Pasted image 20240715161616.png]]
Run Application -> Open up the WebBrowser by clicking the internet symbol inside Actuator. 



# Module 5: Rest Clients


Proxy Factory: This factory _generates a class that extends the given super class and implements the given interfaces_.


# Module 6: Testing

