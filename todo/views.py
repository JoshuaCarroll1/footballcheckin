from django.shortcuts import render
from django.views import generic


# Create your views here.
def get_index(request):
    return render(request, 'todo/index.html')


def get_about(request):
    return render(request, 'todo/about.html')
