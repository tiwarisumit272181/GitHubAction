from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
   path('sayHi/' , views.sayHello , name="sayHello"),
   path('postUser/' , views.postUser , name="postUser")
]
