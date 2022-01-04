from django.contrib import admin

from travelproject import settings
from . import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo')
    #path('add/',views.addition,name='addition')
    #path('about/',views.about,name='about'),
    #path('contact/',views.contact,name='name')
]


