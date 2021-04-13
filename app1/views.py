from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome to Index of app1</h1>")


def sample(request):
    return render(request,"sample1.html")

def carry_data(request,data):
    return HttpResponse(f'<h1>The Recieved data is {data}</h1>')

