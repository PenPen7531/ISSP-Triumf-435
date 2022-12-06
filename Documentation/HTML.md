# HTML Documentation

## What is HTML
HTML, also known as HTML5, or HyperText Markdown Language, is a web development languaged used to create webpages. You can specify headers, paragraphs, links, images, and more on a webpage. Consider HTML the template or strucure of a webpage. HTML is not designed to make the webpage look pretty...that's CSS, which we can directly add to the HTML file, or use an external CSS file with a link to the HTML page. 

## Parts of the HTML Page
There are 2 main parts of the HTML page. 
<ul>
    <li>Header</li>
    <li>Body</li>
</ul>

### Header
The header is usually written in the top part of the HTML document. It contains information about the webpage, such as the refresh rate, the title or the tab name, and links to other resources such as CSS and JavaScript resources. 
#### Linking an External CSS Page
To link an external CSS page, we use the link tag. The link tag will allow us to link an external CSS page. We can use the href argument to point to the CSS resource on the webpage. We will use the rel argument to specificy what resource is being accessed. An example of this is
```
<link rel="stylesheet" href="{{ url_for('static', filename='css/create.css') }}">
```
<b><span>This format is used when working with Flask, the href argument will look different when serving a static webpage without Flask</span> </b>

#### Linking CSS within an HTML Page
To quickly add CSS within a HTML page, we can use the styles tag. This will allow CSS to be added within the HTML page. An example would be:
```
<styles>
    background-color: red;
</styles>
```

#### Linking an External JavaScript Page
To link an external JavaScript page, we use the script tag. This will allow us to connect external JavaScript code with our HTML page. We will use the src argument to point to the JavaScript file. An example of this would be:
```
<script src="../../static/js/create.js"></script>
```
<br>

You can also use the script tag to make inline JavaScript code. Like this:
```
<script>
    //Some JavaScript Code
</script>
```