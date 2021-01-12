from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path('', views.index, name="home"),
    path('studentquery', views.studentquery, name='about'),
    path('profile', views.studentprofile, name='profile'),
    path('studentmenu', views.studentmenu, name='menu'),
    path('studentledger', views.studentledger, name='ledger'),
    path('studentpayment', views.studentpayment, name='fee'),
    path('studentdashboard', views.studentdashboard, name='studentdashboard'),
    path('studenttransport', views.studenttransport, name="studenttransport"),
    path('studentnotification', views.studentnotification, name="studentnotification"),





]