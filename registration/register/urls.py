from django.urls import path
from register import views

urlpatterns = [
   path('',views.reg),
   path('login',views.ulogin)
]
