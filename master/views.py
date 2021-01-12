from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.utils.datastructures import MultiValueDictKeyError
from .models import Notification,Transport, Mess_menu, Register_student, Rooms, Complaint
from datetime import datetime, date
from random import randrange

today = date.today()

d1=today.strftime("%Y-%M-%D")

# Create your views here.
def admindashboard(request):
    re_data= Register_student.objects.all()
    re_data1= Complaint.objects.all()

    return render(request, 'admindashboard.html',{'message1':re_data,"mes":re_data1})


def adminstudent(request):
    re_data= Register_student.objects.all().order_by('-id')
    id_data= Register_student.objects.all()
    context={'message':re_data}
    # print(context['message'])

    return render(request, 'adminstudentlist.html',context)


def adminroom(request):
    re_data = Rooms.objects.all()

    return render(request, 'adminroom.html',{'message':re_data})


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


def admintransport(request):

    re_data = Transport.objects.all().order_by('to')
    # print(re_data)
    if(request.method=="POST"):
        bu = request.POST.get('bus')
        tim = request.POST.get('time')
        fr = request.POST.get('from')
        vi = request.POST.get('via')
        to4 = request.POST.get('to2')
        if(bu!="" and tim!=None and fr!=None and vi!=None and to4!=None):
            transport = Transport(bus=bu,time=tim,From=fr, via=vi, to=to4)
            transport.save()
            return HttpResponseRedirect("admintransport",{'message':re_data})

    return render(request, 'admintransport.html',{'message':re_data})
    # return HttpResponseRedirect('admintransport.html')


def adminledger(request):

    return render(request, 'adminledger.html')


def adminpayment(request):

    return render(request, 'adminpayment.html')


def admincomplaint(request):

    re_data = Complaint.objects.all()

    return render(request, 'adminquery.html',{'message':re_data})


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
        usr.save()
        user= Register_student(sname=s_name, smobile=s_mobile, fname=f_name, fmobile=f_mobile, semail=email,gender=gender1,dob=dob1, college=country1,course=course1, acadmic=acadmic1, address1=addr1, address2=addr2, city= city1, zip_code=zip1, country=country1,gov_type=g_type, gov_id=g_id, room_block=block1, room_no=room1, room_type=room_type1, acc_plan=plan1, final_fee=fee1)
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
    item.delete()
    return redirect("/adminstudent")
