from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    # path('', views.index, name= 'home'),
    path('', views.updates, name= 'updates'),
    path('about', views.about, name= 'about'),
    # path('contact', views.contact, name= 'contact'),
    path('news', views.get_news, name= 'generalnews'),
    # path('vaccine', views.vaccine_pin, name= 'pincode'),
    path('vaccine', views.vaccine_print),
]