from django.db import models
from emp_app.utils import *
from emp_app.CommonFileds import CommonAbstract

class Education(CommonAbstract):
    date_of_completion = models.DateField(null=False)
    field = models.CharField(max_length=50, null=False)
    additional_notes = models.CharField(max_length=60)
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False)
    degree_id = models.ForeignKey(Degree, on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'Education'
