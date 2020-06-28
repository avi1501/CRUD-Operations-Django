from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['firstName', 'lastName', 'enrollment', 'emailId', 'subjects' ]
        labels = {
            'First Name': 'firstName',
            'Last Name': 'lastName',
            'Enrollment No': 'enrollment',
            'Email Id': 'emailId',
            'Subject': 'subjects',

        }

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['subjects'].empty_label = "Select"


#
# class Student(models.Model):
#     firstName = models.CharField(max_length=20)
#     lastName = models.CharField(max_length=20)
#     enrollment = models.IntegerField()
#     subjects = models.ForeignKey(Subject, on_delete=models.CASCADE)
#     emailId = models.EmailField(max_length=50)
#
