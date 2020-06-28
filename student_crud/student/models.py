from django.db import models


# Create your models here.

class Subject(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title


class Student(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    enrollment = models.PositiveIntegerField()
    subjects = models.ForeignKey(Subject, on_delete=models.CASCADE)
    emailId = models.EmailField(max_length=50)

    def __str__(self):
        return self.firstName+" "+self.lastName
