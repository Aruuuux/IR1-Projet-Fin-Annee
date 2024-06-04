from django.shortcuts import render, redirect
from .forms import UserForm
from databaseprojet.models import Speciality, Roles

def indexview(request):
    return render(request, 'index.html')

def psswrdforgot(request):
    return render(request, 'psswrdforgot.html')


def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
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

