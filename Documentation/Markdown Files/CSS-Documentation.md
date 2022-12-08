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

### Classes
Classes allow groups of elements to be selected at the same time. This allows elements that need the same styling to be styled at the same time. This reduces the code needed to be produced.
An example of this is shown below. We will have multiple list items that will need the same background color and width. So let's give all of them the same class.

```HTML
<li class="list">List Element 1</li>
<li class="list">List Element 2</li>
<li class="list">List Element 3</li>
<li class="list">List Element 4</li>
```
Now since all these HTMl elements have the same class. We can use the same CSS code for all. 

```CSS
.list{
    background-color: grey;
}
```
Now all the list items have the background colour of grey.

### Elements
Elements can also be grouped based on the type of the element. So all H1s can be grouped together into the same CSS block without having to specify an class. This can be used but it is not recommended since different elements with the same type can conflict in CSS. Let's take a look at a bad example. 
<br>
Let's say you want to change 1 paragraph tag to have the background colour of red. But you want to have the rest of the paragraphs tags to have a background colour of blue. If you were to use just the element to specify the CSS, then all p tags will then be the colour red or blue. This is why classes and IDs are very important and CSS will select the highest priority specified above. 

```HTML
<!-- Elements without any class or ID -->
<p>I want this blue</p>
<p>I also want this blue
<p>I want this red</p>
```

```CSS
/* Both Tags will now be red */
p{
    background-colour: red;
}
```
<br>
Now let's take a look at how it should be done. If you want all elements of the same type to have the same background colour then fine. Selecting just based on the element is fine. But I would recommend using an ID for the one P tag that wants a background colour of red, and then either use a class for the other p tags or just select all the p tags. See the example below:

```HTML
<!-- The red element has an ID -->
<p>I want this blue</p>
<p>I also want this blue</p>
<p id="redBackground">I want this red</p>
```

Now that we have the ID tag in the paragraph element that we want red, we can specify it in our CSS file. And then since CSS uses the most specific, we can then use the p element to make every other paragraph blue

```CSS
/* The ID. It is also more specific so it will take priority over the p tag. */
#redBackground{
    background-color:red;
}

p{
    background-color: blue;
}
```
