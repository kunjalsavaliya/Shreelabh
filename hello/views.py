from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'hello/index.html')

# Create your views here.
