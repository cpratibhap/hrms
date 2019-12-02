from django.db import models
from emp_app.utils import *
from emp_app.validators import *


class CountryDialCode(models.Model):
    country_code = models.CharField(max_length=3, null=False)
    iso2 = models.CharField(max_length=2, null=False)
    country_prefix = models.IntegerField(null=False)
    country_name = models.CharField(max_length=50, null=False, validators=[name_validators])

    class Meta:
        db_table = 'Country_dial_code'

    def __str__(self):
        return self.country_name

'''
class Country(models.Model):
    country_name = models.ForeignKey(CountryDialCode, on_delete=models.SET_NULL, null=True)
    country_dial_code = models.ForeignKey(CountryDialCode, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'Country'

    def __str__(self):
        return self.country_name
'''
