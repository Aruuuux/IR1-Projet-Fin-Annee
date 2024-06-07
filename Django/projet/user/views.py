from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import login, authenticate
from databaseprojet.models import Speciality, Roles, User
import random
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.urls import reverse_lazy
from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeView,
                                       PasswordChangeDoneView,
                                       PasswordResetView,
                                       PasswordResetDoneView,
                                       PasswordResetConfirmView,
                                       PasswordResetCompleteView)

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

def emailsent(request):
    return render(request, 'emailsent.html')

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

class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    success_url = reverse_lazy('password_reset_done')
    email_template_name = 'registration/password_reset_email.html'

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'



User = get_user_model()

def password_reset_confirm(request, uidb64=None, token=None):
    assert uidb64 is not None and token is not None  # Vérifiez que les deux paramètres sont présents
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        # Le lien est valide, vous pouvez permettre à l'utilisateur de changer son mot de passe
        return render(request, 'registration/password_reset_confirm.html', {'validlink': True})
    else:
        # Le lien n'est pas valide
        return render(request, 'registration/password_reset_confirm.html', {'validlink': False})

    

def E404(request, exception=None):
    return render(request, '404.html', status=404)

def E500(request):
    return render(request, '500.html', status=500)

def E403(request, exception=None):
    return render(request, '403.html', status=403)

def E400(request, exception=None):
    return render(request, '400.html', status=400)