from django.db import models

class Visit(models.Model):
    id = models.IntegerField(primary_key=True)
    visitor_name = models.CharField(max_length=200)
    organization_name = models.CharField(max_length=15)
    purpose = models.CharField(max_length=150)
    cnic =models.CharField(max_length=15)
    contact_no = models.CharField(max_length=11)
    checkin_time =models.DateTimeField()
    checkout_time = models.DateTimeField(default=None)
    gender = models.CharField(max_length=15)
    employee_id = models.CharField(max_length=30)
    status= models.CharField(max_length=10)
    group_id = models.IntegerField()
    status2 = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'visit'


# class Department(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=50)

#     class Meta:
#         managed = False
#         db_table = 'Department'

# class Employee(models.Model):
#     emp_id = models.IntegerField(primary_key=True)
#     emp_name = models.CharField(max_length=50)
#     designation = models.CharField(max_length=30)
#     emp_cnic= models.CharField(max_length=15)
#     department_id = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'Employee'


class emp_info_vw(models.Model):
    employee_number= models.CharField(max_length=30,primary_key=True)
    name = models.CharField(max_length=393)
    email_address = models.CharField(max_length=240)
    position_name = models.CharField(max_length=4000)
    
    class Meta:
        managed = False
        db_table = 'EMP_INFO_VW'

class dep_info_vw(models.Model):
    organization_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=240)

    class Meta:
        managed = False
        db_table = 'dep_info_vw'


class hpml_hr_visitor_view(models.Model):
    id = models.IntegerField(primary_key=True)
    visitor_name = models.CharField(max_length=200)
    organization_name = models.CharField(max_length=15)
    purpose = models.CharField(max_length=150)
    cnic =models.CharField(max_length=15)
    contact_no = models.CharField(max_length=11)
    name = models.CharField(max_length=393)
    checkin_time =models.DateTimeField()
    checkout_time = models.DateTimeField(default=None)
    status= models.CharField(max_length=10)
    status2 = models.CharField(max_length=15)
    
    class Meta:
        managed=False
        db_table= 'hpml_hr_visitor_view'

    
# class HPML_HR_EMPLOYEE_INFO(models.Model):
#    organization_id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=240)
    
#     class Meta:
#         managed = False
#         db_table = 'HPML_HR_EMP_INFO'

# class HPML_HR_ORGANIZATIONS(models.Model):
#     organization_id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=240)

#     class Meta:
#         managed = False
#         db_table = 'HPML_HR_ORGANIZATIONS'


