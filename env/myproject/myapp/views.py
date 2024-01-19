from django.shortcuts import render

# create your views here.

def home(request):
    return render(request,'home.html')

def foodmenu(request):
    return render(request,'foodmenu.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

