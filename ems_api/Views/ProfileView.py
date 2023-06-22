
from pstats import Stats
import statistics
from django.http import Http404
from rest_framework.response import Response
from ems_api.Models.Profile import Profile
from ems_api.serializers import ProfileSerializer
from ems_api.Models.Feedback import Feedback
from ems_api.serializers import FeedbackSerializer
from rest_framework.views import APIView
from rest_framework import status
class ProfileList(APIView):
    """
    List all profiles or create a new profile.
    """
    def get(self, request, format=None):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class ProfileDetail(APIView):
    """
    Retrieve, update or delete a profile instance.
    """
    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class ProfileDetailView(APIView):
    def get(self, request, employee_id):
        try:
            profile = Profile.objects.get(employee_id=employee_id)
        except Profile.DoesNotExist:
            return Response({'message': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    