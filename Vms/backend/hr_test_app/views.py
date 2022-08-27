from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from django.db import connections
from django.db import connection
from rest_framework.parsers import JSONParser
from django.core.paginator import Paginator
# Create your views here.
from django.shortcuts import render
from django.apps import apps
import cx_Oracle
from .models import Visit,emp_info_vw,dep_info_vw,hpml_hr_visitor_view
from .serializers import  VisitSerializer,emp_info_vwSerializer,dep_info_vwSerializer,hpml_hr_visitor_viewSerializer
from django.http.response import JsonResponse

@csrf_exempt
def departmentApi(request, id1=0):
    if request.method == "GET":
        departments = dep_info_vw.objects.all()
        departments_serializer = dep_info_vwSerializer(departments,many = True)
        return JsonResponse(departments_serializer.data,safe=False)

    elif request.method == "POST":
        department_data = JSONParser().parse(request)
        department_serializer = dep_info_vwSerializer(data=department_data )
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully!!",safe=False)
        return JsonResponse("Failed to Add",safe=False)

    elif request.method=="PUT":
        department_data = JSONParser().parse(request)
        department= dep_info_vw.objects.get(id=department_data['id'])
        department_serializer =dep_info_vwSerializer(department, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Succesfully!!",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    
    elif request.method=="DELETE":
        department = dep_info_vw.objects.get(id=id1)
        department.delete()
        return JsonResponse("Deleted Successfully!! ",safe=False)




@csrf_exempt
def employeeApi(request, id1=0):
    if request.method == "GET":
        emp = emp_info_vw.objects.all()
        employees_serializer =emp_info_vwSerializer(emp,many = True)
        return JsonResponse(employees_serializer.data  ,safe=False)

    elif request.method == "POST":
        employee_data = JSONParser().parse(request)
        employee_serializer = emp_info_vwSerializer(data=employee_data )
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully!!",safe=False)
        return JsonResponse("Failed to Add",safe=False)
        
    elif request.method=="PUT":
        employee_data = JSONParser().parse(request)
        employee= emp_info_vw.get(id=employee_data['id'])
        employee_serializer =emp_info_vwSerializer(employee, data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated Succesfully!!",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    
    elif request.method=="DELETE":
        employee = emp_info_vw.objects.get(id=id1)
        employee.delete()
        return JsonResponse("Deleted Successfully!! ",safe=False)


@csrf_exempt
def visitApi(request, id1=0):
    if request.method == "GET":
        visitors = Visit.objects.all()
        visitors_serializer = VisitSerializer(visitors,many = True)
        return JsonResponse(visitors_serializer.data,safe=False)

    elif request.method == "POST":
        visitor_data = JSONParser().parse(request)
        visitor_serializer = VisitSerializer(data=visitor_data )
        if visitor_serializer.is_valid():
            visitor_serializer.save()
            return JsonResponse("Added Successfully!!",safe=False)
        return JsonResponse("Failed to Add",safe=False)
        
    elif request.method=="PUT":
        visitor_data = JSONParser().parse(request)
        visitor = Visit.objects.get(id=visitor_data['id'])
        visitor_serializer =VisitSerializer(visitor, data=visitor_data)
        if visitor_serializer.is_valid():
            visitor_serializer.save()
            return JsonResponse("Updated Succesfully!!",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    
    elif request.method=="DELETE":
        visitor =Visit.objects.get(id=id1)
        visitor.delete()
        return JsonResponse("Deleted Successfully!! ",safe=False)

@csrf_exempt
def sortVisitorByGroupId(request):
    visit = Visit.objects.all().order_by('group_id').values()
    visit_serializer = VisitSerializer(visit,many = True)
    return JsonResponse(visit_serializer.data,safe=False)


@csrf_exempt
def sortApiDesc(request,id1=0):
    visitors = hpml_hr_visitor_view.objects.all().order_by('-id').values()
    visitors_serializer =hpml_hr_visitor_viewSerializer(visitors,many = True)
    return JsonResponse(visitors_serializer.data,safe=False)


@csrf_exempt
def sortApiAsc(request):
    visitors = hpml_hr_visitor_view.objects.all().order_by('id').values()
    visitors_serializer = hpml_hr_visitor_viewSerializer(visitors,many = True)
    return JsonResponse(visitors_serializer.data,safe=False)

@csrf_exempt
def sortStatus(request,status):
    visitor = hpml_hr_visitor_view.objects.filter(status__icontains=status).values()
    visitors_serializer = hpml_hr_visitor_viewSerializer(visitor,many = True)
    return JsonResponse(visitors_serializer.data,safe=False)

@csrf_exempt
def visitoridsearch(request, pk):
    visitor = hpml_hr_visitor_view.objects.get(pk=pk)
    if request.method == 'GET': 
        Visitor_serializer = hpml_hr_visitor_viewSerializer(visitor) 
        return JsonResponse(Visitor_serializer.data) 

@csrf_exempt
def visitoridsearch2(request, pk):
    visitor = Visit.objects.get(pk=pk)
    if request.method == 'GET': 
        Visitor_serializer = VisitSerializer(visitor) 
        return JsonResponse(Visitor_serializer.data) 


@csrf_exempt
def employeeidSearch(request,pk):
    employee = emp_info_vw.objects.get(pk=pk)
    if request.method == 'GET': 
        Employee_serializer =emp_info_vwSerializer(employee) 
        return JsonResponse(Employee_serializer.data) 
@csrf_exempt
def visitoridedit(request,id1=0):
    if request.method=="PUT":
        visitor_data = JSONParser().parse(request)
        visitor = Visit.objects.get(id=visitor_data['id'])
        visitor_serializer =VisitSerializer(visitor, data=visitor_data)
        if visitor_serializer.is_valid():
            visitor_serializer.save()
            return JsonResponse("Updated Succesfully!!",safe=False)
        return JsonResponse("Failed to Add",safe=False)
@csrf_exempt
def visitornamesearch(request,pk):
    # visitor_data = JSONParser().parse(request)
    visitor = hpml_hr_visitor_view.objects.filter(visitor_name__icontains=pk).values()
    visitors_serializer = hpml_hr_visitor_viewSerializer(visitor,many = True)
    return JsonResponse(visitors_serializer.data,safe=False)

@csrf_exempt
def visitorFilter(request,pk):
    # visitor_data = JSONParser().parse(request)
    visitor = Visit.objects.filter(status__icontains=pk).values()
    visitors_serializer = VisitSerializer(visitor,many = True)
    return JsonResponse(visitors_serializer.data,safe=False)

@csrf_exempt
def visitorStatusCount(req,pk):
    visitor = Visit.objects.filter(status__icontains=pk).count()
    return JsonResponse( visitor,safe=False)

@csrf_exempt
def employeenamesearch(request,pk):
    # visitor_data = JSONParser().parse(request)
    employee = emp_info_vw.objects.filter(name__icontains=pk).values()
    return JsonResponse( list(employee),safe=False)

@csrf_exempt
def employeenamefromvisitor(request,na):
    # visitor_data = JSONParser().parse(request)
    visitor = hpml_hr_visitor_view.objects.filter(name__icontains=na).values()
    visitors_serializer = hpml_hr_visitor_viewSerializer(visitor,many = True)
    return JsonResponse( visitors_serializer.data,safe=False)


@csrf_exempt
def visitrecordbynumber(request,number):
    visitor = Visit.objects.filter(contact_no__icontains=number).order_by('id').values().reverse()[:1] 
    visitors_serializer = VisitSerializer(visitor,many = True)
    return JsonResponse(visitors_serializer.data,safe=False)

@csrf_exempt
def visitrecordbycnic(request,cnic):
    visitor = Visit.objects.filter(cnic__icontains=cnic).order_by('id').values().reverse()[:1] 
    # visitor = visitor[-1]
    visitors_serializer = VisitSerializer(visitor,many = True)
    return JsonResponse(visitors_serializer.data,safe=False)


@csrf_exempt
def visitrecordbycontact(request,contact):
    visitor =Visit.objects.filter(contact_no__icontains=contact).order_by('id').values().reverse()[:1]
    visitor_serializer = VisitSerializer(visitor,many=True)
    return JsonResponse(visitor_serializer.data,safe=False)

@csrf_exempt
def empview(request):
    view = hpml_hr_visitor_view.objects.all()
    view_serializer = hpml_hr_visitor_viewSerializer(view,many = True)
    return JsonResponse(view_serializer.data,safe=False)


# @csrf_exempt
# def departmentApi(request, id1=0):
#     if request.method == "GET":
#         departments = Department.objects.all()
#         departments_serializer = DepartmentSerializer(departments,many = True)
#         return JsonResponse(departments_serializer.data,safe=False)

#     elif request.method == "POST":
#         department_data = JSONParser().parse(request)
#         department_serializer = DepartmentSerializer(data=department_data )
#         if department_serializer.is_valid():
#             department_serializer.save()
#             return JsonResponse("Added Successfully!!",safe=False)
#         return JsonResponse("Failed to Add",safe=False)

#     elif request.method=="PUT":
#         department_data = JSONParser().parse(request)
#         department= Department.objects.get(id=department_data['id'])
#         department_serializer =DepartmentSerializer(department, data=department_data)
#         if department_serializer.is_valid():
#             department_serializer.save()
#             return JsonResponse("Updated Succesfully!!",safe=False)
#         return JsonResponse("Failed to Add",safe=False)
    
#     elif request.method=="DELETE":
#         department = Department.objects.get(id=id1)
#         department.delete()
#         return JsonResponse("Deleted Successfully!! ",safe=False)




# @csrf_exempt
# def employeeApi(request, id1=0):
#     if request.method == "GET":
#         emp = Employee.objects.all()
#         employees_serializer = EmployeeSerializer(emp,many = True)
#         return JsonResponse(employees_serializer.data,safe=False)

#     elif request.method == "POST":
#         employee_data = JSONParser().parse(request)
#         employee_serializer = EmployeeSerializer(data=employee_data )
#         if employee_serializer.is_valid():
#             employee_serializer.save()
#             return JsonResponse("Added Successfully!!",safe=False)
#         return JsonResponse("Failed to Add",safe=False)
        
#     elif request.method=="PUT":
#         employee_data = JSONParser().parse(request)
#         employee= Employee.objects.get(id=employee_data['id'])
#         employee_serializer =EmployeeSerializer(employee, data=employee_data)
#         if employee_serializer.is_valid():
#             employee_serializer.save()
#             return JsonResponse("Updated Succesfully!!",safe=False)
#         return JsonResponse("Failed to Add",safe=False)
    
#     elif request.method=="DELETE":
#         employee = Employee.objects.get(id=id1)
#         employee.delete()
#         return JsonResponse("Deleted Successfully!! ",safe=False)


# @csrf_exempt
# def visitApi(request, id1=0):
#     if request.method == "GET":
#         visitors = Visit.objects.all()
#         visitors_serializer = VisitSerializer(visitors,many = True)
#         return JsonResponse(visitors_serializer.data,safe=False)

#     elif request.method == "POST":
#         visitor_data = JSONParser().parse(request)
#         visitor_serializer = VisitSerializer(data=visitor_data )
#         if visitor_serializer.is_valid():
#             visitor_serializer.save()
#             return JsonResponse("Added Successfully!!",safe=False)
#         return JsonResponse("Failed to Add",safe=False)
        
#     elif request.method=="PUT":
#         visitor_data = JSONParser().parse(request)
#         visitor = Visit.objects.get(id=visitor_data['id'])
#         visitor_serializer =VisitSerializer(visitor, data=visitor_data)
#         if visitor_serializer.is_valid():
#             visitor_serializer.save()
#             return JsonResponse("Updated Succesfully!!",safe=False)
#         return JsonResponse("Failed to Add",safe=False)
    
#     elif request.method=="DELETE":
#         visitor =Visit.objects.get(id=id1)
#         visitor.delete()
#         return JsonResponse("Deleted Successfully!! ",safe=False)

# @csrf_exempt
# def sortApiDesc(request,id1=0):
#     visitors = Visit.objects.all().order_by('-id').values()
#     visitors_serializer = VisitSerializer(visitors,many = True)
#     return JsonResponse(visitors_serializer.data,safe=False)


# @csrf_exempt
# def sortApiAsc(request):
#     visitors = Visit.objects.all().order_by('id').values()
#     visitors_serializer = VisitSerializer(visitors,many = True)
#     return JsonResponse(visitors_serializer.data,safe=False)

# @csrf_exempt
# def visitoridsearch(request, pk):
#     visitor = Visit.objects.get(pk=pk)
#     if request.method == 'GET': 
#         Visitor_serializer = VisitSerializer(visitor) 
#         return JsonResponse(Visitor_serializer.data) 


# @csrf_exempt
# def employeeidSearch(request,pk):
#     employee = Employee.objects.get(pk=pk)
#     if request.method == 'GET': 
#         Employee_serializer = EmployeeSerializer(employee) 
#         return JsonResponse(Employee_serializer.data) 
# @csrf_exempt
# def visitoridedit(request,id1=0):
#     if request.method=="PUT":
#         visitor_data = JSONParser().parse(request)
#         visitor = Visit.objects.get(id=visitor_data['id'])
#         visitor_serializer =VisitSerializer(visitor, data=visitor_data)
#         if visitor_serializer.is_valid():
#             visitor_serializer.save()
#             return JsonResponse("Updated Succesfully!!",safe=False)
#         return JsonResponse("Failed to Add",safe=False)
# @csrf_exempt
# def visitornamesearch(request,pk):
#     # visitor_data = JSONParser().parse(request)
#     visitor = Visit.objects.filter(name__icontains=pk).values()
#     return JsonResponse( list(visitor),safe=False)

# @csrf_exempt
# def employeenamesearch(request,pk):
#     # visitor_data = JSONParser().parse(request)
#     employee = Employee.objects.filter(emp_name__icontains=pk).values()
#     return JsonResponse( list(employee),safe=False)

# def connections():
#     h = '140.1.20.16' #Your host name/ip
#     p = '1576' #Your port number
#     sid = 'TEST' #Your sid
#     u = 'HPMLVMS' #Your login user name
#     pw = 'HPMLVMS202207' #Your login password
#     d = cx_Oracle.makedsn(h, p, sid=sid)
#     conn = cx_Oracle.connect(user=u, password=pw, dsn=d)
#     return conn


# def list(request):
#     depts = []
#     with connection.cursor() as cursor:
#         c=cursor.execute("SELECT * FROM Department")
#         for row in c:
#             depts.append({"id": row[0], "name": row[1]})
#         cursor.close()
#     return render(request, 'abc.html', {'depts':depts})
  

# def adddept(request):
#     if request.method == 'GET':
#         return render(request, 'adddept.html', {'dept':{}})
#     if request.method == 'POST':
#         form = DeptForm(request.POST)
#         if form.is_valid():
#             id = form.cleaned_data.get("id")
#             name = form.cleaned_data.get("name")
#         # conn = connections()
#         # cursor=conn.cursor()
#             cursor =connection.cursor()
#             query = ''' INSERT INTO Department(id,:name) VALUES (%i,%c)'''
#             cursor.execute(query, [id,name])
#             # connection.commit()
#             # connection.close()
#         # conn.close()
#         return redirect('list')

# def addvisitor(request):
#     if request.method == 'GET':
#         return render(request, 'visitorlist.html', {'visit':{}})
#     if request.method == 'POST':
#         form = VisitForm(request.POST)
#         if form.is_valid():
#             # id=request.POST['id']
#             # name=request.POST['name']
#             # organization_name=request.POST['organization_name']
#             # purpose= request.POST['purpose']
#             # cnic = request.POST['cnic']
#             # contact_no=request.POST['contact_no']
#             # employee_id=request.POST['employee_id']
#             # department_id=request.POST['department_id']
#             id1 = form.cleaned_data.get("id1")
#             name1 = form.cleaned_data.get("name1")
#             organization_name=form.cleaned_data.get("organization_name")
#             purpose=form.cleaned_data.get("purpose")
#             cnic=form.cleaned_data.get("cnic")
#             contact_no=form.cleaned_data.get("contact_no")
#             employee_id= form.cleaned_data.get("employee_id")
#             department_id=form.cleaned_data.get("department_id")
#         conn = connections()
#         cursor = conn.cursor()
#         sql="INSERT INTO Visit(id,name,organization_name,purpose,cnic,contact_no,employee_id,department_id) VALUES(:id1, :name1,:organization_name,:purpose,:cnic,:contact_no, :employee_id, :department_id )"
#         # sql="INSERT INTO Visit(id,name,organization_name,purpose,cnic,contact_no,employee_id,department_id) VALUES(:id1, :name1, :organization_name, :purpose, :cnic, :contact_no, :employee_id, :department_id )"
#         cursor.execute(sql, [id1,name1,organization_name,purpose,cnic,contact_no,employee_id,department_id])
#         conn.commit()
#         conn.close()
#         return redirect('list')

# def updatedept(request, id):
#     cr = []
#     conn = connections()
#     cursor = conn.cursor()
#     if request.method == 'GET':
#         cursor.execute("SELECT * FROM Department WHERE id = :id", [id])
#         row = cursor.fetchone()
#         cr.append({"id": row[0], "name": row[1]})
#         conn.close()
#         return render(request, 'adddept.html', {'dept':cr[0]})
#     if request.method == 'POST':
#         form = DeptForm(request.POST)
#         if form.is_valid():
#             name = str(form.cleaned_data.get("name"))
#             cursor.execute("UPDATE Department SET name = :name WHERE id = :id", [name, id])
#             conn.commit()
#         conn.close()
#         return redirect('list')

# def deletedept(request, id):
#     conn = connections()
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM Department WHERE id = :id", [id])
#     conn.commit()
#     conn.close()
#     return redirect('list')


# def empv(request):
#     res = """<h2 align="center">Grid of all employees</h2>
#              <hr>"""
#     objects = Department.objects.all()
#     count = 0  # initialize name count for each row

#     for emp in objects:
#         if count == 4:
#             res += '&nbsp;&nbsp;&nbsp;&nbsp;' +str (emp.id) + \
#                 ' ' + emp.name + '&nbsp;&nbsp;&nbsp;&nbsp;||</p>'
#             count = 0  # reset the name count for each row
#         else:
#             if count == 0:
#                 res += '<p align="center">'+'||'
#             res += '&nbsp;&nbsp;&nbsp;&nbsp;' + str(emp.id)+ \
#                 ' ' +  emp.name + '&nbsp;&nbsp;&nbsp;&nbsp;||'
#             count += 1

#     return HttpResponse(res)



