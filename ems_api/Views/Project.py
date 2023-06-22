
from pstats import Stats
import statistics
from django.http import Http404

from ems_api.Models.Project import Project
from ems_api.serializers import ProjectSerializer
from ems_api.Models.Profile import Profile
from ems_api.serializers import ProfileSerializer
from ems_api.Models.Feedback import Feedback
from ems_api.serializers import FeedbackSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class ProjectList(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjecDetail(APIView):
    def get(self, request, pk):
        project = Project.objects.get(pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    
    def put(self, request, pk):
        project = Project.objects.get(pk=pk)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        project = Project.objects.get(pk=pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ProjectDetailView(APIView):
    def get(self, request, employee_id):
        try:
            profile = Project.objects.filter(employee_id=employee_id)
        except Project.DoesNotExist:
            return Response({'message': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProjectSerializer(profile, many=True)
        return Response(serializer.data)
