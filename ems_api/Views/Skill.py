from pstats import Stats
import statistics
from django.http import Http404

from ems_api.Models.Skill import Skill
from ems_api.serializers import SkillSerializer
from ems_api.Models.Profile import Profile
from ems_api.serializers import ProfileSerializer
from ems_api.Models.Feedback import Feedback
from ems_api.serializers import FeedbackSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
class SkillList(APIView):
    def get(self, request):
        projects = Skill.objects.all()
        serializer = SkillSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SkillDetail(APIView):
    def get(self, request, pk):
        skill = Skill.objects.get(pk=pk)
        serializer = SkillSerializer(skill)
        return Response(serializer.data)
    
    def put(self, request, pk):
        skill = Skill.objects.get(pk=pk)
        serializer = SkillSerializer(skill, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        skill = Skill.objects.get(pk=pk)
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SkillDetailView(APIView):
    def get(self, request, employee_id):
        try:
            skill= Skill.objects.filter(emp_id=employee_id)
        except Skill.DoesNotExist:
            return Response({'message': 'skill  not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SkillSerializer(skill, many=True)
        return Response(serializer.data)