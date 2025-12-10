from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse



def index(request):
    return render(request,"index.html",{})
def index2(request):
    return render(request,"index2.html",{})
