from django.db import models
from emp_app.utils import *
from emp_app.CommonFileds import CommonAbstract
from emp_app.validators import *
# from emp_app.EmployeeInfo import EmployeeInfo
from emp_app.CountryDialCode import CountryDialCode
# from leave_app.models import *


class Employee(CommonAbstract):
    first_name = models.CharField(max_length=50, null=False, validators=[name_validators])
    middle_name = models.CharField(max_length=50, null=True, validators=[name_validators])
    last_name = models.CharField(max_length=50, null=False, validators=[name_validators])
    email_id = models.EmailField(validators=[email_validators], null=False, unique=True)
    aadhar_no = models.IntegerField(null=False)
    emp_status = models.BooleanField(default=False)
    # leave_request_info = models.ForeignKey(LeaveRequest, on_delete=models.CASCADE, null=True)
    # emp_info = models.OneToOneField(EmployeeInfo)
    # country_id = models.ForeignKey(CountryDialCode, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='documents/%Y/%m/%d/', max_length=100, validators=[validate_image_file_extension])

    class Meta:
        db_table = 'Basic_Info'

    def __str__(self):
        return self.first_name


