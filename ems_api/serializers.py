from rest_framework import serializers
from ems_api.Models.Employee import Employee



from ems_api.Models.Feedback import Feedback

from ems_api.Models.Skill import Skill
from ems_api.Models.Manager import Manager

from ems_api.Models.POC import POC
from ems_api.Models.Role import Role
from ems_api.Models.Trainer import Trainer
from ems_api.Models.TrainerFeedback import TrainerFeedback
from ems_api.Models.Training import Training

from ems_api.Models.Project import Project
from ems_api.Models.Profile import Profile





class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'



# ['Name', 'Local Grade','Role Name','People Manager','Project Code','Start Date','End Date','Booking Type','Joining Date','Final Client Name','City','Segment Employee CT','EL Mapping','Type','Skill Group','Final Grade','EGO']
# class FresherSerializer(serializers.ModelSerializer):
#     local_employee_id = serializers.IntegerField(source='Local Employee ID', required=True)
#     global_group_id = serializers.IntegerField(source='Global Group ID', required=False)
#     name = serializers.CharField(source='Name', required=True)
#     local_grade = serializers.CharField(source='Local Grade', required=False)
#     role_name = serializers.CharField(source='Role Name', required=False)
#     people_manager = serializers.CharField(source='People Manager', required=False)
#     project_code = serializers.CharField(source='Project Code', required=False)
#     start_date = serializers.DateField(source='Start Date', required=False)
#     end_date = serializers.DateField(source='End Date', required=False)
#     booking_type = serializers.CharField(source='Booking Type', required=False)
#     joining_date = serializers.DateField(source='Joining Date', required=False)
#     final_client_name = serializers.CharField(source='Final Client Name', required=False)
#     city = serializers.CharField(source='City', required=False)
#     segment_employee_ct = serializers.CharField(source='Segment Employee CT', required=False)
#     el_mapping = serializers.CharField(source='EL Mapping', required=False)
#     type = serializers.CharField(source='Type', required=False)
#     skill_group = serializers.CharField(source='Skill Group', required=False)
#     finalgrade = serializers.CharField(source='Final Grade', required=False)
#     ego = serializers.CharField(source='EGO', required=False)

#     class Meta:
#         model = Fresher
#         fields = ['local_employee_id', 'global_group_id', 'name', 'local_grade', 'role_name', 'people_manager',
#                   'project_code', 'start_date', 'end_date', 'booking_type', 'joining_date', 'final_client_name',
#                   'city', 'segment_employee_ct', 'el_mapping', 'type', 'skill_group', 'finalgrade', 'ego']






class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = "__all__"



class POCSerializer(serializers.ModelSerializer):
    class Meta:
        model = POC
        fields = "__all__"


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = "__all__"


class TrainerFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainerFeedback
        fields = "__all__"



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):


    class Meta:
        model = Project
        fields = ('id', 'name', 'start_date', 'end_date', 'employee', 'manager_name')

class POCSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = POC
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Skill
        fields = '__all__'

class TrainingSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Training
        fields = '__all__'

    



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','employee', 'phone_number', 'location', 'designation', 'image')














    
