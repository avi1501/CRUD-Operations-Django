from django.shortcuts import render, redirect

from .forms import StudentForm
from .models import Student


# Create your views here.

def student(request, sid=0):
    if request.method == 'POST':
        if sid == 0:
            form = StudentForm(request.POST)
        else:
            stu = Student.objects.get(id=sid)
            form = StudentForm(request.POST, instance=stu)
        if form.is_valid():
            form.save()
        return redirect('/student/list/')
    else:
        if sid == 0:
            form = StudentForm()
        else:
            stu = Student.objects.get(id=sid)
            form = StudentForm(instance=stu)
    template = 'student/home.html'
    context = {
        'title': 'homepage',
        'form': form
    }
    return render(request, template, context)


def all_student(request):
    student_data = Student.objects.all()
    template = 'student/list.html'
    context = {
        'title': 'All students',
        'all_students': student_data
    }
    return render(request, template, context)


def delete(request, sid):
    data=Student.objects.get(id=sid)
    data.delete()
    return redirect('/student/list/')
