from django.forms.widgets import HiddenInput
from pyowm import OWM



'''
#Error/Old
API_key = '7e7dae4857ca4c6e4f1566f301e5e591'
owm = OWM(API_key)
mgr = owm.weather_manager()
obs = mgr.weather_at_coords(-0.107331,51.503614)  
seoul_weather = obs.get_weather()
print(seoul_weather)
res = seoul_weather.get_wind() 
print(res)
'''
'''
#New, Testing to use it for the website
API_key = '7e7dae4857ca4c6e4f1566f301e5e591'
owm = OWM(API_key)
mgr = owm.weather_manager()
obs = mgr.weather_at_coords(-0.107331,51.503614)
w = obs.weather
print(w) #<pyowm.weatherapi25.weather.Weather - reference_time=2021-08-11 09:23:03+00:00, status=clouds, detailed_status=scattered clouds>
res = w.status 
print(res, '1') # Rain
res1 = w.detailed_status
print(res1, '2') # moderate/light rain
w2 = obs.weather.wind()
print(w2, '3') # {'speed': 3.6, 'deg': 250}
'''
'''
a = 'Hi'
b = 'Jiwon'
c = 'Have a nice day'
print(a, ',', b,'.', c,'.')
'''

p = (1,2,3,4)
print(p[1])