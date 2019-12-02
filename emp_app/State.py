from django.db import models
from emp_app.utils import *
from emp_app.validators import *


class State(models.Model):
    # country_dial_code = models.ForeignKey(CountryDialCode, on_delete=models.CASCADE, null=False)
    state_name = models.CharField(max_length=50, null=False, validators=[name_validators])

    class Meta:
        db_table = 'State'

    def __str__(self):
        return self.state_name

