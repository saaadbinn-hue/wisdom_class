from .import views
from django.urls import path
from django.contrib import admin


urlpatterns = [
    path('',views.Home,name="home"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about),
]
