from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    html="""
    
<html>
<head>
<title>string format</title>
</head>
<body>
<div>
<form action="" method='get'>
<input type="text" name="inputtext" placeholder="enter your text" value= '{1}'/>
<p>{0}</p>
<hr/>
<br/>
<table>
    <tr>
        <td> <input type="submit" name="upper" value="uppercase"/></td>
        <td> <input type="submit" name="lower" value="lowercase"/></td>
        <td> <input type="submit" name="capitalize" value="capitalizecase"/></td>
        <td> <input type="submit" name="bold" value="boldcase"/></td>
        <td> <input type="submit" name="title" value="titlecase"/></td>
        <td> <input type="submit" name="count" value="countcase"/></td>
        <td> <input type="submit" name="itallic" value="itallic"/></td>
    </tr>
</div>
</form>


</body>
</html>"""
    if "inputtext" in request.GET:
        inputtext = request.GET["inputtext"]
        print(inputtext)
    if 'upper' in request.GET:   
        outputstring = html.format(inputtext.upper(),inputtext)
    elif 'lower' in request.GET:
        outputstring = html.format(inputtext.lower(),inputtext)
    elif 'capitalize' in request.GET:
        outputstring = html.format(inputtext.capitalize(),inputtext)
    elif 'bold' in request.GET:
        inp = f'<b>{inputtext}</b>'
        outputstring = html.format(inp,inputtext)
    elif 'title' in request.GET:
        outputstring = html.format(inputtext.title(),inputtext)
    elif 'count' in request.GET:
        outputstring = html.format(inputtext.count(),inputtext)
    elif 'itallic' in request.GET:
        inp=f'<i>{inputtext}</i>'
        outputstring = html.format(inp,inputtext)   
    else:
        outputstring =html
        


    return HttpResponse(outputstring)
