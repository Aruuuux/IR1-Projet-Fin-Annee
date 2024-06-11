# user/views.py
from django.shortcuts import get_object_or_404, render, redirect
from .forms import UserForm,FilterForm
from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import views as auth_views
from django.contrib.auth import login, authenticate
from databaseprojet.models import Speciality, Roles, User, Course, Score
from .forms import UserForm, FilterForm

import random, csv
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.template.defaultfilters import slugify
from datetime import datetime
from django.utils import formats
from django.contrib.auth import get_user_model
from django.utils.encoding import force_str
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.urls import reverse_lazy
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeView,
                                       PasswordChangeDoneView,
                                       PasswordResetView,
                                       PasswordResetDoneView,
                                       PasswordResetConfirmView,
                                       PasswordResetCompleteView)

def admin(request):
    return render(request, 'user/admin.html')

def main(request):
    roles = User._meta.get_field('roles').choices
    specialities = specialities = Speciality.SPECIALITY_CHOICES
    
    if request.method == 'POST':
        form = FilterForm(request.POST, request.FILES)
        
        if form.is_valid():
            selected_years = request.POST.getlist('year')
            selected_lessons = request.POST.getlist('lesson')
            selected_specialities = request.POST.getlist('cursus')
            selected_identifications = request.POST.getlist('identification')
            print("SELECTED : ",selected_years,selected_lessons,selected_specialities,selected_identifications)
            users = User.objects.all()  # Start with all users
            
            # Apply filters based on form data
            if selected_years:
                users = users.filter(year__in=selected_years)
                
            if selected_lessons:
                users = users.filter(lesson__id__in=selected_lessons)
                
            if selected_specialities:
                users = users.filter(speciality_id__in=selected_specialities)
                
            if selected_years or selected_lessons or selected_specialities or selected_identifications:
                
                selected_filters = []
                if selected_identifications:
                    if "1" in selected_identifications:
                        selected_filters.append('student_id')
                    if "2" in selected_identifications:
                        selected_filters.append('last_name')
                        selected_filters.append('first_name')
                        #add photo    
                if selected_years:
                    selected_filters.append('year')
                if selected_specialities:
                    selected_filters.append('speciality_id')
                if selected_lessons:
                    selected_filters.append('lesson')
                
                
                    
            else:
                
                selected_filters = ['year', 'lesson', 'speciality_id', 'last_name', 'first_name']
            
            form = FilterForm()
            context = {
                'form': form,
                'specialities': specialities,
                'users': users,
                'selected_filters': selected_filters
            }
            print(context)
            return render(request, 'user/main.html', context)

    else:
        form = FilterForm()
    
    # If it's a GET request or the form is invalid, display all users and all filters
    users = User.objects.all()
    selected_filters = ['year', 'lesson', 'speciality_id','last_name','first_name' ]
    
    # Render the template with initial context
    return render(request, 'user/main.html', {
        'form': form,
        'specialities': specialities,
        'users': users,
        'selected_filters': selected_filters
    })

    


def indexview(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email)
            if password == user.password:
                messages.success(request, 'Successfully logged in.')
                return redirect('user:userslist')
            else:
                messages.error(request, 'Invalid email or password')
        except User.DoesNotExist:
            messages.error(request, 'Invalid email or password')
    
    return render(request, 'user/index.html')

#######
def psswrdforgot(request):
    return render(request, 'psswrdforgot.html')

def psswrdresetdone(request):
    return render(request, 'password_reset_done.html')


def psswrdresetcomplete(request):
    print("PASSWORD RESET COMPLETE")
    return render(request, 'password_reset_complete.html')
#############

def profile(request):
    return render(request, 'user/profile.html')

def parametre(request):
    return render(request, 'user/parametre.html')

def emailsent(request):
    return render(request, 'user/emailsent.html')

def changepsswrd(request):
    return render(request,'user/changepsswrd.html')

def edt(request):
    return render(request,'user/edt.html')

