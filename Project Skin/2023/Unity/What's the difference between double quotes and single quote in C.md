" " : for multiple character.
' '   : for Single character. Testing the First Character

+ When you say string s = "this string" then s[0] is a character at a specific index in that string (in this case s[0] == 't').

+ So to answer your question, use double quotes or single quotes. You can think of the following as meaning the same thing
```csharp
string s = " word word";

// Check for space as first character using single quotes
if(s[0] == ' ') {
    // Do something
}

// Check for space using string notation
if(s[0] == " "[0]) {
    // Do something
}
```


