# # from django.http import Http404
# # from rest_framework.views import APIView
# # from rest_framework.response import Response
# # from rest_framework import status
# # from ems_api.Models.Employee import Employee
# # from ems_api.Models.Project import Project
# # from ems_api.Models.POC import POC
# # from ems_api.Models.Skill import Skill
# # from ems_api.Models.Training import Training
# # from ems_api.Models.Profile import Profile
# # from ems_api.Models.Feedback import Feedback
# # from .serializers import EmployeeSerializer, ProjectSerializer, FeedbackSerializer,  POCSerializer, TrainingSerializer, SkillSerializer, ProfileSerializer

# # class EmployeeList(APIView):
# #     def get(self, request):
# #         employees = Employee.objects.all()
# #         serializer = EmployeeSerializer(employees, many=True)
# #         return Response(serializer.data)

# #     # def post(self, request):
# #     #     serializer = EmployeeSerializer(data=request.data)
# #     #     if serializer.is_valid():
# #     #         serializer.save()
# #     #         return Response(serializer.data, status=status.HTTP_201_CREATED)
# #     #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# # class EmployeeDetail(APIView):
# #     def get(self, request, pk):
# #         employee = Employee.objects.get(pk=pk)
# #         serializer = EmployeeSerializer(employee)
# #         return Response(serializer.data)
    
# #     def put(self, request, pk):
# #         employee = Employee.objects.get(pk=pk)
# #         serializer = EmployeeSerializer(employee, data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #     def delete(self, request, pk):
# #         employee = Employee.objects.get(pk=pk)
# #         employee.delete()
# #         return Response(status=status.HTTP_204_NO_CONTENT)

# # # class ProjectList(APIView):
# # #     def get(self, request):
# # #         projects = Project.objects.all()
# # #         serializer = ProjectSerializer(projects, many=True)
# # #         return Response(serializer.data)

# # #     def post(self, request):
# # #         serializer = ProjectSerializer(data=request.data)
# # #         if serializer.is_valid():
# # #             serializer.save()
# # #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# # #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# # # class ProjecDetail(APIView):
# # #     def get(self, request, pk):
# # #         project = Project.objects.get(pk=pk)
# # #         serializer = ProjectSerializer(project)
# # #         return Response(serializer.data)
    
# # #     def put(self, request, pk):
# # #         project = Project.objects.get(pk=pk)
# # #         serializer = ProjectSerializer(project, data=request.data)
# # #         if serializer.is_valid():
# # #             serializer.save()
# # #             return Response(serializer.data)
# # #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # #     def delete(self, request, pk):
# # #         project = Project.objects.get(pk=pk)
# # #         project.delete()
# # #         return Response(status=status.HTTP_204_NO_CONTENT)
    
# # # class ProjectDetailView(APIView):
# # #     def get(self, request, employee_id):
# # #         try:
# # #             profile = Project.objects.filter(employee_id=employee_id)
# # #         except Project.DoesNotExist:
# # #             return Response({'message': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)

# # #         serializer = ProjectSerializer(profile, many=True)
# # #         return Response(serializer.data)

# # # class TrainingList(APIView):
# # #     def get(self, request):
# # #         projects = Training.objects.all()
# # #         serializer = TrainingSerializer(projects, many=True)
# # #         return Response(serializer.data)

# # #     def post(self, request):
# # #         serializer = TrainingSerializer(data=request.data)
# # #         if serializer.is_valid():
# # #             serializer.save()
# # #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# # #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # # class TrainingDetail(APIView):
# # #     def get(self, request, pk):
# # #         training = Training.objects.get(pk=pk)
# # #         serializer = TrainingSerializer(training)
# # #         return Response(serializer.data)
    
# # #     def put(self, request, pk):
# # #         training = Training.objects.get(pk=pk)
# # #         serializer = TrainingSerializer(training, data=request.data)
# # #         if serializer.is_valid():
# # #             serializer.save()
# # #             return Response(serializer.data)
# # #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # #     def delete(self, request, pk):
# # #         training = Training.objects.get(pk=pk)
# # #         training.delete()
# # #         return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# # # class TrainingDetailView(APIView):
# # #     def get(self, request, employee_id):
# # #         try:
# # #             training = Training.objects.filter(employee_id=employee_id)
# # #         except Training.DoesNotExist:
# # #             return Response({'message': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)

