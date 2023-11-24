from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def calculate():
    x = 1
    y = 2
    return x

def sayHello(req):
    x = calculate()
    y = 2
    return render(req, "hello.html", {'name': "Muthiah"})

