from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.utils.datastructures import MultiValueDictKeyError
from .models import Notification,Transport, Mess_menu, Register_student, Rooms, Complaint
from datetime import datetime, date
import calendar
from random import randrange
from django.core.mail import send_mail
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

today = date.today()

d1=today.strftime("%Y-%M-%D")

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

# Create your views here.
@login_required
def admindashboard(request):
    re_data= Register_student.objects.all()
    am = Complaint.objects.all().order_by('-id')[:1]
    
    return render(request, 'admindashboard.html',{'message1':re_data,'mes':am})

@login_required
def adminstudent(request):
    re_data= Register_student.objects.all().order_by('-id')
    context={'message':re_data}
    if( request.method=='POST'):
        sid= request.POST['sid']
        field= request.POST['field']
        here= request.POST['here']
        data= Register_student.objects.get(pk=sid)
        if (field=="smobile"):
            data.smobile=here
        elif(field=="fname"):
            data.fname=here
        elif(field=="fmobile"):
            data.fmobile=here
        elif(field=="dob"):
            data.dob=here
        elif(field=="college"):
            data.college=here
        elif(field=="course"):
            data.course=here
        elif(field=="acadmic"):
            data.acadmic=here
        elif(field=="fadd"):
            data.address1=here
        elif(field=="sadd"):
            data.address2=here
        elif(field=="zip"):
            data.zip_code=here
        elif(field=="country"):
            data.country=here
        elif(field=="idt"):
            data.gov_type=here
        elif(field=="idn"):
            data.gov_id=here
        elif(field=="roomb"):
            data.room_block=here
        elif(field=="roomn"):
            data.room_no=here
        elif(field=="roomt"):
            data.room_type=here
        elif(field=="accp"):
            data.acc_plan=here
        else:
            data.final_fee=here

        data.save()
        return HttpResponseRedirect("adminstudent",context)




    return render(request, 'adminstudentlist.html',context)

@login_required
def adminroom(request):
    re_data = Rooms.objects.all()

    return render(request, 'adminroom.html',{'message':re_data})

@login_required
def adminmenu(request):
    re_data = Mess_menu.objects.all()
    if (request.method=='POST'):
        ti = request.POST.get('time')
        dy= request.POST.get('day')
        tx = request.POST.get('txt')
        re = Mess_menu.objects.get(pk=dy)
        if (ti=="breakfast"):
            re.breakfast=tx
        elif (ti=="lunch"):
            re.lunch= tx
        elif(ti=="snack"):
            re.snack= tx
        else:
            re.dinner= tx
        # print(re)
        re.save()
        return HttpResponseRedirect("adminmenu",{'message':re_data})
    
    return render(request, 'adminmenu.html',{'message':re_data})

@login_required
def admintransport(request):

    re_data = Transport.objects.all().order_by('to')
    # print(re_data)
    if(request.method=="POST"):
        bu = request.POST.get('bus')
        tim = request.POST.get('time')
        fr = request.POST.get('from')
        to4 = request.POST.get('to2')
        if(bu!="" and tim!=None and fr!=None and to4!=None):
            transport = Transport(bus=bu,time=tim,From=fr, to=to4)
            transport.save()
            return HttpResponseRedirect("admintransport",{'message':re_data})

    return render(request, 'admintransport.html',{'message':re_data})
    # return HttpResponseRedirect('admintransport.html')

@login_required
def adminledger(request):

    return render(request, 'adminledger.html')

@login_required
def adminpayment(request):

    return render(request, 'adminpayment.html')

@login_required
def admincomplaint(request):

    re_data = Complaint.objects.all().order_by('-id')

    return render(request, 'adminquery.html',{'message':re_data})

@login_required
def adminnotification(request):


    if (request.method=='POST'):
        # try:
        #     category= request.POST.get('category','false')
        #     message= request.POST['message1']
        # except MultiValueDictKeyError:
        #     message = False
        category1 = request.POST.get('category')
        message1 = request.POST.get('message')

        notification = Notification(category=category1,message=message1,date_time=d1)
        notification.save()

    return render(request, 'adminnotification.html')

