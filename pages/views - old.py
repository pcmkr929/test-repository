"""
    This view is without render(), using the simple HttpResponse()
    This goes until the "Django Templates" part of the youtube tutorial
        "Python Django Web Framework - Full Course for Beginners"
        ~ 1/3 passed in the video, so its still at the beginning
"""

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
    
    return HttpResponse("<h1>Hello, World!</h1>") # string of HTML code

def contact_view(request, *args, **kwargs):
    return HttpResponse("<h1>Contact Page</h1>")