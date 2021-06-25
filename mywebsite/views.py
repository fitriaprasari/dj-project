import requests
from django.shortcuts import render

def index(request):
	context = {
	 	# 'title':'Kelas Terbuka',
	 	# 'heading':'Selamat Datang',
	 	# 'subheading':'di kelas terbuka',
	}
	return render(request,'index.html',context)

def login(request):
	context = {
	 	# 'title':'Kelas Terbuka',
	 	# 'heading':'Selamat Datang',
	 	# 'subheading':'di kelas terbuka',
	}
	return render(request,'login.html',context)	

# def register(request):
	
# 	context = {
# 	 	# 'title':'Kelas Terbuka',
# 	 	# 'heading':'Selamat Datang',
# 	 	# 'subheading':'di kelas terbuka',
# 		 nav = {getdata }
# 	}
# 	return render(request,'register.html',context)	

def caripartner(request):
	context = {
	 	# 'title':'Kelas Terbuka',
	 	# 'heading':'Selamat Datang',
	 	# 'subheading':'di kelas terbuka',
	}
	return render(request,'layout-static.html',context)	

def transactions(request):
	context = {
	 	# 'title':'Kelas Terbuka',
	 	# 'heading':'Selamat Datang',
	 	# 'subheading':'di kelas terbuka',
	}
	return render(request,'tables.html',context)	

def req(request):
	# get the list of todos
   response = requests.get('http://localhost:8989/api/v1/admin/partners')

   # transfor the response to json objects
   datas = response.json()
   return render(request, "home.html", {"datas": datas})

	