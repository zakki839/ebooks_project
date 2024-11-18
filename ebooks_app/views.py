from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    name = "Doe"
    return render(request, 'home.html', {'name': name})

def book_list(request):
    return HttpResponse("Book List")

def book_detail(request, slug):
    # 'slug' will be passed in the URL pattern
    return HttpResponse(f"Book Detail: {slug}")

def blog_list(request):
    return HttpResponse("Blog List from app")

def contact(request):
    return HttpResponse("Contact us")
