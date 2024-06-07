from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import login, authenticate
from databaseprojet.models import Speciality, Roles, User
import random

def admin(request):
    return render(request, 'admin.html')

def main(request):
    return render(request, 'main.html')

def indexview(request):
    return render(request, 'index.html')

def psswrdforgot(request):
    return render(request, 'psswrdforgot.html')

def profile(request):
    return render(request, 'user/profile.html')

def parametre(request):
    return render(request, 'user/parametre.html')

def changepsswrd(request):
    return render(request,'changepsswrd.html')

def edt(request):
    return render(request,'edt.html')

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


            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=user.email, password=raw_password)
            login(request, user)
            roles = Roles.objects.all()
            specialities = Speciality.objects.all()
            print(roles)
            return render(request, 'createuser.html', {'roles': roles, 'specialities': specialities})
    else:
        form = UserForm()
        roles = Roles.objects.all()
        specialities = Speciality.objects.all()
        print(roles)
        return render(request, 'createuser.html', {'roles': roles, 'specialities': specialities, 'form':form})
    # return render(request, 'createuser.html')
        
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
