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
> Allow you to quick test all your Repository Method on the proxy database without the need of runing -> Save Time and Effort
+ Proxy Database: In-Memory Database / Test Container

0) We will test all the Repository Method on the real database, so we will need to **Compose Docker**  first. 
```sh
docker compose up
```
If you not using Docker, remember to active your **application.properties** 
```java
#spring.datasource.url=jdbc:postgresql://localhost:5432/ProjectOne
#spring.datasource.username=postgres
#spring.datasource.password=cmcuni
#spring.datasource.driver-class-name=org.postgresql.Driver
#spring.jpa.database-platform=org.hibernate.dialect.PostgreSQLDialect
```


1) Create a Test File of your Repository or Controller
	![[Pasted image 20240802110340.png]]
2) Here a Example Repository for you to test
```java
public class InMemoryRunRepository {
    private static final Logger log = LoggerFactory.getLogger(InMemoryRunRepository.class);
    private final List<Run> runs = new ArrayList<>();

    public List<Run> findAll() {
        return runs;
    }

    public Run findById(Integer id){
        return runs.stream()
                .filter(run -> run.id().equals(id))
                .findFirst()
                .orElse(null);
    }

    public void create(Run run){
        Run newRun = new Run(run.id(),
                run.title(),
                run.startedOn(),
                run.completedOn(),
                run.kilometers(),
                run.location(), null);
        runs.add(newRun);
    }

    public void update(Run run, Integer id){
        Run updatedRun = new Run(id,
                run.title(),
                run.startedOn(),
                run.completedOn(),
                run.kilometers(),
                run.location(), null);
        runs.set(id, updatedRun);
    }

    public void delete(Integer id){
        runs.removeIf(run -> run.id().equals(id));
    }

    public int count(){
        return runs.size();
    }
}
```
3) Hover your Mouse above the Class and `Alt + Fn + Insert` ->  Generate Test  (JUnit5)
	![[Pasted image 20240802110509.png]]
4) Check the **test folder** to find your test file
	![[Pasted image 20240802110852.png]]
5) In here you can insert Object to the test database manually
+ @BeforeEach allow you to setup inserted Data to the proxy database (real database but will automatically reset after test run) 
```java
class InMemoryRunRepositoryTest {

    InMemoryRunRepository repository;
    @BeforeEach
    void SetUp(){
        repository = new InMemoryRunRepository();
        repository.create(
                new Run(1,
                "Morning Run",
                LocalDateTime.now(),
                        LocalDateTime.now().plusMinutes(30),
                10,
                Location.OUTDOOR,
                null));

        repository.create(
                new Run(2,
                "Evening Run",
                LocalDateTime.now(),
                        LocalDateTime.now().plusMinutes(30),
                10,
                Location.OUTDOOR,
                null));
    }
```
@Test allow you to test each of your Method.
```java
    @Test
    void shouldFindAllRuns(){
        List<Run> runs = repository.findAll();
        assertEquals(2, runs.size(), "This return all runs");
    }

    @Test
    void shouldFindRunById() {
        Run run = repository.findById(1);
    }

    @Test
    void shouldCreateRun() {
        Run run = new Run(3,
                "Morning Run",
                LocalDateTime.now(),
                LocalDateTime.now().plusMinutes(30),
                10,
                Location.OUTDOOR,
                null);
        repository.create(run);
        assertEquals(3, repository.findAll().size(), "This should create a new run");
    }

    @Test
    void shouldUpdateRun() {
        Run run = new Run(3,
                "Morning Run",
                LocalDateTime.now(),
                LocalDateTime.now().plusMinutes(30),
                10,
                Location.OUTDOOR,
                null);
        repository.update(run, 1);
        assertEquals("Morning Run", repository.findById(1).title(), "This should update the run");
    }

    @Test
    void shouldDeleteRun() {
        repository.delete(1);
        assertEquals(1, repository.findAll().size(), "This should delete the run");
    }

    @Test
    void shouldCountRuns(){
        assertEquals(2, repository.count(), "This should count the number of runs");
    }
}
```