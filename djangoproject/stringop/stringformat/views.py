from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    htmlstring ="""<html>
<head>
<title>StringFormat</title>
</head>

<body>
<div>
<form action="">
<input type="text" name="inputtext" placeholder="Enter you text" value='{1}' />
<p> {0} </p>
<hr />
<br />
<table border=0>
	<tr>
    	<td>	<input type="submit" name="upper" value="UpperCase" /> </td>
        <td>	<input type="submit" name="lower" value="LowerCase" /> </td>
        <td>	<input type="submit" name="capitalize" value="CapitalizeCase" /> </td>
        <td>	<input type="submit" name="title" value="TitleCase" /> </td>
        <td>	<input type="submit" name="bold" value="Bold" /> </td>
        <td>	<input type="submit" name="itallic" value="Itallic" /> </td>
        
    </tr>
    
</table>

</form>
</div>
</body>

</html>"""

    if "inputtext" in request.GET:
        inputtext = request.GET['inputtext']

        print(inputtext)
        if 'upper' in request.GET:
            outputstring = htmlstring.format(inputtext.upper(), inputtext)
        elif 'lower' in request.GET:
            outputstring = htmlstring.format(inputtext.lower(), inputtext)
        elif 'capitalize' in request.GET:
            outputstring = htmlstring.format(inputtext.capitalize(), inputtext)
        elif 'title' in request.GET:
            outputstring = htmlstring.format(inputtext.title(), inputtext)
        elif 'bold' in request.GET:
            inp = f'<b>{inputtext}</b>'
            outputstring = htmlstring.format(inp, inputtext)
        elif 'itallic' in request.GET:
            inp = f'<i>{inputtext}</i>'
            outputstring = htmlstring.format(inp, inputtext)    

    else:
        outputstring = htmlstring

    return HttpResponse(outputstring)