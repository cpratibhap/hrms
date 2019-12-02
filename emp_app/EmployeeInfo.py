from django.db import models
from emp_app.utils import *
from emp_app.validators import *
from emp_app.CountryDialCode import CountryDialCode


class EmployeeInfo(models.Model):
    emp_age = models.IntegerField(null=False)
    emp_dob = models.DateField(null=False)
    hire_date = models.DateField(null=False)
    salary = models.FloatField(null=False)
    mobile_no = models.CharField(max_length=13, null=False, validators=[mobile_regex])
    gender = models.CharField(max_length=60, null=False)
    pan_no = models.CharField(max_length=20, null=False)
    permanent_address = models.TextField(max_length=400, null=False)
    blood_group = models.CharField(max_length=10, null=False)
    about_me = models.CharField(max_length=400)
    marital_status = models.CharField(max_length=3, choices=[('M', 'Married'), ('U', 'Unmarried')])
    relieving_date = models.DateField(null=True)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE, null=False)
    job_id = models.ForeignKey(JobTitle, on_delete=models.CASCADE, null=False)
    degree_id = models.ForeignKey(Degree, on_delete=models.CASCADE, null=False)
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False)
    emp_type_id = models.ForeignKey(EmployeeType, on_delete=models.CASCADE, null=False)
    designation_id = models.ForeignKey(Designation, on_delete=models.CASCADE, null=False)
    country_id = models.ForeignKey(CountryDialCode, on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'Personal_Info'





