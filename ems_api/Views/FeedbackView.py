
from django.http import Http404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ems_api.Models.Feedback import Feedback
from ems_api.serializers import FeedbackSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import status as stats
from rest_framework.response import Response

class FeedbackList(APIView):
    def get(self, request):
        feedback = Feedback.objects.all()
        serializer = FeedbackSerializer(feedback, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FeedbackDetail(APIView):
    def get_object(self, pk):
        try:
            return Feedback.objects.get(pk=pk)
        except Feedback.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        feedback = self.get_object(pk)
        serializer = FeedbackSerializer(feedback)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        feedback = self.get_object(pk)
        serializer = FeedbackSerializer(feedback, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        feedback = self.get_object(pk)
        feedback.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class FeedbackDetailView(APIView):
    def get(self, request, employee_id):
        try:
            feedback= Feedback.objects.filter(fresher_id=employee_id)
        except Feedback.DoesNotExist:
            return Response({'message': 'Still no feedback get '}, status=status.HTTP_404_NOT_FOUND)

        serializer = FeedbackSerializer(feedback, many=True)
        return Response(serializer.data)