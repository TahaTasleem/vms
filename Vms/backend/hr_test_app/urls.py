from django.urls import path
from django.urls import re_path as url
# from django.conf.urls import url
from . import views
# from hr_test_app.views import index
urlpatterns=[
    url(r'^department/$',views.departmentApi),   
    url(r'^department/([0-9]+)$',views.departmentApi),

    url(r'^employee/$',views.employeeApi),
    # url(r'^employee/([0-9]+)$',views.employeeApi),
    url(r'^employee/([0-9]+)$',views.employeeidSearch),
    url(r'^employee/([A-Za-z.\s_-]+)$',views.employeenamesearch),

    #Temporary URL
    url(r'^visitorbygroup/asc/$',views.sortVisitorByGroupId),

    url(r'^newappointment/$',views.visitApi),
    url(r'^newappointment/([0-9]+)$',views.visitApi),

    url(r'^newappointments/([0-9]+)$',views.visitoridsearch2),
    url(r'^newappointmentedit/([0-9]+)$',views.visitoridedit),

    url(r'^empappointment/$',views.visitApi),
    url(r'^empappointment/([0-9]+)$',views.visitoridsearch),
    url(r'^empappointments/([0-9]+)$',views.visitoridedit),


    url(r'^visitor/desc/$',views.sortApiDesc),
    url(r'^visitor/asc/$',views.sortApiAsc),
    url(r'^visitor/filter/([A-Za-z.\s_-]+)$',views.visitorFilter),
    url(r'^visitor/filter/count/([A-Za-z.\s_-]+)$',views.visitorStatusCount),

    url(r'^visitor/([0-9]+)$', views.visitoridsearch),
    url(r'^visitors/([a-z]+)$', views.visitornamesearch),


    url(r'^visitorsearch/([0-9]+)$',views.visitrecordbynumber),
    url(r'^visitorsearchs/([0-9]+)$',views.visitrecordbycnic),
    url(r'^visitorsearchcontact/([0-9]+)$',views.visitrecordbycontact),

    url(r'^emp_view/$',views.empview),
    url(r'^sortstatus/([A-Za-z.\s_-]+)$',views.sortStatus),
    url(r'^employeefromvisitor/([A-Za-z.\s_-]+)$',views.employeenamefromvisitor),


    # path('',views.departmentApi,name='deoartmentApi'),
    # path('adddept',views.adddept,name='adddept'),
    # path('updatedept/<int:id>', views.updatedept, name = 'updatedept'),
    # path('deletedept/<int:id>', views.deletedept, name = 'deletedept'),
    # path('addvisitor', views.addvisitor, name = 'addvisitor'),
    # path('emp/',views.empv)
]