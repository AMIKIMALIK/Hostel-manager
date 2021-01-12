from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.utils.datastructures import MultiValueDictKeyError
from student import messmenu
from master.models import Notification, Complaint, Transport, Mess_menu
from datetime import datetime


# Create your views here.


def index(request):
    return render(request, 'index.html')

# Below function for student view


def studentdashboard(request):
    recent_notify = Notification.objects.all().order_by('-id')[:1]
    return render(request, 'studentdashboard.html',{'message':recent_notify})


def studentledger(request):
    return render(request, 'studentledger.html')


def studentpayment(request):
    return render(request, 'studentpayment.html')


def studentmenu(request):

    data= Mess_menu.objects.all()


    return render(request, "studentmenu.html",{"message":data})


def studenttransport(request):
    re_data = Transport.objects.all().order_by('time')

    return render(request, 'studenttransport.html',{'message':re_data})


def studentquery(request):

    date1 = datetime.now()
    date1 = str(date1)
    d1 = date1[:19]

    if (request.method=="POST"):
        cat = request.POST['category']
        mes = request.POST['message']

        data = Complaint(category=cat, message=mes,datetime=d1,status=1)
        data.save()

        return HttpResponseRedirect("studentquery")

    return render(request, 'studentquery.html')


def studentprofile(request):
    return render(request, 'profile.html')


def studentnotification(request):
    data = Notification.objects.all()

    return render(request, 'studentnotification.html',{"message":data})


# Below function are for Admin View


