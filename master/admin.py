from django.contrib import admin
from .models import Notification,Transport, Mess_menu, Register_student, Rooms, Complaint, register_table


admin.site.site_header="Hostel Manager"
admin.site.register(Notification)
admin.site.register(Transport)
admin.site.register(Mess_menu)
admin.site.register(Register_student)
admin.site.register(Rooms)
admin.site.register(Complaint)
admin.site.register(register_table)
# Register your models here.
