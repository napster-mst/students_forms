from django.db import models


# Create your models here.
class Department(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Gender(models.Model):
    sex = models.CharField(max_length=10)

    def __str__(self):
        return self.sex


class Student(models.Model):
    first_name = models.CharField(max_length=12, default="")
    last_name = models.CharField(max_length=12, default="")
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
