Weather Information Website Project 
=====

Introduction
----

Hi, this is my weather website project.
The website that gives weather information of the location pin-pointed or searched by a user. It is created by using Django formattings and Python language.

Once you finish downloading Django, you can start from creating a project.

Then, create an app using Django commands within the directory that includes **manage.py**.

```
$ startapp dailyweather 
```

### dailyWeather File

The dailyWeather file will have initially,
- admin.py
- apps.py
- models.py
- tests.py
- views.py

Create **urls.py** file and add:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

```python

```

### weathersite File

