from django.db import models
from emp_app.utils import*
from emp_app.CommonFileds import CommonAbstract
from emp_app.validators import *


class Degree(CommonAbstract):
    degree_name = models.CharField(max_length=80, null=False, validators=[name_validators])

    class Meta:
        db_table = 'Degree_Info'

    def __str__(self):
        return self.degree_name
