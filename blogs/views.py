from django.shortcuts import render
from blogs.models import Blogs
# Create your views here.

def home(request):
	blog = Blogs.objects.all()
	context = {
		'title': 'Clean Blog',
		'slogan': 'A Clean Blog Theme by Start Bootstrap',
		'image': 'static/home-bg.jpg',
		'blogs': blog
	}
	return render(request,'home.html', context)


def contact(request):
	context = {
		'title': 'Contact Me',
		'slogan': 'Have questions? I have answers (maybe).',
		'image': 'static/contact-bg.jpg',	
	}
	return render(request,'contact.html', context)


def about(request):
	context = {
		'title': 'About Me',
		'slogan': 'This is what I do.',
		'image': 'static/about-bg.jpg',
	}
	return render(request,'about.html', context)


def post(request):
	context = {
		'image': 'static/post-bg.jpg',	
	}
	return render(request,'post.html', context)