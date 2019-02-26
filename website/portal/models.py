from django.db import models
from django.contrib.auth.models import User


class Personal(models.Model):
    name = models.CharField(max_length=250)
    dept = models.CharField(max_length=25)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    regno = models.BigIntegerField(primary_key=True)

    def __str__(self):
        return self.name + ' - ' + self.dept + ' - ' + str(self.regno)
