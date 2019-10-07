from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    #print(args,kwargs)
    #print(request.user)
    #return HttpResponse("<h1>Hello world</h1>")
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [123,456,789],
        "my_title": "gordon has a go at tryDjango",
        "my_html": "<h4>Render as HTML with the safe filter</h4>"
    }
    return render(request, "home.html", my_context)

def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact Page</h1>")