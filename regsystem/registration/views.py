from .serializers import Registerserializer
from. models import Register
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

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
@api_view(['GET'])
def Userdetails(request):
    try:
        user = Register.objects.get(id=2)
        serializer = Registerserializer(user)
        return Response(serializer.data)
    except Exception as e:
        data = {
            'message':'User not found'
        }
        return Response(data, status = 200)
@api_view(['GET'])
def Searchuser(request):
    
        query = request.query_params.get('q', None)
        if query:
                user = Register.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query))
                serializer = Registerserializer(user,many=True)
                return Response(serializer.data)
        

    #except Exception as e:
        return Response({'message':'Please enter a search parameter'}, status = 200)     
         


    



# Create your views here.
