from django.http.response import HttpResponse
from .models import GPSPosition
from django.shortcuts import get_object_or_404, render, redirect
from .form import PostForm, MapForm
from pyowm import OWM
from django.utils import timezone

# Create your views here.
# def post_new2(request, id):
#     post = get_object_or_404(GPSPosition, pk=id)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             API_key = '7e7dae4857ca4c6e4f1566f301e5e591'
#             owm = OWM(API_key)
#             mgr = owm.weather_manager()
#             obs = mgr.owm.coord_at(post.latitude,post.logitude)
#             # obs = mgr.weather_at_place('London,GB')
#             w = obs.weather
#             res = w.status # Clouds
#             res1 = w.detailed_status # scattered clouds 
#             w2 = obs.weather.wind() # {'speed': 3.6, 'deg': 250} 
#             post.weather_three = res,';',res1,';', w2  
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', id=id)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'dailyweather/post_edit.html', {'form': form})

import requests
# lat = 경도를 적어주세요
# lng = 위도를 적어주세요

# weather_url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lng}&exclude=hourly,daily&appid=____나의인증키를넣어준다____'
# res = requests.get(weather_url)
# data = res.json()
# temp = data['current']['temp']-273.15
# if temp < 0:
#     print(f'현재 온도는 {temp}도 입니다. 목도리하고 나가세요!')
 

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            print(post.latitude)
            
            API_key = '7e7dae4857ca4c6e4f1566f301e5e591'
            owm = OWM(API_key)
            mgr = owm.weather_manager()
            obs = mgr.weather_at_coords(int(post.latitude),int(post.longitude))
            w = obs.weather
            res = w.status # Clouds
            res1 = w.detailed_status # scattered clouds 
            w2 = obs.weather.wind() # {'speed': 3.6, 'deg': 250} 
            post.weather = res,';',res1,';', w2  
            post.data_pub = timezone.now()
            post.save()
            
            return HttpResponse(post.weather)
    else:
        form = PostForm()
    return render(request, 'dailyweather/post_edit.html', {'form': form})

#display map
def map_insert(request):
    form = MapForm()
    return render(request, 'addmap.html', {'form': form})    