# # #         serializer = TrainingSerializer(training, many=True)
# # #         return Response(serializer.data)

# # ########## **********  POC *************************  ##################
# # # class POCList(APIView):
# # #     def get(self, request):
# # #         projects = POC.objects.all()
# # #         serializer = POCSerializer(projects, many=True)
# # #         return Response(serializer.data)

# # #     def post(self, request):
# # #         serializer = POCSerializer(data=request.data)
# # #         if serializer.is_valid():
# # #             serializer.save()
# # #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# # #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# # # class POCDetail(APIView):
# # #     def get(self, request, pk):
# # #         poc = POC.objects.get(pk=pk)
# # #         serializer = POCSerializer(poc)
# # #         return Response(serializer.data)
    
# # #     def put(self, request, pk):
# # #         poc = POC.objects.get(pk=pk)
# # #         serializer = POCSerializer(poc, data=request.data)
# # #         if serializer.is_valid():
# # #             serializer.save()
# # #             return Response(serializer.data)
# # #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # #     def delete(self, request, pk):
# # #         poc = POC.objects.get(pk=pk)
# # #         poc.delete()
# # #         return Response(status=status.HTTP_204_NO_CONTENT)


# # # class POCDetailView(APIView):
# # #     def get(self, request, employee_id):
# # #         try:
# # #             poc= POC.objects.filter(employee_id=employee_id)
# # #         except POC.DoesNotExist:
# # #             return Response({'message': 'POC  not found'}, status=status.HTTP_404_NOT_FOUND)

# # #         serializer = POCSerializer(poc, many=True)
# # #         return Response(serializer.data)


    
# # # class SkillList(APIView):
# # #     def get(self, request):
# # #         projects = Skill.objects.all()
# # #         serializer = SkillSerializer(projects, many=True)
# # #         return Response(serializer.data)

# # #     def post(self, request):
# # #         serializer = SkillSerializer(data=request.data)
# # #         if serializer.is_valid():
# # #             serializer.save()
# # #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# # #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# # # class SkillDetail(APIView):
# # #     def get(self, request, pk):
# # #         skill = Skill.objects.get(pk=pk)
# # #         serializer = SkillSerializer(skill)
# # #         return Response(serializer.data)
    
# # #     def put(self, request, pk):
# # #         skill = Skill.objects.get(pk=pk)
# # #         serializer = SkillSerializer(skill, data=request.data)
# # #         if serializer.is_valid():
# # #             serializer.save()
# # #             return Response(serializer.data)
# # #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # #     def delete(self, request, pk):
# # #         skill = Skill.objects.get(pk=pk)
# # #         skill.delete()
# # #         return Response(status=status.HTTP_204_NO_CONTENT)

# # # class SkillDetailView(APIView):
# # #     def get(self, request, employee_id):
# # #         try:
# # #             skill= Skill.objects.filter(emp_id=employee_id)
# # #         except Skill.DoesNotExist:
# # #             return Response({'message': 'skill  not found'}, status=status.HTTP_404_NOT_FOUND)

# # #         serializer = SkillSerializer(skill, many=True)
# # #         return Response(serializer.data)


# # # class ProfileList(APIView):
# # #     """
# # #     List all profiles or create a new profile.
# # #     """
# # #     def get(self, request, format=None):
# # #         profiles = Profile.objects.all()
# # #         serializer = ProfileSerializer(profiles, many=True)
# # #         return Response(serializer.data)

# # #     def post(self, request, format=None):
# # #         serializer = ProfileSerializer(data=request.data)
# # #         if serializer.is_valid():
# # #             serializer.save()
# # #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# # #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# # # class ProfileDetail(APIView):
# # #     """
# # #     Retrieve, update or delete a profile instance.
# # #     """
# # #     def get_object(self, pk):
# # #         try:
# # #             return Profile.objects.get(pk=pk)
# # #         except Profile.DoesNotExist:
# # #             raise Http404

