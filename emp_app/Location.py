from django.db import models
from emp_app.CommonFileds import CommonAbstract


class Location(CommonAbstract):
    location_name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'Location'

    def __str__(self):
        return self.location_name