from django.db import models
import uuid
# Create your models here.
class Student(models.Model):
    id         = models.UUIDField(default=uuid.uuid4, unique= True, primary_key= True, editable= False)
    firstName  = models.CharField(max_length= 50, null = False, blank= False)
    lastName   = models.CharField(max_length= 50, null = False, blank= False)
