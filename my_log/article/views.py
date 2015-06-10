from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('Hello Python,Hello Django')
def detail(request,my_args):
    return HttpResponse('input number is %s'% my_args)
