from django.urls import path
# from .views import index, word
from .views import index, word

urlpatterns = [
    path('', index, name='index'),
    path('word/', word, name='word')
]

