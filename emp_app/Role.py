from django.db import models
from emp_app.utils import *
from emp_app.validators import *
from emp_app.CommonFileds import CommonAbstract


class Role(CommonAbstract):
    role_name = models.CharField(max_length=50, null=False, validators=[name_validators])
    mobile_no = models.CharField(max_length=13, validators=[mobile_regex], null=False)

    class Meta:
        db_table = 'Role'

    def __str__(self):
        return self.role_name