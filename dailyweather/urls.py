from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('<int:id>/', views.post_new2),
    path('new/', views.post_new, name='post_new'),

]