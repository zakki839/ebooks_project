from django.shortcuts import render,HttpResponse




# Create your views here.

def blog_list(request):
    return HttpResponse("Blog List")
