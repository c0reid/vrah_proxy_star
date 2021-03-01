from django.shortcuts import render
from django.http import HttpResponse



def home_page_view2(request):
    return HttpResponse('Hello, World!')



def home_page_view(request):
    return render(request,'home.html')
