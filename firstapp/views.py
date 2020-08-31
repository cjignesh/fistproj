from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def name(request):
    return render(request, "name.html")

def home(request):
    #return HttpResponse("Happy Birth Day")
    name = request.POST['name']
    return render(request, "home.html", {'name': name})

def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2
    return render(request, "result.html", {'result': res})
