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
from ems_api.Models.Employee import Employee
from ems_api.serializers import EmployeeSerializer
from dateutil.parser import parse
from datetime import datetime

class EmployeeImportView(APIView):

    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({'error': 'No file was provided.'}, status=status.HTTP_400_BAD_REQUEST)

        data = pd.read_excel(file)
        # required_columns = ['Local Employee ID', 'Global Group ID', 'Name of the Employee','Email_Id', 'Local Grade','People Manager', 'Joining Date(DHR)', 'City', 'Primary Skill Group', 'Upgraded Skill','LML', 'Training SPOC', 'Training account', 'Training Skill', 'Start Date','Training End date', 'Before Traning Rating[1-least, 5-Best]','Rating till date(1: least to 5 :5 best)', 'Remarks', 'Confidence of Placement','Status', 'Account (Shadow/allocation)', 'BU', 'EGO', 'Udaan']

        # missing_columns = set(required_columns) - set(data.columns)
        # if missing_columns:
        #     return Response({'error': f'The following columns are missing: {", ".join(missing_columns)}.'},
        #                     status=status.HTTP_400_BAD_REQUEST)

        for index, row in data.iterrows():
            employee_id = row['Local Employee ID']
            employee = Employee.objects.filter(local_employee_id=employee_id).first()
            if not employee:
                employee = Employee(local_employee_id=employee_id)
           
            employee.joining_date = row.get('Joining Date(DHR)',None)

            employee.global_group_id = row.get('Global Group ID')
            employee.name = row.get('Name')
            
            ema = row.get('Email ID',None)
            print(ema)
            # if ema == "#N/A" or type(ema) != str:  # Checking if 'sts' is not None and not equal to a single space
            #     employee.Email_Id = "NO Email Provided"
            # else:
            #     employee.Email_Id = row.get('Email ID')

            employee.local_grade = row.get('Local Grade')
            employee.people_manager = row.get('People Manager')
            employee.city = row.get('City')
            employee.primary_skill_group = row.get('Primary Skill Group')
            employee.upgraded_skill = row.get('Upgraded Skill', None)
            employee.lml = row.get('LML', None)
            employee.training_spoc = row.get('Training SPOC', None)
            employee.training_account = row.get('Training account', None)
            employee.training_skill = row.get('Training Skill', None)
            employee.final_skillset = row.get('Final Skillset', None)
            employee.overall_status = row.get('Overall Status', None)

            
            employee.start_date = row.get('Start Date',None)

            
            employee.training_end_date = row.get('Training End date',None)

            # Check if the value is not NaN and is a number before assigning it
            before_training_rating = row.get('Before Traning Rating[1-least, 5-Best]', None)
            if pd.notna(before_training_rating) and not pd.isna(before_training_rating):
                employee.before_training_rating = before_training_rating

            # Check if the value is not NaN and is a number before assigning it
            rating_till_date = row.get('Rating till date(1: least to 5 :5 best)', None)
            if pd.notna(rating_till_date) and not np.isnan(rating_till_date):
                employee.rating_till_date = rating_till_date

            employee.remarks = row.get('Remarks', None)
            employee.confidence_of_placement = row.get('Confidence of Placement', None)
            sts = row.get('Status', None)
            if sts == "nan" or type(sts) != str:  # Checking if 'sts' is not None and not equal to a single space
                employee.status = "Self Learning"
            else:
                employee.status = sts

            employee.account = row.get('Account (Shadow/allocation)', None)
            
            employee.bu = row.get('BU', None)
            employee.ego = row.get('EGO', None)
            employee.udaan = row.get('Udaan', None)
            
            if employee.email_id != "NO Email Provided":
                # Creating credentials for the user
                registration_url = '/api/users/register/'  # Use the relative URL
                upass = str(employee_id) + "@abc"
                registration_data = {
                    'emp_id': employee_id,
                    'email': employee.email_id,
                    'name': employee.name,
                    "role_id": 3,
                    "password": upass,
                    "password2": upass,
                    # Include other required fields for registration
                }
                client = Client()
                response = client.post(registration_url, registration_data)
                print(response.content)    
                # if response.status_code == 201:
                #     print("Entered if")
                #     try:
                #         # Send email
                #         email_subject = 'Welcome to EMCap!'
                #         email_message = f'Hello {employee.name},\n\nWelcome to our app! Your credentials are:\nUsername: {employee.Email_Id}\nPassword: {upass}\n\nPlease login using these credentials.\n\nBest regards,\nYour App Team'
                #         sender_email = 'chiragawasthi9@gmail.com'
                #         receiver_email = employee.Email_Id
                #         print("set the fields")
                #         # Create a multipart message
                #         message = MIMEMultipart()
                #         message['Subject'] = email_subject
                #         message['From'] = sender_email
                #         message['To'] = receiver_email
                #         print("multipart message created ")
                #         # Attach the message body
                #         message.attach(MIMEText(email_message, 'plain'))

                #         # SMTP server configuration
                #         smtp_host = 'smtp.gmail.com'
                #         smtp_port = 587
                #         smtp_username = 'chiragawasthi9@gmail.com'
                #         smtp_password = 'xrfwvyprwaicancv'
                #         print("smtp configured and now sending the server request ")
                #         # Create an SMTP connection
                #         with smtplib.SMTP(smtp_host, smtp_port) as server:
                #             server.starttls()
                #             server.login(smtp_username, smtp_password)
                #             server.sendmail(sender_email, receiver_email, message.as_string())

                #         print("Email sent successfully!")
                #     except Exception as e:
                #         print("An error occurred while sending the email:", str(e))
                # else:
                #     print(f"Registration failed for employee ID: {employee_id}")

                employee.save()
                print("Employee saved")
        return Response({'success': 'Data imported successfully.'}, status=status.HTTP_201_CREATED)
    
class EmployeeProjectUpdate(APIView):
    def put(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({'error': 'No file was provided.'}, status=status.HTTP_400_BAD_REQUEST)

        data = pd.read_excel(file)
        missing_columns = ['Local Employee ID', 'Project']

        if any(column not in data.columns for column in missing_columns):
            return Response({'error': 'The required columns are missing in the file.'},
                            status=status.HTTP_400_BAD_REQUEST)

        data = data.dropna(subset=['Project'])  # Remove rows with empty project values

        for index, row in data.iterrows():
            local_employee_id = row['Local Employee ID']
            project = row['Project']

            employee = Employee.objects.filter(local_employee_id=local_employee_id).first()
            if employee and project:
                employee.project_name = project
                employee.save()

        return Response({'success': 'Project data updated successfully.'}, status=status.HTTP_200_OK)


class EmployeeList(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)


class EmployeeDetail(APIView):
    def get(self, request, pk):
        employee = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    
    def put(self, request, pk):
        employee = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = Employee.objects.get(pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)