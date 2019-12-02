from django.db import models
from emp_app.validators import *


class CommonAbstract(models.Model):
    added_by = models.CharField(max_length=50, null=False, validators=[name_validators])
    added_time = models.TimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=50, null=False)
    modified_time = models.TimeField(auto_now=True)  #blank=True
    is_deleted = models.BooleanField(default=False, null=False)

    class Meta:
        db_table='Comn_abs'
        abstract = True
