from django.shortcuts import render, redirect
from .forms import UserForm
from databaseprojet.models import Speciality, Roles
from django.contrib.auth import login, authenticate

def admin(request):
    return render(request, 'admin.html')

def main(request):
    return render(request, 'main.html')

def indexview(request):
    return render(request, 'index.html')

def psswrdforgot(request):
    return render(request, 'psswrdforgot.html')

def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
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

