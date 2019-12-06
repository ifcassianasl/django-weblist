from django.shortcuts import render
from .models import Search
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus

BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/?query=python%20tutor'

def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST['search']
    
    new_s = Search(search=search)
    new_s.save()

    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text

    soup = BeautifulSoup(data, features='html.parser')
    post_titles = soup.find_all('a', {'class': 'result-title'})
    post_listings = soup.find_all('li', {'class': 'result-row'})
    
    stuff_for_frontend = {
        'search': search,
    }
    return render(request, 'web_list/new_search.html', stuff_for_frontend)