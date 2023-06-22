from django.contrib import admin
from django.urls import path, include
from ems_api.Views.AnotherTableEmployeeView import AnotherEmployeeDetail, AnotherEmployeeList
from ems_api.Views.EmployeeViews import EmployeeImportView, EmployeeDetail, EmployeeList, EmployeeProjectUpdate
from ems_api.Views.HelloWorldViews import hello_world
# from ems_api.Views.EmployeeSkillViews import EmployeeSkillView, EmployeeSkillView_id


# from ems_api.Views.TrainingViews import TrainingView, TrainingView_id


# from ems_api.Views.TrainerViews import TrainerView, TrainerView_id

from ems_api.Views.ManagerViews import ManagerView,ManagerView_id,ManagerViewByUserId
from ems_api.Views.FeedbackView import FeedbackList,FeedbackDetail,FeedbackDetailView
from ems_api.Views.TrainingView import TrainingList,TrainingDetail,TrainingDetailView
from ems_api.Views.POC  import POCDetail,POCDetailView, POCList
from ems_api.Views.Skill import SkillDetailView,SkillDetail, SkillList
from ems_api.Views.ProfileView import ProfileDetailView, ProfileList, ProfileDetail,ProfileDetailView
from ems_api.Views.Project import ProjectList, ProjecDetail,   ProjectDetailView
from ems_api.views import ImportEmployeesAPIView




urlpatterns = [
    path('hello/', hello_world),
    # path('empskills/', EmployeeSkillView),
    # path('empskills/<id>', EmployeeSkillView_id),
    


    path('trainings/',TrainingList.as_view(), name='trainings'), #for add one and get all
    path('trainings/<int:pk>/',TrainingDetail.as_view(), name='trainings'),#getbyid , update , delete
    path('emptrainings/<str:employee_id>/',TrainingDetailView.as_view(), name='emptrainings'), #get by employee id


    path('skils/',SkillList.as_view(), name='skils'),
    path('skils/<int:pk>/',SkillDetail.as_view(), name='skils'), #getbyid , update , delete
    path('empskills/<str:employee_id>/',SkillDetailView.as_view(), name='skills'), #get by employee id

    path('pocs/',POCList.as_view(), name='Pocs'),
    path('pocs/<int:pk>/',POCDetail.as_view(), name='Pocs'),#getbyid , update , delete over primary key id
    path('emppocs/<str:employee_id>/',POCDetailView.as_view(), name='Pocs'),

    
    path('projects/',ProjectList.as_view(), name='projects'),  #for add one and get all
    path('empprojects/<str:employee_id>/', ProjectDetailView.as_view()),  # get by employee id
    path('empproject/<int:pk>/', ProjecDetail.as_view()),  #getbyid , update , delete over primary key  id


    path('employees/',EmployeeList.as_view(), name='employees'), #for add one and get all
    path('employee/<str:pk>/', EmployeeDetail.as_view(), name='employee'), #get by employee id
    

    path('profiles/', ProfileList.as_view()), #for add one and get all
    path('profiles/<int:pk>/', ProfileDetail.as_view()), #getbyid , update , delete over primary key  id
    path('empprofiles/<str:employee_id>/', ProfileDetailView.as_view()), #get by employee id


    path('feedback/', FeedbackList.as_view()), #for add one and get all
    path('feedback/<int:pk>/', FeedbackDetail.as_view()),   #getbyid , update , delete over primary key  id
    path('empfeedbacks/<str:employee_id>/', FeedbackDetailView.as_view()),

    # path('training/<id>',TrainingView_id),

    
    # path('trainer/',TrainerView),
    # path('trainer/<id>',TrainerView_id),
    path('rmemployees/', AnotherEmployeeList.as_view(), name='rmemployee-list'),
    path('rmemployees/<int:pk>/', AnotherEmployeeDetail.as_view(), name='rmemployee-detail'),

    
    path('manager/<id>/',ManagerView_id),  
    path('managers/',ManagerView),
    path('manager/user/<int:user_id>/', ManagerViewByUserId),
    # path('import-data/', FresherImportView.as_view(), name='Fresher_Data_Import'),
    path('import-employees/', ImportEmployeesAPIView.as_view(), name='import-employees'),
    path('import-employees-project/', EmployeeProjectUpdate.as_view(), name='import-employees-project')
    
    
]
