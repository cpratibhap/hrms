from django.db import models
from emp_app.utils import *
from emp_app.CommonFileds import CommonAbstract
from emp_app.validators import *


class Department(CommonAbstract):
    department_name = models.CharField(max_length=60, null=False, validators=[name_validators])

    class Meta:
        db_table = 'Department_Info'

    def __str__(self):
        return self.department_name
