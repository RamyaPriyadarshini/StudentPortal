from django.db import models
from django.contrib.auth.models import User


class Personal(models.Model):
    Name = models.CharField(max_length=250)
    Course = models.CharField(max_length=25)
    Department = models.CharField(max_length=25)
    Batch = models.IntegerField()
    RegNo = models.BigIntegerField(primary_key=True)
    Section = models.CharField(max_length=25)
    Gender = models.CharField(max_length=7)
    BloodGroup = models.CharField(max_length=7)
    StudentMobNo = models.BigIntegerField()
    StudentMailID = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    DOB = models.DateField(auto_now=False, auto_now_add=False)
    Address = models.CharField(max_length=500)

    def __str__(self):
        return self.Name + ' - ' + self.Department + ' - ' + str(self.RegNo)


class Leave(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    leavType = models.CharField(max_length=50)
