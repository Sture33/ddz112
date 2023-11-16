from django.shortcuts import render

from app11.models import Student


def student_list(request):
    context = {'student_list': Student.objects.all()}
    return render(request, 'student_list.html', context)

def student_update(request, pk):
    student = Student.objects.get(pk=pk)
    context = {'instruments': Student.instruments, 'grades': [(str(i), str(i)) for i in range(1, 13)], 'student':student, 'script':'function(){window.location.href = "127.0.0.1:8000/"}'}
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.surname = request.POST.get('surname')
        student.age = request.POST.get('age')
        student.course = request.POST.get('course')
        student.music_instrument = request.POST.get('music_instrument')
        student.grade = request.POST.get('grade')
        student.paid = request.POST.get('paid', False)

        student.save()

    return render(request, 'student_update.html',context)

def student_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        age = request.POST.get('age')
        course = request.POST.get('course')
        music_instrument = request.POST.get('music_instrument')
        grade = request.POST.get('grade')
        paid = request.POST.get('paid', False)

        student = Student(
            name=name,
            surname=surname,
            age=age,
            course=course,
            music_instrument=music_instrument,
            grade=grade,
            paid=paid
        )
        student.save()

    return render(request, 'student_create.html',context={'instruments':Student.instruments,'grades':[(str(i),str(i)) for i in range(1,13)]})

def student_detail(request, pk):
    context = {'student': Student.objects.get(pk=pk)}
    return render(request, 'student_detail.html', context)
