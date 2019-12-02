from django.db import models
from emp_app.utils import *
from emp_app.CommonFileds import CommonAbstract


class WorkExperience(CommonAbstract):
    emp_id = models.IntegerField(null=False)
    previous_company = models.CharField(max_length=100, null=True)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)
    job_id = models.ForeignKey(JobTitle, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Work_Experience'
