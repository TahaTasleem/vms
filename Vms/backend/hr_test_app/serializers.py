from rest_framework import serializers
from hr_test_app.models import Visit ,emp_info_vw,dep_info_vw,hpml_hr_visitor_view

# class DepartmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model =  Department
#         fields = ('id','name')


# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         fields = ('emp_id','emp_name','designation','emp_cnic','department_id')

class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model=Visit
        fields = ('id','visitor_name','organization_name','purpose','cnic','contact_no','checkin_time','checkout_time','gender','employee_id','status','status2','group_id')


class emp_info_vwSerializer(serializers.ModelSerializer):
    class Meta:
        model=emp_info_vw
        fields = ('employee_number','name','email_address','position_name')

class dep_info_vwSerializer(serializers.ModelSerializer):
    class Meta:
        model=dep_info_vw
        fields = ('organization_id','name')

class hpml_hr_visitor_viewSerializer(serializers.ModelSerializer):
    class Meta:
        model= hpml_hr_visitor_view
        fields=('id','visitor_name','organization_name','purpose','cnic','contact_no','name', 'checkin_time','checkout_time' ,'status','status2' )


