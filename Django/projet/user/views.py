from django.shortcuts import render, redirect
from .forms import UserForm
from databaseprojet.models import Speciality, Roles,User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
# Imaginary function to handle an uploaded file.
from .import_data import handle_uploaded_file


def admin(request):
    return render(request, 'admin.html')

def main(request):
    return render(request, 'main.html')

def indexview(request):
    return render(request, 'index.html')

def psswrdforgot(request):
    return render(request, 'psswrdforgot.html')

def BDDviewer(request):
    return render(request, 'BDDviewer.html')

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

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})