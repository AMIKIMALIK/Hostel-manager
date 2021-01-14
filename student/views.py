from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.utils.datastructures import MultiValueDictKeyError
from student import messmenu
from master.models import Notification, Complaint, Transport, Mess_menu, Register_student
from datetime import datetime, date
from django.contrib.auth.decorators import login_required
import calendar


# Create your views here.

def find_time():
    now = datetime.now()
    today = date.today() 
    today =str(today)
    year= today[:4]
    month= today[5:7]
    day= today[8:10]
    today=(day+" "+month+" "+year)
    day, month, year = (int(i) for i in today.split(' '))
    dayNumber = calendar.weekday(year, month, day)
    current_time = now.strftime("%H:%M")
    current_time = current_time.replace(":","")
    # print("Current Time =", current_time) 
    days =["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    return (dayNumber, current_time)


def index(request):
    return render(request, 'index.html')

# Below function for student view

@login_required
def studentdashboard(request):
    recent_notify = Notification.objects.all().order_by('-id')[:1]
    day1, time = find_time()
    day1 = day1+1
    if (int(time)<=930):
        ti='breakfast'
    elif (int(time)<=1330):
        ti= 'lunch'
    elif(int(time)<=1800):
        ti= 'snack'
    elif(int(time)<=2130):
        ti= 'dinner'
    week_day= Mess_menu.objects.get(id=day1)
    if (ti=="breakfast"):
        tx = week_day.breakfast
    elif (ti=="lunch"):
        tx = week_day.lunch
    elif(ti=="snack"):
        tx = week_day.snack
    else:
        tx = week_day.dinner

    us = Register_student.objects.get(semail=request.user.username)
    coll = us.college
    f1= Transport.objects.filter(From=coll)
    f2= Transport.objects.filter(to=coll)

    context={"messag":recent_notify,"mess":tx,"ti":ti,"f1":f1,"f2":f2,"rn":us.room_no,"rb":us.room_block,'nam':us.sname,"smob": us.smobile,'fnam':us.fname,'fmob': us.fmobile,'dob':us.dob,'em':us.semail,'gen': us.gender,'cou': us.course,'aca': us.acadmic,'add': us.address1,'cty': us.city,'pin': us.zip_code,'coun': us.country,'coll' : us.college}
    
    return render(request, 'studentdashboard.html',context)

@login_required
def studentledger(request):
    return render(request, 'studentledger.html')

@login_required
def studentpayment(request):
    return render(request, 'studentpayment.html')

@login_required
def studentmenu(request):

    data= Mess_menu.objects.all()


    return render(request, "studentmenu.html",{"message":data})

@login_required
def studenttransport(request):
    re_data = Transport.objects.all().order_by('bus')

    return render(request, 'studenttransport.html',{'message':re_data})

@login_required
def studentquery(request):

    date1 = datetime.now()
    date1 = str(date1)
    d1 = date1[:19]

    query = Complaint.objects.filter(student_id=request.user.username)

    if (request.method=="POST"):
        cat = request.POST['category']
        mes = request.POST['message']
        data = Complaint(category=cat, message=mes,datetime=d1,status=1, student_id=request.user.username)
        data.save()

        return HttpResponseRedirect("studentquery",{"query":query})

    return render(request, 'studentquery.html',{"query":query})

@login_required
def studentprofile(request):
    return render(request, 'profile.html')

@login_required
def studentnotification(request):
    data = Notification.objects.all().order_by('-id')

    return render(request, 'studentnotification.html',{"message":data})




