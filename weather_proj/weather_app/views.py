from django.shortcuts import render 
import requests
import datetime


# Create your views here.
def index (request):
   if request.method=='POST':
      city= request.POST.get('city', 'Lahore')
   else:
      ip_info = requests.get('https://ipinfo.io/json')
      ip_data = ip_info.json()
      city = ip_data.get('city', 'Lahore')
      
     
      
      
      
   url =  f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a90f6047f1c5133d228add37244b364e'
   params  ={'units':'metric'} 
   response = requests.get(url, params =params)
   
   data=response.json()

   description = data['weather'][0]['description']
   icon = data['weather'][0]['icon']
   temp=data['main']['temp']
   day= datetime.date.today()
   

   return render(request, 'weather_app/index.html',{'description':description, 'icon':icon, 'temp':temp, 'day':day, 'city':city})