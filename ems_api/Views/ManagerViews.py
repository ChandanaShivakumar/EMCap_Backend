from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ems_api.Models.Manager import Manager
from ems_api.serializers import ManagerSerializer
from rest_framework.parsers import MultiPartParser, FormParser

@api_view(['GET', 'POST'])
def ManagerView(request):
    if request.method == 'GET':
        manager = Manager.objects.all()
        serializers = ManagerSerializer(manager, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = ManagerSerializer(data=request.data, context={'request': request})
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

   

@api_view(['GET','PUT','DELETE'])
def ManagerView_id(request,id):
    try:
        manager = Manager.objects.get(pk=id)
    
    except Manager.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
       serializers = ManagerSerializer(manager)
       return Response(serializers.data)
    elif request.method == 'PUT':
         serializers = ManagerSerializer(manager,request.data)
         if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
         return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
      manager.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def ManagerViewByUserId(request, user_id):
    try:
        manager = Manager.objects.get(user_id=user_id)
        serializer = ManagerSerializer(manager)
        return Response(serializer.data)
    except Manager.DoesNotExist:
        return Response({'error': 'Manager not found for the given user ID.'})

