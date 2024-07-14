from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#def say_hello(request):
    #return HttpResponse('Hello World') #return crude html

def say_hello(request):
    return render(request, 'hello.html') #passes a html file :3