# # #     def get(self, request, pk, format=None):
# # #         profile = self.get_object(pk)
# # #         serializer = ProfileSerializer(profile)
# # #         return Response(serializer.data)

# # #     def put(self, request, pk, format=None):
# # #         profile = self.get_object(pk)
# # #         serializer = ProfileSerializer(profile, data=request.data)
# # #         if serializer.is_valid():
# # #             serializer.save()
# # #             return Response(serializer.data)
# # #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # #     def delete(self, request, pk, format=None):
# # #         profile = self.get_object(pk)
# # #         profile.delete()
# # #         return Response(status=status.HTTP_204_NO_CONTENT)
    

# # # class ProfileDetailView(APIView):
# # #     def get(self, request, employee_id):
# # #         try:
# # #             profile = Profile.objects.get(employee_id=employee_id)
# # #         except Profile.DoesNotExist:
# # #             return Response({'message': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)

# # #         serializer = ProfileSerializer(profile)
# # #         return Response(serializer.data)
    


    



# # # class FeedbackList(APIView):
# # #     def get(self, request):
# # #         feedback = Feedback.objects.all()
# # #         serializer = FeedbackSerializer(feedback, many=True)
# # #         return Response(serializer.data)

# # #     def post(self, request):
# # #         serializer = FeedbackSerializer(data=request.data)
# # #         if serializer.is_valid():
# # #             serializer.save()
# # #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# # #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # # class FeedbackDetail(APIView):
# # #     def get_object(self, pk):
# # #         try:
# # #             return Feedback.objects.get(pk=pk)
# # #         except Feedback.DoesNotExist:
# # #             raise Http404

# # #     def get(self, request, pk, format=None):
# # #         feedback = self.get_object(pk)
# # #         serializer = FeedbackSerializer(feedback)
# # #         return Response(serializer.data)

# # #     def put(self, request, pk, format=None):
# # #         feedback = self.get_object(pk)
# # #         serializer = FeedbackSerializer(feedback, data=request.data)
# # #         if serializer.is_valid():
# # #             serializer.save()
# # #             return Response(serializer.data)
# # #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # #     def delete(self, request, pk, format=None):
# # #         feedback = self.get_object(pk)
# # #         feedback.delete()
# # #         return Response(status=status.HTTP_204_NO_CONTENT)
    
# # # class FeedbackDetailView(APIView):
# # #     def get(self, request, employee_id):
# # #         try:
# # #             feedback= Feedback.objects.filter(fresher_id=employee_id)
# # #         except Feedback.DoesNotExist:
# # #             return Response({'message': 'Still no feedback get '}, status=status.HTTP_404_NOT_FOUND)

# # #         serializer = FeedbackSerializer(feedback, many=True)
# # #         return Response(serializer.data)



# import pandas as pd
# from rest_framework.views import APIView
# from rest_framework.response import Response

# from ems_api.Models.Employee import Employee
# # class ImportEmployeesAPIView(APIView):
# #     def post(self, request, format=None):
# #         excel_file = request.FILES['file']
# #         df = pd.read_excel(excel_file)

