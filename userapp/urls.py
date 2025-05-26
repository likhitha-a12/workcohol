from django.urls import path , include
from django.contrib import admin
from userapp import views
from . import views
urlpatterns=[   
    path('',views.user,name='register'),
     path('login/',views.login,name='login'),
     path('logout/',views.logout,name='logout'),
]

