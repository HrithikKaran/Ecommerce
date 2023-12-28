# I have created this view file
from django.shortcuts import render

def index(request):
    return render(request,'index.html')