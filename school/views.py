from django.shortcuts import render
from django.http import request

def index(request):
    context ={}
    return render(request, 'school/index.html',context)
def registeral(request):
    

