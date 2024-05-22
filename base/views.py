from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q 
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(['GET'])
def endpoints(request):
    data = Advocate.objects.all()
    context = {
        'advocate':data
    }
    data = ['/advocate','advocate/username']
    return Response(data)
    # return render(request,'home.html',context)

@api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
def advocate_list(request):
    
    if request.method == 'GET':

        query = request.GET.get('query')

        if query == None:
            query = ''
        
        advocate = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
        serializer = Advocateserializer(advocate, many= True)
        if not advocate:
            return Response('The data is not present')
        return Response(serializer.data)
    
    if request.method == 'POST':
        Advocate.objects.create(
        username = request.data['username'],
        bio = request.data['bio']
    )
    
    return Response('added')


class Advocatedetails(APIView):
    def get(self, request, username):
        try:
            advocate = Advocate.objects.get(username= username)
            serializer = Advocateserializer(advocate, many=False)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response('The data is not present')
        
    def put(self, request, username):
        advocate = Advocate.objects.get(username = username)
        advocate.username = request.data['username']
        advocate.bio = request.data['bio']
        advocate.save()
        serializer = Advocateserializer(advocate, many = False)
        return Response(serializer.data)
    
    def delete(self, request, username):
        advocate = Advocate.objects.get(username= username)
        advocate.delete()
        return Response('User is deleted')