from django.conf.urls import url
# from django.contrib import admin
from .views import *

urlpatterns = [
	url(r'^$', home, name='home'),
    url('home', home, name='home'),
    url('world', world,name='world'),
    url('business', business, name='business'),
    url('entertainment', entertainment, name='entertainment'),
    url('health', health,name='health'),
    url('science', science,name='science'),
    url('sports', sports, name='sports'),
    url('technology', technology, name='technology'),
    url('about', about, name='about'),
    url('search', search, name='search')

]