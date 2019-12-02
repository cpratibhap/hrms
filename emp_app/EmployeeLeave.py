from django.db import models
from leave_app.models import *
from .Employee import Employee


class EmployeeLeave(models.Model):
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False)
    leave_request_info = models.ForeignKey(LeaveRequest, on_delete=models.CASCADE)
    leave_balance_info = models.ForeignKey(LeaveBalance, on_delete=models.CASCADE)
    leave_type_info = models.ForeignKey(LeaveType, on_delete=models.CASCADE)

    class Meta:
        db_table = 'EmpLeave'


class ManagerEmpLeaveStatus(models.Model):
    leave_status_info = models.ForeignKey(LeaveStatus, on_delete=models.CASCADE)

