from pstats import Stats
import statistics
from django.http import Http404
from rest_framework.response import Response
from ems_api.Models.Training import Training
from ems_api.serializers import TrainingSerializer
from ems_api.Models.Profile import Profile
from ems_api.serializers import ProfileSerializer
from ems_api.Models.Feedback import Feedback
from ems_api.serializers import FeedbackSerializer
from rest_framework.views import APIView
from rest_framework import status


class TrainingList(APIView):
    def get(self, request):
        projects = Training.objects.all()
        serializer = TrainingSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TrainingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TrainingDetail(APIView):
    def get(self, request, pk):
        training = Training.objects.get(pk=pk)
        serializer = TrainingSerializer(training)
        return Response(serializer.data)
    
    def put(self, request, pk):
        training = Training.objects.get(pk=pk)
        serializer = TrainingSerializer(training, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        training = Training.objects.get(pk=pk)
        training.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class TrainingDetailView(APIView):
    def get(self, request, employee_id):
        try:
            training = Training.objects.filter(employee_id=employee_id)
        except Training.DoesNotExist:
            return Response({'message': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TrainingSerializer(training, many=True)
        return Response(serializer.data)