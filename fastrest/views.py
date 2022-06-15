from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .models import emp_details
from .serializers import employeeSerializer
from. import serializers 
# from fastapi import FastAPI 
# from fastapi.requests import Request
# Create your views here.


# app = FastAPI()

class AddressBookApplication(viewsets.ModelViewSet):
     queryset = emp_details.objects.all()
     serializer_class = serializers.employeeSerializer

# by initializing this serializer_class we are telling, we have to use this employeeSerializer for the json conversion for this AddressBookApplication
# this class will create list(), retrive(), create(), update(), delete() sub classes for web methods (CRUD)


    