from django.contrib import admin
from django.urls import path
from master import views

urlpatterns = [
    # path('', views.index, name="home"),
    path('admindashboard', views.admindashboard, name='admindashboard'),
    path('adminstudent', views.adminstudent, name="adminstudent"),
    path('adminroom', views.adminroom, name="adminroom"),
    path('adminmenu', views.adminmenu, name="adminmenu"),
    path('admintransport', views.admintransport, name="admintransport"),
    path('adminledger', views.adminledger, name="adminledger"),
    path('adminpayment', views.adminpayment, name="adminpayment"),
    path('adminquery', views.admincomplaint, name="adminquery"),
    path('adminnotification', views.adminnotification, name="adminnotification"),
    path('registerstudent', views.registerstudent, name='registerstudent'),
    path('viewstudent/<int:id>', views.viewstudent),
    path('editstudent/<int:id>', views.editstudent),
    path('deletestudent/<int:id>', views.deletestudent)




]