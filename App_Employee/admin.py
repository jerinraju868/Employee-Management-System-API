from django.contrib import admin
from  App_Employee.models import LeaveApplicationModel

# Adding the LeaveApplicationModel to the admin page
admin.site.register(LeaveApplicationModel)