
from django.urls import path
from . import views

urlpatterns =[
   path('', views.Home, name='Home'),
   path('RegisteredUsers',views.RegisteredUsers, name='RegisteredUsers'),
   path('Deleteuser', views.Deleteuser, name='Deleteuser')
]