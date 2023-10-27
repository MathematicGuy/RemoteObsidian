### Class Selector

> Access id & class in CSS
```css
#header1{} -> id
.header2{} -> class
#header1, .header2 {} -> group 2 tag together
```


> Class selector
![[Pasted image 20231027083356.png]]*All p tag with class big will have 20px font-size* 


> [**The Descendant Selector** matches all elements that are descendants of a specified element.]([W3Schools Tryit Editor](https://www.w3schools.com/Css/tryit.asp?filename=trycss_sel_element_element))
```css
article p{
	color: blue;
}
```
**> All p exist inside article tag will be blue**


> [**The child selector** (>) selects all elements that are the children of a specified element]([W3Schools Tryit Editor](https://www.w3schools.com/Css/tryit.asp?filename=trycss_sel_element_gt)) 
```html
<div>
  <p>Paragraph 1 in the div.</p>
  <p>Paragraph 2 in the div.</p>
  <section>
    <!-- not Child but Descendant -->
    <p>Paragraph 3 in the div (inside a section element).</p>
  </section>
  <p>Paragraph 4 in the div.</p>
</div>
```
> *All p tag under the article tag will be blue*.
```css
article > p {
	color: blue;
}
```


[**Adjacent sibling selector**]([W3Schools Tryit Editor](https://www.w3schools.com/Css/tryit.asp?filename=trycss_sel_element_pluss))
```html
<div>
  <p>Paragraph 1 in the div.</p>
  <p>Paragraph 2 in the div.</p>
</div>

<p>Paragraph 3. After a div.</p> -> only this take affect 
<p>Paragraph 4. After a div.</p>
```
> *The + selector is used to select **an element that is directly after** another specific element.* -> **1st p after div take effect**
```css
div + p {
  background-color: yellow;
}
```

[**General Sibling Selector (~)**]([W3Schools Tryit Editor](https://www.w3schools.com/Css/tryit.asp?filename=trycss_sel_element_tilde))
```html
<div>
  <p>Paragraph 2.</p>
</div>

<p>Paragraph 3.</p> -> this take effect
<p>Paragraph 4.</p> -> this take effect
<p>Paragraph 4.</p> -> this take effect
<p>Paragraph 4.</p> -> this take effect
```
> *The general sibling selector (~) selects **all elements that are next** siblings of a specified element.* -> **all p after div take effect**

```css
div ~ p {
  background-color: yellow; 
}
```

**SUMMARY**
+ Combining selectors
	• Element with class selector (selector. class)
	• Child (direct) selector (selector > selector)
	• Descendent selector (selector selector)
	• Adjacent sibling selector (selector + selector)
	• General sibling selector (selector ~ selector)

### Pseudo-Class Selector
Many pseudo-class selectors exist
We cover:
	 :link
	:visited
	: hover
	: active
	:nth-child(...)
