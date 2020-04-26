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
	published =[]

	for i in range(len(articles)):
		myarticles = articles[i]

		news.append(myarticles['title'])
		desc.append(myarticles['description'])
		img.append(myarticles['url'])
		published.append(myarticles['publishedAt'])
	mylist = zip(news,  desc, img, published)
	# print(mylist)
	return render(request, 'index.html', context = {'mylist':mylist})


