from django.shortcuts import render
from django.http import HttpResponse # This is needed


# Create your views here.

# "Think of views as a place that handle your various web pages"
#   Do this with either functions or classes

# *args, **kwargs are python specific
# *args is used to send a non-keyworded and
#  variable length argument list to the function
# **kwargs allows to pass keyworded variable length
#   of arguments to a function
# args are passed as a tuple ()
# kwargs are passed as a dictionary {}
# https://stackoverflow.com/questions/3394835/use-of-args-and-kwargs

def home_view(request, *args, **kwargs):
    # This code will be executed if the home_view is called
    print(args, kwargs) # prints the passed args and kwargs to the console
    print(request.user) # prints the requesting user to the console
    
    log_user = "The user '{}' has entered the Website"
    print(log_user.format(request.user))
    
    #return HttpResponse("<h1>Hello, World!</h1>") # string of HTML code
    return render(request, "home.html", {})        # context: empty dictionary {}

def contact_view(request, *args, **kwargs):
    my_context = {
        "title": "this is about us",
        "this_is_true": True, 
        "my_number": 123,
        "my_list": [142, 4242, 80085, "Yoda"],
        "my_html": "<h1>Hello, world, sukka</h1>",
    }
    return render(request, "contact.html", my_context)