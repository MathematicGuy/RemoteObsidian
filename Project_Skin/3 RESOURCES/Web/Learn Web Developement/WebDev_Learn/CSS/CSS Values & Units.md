> **By understanding the different types of CSS units and how to use them, you can create more flexible and responsive web pages.**

vh stands for **viewport height**
+ **100vh**  would represent 100% of the viewport's height or the **full height of the screen**
+ Specifying **10vh is equivalent to occupying 10%** of entire visible **screen height**.
	If you look carefully, you can see that **50vh means 50%, which will cover half of the entire screen height**


# [Learn CSS Units – Em, Rem, VH, and VW with Code Examples ✨✨](https://www.freecodecamp.org/news/learn-css-units-em-rem-vh-vw-with-code-examples/#:~:text=The%20full%20form%20of%20VH,of%20entire%20visible%20screen%20height.&text=If%20you%20look%20carefully%2C%20you%20can%20see%20that%2050vh%20means,of%20the%20entire%20screen%20height.)

CSS units are used to specify the size, position, and other properties of HTML elements. There are two main types of CSS units: absolute and relative.

**Absolute units** have a fixed value, regardless of the size or resolution of the device on which the web page is being displayed. Some common absolute CSS units include:

- **Pixels (px)**: Pixels are the smallest unit of measurement in CSS. One pixel is equal to a single dot on the display screen.
- **Centimeters (cm)**: Centimeters are a metric unit of measurement equal to one hundredth of a meter.
- **Inches (in)**: Inches are an imperial unit of measurement equal to one twelfth of a foot.

**Relative units** are based on the size or resolution of the device on which the web page is being displayed. Some common relative CSS units include:

- **Percentage (%)**: Percentage values are relative to the size of the element's parent element. For example, a width value of 50% would make the element half as wide as its parent element.
	
- **Ems (em)**: Ems are relative to the font size of the element. For example, a font-size value of 2em would make the element's font twice as large as the font size of its parent element.
	
- **Rems (rem)**: Rems are similar to ems, but they are relative to the font size of the root element of the document. This means that rems are more consistent across different devices and browsers.

In addition to the units listed above, there are also a number of specialized CSS units, such as those used for gradients, shadows, and transformations.

It is important to choose the right CSS units for your needs. Absolute units can be useful for specifying the size of elements that need to be the same size on all devices, such as buttons and logos. Relative units can be useful for creating flexible layouts that will look good on a variety of devices.

```css
/* Set the width of an element to 100 pixels. */
.my-element {
  width: 100px;
}

/* Set the height of an element to 50% of the height of its parent element. */
.my-element {
  height: 50%;
}

/* Set the font size of an element to 2em, which is twice the font size of its parent element. */
.my-element {
  font-size: 2em;
}

/* Set the font size of an element to 1rem, which is the same as the font size of the root element of the document. */
.my-element {
  font-size: 1rem;
}

```