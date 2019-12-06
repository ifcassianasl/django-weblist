from django.shortcuts import render
from .models import Search
from bs4 import BeautifulSoup

def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST['search']
    stuff_for_frontend = {
        'search': search,
    }
    return render(request, 'web_list/new_search.html', stuff_for_frontend)