# #         for _, row in df.iterrows():
# #             employee = Employee(
# #                 local_employee_id=row['Local Employee ID'],
# #                 global_group_id=row['Global Group ID'],
# #                 name=row['Name'],
# #                 local_grade=row['Local Grade'],
# #                 role_name=row['Role Name'],
# #                 production_unit=row['Production Unit'],
# #                 production_unit_name=row['Production Unit Name'],
# #                 local_approver=row['Local Approver'],
# #                 people_manager=row['People Manager'],
# #                 project_code=row['Project Code'],
# #                 project_name=row['Project Name'],
# #                 client_group_name=row['Client Group Name'],
# #                 start_date=row['Start Date'],
# #                 end_date=row['End Date'],
# #                 # loading=row['Loading'],
# #                 # leavers_last_working_day=row["Leaver's Last Working Day"],
# #                 type_of_project=row['Type Of Project'],
# #                 # category=row['Category'],
# #                 base_location=row['Base Location'],
# #                 production_unit_rm_name=row['Production Unit RM Name'],
# #                 resource_practice_area=row['Resource Practice Area'],
# #                 booking_type=row['Booking Type'],
# #                 joining_date_dhr=row['Joining Date(DHR)'],
# #                 final_client_name=row['Final Client Name'],
# #                 city=row['City'],
# #                 # mm=row['MM'],
# #                 engineering_unit=row['Engineering Unit'],
# #                 cluster=row['Cluster'],
# #                 el_mapping=row['EL Mapping'],
# #                 billability=row['Billability'],
# #                 employee_type=row['Type'],
# #                 skill_group=row['Skill Group'],
# #                 # source=row['Source'],
# #                 mapped_grade=row['Mapped Grade'],
# #                 final_grade=row['Final Grade'],
# #                 # category=row['Category'],
# #                 vertical_segment=row['Vertical Segment'],
# #                 # target_billing_date=row['Target Billing Date/From Date'],
# #                 # target_customer=row['Target Customer'],
# #                 # new_requirement_backfill=row['New Requirement/Backfill'],
# #                 # manual_allocation_category=row['Manual Allocation Category'],
# #                 # edm_mapping=row['EDM Mapping'],
# #                 # bu_manual_change=row['BU Manual Change'],
# #                 resignation_status=row['Resignation Status'],
# #                 ego=row['EGO'],
# #                 # account_holder1=row['Account Holder1'],
# #                 # new_entries_spe=row['New Enteries - SPE'],
# #                 udaan_batch=row['Udaan Batch'],
# #                 udaan_status=row['Udaan status'],
# #                 non_deployable=row['Non Deployable'],
# #                 email_id=row['Email']
               
# #             )
# #             employee.save()

# #         return Response({'message': 'Employees imported successfully.'})


# class ImportEmployeesAPIView(APIView):
#     def post(self, request, format=None):
#         excel_file = request.FILES['file']
#         df = pd.read_excel(excel_file)

#         for _, row in df.iterrows():
#             employee_id = row['Local Employee ID']
#             try:
#                 employee = Employee.objects.get(local_employee_id=employee_id)
#                 # Update the employee fields with new data
#                 employee.global_group_id = row['Global Group ID']
#                 employee.name = row['Name']
#                 employee.local_grade = row['Local Grade']
#                 employee.role_name = row['Role Name']
#                 employee.production_unit = row['Production Unit']
#                 employee.production_unit_name = row['Production Unit Name']
#                 employee.local_approver = row['Local Approver']
#                 employee.people_manager = row['People Manager']
#                 employee.project_code = row['Project Code']
#                 employee.project_name = row['Project Name']
#                 employee.client_group_name = row['Client Group Name']
#                 employee.start_date = row['Start Date']
#                 employee.end_date = row['End Date']
#                 employee.type_of_project = row['Type Of Project']
#                 employee.base_location = row['Base Location']
#                 employee.production_unit_rm_name = row['Production Unit RM Name']
#                 employee.resource_practice_area = row['Resource Practice Area']
#                 employee.booking_type = row['Booking Type']
#                 employee.joining_date_dhr = row['Joining Date(DHR)']
#                 employee.final_client_name = row['Final Client Name']
#                 employee.city = row['City']
#                 employee.engineering_unit = row['Engineering Unit']
#                 employee.cluster = row['Cluster']
#                 employee.el_mapping = row['EL Mapping']
#                 employee.billability = row['Billability']
#                 employee.employee_type = row['Type']
#                 employee.skill_group = row['Skill Group']
#                 employee.mapped_grade = row['Mapped Grade']
#                 employee.final_grade = row['Final Grade']
#                 employee.vertical_segment = row['Vertical Segment']
#                 employee.resignation_status = row['Resignation Status']
#                 employee.ego = row['EGO']
#                 employee.udaan_batch = row['Udaan Batch']
#                 employee.udaan_status = row['Udaan status']
#                 employee.non_deployable = row['Non Deployable']
#                 employee.email_id = row['Email']
#                 # Update other fields as needed
#                 employee.save()
#             except Employee.DoesNotExist:
#                 # Create a new employee if not found
#                 employee = Employee(
#                     local_employee_id=row['Local Employee ID'],
#                     global_group_id=row['Global Group ID'],
#                     name=row['Name'],
#                     local_grade=row['Local Grade'],
#                     role_name=row['Role Name'],
#                     production_unit=row['Production Unit'],
#                     production_unit_name=row['Production Unit Name'],
#                     local_approver=row['Local Approver'],
#                     people_manager=row['People Manager'],
#                     project_code=row['Project Code'],
#                     project_name=row['Project Name'],
#                     client_group_name=row['Client Group Name'],
#                     start_date=row['Start Date'],
#                     end_date=row['End Date'],
#                     type_of_project=row['Type Of Project'],
#                     base_location=row['Base Location'],
#                     production_unit_rm_name=row['Production Unit RM Name'],
#                     resource_practice_area=row['Resource Practice Area'],
#                     booking_type=row['Booking Type'],
#                     joining_date_dhr=row['Joining Date(DHR)'],
#                     final_client_name=row['Final Client Name'],
#                     city=row['City'],
#                     engineering_unit=row['Engineering Unit'],
#                     cluster=row['Cluster'],
#                     el_mapping=row['EL Mapping'],
#                     billability=row['Billability'],
#                     employee_type=row['Type'],
#                     skill_group=row['Skill Group'],
#                     mapped_grade=row['Mapped Grade'],
#                     final_grade=row['Final Grade'],
#                     vertical_segment=row['Vertical Segment'],
#                     resignation_status=row['Resignation Status'],
#                     ego=row['EGO'],
#                     udaan_batch=row['Udaan Batch'],
#                     udaan_status=row['Udaan status'],
#                     non_deployable=row['Non Deployable'],
#                     email_id=row['Email']
#                     # Set other fields accordingly
#                 )
#                 employee.save()

