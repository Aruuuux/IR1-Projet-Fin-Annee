from django.shortcuts import render, redirect
from .forms import UserForm
from databaseprojet.models import Speciality, Roles, User, Course
import random
from django.contrib import messages
from .grade import AddGradeForm

def admin(request):
    return render(request, 'admin.html')

def main(request):
    return render(request, 'main.html')

def indexview(request):
    return render(request, 'index.html')

def psswrdforgot(request):
    return render(request, 'psswrdforgot.html')

def createuser(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.student_id = generate_student_id()
            user.save()
            print(f"First Name: {user.first_name}")
            print(f"Last Name: {user.last_name}")
            print(f"Roles: {user.roles}")
            print(f"Date of Birth: {user.date_of_birth}")
            print(f"Speciality: {user.speciality_id}")
            print(f"Photo: {user.photo}")
            print(f"Email: {user.email}")
            print(f"Password: {user.password}")
            print(f"Year: {user.year}")

    form = UserForm()
    roles = Roles.objects.all()
    specialities = Speciality.objects.all()
    users = User.objects.all()
    return render(request, 'createuser.html', {'form': form, 'roles': roles, 'specialities': specialities, 'users': users})

def edituser(request, user_id):
   return render(request, 'index.html')
    # return render(request, 'admin.html', {'user': user})

def deleteuser(request, user_id):
    return render(request, 'index.html')

def generate_student_id():
    while True:
        student_id = random.randint(22300000, 23300000)
        if not User.objects.filter(student_id=student_id).exists():
            return student_id
        


def add_grade(request):
    course_selected = False
    students = User.objects.none()
    
    if request.method == 'POST':
        if 'course_id' in request.POST:
            course_id = request.POST.get('course_id')
            if course_id:
                course = Course.objects.get(course_id=course_id)
                students = User.objects.filter(
                    speciality_id=course.Speciality_id,
                    year=course.Year,
                    roles='Student'
                )
                course_selected = True
                form = AddGradeForm(request.POST)
                form.fields['student_id'].queryset = students
            else:
                form = AddGradeForm()
        else:
            form = AddGradeForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Grade added successfully!')
                return redirect('add_grade')
    else:
        form = AddGradeForm()
    
    return render(request, 'add_grade.html', {
        'form': form,
        'course_selected': course_selected,
        'students': students
    })