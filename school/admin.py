from django.contrib import admin
from .models import Class_room, Job_id, Employees, Subject, Student, Teacher, Family, Family_type, Teacher_subject,Class_subject
# Register your models here.
admin.site.register(Teacher)
admin.site.register(Job_id)
admin.site.register(Employees)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Family)
admin.site.register(Family_type)
admin.site.register(Teacher_subject)
admin.site.register(Class_subject)
admin.site.register(Class_room)




