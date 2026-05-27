---
category: "3 RESOURCES/Programming/enum class.md"
summary: "This programming reference defines the concept of Java enumerations used to represent groups of constant variables. It provides code examples demonstrating enum declaration and usage in software applications."
keywords: []
confidence: "high"
analyzed_at: "2026-05-27T17:32:07.263427+00:00"
---
An `enum` is a special "class" that represents a group of **constants** (unchangeable variables, like `final` variables).

Example:
Enum Class Location
```java
public enum Location {  
    INDOOR, OUTDOOR  
}
```
So you can only use 2 option: INDOOR or OUTDOOR 
```java
current_location = Location.OUTDOOR 
```
