from django.shortcuts import render
from . models import Student, Course, Trainer


def course_list(request):
    courses = Course.objects.all()
    context = {
        'courses' : courses,
    }
    return render(request, 'course_list.html',context)


def trainer_list(request):
    trainers = Trainer.objects.all()
    context = {
        'trainers': trainers,
    }
    return render(request, 'trainer_list.html',context)


def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'student_list.html', context)
