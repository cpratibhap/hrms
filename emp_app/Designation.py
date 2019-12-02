from django.db import models
from emp_app.utils import *
from emp_app.CommonFileds import CommonAbstract


class Designation(CommonAbstract):
    designation_name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'Designation_Info'

    def __str__(self):
        return self.designation_name