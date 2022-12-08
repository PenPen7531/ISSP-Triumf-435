# CSS Documentation
CSS or Cascading Style Sheet is a web development tool that allows us to position objects on a webpage, change the style and size of fonts, change colours, and more! You can be very creative with CSS. This document will talk about how we use CSS, what we did in this project, and some basic CSS styling. 

## Selecting Elements
There are multiple ways of selecting elements on an HTML page. Based on how specific the selector is, the higher the priority will be. From most priority to lowest, these are:
<ol>
<li>IDs</li>
<li>Classes</li>
<li>Elements</li>
</ol>
<br>

### IDs
IDs allow only a singular object to be selected. This is because IDs can only be given to one element in an HTMl document. Let's see how we can give an HTML element an ID. See the example below

```HTML
<h1 id="myHeader">My Header 1</h1>
```
We can see above, we use the id argument to name the ID. Now let's see how we select it in CSS

```CSS
#myHeader{
    color: red;
}
```

The code above shows us how to select an ID in a CSS style sheet. We can see that we must use # to specify we are trying to select an ID and using the ID name. 