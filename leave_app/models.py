from django.db import models
#from emp_app import EmployeeLeave

# Create your models here.


class LeaveType(models.Model):
    leave_type = models.CharField(max_length=100, null=False)

    class Meta:
        db_table = 'Leave_Type_Info'


class LeaveBalance(models.Model):
    total_leaves = models.IntegerField(null=False)
    available_leaves = models.FloatField(null=False)

    class Meta:
        db_table = 'Leave_Balance_Info'


class LeaveRequest(models.Model):
    date_from = models.DateField(null=False)
    date_to = models.DateField(null=False)
    no_of_days = models.IntegerField(null=False)
    is_informed = models.BooleanField(default=False)
    reason_for_leave = models.CharField(max_length=100)
    # leave_balance_info = models.ForeignKey(LeaveBalance, on_delete=models.CASCADE)
    # leave_type_info = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    # basic_info = models.ForeignKey(Employee, on_delete=models.CASCADE())

    class Meta:
        db_table = 'Leave_Request_Info'


class LeaveStatus(models.Model):
    is_approved = models.BooleanField(default=False)
    approval_date = models.DateField(null=False)
    approval_remarks = models.CharField(max_length=100)
    # leave_request_info = models.ForeignKey(EmployeeLeave, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Leave_Status_Info'

