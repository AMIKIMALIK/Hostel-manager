from django.db import models
from django.contrib.auth.models import User
from datetime import date
today = date.today()
d1 = today.strftime("%Y-%m-%d")

# Create your models here.
class Notification(models.Model):
    category = models.CharField(max_length=40)
    message = models.TextField(max_length=255)
    date_time = models.DateField(default=d1)

    def __str__(self):
        return self.category+" "+ str(self.date_time)

class Transport(models.Model):
    bus = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    From = models.CharField(max_length=40)
    via= models.CharField(max_length=40)
    to= models.CharField(max_length=40)

    def __str__(self):
        return self.bus

class Mess_menu(models.Model):
    day = models.CharField(max_length=20)
    breakfast= models.CharField(max_length=255)
    lunch= models.CharField(max_length=255)
    snack= models.CharField(max_length=255)
    dinner= models.CharField(max_length=255)
    
    def __str__(self):
        return self.day
    
class Register_student(models.Model):
    sname = models.CharField(max_length=40)
    smobile= models.CharField(max_length=20)
    fname= models.CharField(max_length=40)
    fmobile= models.CharField(max_length=20)
    semail= models.EmailField()
    gender= models.CharField(max_length=15)
    dob= models.CharField(max_length=15)
    college= models.CharField(max_length=100)
    course= models.CharField(max_length=100)
    acadmic= models.CharField(max_length=10)
    address1= models.CharField(max_length=255)
    address2= models.CharField(max_length=255, blank=True)
    city= models.CharField(max_length=100)
    zip_code= models.CharField(max_length=20)
    country= models.CharField(max_length=20)
    gov_type= models.CharField(max_length=20)
    gov_id= models.CharField(max_length=20)
    room_block = models.CharField(max_length=20)
    room_no= models.CharField(max_length=10)
    room_type = models.CharField(max_length=10)
    acc_plan= models.CharField(max_length=20)
    final_fee = models.CharField(max_length=10)
    


    def __str__(self):
        return self.sname
    
class Rooms(models.Model):
    room_no = models.CharField(max_length=10)
    floor = models.CharField(max_length=10)
    block = models.CharField(max_length=10)
    room_type = models.CharField(max_length=10)
    room_capacity = models.CharField(max_length=10)
    room_availablity = models.CharField(max_length=10)
    studentid_1st = models.CharField(max_length=10)
    studentid_2nd = models.CharField(max_length=10)
    studentid_3rd = models.CharField(max_length=10)

    def __str__(self):
        return self.room_no
    

class Complaint(models.Model):
    category = models.CharField(max_length=10)
    message = models.CharField(max_length=255)
    status = models.CharField(max_length=10, default=0)
    datetime= models.CharField(max_length=20, default=d1)

    def __str__(self):
        return self.student_id+" "+str(self.category)

class register_table(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    concact = models.IntegerField()

    def __str__(self):
        return self.user.username
    
    