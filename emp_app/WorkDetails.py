from django.db import models
from emp_app.utils import *
from emp_app.validators import *


class WorkDetails(models.Model):
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE, null=False)
    job_id = models.ForeignKey(JobTitle, on_delete=models.CASCADE, null=False)
    degree_id = models.ForeignKey(Degree, on_delete=models.CASCADE, null=False)
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False)
    emp_type_id = models.ForeignKey(EmployeeType, on_delete=models.CASCADE, null=False)
    designation_id = models.ForeignKey(Designation, on_delete=models.CASCADE, null=False)
    emp_Basic_Id = models.ForeignKey(EmployeeInfo, on_delete=models.CASCADE, null=False)
    location_Id = models.ForeignKey(Location,on_delete=models.CASCADE)
    Date_of_Joining = models.DateField(null=False)
    source_id = models.ForeignKey(SourceOfHire, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Work_Details'
