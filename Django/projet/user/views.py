from django.shortcuts import render, redirect
from .forms import UserForm
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

def E404(request, exception=None):
    return render(request, '404.html', status=404)

def E500(request):
    return render(request, '500.html', status=500)

def E403(request, exception=None):
    return render(request, '403.html', status=403)

def E400(request, exception=None):
    return render(request, '400.html', status=400)