

import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.test import Client
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import numpy as np
from ems_api.Models.AnotherTableEmployee import AnotherTableEmployee
from ems_api.serializers import EmployeeSerializer
from dateutil.parser import parse
from datetime import datetime

class AnotherEmployeeDetail(APIView):
    def get(self, request, pk):
        employee = AnotherTableEmployee.objects.get(pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    
    def put(self, request, pk):
        employee = AnotherTableEmployee.objects.get(pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = AnotherTableEmployee.objects.get(pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class AnotherEmployeeList(APIView):
    def get(self, request):
        employees = AnotherTableEmployee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    