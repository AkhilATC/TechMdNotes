## CSS Cookbook 🚀🚀🚀

### CSS Selector

- selectors are ways of grabbing and manipulating HTML
- Different type of selectors are:

1 . Element selector

```css
/* Element selector example */

p{
	font-size: 10px;
}

```

2. Class selector

```css
.class_name{

	/* css attributes */
}
```

3. ID selector

```css
#ELEMENT_ID{
	/* css body */
}
```


### pseudo selectors [link](https://www.w3schools.com/css/css_pseudo_classes.asp)

```css
/* css apply styling only if mouse over */
h2:hover{
	color:red
}

```
- li:only-child - ul having only one li child then 
- li: first-child -  for first child
- li:last-child - for last child
- li:nth-child(2) - for nth child pass child number as arg

### Advanced selectors

```css

/* css applied to <a> tag after h2 */
h2 + a{

	color : red;
}

h2 ~ p{}

ul > li {}
```

### Attribute selectors

```css
img[src$="url"]{}

img[src^="/img"]{}/* url start with "/img"*/

img[src*="/img"] {} /* repleat for all images having url prefix "/img"*/
```

### Properties

```css
background: linear-gradient(to right,white,greenyellow,greenyellow);
background: url("static/imgroot3.jpeg");
background-repeat: no-repeat;
background-size: cover; 
background: rgb(208, 219, 218); /*  bg color changed */

text-transform: uppercase; /* capitalize */
text-align: center; /* text align to center refer justify and other values  */
```
### units

```css
height: 400pc; /* pc,px learn more */
// font-size : 2em;// relative units
vh,vw - view-height, view-width
```

### CSS BOX MODEL 

![box_model](static/css-box-model.png?raw=true "box model in css")

- Every single elements are surrouded by a BOX
- Each layer represents a diffrent part of the model
- Each layer can be stretched and sized either symmetrically or asymmetrically
- __Padding__ represents the space b/w the content and the border
- __Border__ is the divider b/w Padding and Margin, it can be styled using a CSS property called __border__
- The __Margin__ is space b/w the border and all other content


```css
/* refer more */
border: 10px double black;
padding: 10px;
margin: 30px ; 
/* note this -> margin : top-value right-value botton-value left-value; */
/* note this -> padding : top-value right-value botton-value left-value; */
```

#### Display type

1. float

2. display


### Flexbox

- The container is the parent element in which the display type
is active, usually in the form of a div
- Flex items are child elements of the container

__HTML__

```html
<div class="down-text"> <!-- flex container-->
	<p id="groot-down-text">I'm Groot</p> <!-- flex items -->

	<p id="groot-down-text">I'm Groot</p> <!-- flex items -->

	<p id="groot-down-text">I'm Groot</p> <!-- flex items -->

	<p id="groot-down-text">I'm Groot</p> <!-- flex items -->

	<p id="groot-down-text">I'm Groot</p> <!-- flex items -->
</div>
```
__CSS__
```css
.down-text{
	display: flex;
	flex-direction: row;
	flex-wrap: wrap;
	
}
#groot-down-text{
	font-size: 2em;
	font-family: fantasy;
	color: red;
	margin: 20px;
	/* float: right; float element to right */
}
```

__flex-direction__: This property specfies the manner how the child flex items should displayed. For example all child items should displayed as a row then we can provide value as __'row'__ ( some value s are: row,coloumn,row-reverse,coloumn-reverse)
__flex-wrap__: Suppose we need to wrap the child elements in a flex box we can use __flex-wrap:wrap__ it will restrict skewing and rendered it as new row or coloumn.

``` flex-grow; flex-shrink; flex-basis; ```
#### Alignment

1. Horizontal alignment (justify-content)

- flex-start
- flex-end
- center
- space-around
- space-between

![horixontal_align](static/flex-box.png?raw=true "horizontal alignment")

2. vertical alignment (align-items)

- flex-start
- flex-end
- center
- baseline

![vertical_align](static/align-content.png?raw=true "vertical alignment")


### Grid

__HTML__
```html
<div class="grid-groot">
	
	<div class="grid-item"> <p> I "</p></div>
	<div class="grid-item"> <p> A </p></div>
	<div class="grid-item"> <p> M </p></div>

	<div class="grid-item"> <p> G </p></div>
	<div class="grid-item"> <p> R </p></div>
	<div class="grid-item"> <p> O </p></div>
	<div class="grid-item"> <p> O </p></div>
	<div class="grid-item"> <p> T </p></div>

</div>
```
__CSS__

```css
.grid-groot{
	display: grid;
	margin: 10px;
	width: 30%;
	grid-template-columns: auto auto auto ;
	grid-template-rows: auto auto;
	
}
.grid-item{
	background-color: purple;
	font-family: monospace;
	font-size: 3em;
	margin: 10px;
}
```
