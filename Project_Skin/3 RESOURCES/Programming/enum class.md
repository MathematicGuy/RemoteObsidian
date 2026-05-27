---
category: "3 RESOURCES/Programming/enum class.md"
summary: "Explains Java enum classes as structured sets of constant variables, detailing indoor/outdoor location selection."
keywords: ["java enum", "constants", "type safety", "programming syntax"]
confidence: "high"
analyzed_at: "2026-05-27T16:37:23.955444+00:00"
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
