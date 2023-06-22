# Register your models here.
from ems_api.Models.Role import Role
from ems_api.Models.Skill import Skill
from ems_api.Models.POC import POC
from ems_api.Models.Feedback import Feedback
from ems_api.Models.Trainer import Trainer
from ems_api.Models.TrainerFeedback import TrainerFeedback
from ems_api.Models.Training import Training
from ems_api.Models.Manager import Manager
from ems_api.Models.Profile import Profile
from ems_api.Models.Project import Project
from django.contrib import admin
from ems_api.Models.Employee import Employee

admin.site.register(Employee)



admin.site.register(Feedback)

admin.site.register(Skill)
admin.site.register(Manager)

admin.site.register(POC)
admin.site.register(Role)
admin.site.register(Trainer)
admin.site.register(TrainerFeedback)
admin.site.register(Training)
admin.site.register(Profile)
admin.site.register(Project)