#         return Response({'message': 'Employees imported and updated successfully.'})


from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd
from ems_api.Models.Employee import Employee
from ems_api.Models.AnotherTableEmployee import  AnotherTableEmployee

class ImportEmployeesAPIView(APIView):
    def post(self, request, format=None):
        excel_file = request.FILES['file']
        df = pd.read_excel(excel_file)

        existing_employees = set(Employee.objects.values_list('local_employee_id', flat=True))
        excel_employees = set(df['Local Employee ID'])

        # Update or create employees from the Excel file
        for _, row in df.iterrows():
            employee_id = row['Local Employee ID']
            if employee_id in existing_employees:
                try:
                    employee = Employee.objects.get(local_employee_id=employee_id)
                    # Update the employee fields with new data
                    employee.global_group_id = row['Global Group ID']
                    employee.name = row['Name']
                    employee.local_grade = row['Local Grade']
                    employee.role_name = row['Role Name']
                    employee.production_unit = row['Production Unit']
                    employee.production_unit_name = row['Production Unit Name']
                    employee.local_approver = row['Local Approver']
                    employee.people_manager = row['People Manager']
                    employee.project_code = row['Project Code']
                    employee.project_name = row['Project Name']
                    employee.client_group_name = row['Client Group Name']
                    employee.start_date = row['Start Date']
                    employee.end_date = row['End Date']
                    employee.type_of_project = row['Type Of Project']
                    employee.base_location = row['Base Location']
                    employee.production_unit_rm_name = row['Production Unit RM Name']
                    employee.resource_practice_area = row['Resource Practice Area']
                    employee.booking_type = row['Booking Type']
                    employee.joining_date_dhr = row['Joining Date(DHR)']
                    employee.final_client_name = row['Final Client Name']
                    employee.city = row['City']
                    employee.engineering_unit = row['Engineering Unit']
                    employee.cluster = row['Cluster']
                    employee.el_mapping = row['EL Mapping']
                    employee.billability = row['Billability']
                    employee.employee_type = row['Type']
                    employee.skill_group = row['Skill Group']
                    employee.mapped_grade = row['Mapped Grade']
                    employee.final_grade = row['Final Grade']
                    employee.vertical_segment = row['Vertical Segment']
                    employee.resignation_status = row['Resignation Status']
                    employee.ego = row['EGO']
                    employee.udaan_batch = row['Udaan Batch']
                    employee.udaan_status = row['Udaan status']
                    employee.non_deployable = row['Non Deployable']
                    employee.email_id = row['Email']
                    # Update other fields as needed
                    employee.save()
                except Employee.DoesNotExist:
                    pass  # Employee already exists, skip creating
            else:
                # Create a new employee
                employee = Employee(
                    local_employee_id=row['Local Employee ID'],
                    global_group_id=row['Global Group ID'],
                    name=row['Name'],
                    local_grade=row['Local Grade'],
                    role_name=row['Role Name'],
                    production_unit=row['Production Unit'],
                    production_unit_name=row['Production Unit Name'],
                    local_approver=row['Local Approver'],
                    people_manager=row['People Manager'],
                    project_code=row['Project Code'],
                    project_name=row['Project Name'],
                    client_group_name=row['Client Group Name'],
                    start_date=row['Start Date'],
                    end_date=row['End Date'],
                    type_of_project=row['Type Of Project'],
                    base_location=row['Base Location'],
                    production_unit_rm_name=row['Production Unit RM Name'],
                    resource_practice_area=row['Resource Practice Area'],
                    booking_type=row['Booking Type'],
                    joining_date_dhr=row['Joining Date(DHR)'],
                    final_client_name=row['Final Client Name'],
                    city=row['City'],
                    engineering_unit=row['Engineering Unit'],
                    cluster=row['Cluster'],
                    el_mapping=row['EL Mapping'],
                    billability=row['Billability'],
                    employee_type=row['Type'],
                    skill_group=row['Skill Group'],
                    mapped_grade=row['Mapped Grade'],
                    final_grade=row['Final Grade'],
                    vertical_segment=row['Vertical Segment'],
                    resignation_status=row['Resignation Status'],
                    ego=row['EGO'],
                    udaan_batch=row['Udaan Batch'],
                    udaan_status=row['Udaan status'],
                    non_deployable=row['Non Deployable'],
                    email_id=row['Email']
                    # Set other fields accordingly
                )
                employee.save()

        # Move employees not present in the Excel file to AnotherTableEmployee
        missing_employees = Employee.objects.exclude(local_employee_id__in=excel_employees)
        for missing_employee in missing_employees:
            new_another_employee = AnotherTableEmployee(
                local_employee_id=missing_employee.local_employee_id,
                global_group_id=missing_employee.global_group_id,
                name=missing_employee.name,
                local_grade=missing_employee.local_grade,
                role_name=missing_employee.role_name,
                production_unit=missing_employee.production_unit,
                production_unit_name=missing_employee.production_unit_name,
                local_approver=missing_employee.local_approver,
                people_manager=missing_employee.people_manager,
                project_code=missing_employee.project_code,
                project_name=missing_employee.project_name,
                client_group_name=missing_employee.client_group_name,
                start_date=missing_employee.start_date,
                end_date=missing_employee.end_date,
                type_of_project=missing_employee.type_of_project,
                base_location=missing_employee.base_location,
                production_unit_rm_name=missing_employee.production_unit_rm_name,
                resource_practice_area=missing_employee.resource_practice_area,
                booking_type=missing_employee.booking_type,
                joining_date_dhr=missing_employee.joining_date_dhr,
                final_client_name=missing_employee.final_client_name,
                city=missing_employee.city,
                engineering_unit=missing_employee.engineering_unit,
                cluster=missing_employee.cluster,
                el_mapping=missing_employee.el_mapping,
                billability=missing_employee.billability,
                employee_type=missing_employee.employee_type,
                skill_group=missing_employee.skill_group,
                mapped_grade=missing_employee.mapped_grade,
                final_grade=missing_employee.final_grade,
                vertical_segment=missing_employee.vertical_segment,
                resignation_status=missing_employee.resignation_status,
                ego=missing_employee.ego,
                udaan_batch=missing_employee.udaan_batch,
                udaan_status=missing_employee.udaan_status,
                non_deployable=missing_employee.non_deployable,
                email_id=missing_employee.email_id
                # Set other fields accordingly
            )
            new_another_employee.save()
            missing_employee.delete()

        return Response({'message': 'Employees imported and updated successfully.'})