`"."` mean it match any characters -> match all chars but *only scan for 1 char*
`*` matches zero or more occurences -> `.*` -> *match all chars and scan for all chars*
`?` makes the match non-graddy, ensuring it stops at the very first `|}` it finds rather than jumping to the end of the string.
+ ? Only delete `inner_content` within `{}` when use `{{.*?}}`, without `?` between content be deleted as well -> in case of `{{inner_content}} between_content {{inner_content}}`

**`\|\}`**: Matches the closing literal vertical bar and brace. Because `{|` and `|}` is special characters.
-> this allow nested Regex structure 

+ ? What if the string have content after breakline ? ie. Multiline content.
+ $ `re.DOTALL` flag to the `re.sub()` so teh `.` character matches newlines. 