from django.db import models
from emp_app.CommonFileds import *


class SourceOfHire(CommonAbstract):
    source_name = models.CharField(max_length=60, null=False)

    class Meta:
        db_table = 'SourceOfHire'

    def __str__(self):
        return self.source_name

