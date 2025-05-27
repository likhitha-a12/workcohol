#eventapp/urls.py#

from django.urls import path, include
from rest_framework import routers
from . import views
from .views import EventViewSet

router = routers.DefaultRouter()
router.register(r'events', EventViewSet) 


urlpatterns = [
    path('api/', include(router.urls)),  
    path('api/contact/', views.contact_api, name='contact_api'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('booking/', views.booking, name='booking'),  
    path('contact/', views.contact, name='contact'),
    
]



