from django.shortcuts import render
from django.http import HttpResponse

def count(n):
    return len(n)
# Create your views here.

def index(request):
    return HttpResponse("who is this")

def any(request, name):
    r=f"mr {name} has {count(name)} peepeepoopoo"
    return HttpResponse(r.capitalize())

