from django.shortcuts import get_object_or_404, render, redirect
from .forms import UserForm
from databaseprojet.models import Speciality, Roles, User
import random
from django.contrib import messages

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
            messages.success(request, 'User has been created successfully.')
            roles = Roles.objects.all()
            specialities = Speciality.objects.all()
            users = User.objects.all()
            return render(request, 'userslist.html',  {'users': users,'roles': roles,'specialities': specialities})
    form = UserForm()
    roles = Roles.objects.all()
    specialities = Speciality.objects.all()
    return render(request, 'createuser.html', {'form': form, 'roles': roles, 'specialities': specialities,
                                               })
    
def edituser(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User has been edited successfully.')
            roles = Roles.objects.all()
            specialities = Speciality.objects.all()
            users = User.objects.all()
            context = {
                'users': users,
                'roles': roles,
                'specialities': specialities,
             }
            return render(request, 'userslist.html', context)    
    else:
        form = UserForm(instance=user)
        initial_values = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'roles': user.roles,
            'date_of_birth': user.date_of_birth,
            'speciality_id': user.speciality_id,
            'photo': user.photo,
            'email': user.email,
            'password': user.password,
            'year': user.year
        }
        form = UserForm(instance=user, initial=initial_values)
    roles = Roles.objects.all()
    specialities = Speciality.objects.all()
    users = User.objects.all()
    context = {
        'form': form,
        'user': user,
        'users': users,
        'roles': roles,
        'specialities': specialities,
    }
    return render(request, 'createuser.html', context)
   
def deleteuser(request, user_id):
    user = get_object_or_404(User, id=user_id)
    print(user)
    user.delete()
    messages.success(request, 'User has been deleted successfully.')
    return redirect('userslist') 


def userslist(request):
    first_name = request.GET.get('first_name', '')
    last_name = request.GET.get('last_name', '')
    role_id = request.GET.get('roles', '')
    speciality_id = request.GET.get('speciality_id', '')
    year = request.GET.get('year', '')
    users = User.objects.all()
    if first_name:
        users = users.filter(first_name__icontains=first_name)
    if last_name:
        users = users.filter(last_name__icontains=last_name)
    if role_id:
        users = users.filter(roles__id=role_id)
    if speciality_id:
        users = users.filter(speciality_id=speciality_id)
    if year:
        users = users.filter(year=year)
    roles = Roles.objects.all()
    specialities = Speciality.objects.all()
    context = {
        'users': users,
        'roles': roles,
        'specialities': specialities,
    }
    return render(request, 'userslist.html', context)


def generate_student_id():
    while True:
        student_id = random.randint(22300000, 23300000)
        if not User.objects.filter(student_id=student_id).exists():
            return student_id