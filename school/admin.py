from django.contrib import admin
from .models import Teacher, Student, Subject, Family, Family_type, Teacher_subject, Class_room, Class_subject
# Register your models here.

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Family)
admin.site.register(Family_type)
admin.site.register(Teacher_subject)
admin.site.register(Class_subject)
admin.site.register(Class_room)




