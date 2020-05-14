# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests, json
from django.shortcuts import render
from newsapi import NewsApiClient
# Create your views here.

def home(request):
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

def world(request):
	newsapi = NewsApiClient(api_key='ac3f3a791a17403f911101c1c8893f73')
	all_articles = newsapi.get_everything(sources='bbc-news,the-verge')
	articles = all_articles['articles']
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


def business(request):
	newsapi = NewsApiClient(api_key='ac3f3a791a17403f911101c1c8893f73')
	all_articles = newsapi.get_top_headlines(country='in', category="business")
	articles = all_articles['articles']
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

def entertainment(request):
	newsapi = NewsApiClient(api_key='ac3f3a791a17403f911101c1c8893f73')
	all_articles = newsapi.get_top_headlines(country='in', category='entertainment')
	articles = all_articles['articles']
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

def health(request):
	newsapi = NewsApiClient(api_key='ac3f3a791a17403f911101c1c8893f73')
	all_articles = newsapi.get_top_headlines(country='in', category='health')
	articles = all_articles['articles']
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

def science(request):
	newsapi = NewsApiClient(api_key='ac3f3a791a17403f911101c1c8893f73')
	all_articles = newsapi.get_top_headlines(country='in', category='science')
	articles = all_articles['articles']
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


def sports(request):
	newsapi = NewsApiClient(api_key='ac3f3a791a17403f911101c1c8893f73')
	all_articles = newsapi.get_top_headlines(country='in', category='sports')
	articles = all_articles['articles']
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

def technology(request):
	newsapi = NewsApiClient(api_key='ac3f3a791a17403f911101c1c8893f73')
	all_articles = newsapi.get_top_headlines(country='in', category='technology')
	articles = all_articles['articles']
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

def about(request):
	return render(request,'about.html',{})

def search(request):
	keyword=""
	if request.method=='POST':
		keyword=request.POST['keyword']
	url="https://newsapi.org/v2/everything?q="+keyword+"&apiKey=ac3f3a791a17403f911101c1c8893f73&language=en&sortBy=publishedAt"
	api_request=requests.get(url)
	api=json.loads(api_request.content)
	if api["status"]=="error":
		return render(request,'index.html',{'KeyError': 'KeyError'})
	# return render(request,'index.html',{'api':api,'keyword':keyword})
	articles = api['articles']
	desc = []
	news = []
	img = []
	url = []
	published =[]
	
	try:
		for i in range(len(api)):
			myarticles = articles[i]

			img.append(myarticles['urlToImage'])
			news.append(myarticles['title'])
			desc.append(myarticles['description'])
			url.append(myarticles['url'])
			published.append(myarticles['publishedAt'])
	except IndexError:
 		pass
 	except KeyError:
 		pass
	mylist = zip(img, news,  desc, url, published)
	# print(mylist)
	return render(request, 'index.html', {'mylist':mylist, 'keyword': keyword})