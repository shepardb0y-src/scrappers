from django.shortcuts import render

# Create your views here.
import requests
from bs4 import BeautifulSoup


def scrape(request):
    page = requests.get('https://www.google.com')
    soup = BeautifulSoup(page.text, "html.parser")

    link_address = []

    for link in soup.find_all('a'):
        link_address.append(link.get('href'))

    return render(request, 'myapp/result.html', {'link_address': link_address})
