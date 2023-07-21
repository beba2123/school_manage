from django.db import models
import uuid
# Create your models here.
class Student(models.Model):
    id         = models.UUIDField(default=uuid.uuid4, unique= True, primary_key= True, editable= False)
    firstName  = models.CharField(max_length= 50, null = False, blank= False)
    middelName = models.CharField(max_length= 50, null = False, blank= False)
    lastName   = models.CharField(max_length= 50, null = False, blank= False)
    email      = models.EmailField(max_length= 100, null = False, blank= False)
    phone      = models.IntegerField(max_length= 12, null=False, blank=False)
    age        = models.IntegerField(max_length=3, null = False, blank= False)
    sex        = models.CharField(max_length=1, null = False, blank= False)
    class_room_id = models.ForeignKey()


class Family(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    firstName = models.CharField(max_length=50, null=False, blank=False)
    middelName = models.CharField(max_length=50, null=False, blank=False)
    lastName = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    phone = models.IntegerField(max_length= 12, null=False, blank=False)
    sex = models.CharField(max_length=1, null=False, blank=False)

class Family_type(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    typeName = models.CharField(max_length=50, null=False, blank=False)
class Student_Family(models.Model):
    familyTypeId = models.ForeignKey(Family_type, on_delete= models.CASCADE(), blank=False)
    studentId = models.ForeignKey(Student, on_delete= models.CASCADE(), blank= False)
    familyId = models.ForeignKey(Family, on_delete= models.CASCADE(), blank= False)

class Subject(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    subjectName = models.CharField(max_length=50, null=False, blank=False)

class Class_room(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    roomName = models.CharField(max_length=50, null=False, blank=False)
class Teacher(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    firstName = models.CharField(max_length=50, null=False, blank=False)
    middelName = models.CharField(max_length=50, null=False, blank=False)
    lastName = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    phone = models.IntegerField(max_length=12, null=False, blank=False)
    sex = models.CharField(max_length=1, null=False, blank=False)
class Class_subject(models.Model):
    classRoomId = models.ForeignKey(Class_room, on_delete=models.CASCADE(), blank=False)
    subjectId = models.ForeignKey(Subject, on_delete=models.CASCADE(), blank=False)
    teacherId = models.ForeignKey(Teacher, on_delete=models.CASCADE(), blank=False)
class Teacher_subject(models.Model):
    teacherId = models.ForeignKey(Teacher, on_delete=models.CASCADE(), blank=False)
    subjectId = models.ForeignKey(Student, on_delete=models.CASCADE(), blank=False)


