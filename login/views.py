# Create your views here.
import requests
from django.shortcuts import render

def login(request):
	context = {
	 	# 'title':'Kelas Terbuka',
	 	# 'heading':'Selamat Datang',
	 	# 'subheading':'di kelas terbuka',
	}
	return render(request,'login/login.html',context)

def register(request):
	context = {
	 	# 'title':'Kelas Terbuka',
	 	# 'heading':'Selamat Datang',
	 	# 'subheading':'di kelas terbuka',
	}
	return render(request,'login/register.html',context)