from pstats import Stats
import statistics
from django.http import Http404
from rest_framework.response import Response
from ems_api.Models.POC import POC
from ems_api.serializers import POCSerializer
from ems_api.Models.Profile import Profile
from ems_api.serializers import ProfileSerializer
from ems_api.Models.Feedback import Feedback
from ems_api.serializers import FeedbackSerializer
from rest_framework.views import APIView
from rest_framework import status

class POCList(APIView):
    def get(self, request):
        projects = POC.objects.all()
        serializer = POCSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = POCSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class POCDetail(APIView):
    def get(self, request, pk):
        poc = POC.objects.get(pk=pk)
        serializer = POCSerializer(poc)
        return Response(serializer.data)
    
    def put(self, request, pk):
        poc = POC.objects.get(pk=pk)
        serializer = POCSerializer(poc, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        poc = POC.objects.get(pk=pk)
        poc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class POCDetailView(APIView):
    def get(self, request, employee_id):
        try:
            poc= POC.objects.filter(employee_id=employee_id)
        except POC.DoesNotExist:
            return Response({'message': 'POC  not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = POCSerializer(poc, many=True)
        return Response(serializer.data)