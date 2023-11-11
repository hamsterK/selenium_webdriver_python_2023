"""
syntax => webdriver.execute)script(script, *args)

.execute_script("return arguments[0].scrollIntoView(true);", element =>
scroll to make the desired element visible

.execute_script("window.open('http://parsinger.ru', 'tab2');") =>
creates new tab with name tab2

.execute_script("return document.body.scrollHeight") =>
return height of element 'body'

.execute_script("return window.innerHeight") =>
return height of browser window

.execute_script("return window.innerWidth") =>
return width of browser window

.execute_script("window.scrollBy(X, Y)") =>
scroll in pixels (X, Y)

.execute_script("alert('Text for alert')") =>
raise alert

.execute_script("return document.title;") =>
return title of open document

.execute_script("return document.documentURI;") =>
return URL of the document

.execute_script(return document.readyState;") =>
return state of the page (complete if loaded)

.execute_script("return document.anchors;") =>
return list of anchors on the page =>
[x.tag_name for x in browser.execute_script("return document.anchors;")]

.execute_script("return document.cookie;") =>
return string containing all cookies of the document devided by coma

.execute_script("return document.domain;") =>
return domain of the current document

.execute_script("return document.forms;") =>
return list of all forms on the page

.execute_script("window.scrollTo(X, Y);") =>
scroll to given coordinates

.execute_script("return document.getElementsByClassName('container');") =>
return list of all elements of given class

.execute_script("return document.getElementsByTagName('container');") =>
return list of all elements with given tag

.execute_script("return document.getElementById('some-id');") =>
return element with given ID

"""
