# Create your views here.
import json
import requests
from django.shortcuts import render

def partners(request):
	# get the list of todos
   response = requests.get('http://localhost:8989/api/v1/admin/partners')

   # transfor the response to json objects
   resp = response.json()
   datas = resp['data']['content']
   
   return render(request, "partners/view_partners.html", {"datas": datas})

# def detail(request, data):
# def detail(request,data):
def detail(request,data):
    data = request.get(data)
    print('======================')
    print(data+"oooooooooooooooo")
    return render(request,"partners/detail_partners.html")