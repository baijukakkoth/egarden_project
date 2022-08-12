from ast import Return
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def callpage(request):
    return render(request, 'loginpage.html')

def callsingup(request):
    return render(request, 'signuppage.html')

def callheadfoot(request):
    return render(request, 'head_foot.html')

def callchecktest(request):
    return render(request, 'check_test.html')

