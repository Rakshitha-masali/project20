from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>hello this is app2 view</h1>")

def sample2(request):
    return render(request,"sample2.html")

def carry(request,data):
    return HttpResponse(f'<h1>welcome to {data}</h1>')
    

