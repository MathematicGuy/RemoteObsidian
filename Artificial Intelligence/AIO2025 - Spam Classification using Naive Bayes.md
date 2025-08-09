**Regex to Remove Puntual in sentence**
`[` and `]` define character set
`^` match any character not in the character set -> i.e. `[the_set]`
`\w` matches any word from `a-z, A-Z, 0-9`
`\s` matches any whitespace char include spaces, tabs, newlines, etc.

**Use Case: remove everything except for `\w` and `\s`**
If you write `\\w`, it mean any characters that is `\w`. So `[\\w\\s]` would mean for any characters that is `\w` and `\s`. And `^[\\w\\s]` mean for every character that is not `\\w` and `\\s`. Since `re.sub()` is a function that remove any thing inside the `()`, the commad `re.sub(r'[^\w\s]')` would remove everything except for character `\w` and `\s`. 

---

