from django.db import models
import uuid
# Create your models here.
class Class_room(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    roomName = models.CharField(max_length=50, null=False, blank=False)
    def __str__(self):
        return self.roomName
class Job_id:
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=50, null=False, blank=False)

class Employees:
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    firstName = models.CharField(max_length=50, null=False, blank=False)
    middelName = models.CharField(max_length=50, null=False, blank=False)
    lastName = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    phone = models.IntegerField(null=False, blank=False)
    address = models.CharField(max_length=50, null=False, blank=False)
    sex = models.CharField(max_length=1, null=False, blank=False)
    registrationDate = models.DateField(auto_now_add= True)
    job_id = models.ForeignKey(Job_id)

class Family_type(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    typeName = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.typeName
class Family(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    firstName = models.CharField(max_length=50, null=False, blank=False)
    middelName = models.CharField(max_length=50, null=False, blank=False)
    lastName = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    phone = models.IntegerField(null=False, blank=False)
    sex = models.CharField(max_length=1, null=False, blank=False)
    family_type_id = models.ForeignKey(Family_type, on_delete= models.SET_NULL,null=True)
    def __str__(self):
        return self.firstName
class Student(models.Model):
    id         = models.UUIDField(default=uuid.uuid4, unique= True, primary_key= True, editable= False)
    firstName  = models.CharField(max_length= 50, null = False, blank= False)
    middelName = models.CharField(max_length= 50, null = False, blank= False)
    lastName   = models.CharField(max_length= 50, null = False, blank= False)
    email      = models.EmailField(max_length= 100, null = False, blank= False)
    phone      = models.IntegerField(null=False, blank=False)
    age        = models.IntegerField(null = False, blank= False)
    sex        = models.CharField(max_length=1, null = False, blank= False)
    class_room_id = models.ForeignKey(Class_room, on_delete=models.SET_NULL, null=True)
    family_id = models.ForeignKey(Family, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.firstName
class Subject(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    subjectName = models.CharField(max_length=50, null=False, blank=False)
    def __str__(self):
        return self.subjectName

class Teacher(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    employees_id = models.ForeignKey(Employees, on_delete= models.SET_NULL, null=True)
    def __str__(self):
        return self.firstName
class Class_subject(models.Model):
    classRoomId = models.ForeignKey(Class_room, on_delete=models.SET_NULL, null=True, blank=False)
    subjectId = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=False)
    def __str__(self):
        return self.classRoomId.__str__() + ' ' + self.subjectId.__str__()
class Teacher_subject(models.Model):
    teacherId = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=False)
    subjectId = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=False)
    def __str__(self):
        return self.teacherId.__str__() + ' ' + self.subjectId.__str__()


