from django.urls import path,include
from django.contrib import admin
from . import views
from rest_framework import routers
#we have to map urls into the viewset functions inside the application. 
router = routers.DefaultRouter()
router.register('emp_details',views.AddressBookApplication)

#router urls need to map to our application urls.

urlpatterns = [
    path('',include(router.urls)),
    
]