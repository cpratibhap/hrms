from django.db import models
from emp_app.utils import *
from emp_app.CommonFileds import CommonAbstract


class EmployeeType(CommonAbstract):
    emp_type = models.CharField(max_length=80, null=False)

    class Meta:
        db_table = 'Employee_Type'

    def __str__(self):
        return self.emp_type