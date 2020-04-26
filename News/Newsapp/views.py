# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from newsapi import NewsApiClient
# Create your views here.

def index(request):
	newsapi = NewsApiClient(api_key='ac3f3a791a17403f911101c1c8893f73')
	top_headlines = newsapi.get_top_headlines(country='in')
	articles = top_headlines['articles']
	desc = []
	news = []
	img = []
	url = []
	published =[]

	for i in range(len(articles)):
		myarticles = articles[i]

		img.append(myarticles['urlToImage'])
		news.append(myarticles['title'])
		desc.append(myarticles['description'])
		url.append(myarticles['url'])
		published.append(myarticles['publishedAt'])
	
	mylist = zip(img, news,  desc, url, published)
	# print(mylist)
	return render(request, 'index.html', context = {'mylist':mylist})