def createuser(request):
    print("import user launch")
    print(request.FILES)
    if request.method == 'POST' and request.FILES.get('csv_file'):
        print("premier if")
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            print("error in csv")
            messages.error(request, 'Please upload a CSV file.')
            return redirect('createuser')

        try:
            
            decoded_file = csv_file.read().decode('latin-1').splitlines()
            reader = csv.reader(decoded_file)

            header = next(reader)
            header = header[0].split(',')  # Split header into individual columns
            print(header)  # Debugging header

            for row in reader:
                row = row[0].split(',')  # Split row into individual columns
                row_data = dict(zip(header, row))

                first_name = row_data['first_name'].strip()
                last_name = row_data['last_name'].strip()
                role_name = row_data['roles'].strip()
                date_of_birth = row_data['date_of_birth'].strip()
                speciality_name = row_data['speciality_id'].strip()
                email = row_data['email'].strip()
                password = row_data['password'].strip()
                year = row_data['year'].strip()
                student_id = generate_student_id()
                try:
                    
                    role = Roles.objects.get(name=role_name)
                except Roles.DoesNotExist:
                    messages.error(request, f'Role "{role_name}" does not exist.')
                    print("role 'nexist pas")
                    return redirect('createuser')

                try:
                    speciality = Speciality.objects.get(name=speciality_name)
                except Speciality.DoesNotExist:
                    messages.error(request, f'Speciality "{speciality_name}" does not exist.')
                    print("spe n'existe pas")
                    return redirect('createuser')

                # Create user instance
                print("create user")
                user = User(
                    first_name=first_name,
                    last_name=last_name,
                    roles=role,
                    date_of_birth=date_of_birth,
                    speciality_id=speciality,
                    email=email,
                    password=password,
                    student_id=student_id,
                    year=year
                )
                # Save user instance
                try:
                    user.save()
                    messages.success(request, 'Users have been imported successfully.')
                    print("good")
                    return redirect('createuser')
                except:
                    messages.error(request, 'There were errors while updating the user')
                    print("error while update")
                    return redirect('createuser')
        except UnicodeDecodeError:
            messages.error(request, 'Error decoding file. Please make sure the file is encoded in Latin-1.')
            print("error decode")
        except Exception as e:
            messages.error(request, f'An error occurred while importing users: {e}')
            print("error in user import")
    elif request.method == 'POST' and not request.FILES.get('csv_file'):
        form = UserForm(request.POST, request.FILES)
        print("err",form.errors)
        if form.is_valid():
            
            user = form.save(commit=False)
            user.student_id = generate_student_id()
            
            # Generate email address using first name and last name
            email = f"{slugify(user.first_name)}.{slugify(user.last_name)}@uha.fr"
            user.email = email
            
            # Check password length
            password = form.cleaned_data.get('password')
            if len(password) < 8:
                messages.error(request, 'Password must be at least 8 characters long.')
                return redirect('user:createuser')
            
            # Check if age is greater than 18
            date_of_birth = form.cleaned_data.get('date_of_birth')
            if date_of_birth:
                age = datetime.now().year - date_of_birth.year - ((datetime.now().month, datetime.now().day) < (date_of_birth.month, date_of_birth.day))
                if age < 18:
                    messages.error(request, 'User must be at least 18 years old.')
                    return redirect('user:createuser')
            user.password = password
            try:
                user.save()
                messages.success(request, 'User has been created successfully.')
                return redirect('user:createuser')
            except:
                messages.error(request, 'There were errors while creating the user')
            
        else:
            messages.error(request, 'There were errors in the form. Please correct them and try again.')
    else:
        form = UserForm()
    roles = User._meta.get_field('roles').choices
    specialities = specialities = Speciality.objects.all()

    return render(request, 'user/createuser.html', {'form': form, 'roles': roles, 'specialities': specialities, 'messages': messages.get_messages(request)})



def edituser(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        print(form.errors)
        if form.is_valid():
            user = form.save(commit=False)
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = f"{slugify(first_name)}.{slugify(last_name)}@uha.fr"
            user.email = email
            
            # Check password length
            password = form.cleaned_data.get('password')
            if password and len(password) < 8:
                messages.error(request, 'Password must be at least 8 characters long.')
                return redirect('user:edituser', user_id = user_id)
            
            # Check if age is greater than 18
            date_of_birth = form.cleaned_data.get('date_of_birth')
            if date_of_birth:
                age = datetime.now().year - date_of_birth.year - ((datetime.now().month, datetime.now().day) < (date_of_birth.month, date_of_birth.day))
                if age < 18:
                    messages.error(request, 'User must be at least 18 years old.')
                    return redirect('user:edituser', user_id = user_id)

            try:
                user.save()
                messages.success(request, 'User has been updated successfully.')
                return redirect('user:userslist')
            except:
                messages.error(request, 'There were errors while updating the user')
    else:
        form = UserForm(instance=user)
        initial_values = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'roles': user.roles,
            'date_of_birth': formats.date_format(user.date_of_birth, "Y-m-d"),
            'speciality_id': user.speciality_id,
            'photo': user.photo,
            'email': user.email,
            'password': user.password,
            'year': user.year
        }
        form = UserForm(instance=user, initial=initial_values)
    roles = User._meta.get_field('roles').choices
    specialities = specialities = Speciality.SPECIALITY_CHOICES
    users = User.objects.all()
    return render(request, 'user/createuser.html', {'form': form, 'roles': roles, 'specialities': specialities, 'users': users})