def passgen(name):
    rand= randrange(11111,99999)
    sname = name.split()
    sname1 = len(sname)
    rand1= randrange(0,sname1)
    sn = sname[rand1]
    sn = str(sn)
    sn = sn.lower()
    if (len(sn)==2):
        rand= randrange(11111111,99999999)
    elif (len(sn)==3):
        rand= randrange(1111111,9999999)
    elif (len(sn)==4):
        rand= randrange(111111,999999)
    elif (len(sn)==5):
        rand= randrange(11111,99999)
    elif (len(sn)==6):
        rand= randrange(1111,9999)
    elif (len(sn)==7):
        rand= randrange(111,999)
    else:
        rand= randrange(111,999)
    rand = str(rand)
    passg = sn+rand
    print(passg)
    return passg

def first_last_name(name):
    sname = name.split()
    if (len(sname)==1):
        first = sname[0]
        last= ""
    else:
        first = sname[0]
        last= sname[-1]
    return first, last

@login_required
def registerstudent(request):
    id_data= Register_student.objects.only('studentid')
    if request.method =='POST':
        s_name = request.POST['s_name']
        s_mobile = request.POST['s_mobile']
        f_name = request.POST['f_name']
        f_mobile = request.POST['f_mobile']
        email = request.POST['email']
        gender1 = request.POST['gender']
        dob1 = request.POST['dob']
        college1 = request.POST['college']
        course1 = request.POST['course']
        acadmic1 = request.POST['acadmic']
        addr1 = request.POST['address']
        addr2 = request.POST['address2']
        city1 = request.POST['city']
        zip1 = request.POST['zip']
        country1 = request.POST['country']
        g_type = request.POST['gov_type']
        g_id = request.POST['gov_id']
        block1 = request.POST['block']
        room1 = request.POST['room']
        room_type1 = request.POST['room_type']
        plan1 = request.POST['plan']
        fee1 = request.POST['fee']

        password = passgen(s_name)
        print("Email Id: ",email)
        print("Password: ",password)

        fnam, lnam = first_last_name(s_name)


        usr= User.objects.create_user(username= email, email= email, password= password)
        usr.first_name= fnam
        usr.last_name= lnam
        
        user= Register_student(sname=s_name, smobile=s_mobile, fname=f_name, fmobile=f_mobile, semail=email,gender=gender1,dob=dob1, college=country1,course=course1, acadmic=acadmic1, address1=addr1, address2=addr2, city= city1, zip_code=zip1, country=country1,gov_type=g_type, gov_id=g_id, room_block=block1, room_no=room1, room_type=room_type1, acc_plan=plan1, final_fee=fee1)
        body = f"Hello {s_name}\nYour registration for Hostel Dashboard is successful\nYou login credentials are below:\nUsername: {email}\nPassword: {password}\n Login here: amitmalikapp.pythonanywhere.com"
        send_mail("Login Credentials for Hostel Dashboard",body,"malik02101999@gmail.com",[email],fail_silently=True)
        usr.save()
        user.save()
        # print("user created")
        # return render(request, 'adminregister.html')
        # return redirect('/')
        return HttpResponseRedirect("registerstudent")
    else:
        return render(request, 'adminregister.html')

def deletet(request,id):
    item = Transport.objects.get(id=id)
    item.delete()
    return redirect("/admintransport")

def editstudent(request):
    # item = Register_student.objects.get(id=id)
    # item.delete()
    # return redirect("/adminstudent")
    pass

def viewstudent():
    pass

def deletestudent(request, id):
    item = Register_student.objects.get(id=id)
    em = item.semail
    usr = User.objects.get(username=em)
    item.delete()
    usr.delete()

    return redirect("/adminstudent")



def user_login(request):
    if( request.method=="POST"):
        un= request.POST['username']
        pwd= request.POST['pass']

        user= authenticate(username=un, password=pwd)
        if user:
            login(request, user)
            if user.is_superuser:
                return HttpResponseRedirect('/admin')
            if user.is_staff:
                return HttpResponseRedirect('/admindashboard')
            if user.is_active:
                return HttpResponseRedirect('/studentdashboard')
        else:
            return HttpResponse(user)


    return redirect('index.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def error_404_view(request, exception):
    return render(request,'404.html')


def s_pending(request, id):
    item = Complaint.objects.get(id=id)
    item.status=0
    item.save()
    return redirect("/adminquery")