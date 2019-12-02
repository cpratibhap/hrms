from django.db import models
from emp_app.CommonFileds import CommonAbstract


class JobTitle(CommonAbstract):
    job_title = models.CharField(max_length=80)

    class Meta:
        db_table = 'Job_Info'

    def __str__(self):
        return self.job_title