def deleteuser(request, user_id):
    context = {
        'form': form,
        'user': user,
        'users': users,
        'roles': roles,
        'specialities': specialities,
    }
    return render(request, 'user/createuser.html', context)


   
def deleteuser(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.success(request, 'User has been deleted successfully.')
    return redirect('user:userslist')


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
    return render(request, 'user/userslist.html', context)

def importusers(request):
    print("import user launch")
    print(request)
    if request.method == 'POST' and request.FILES.get('csv_file'):
        print("premier if")
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            print("error in csv")
            messages.error(request, 'Please upload a CSV file.')
            return redirect('user:importusers')

        try:
            decoded_file = csv_file.read().decode('latin-1').splitlines()
            reader = csv.reader(decoded_file)

            header = next(reader)
            header = header[0].split(',')  # Split header into individual columns
            print(header)  # Debugging header

            for row in reader:
                row = row[0].split(',')  # Split row into individual columns
                row_data = dict(zip(header, row))

                first_name = row_data['first_name'].strip()
                last_name = row_data['last_name'].strip()
                role_name = row_data['roles'].strip()
                date_of_birth = row_data['date_of_birth'].strip()
                speciality_name = row_data['speciality_id'].strip()
                email = row_data['email'].strip()
                password = row_data['password'].strip()
                year = row_data['year'].strip()
                student_id = generate_student_id()
                try:
                    role = Roles.objects.get(name=role_name)
                except Roles.DoesNotExist:
                    messages.error(request, f'Role "{role_name}" does not exist.')
                    return redirect('user:importusers')

                try:
                    speciality = Speciality.objects.get(name=speciality_name)
                except Speciality.DoesNotExist:
                    messages.error(request, f'Speciality "{speciality_name}" does not exist.')
                    return redirect('user:importusers')

                # Create user instance
                user = User(
                    first_name=first_name,
                    last_name=last_name,
                    roles=role,
                    date_of_birth=date_of_birth,
                    speciality_id=speciality,
                    email=email,
                    password=password,
                    student_id=student_id,
                    year=year
                )
                # Save user instance
                try:
                    user.save()
                    messages.success(request, 'Users have been imported successfully.')
                    return redirect('user:userslist')
                except:
                    messages.error(request, 'There were errors while updating the user')
                    return redirect('user:userslist')
        except UnicodeDecodeError:
            messages.error(request, 'Error decoding file. Please make sure the file is encoded in Latin-1.')
            print("error decode")
        except Exception as e:
            messages.error(request, f'An error occurred while importing users: {e}')
            print("error in user import")

    roles = Roles.objects.all()
    specialities = Speciality.objects.all()
    users = User.objects.all()
    context = {
        'users': users,
        'roles': roles,
        'specialities': specialities,
    }
    return render(request, 'user/userslist.html', context)

def generate_student_id():
    while True:
        student_id = random.randint(22300000, 23300000)
        if not User.objects.filter(student_id=student_id).exists():
            return student_id



class CustomPasswordResetView(PasswordResetView):
    print("password reset done page")
    template_name = 'registration/password_reset_form.html'
    success_url = reverse_lazy('password_reset/done')
    email_template_name = 'registration/password_reset_email.html'

#np
class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

#nop
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'user/psswrdforgot.html'
    success_url = reverse_lazy('password_reset_complete')

#nop
class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'

User = get_user_model()

def password_reset_confirm(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                return redirect('password_reset_complete')
        else:
            form = SetPasswordForm(user)
        return render(request, 'password_reset_confirm.html', {'form': form, 'validlink': True})
    else:
        return render(request, 'password_reset_confirm.html', {'validlink': False})


def error_400(request, exception=None):
    return render(request, 'user/400.html', status=400)

def error_403(request, exception=None):
    return render(request, 'user/403.html', status=403)
def error_404(request, exception=None):
    return render(request, 'user/404.html', status=404)

def error_500(request):
    return render(request, 'user/500.html', status=500)




def addgrade(request):
    courses = Course.objects.all()
    users = None
    selected_course = None

    if request.method == 'GET' and 'course_id' in request.GET:
        course_id = request.GET.get('course_id')
        if course_id:
            selected_course = get_object_or_404(Course, course_id=course_id)
            users = User.objects.filter(speciality_id=selected_course.Speciality_id, year=selected_course.Year)

    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        student_id = request.POST.get('student_id')
        student_score = request.POST.get('student_score')
        
        if course_id and student_id and student_score:
            selected_course = get_object_or_404(Course, course_id=course_id)
            student = get_object_or_404(User, id=student_id)
            score = Score(student_id=student, course_id=selected_course, student_score=student_score)
            score.save()
            return redirect('user:addgrade')

    context = {
        'courses': courses,
        'users': users,
        'selected_course': selected_course,
    }
    return render(request, 'addgrade.html', context)
