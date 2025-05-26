from django.shortcuts import render
from .serializers import Registerserializer
from. models import Register
from rest_framework import generics
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def Home(request):
    data = {
        'message': 'welcome to the registration system',
        'status': 'success'

    }
    return Response(data, status=200)
@api_view(['GET'])
def RegisteredUsers(request):
    users = Register.objects.all()
    users =Register.objects.order_by('-id')
    users = Register.objects.filter(email__contains='')
    serializer = Registerserializer(users,many = True)
    return Response(serializer.data)
@api_view(['GET','POST'])
def Deleteuser(request):
    try:   
       user_to_erase = Register.objects.get(pk=6)
       user_to_erase.delete()
       data = {
        'message':'user deleted successfully'
     }
       return Response(data, status=200)
    except Exception as e:
     data = {
        'message':'user not found'
     }
     return Response(data, status=200)



    



# Create your views here.
