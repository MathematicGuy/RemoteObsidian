### 1. What is HTML?
**Hypertext** Markup Language
+ Hypertext mean This document link to Other documents. (Which create a gigantic web)
![[Pasted image 20231018101934.png]]

+ Hypermedia -> extension of hyper text
![[Pasted image 20231018102011.png]]

+ Markup -> to mark sth up, to annotate.
![[Pasted image 20231018102059.png]]

+ Language -> HTML (a language follow an order)
![[Pasted image 20231018102315.png]]
	+ Annotates content
	+ Defines document structure

### 2. Relevant History of HTML


+ 1997 - not driven standards -> no format html, bunch of bug
+ 2000 - now: Tmprovement -> HTML5

**2 Main Organization developed HTML5** 
![[Pasted image 20231018103117.png]]
standard -> pick the best out of those evolving, slowly improve. Auto update to user 
evolving -> newest update to date


### 3. Anatomy of an HTML Tag

hr - horizontal rule (can only open, not require to close)
id - must be unique
![[Pasted image 20231018103657.png]]

### 4. Basic HTML Document Structure
```html
<!doctype html>
<meta charset-"utf-8"> // use to display content
```
+ help website run faster and responsive 
This help browsers render those pages correctly, browsers used the doctype declaration to distinguish between noncompliant and compliant pages. 
	not complie ->  web run in *quirks mode* 
	quirks mode -> Assumes that the HTML in the web page is NOT following the HTML standard, i.e., not in standards mode. Styles won't work correctly, etc.

### 5. HTML Content Models
![[Pasted image 20231018105916.png]]
block level -> 1 line for it
inline level -> element inside other element.


### 8. HTML Character Entity References

**3 Characters You Ahould Always Escapse**
![[Pasted image 20231018114318.png]]
**Summary**
+ Help avoid text issues
	&npsp -> non-breaking space (*basically space not causing line break*)
		place after a word to connect the following word
+ Safeguard against more limited character encoding
+ Provide characters not available on a keyboard 
	&copy; -> copyright symbol 


### 9. Creating Links
```html
<a href="http://ww..." target="_blank" title="Like our pages"> Coursera </a>
// target = "_blank" -> open link in new tab 
```


---
[[HTML Code]]

