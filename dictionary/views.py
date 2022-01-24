from django.shortcuts import render
from PyDictionary import PyDictionary


dictionary = PyDictionary()
import requests
from bs4 import BeautifulSoup

# it is some code form stackoverflow to find synonyms
# def synonyms(term):
#     response = requests.get('https://www.thesaurus.com/browse/{}'.format(term))
#     soup = BeautifulSoup(response.text, 'html.parser')
#     soup.find('section', {'class': 'css-191l5o0-ClassicContentCard e1qo4u830'})
#     return [span.text for span in soup.findAll('a', {'class': 'css-1kg1yv8 eh475bn0'})] 


def index(request):
  return render(request, 'index.html')

def word(request):
  search = request.GET.get('search')
  diction = PyDictionary()
  meaning = diction.meaning(search)
  response = requests.get('https://www.thesaurus.com/browse/{}'.format(search))
  soup = BeautifulSoup(response.text, 'html.parser')
  soup.find('section', {'class': 'css-191l5o0-ClassicContentCard e1qo4u830'})
  synonyms = [span.text for span in soup.findAll('a', {'class': 'css-1kg1yv8 eh475bn0'})] 

# I can not do my dictionary to find antonyms of searching word
  # antonyms = diction.antonym(search)
  
  context = {'meaning': meaning['Noun'][0],
            'synonyms': synonyms,
              # 'antonyms': antonyms,
              'search': search,
            }
  return render(request, 'word.html', context)

