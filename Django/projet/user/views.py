from django.shortcuts import get_object_or_404, render, redirect
from .forms import UserForm
from databaseprojet.models import Speciality, Roles, User
import random, csv
from django.contrib import messages
from django.template.defaultfilters import slugify

def indexview(request):
    return render(request, 'index.html')

def psswrdforgot(request):
    return render(request, 'psswrdforgot.html')

def createuser(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            user = form.save(commit=False)
            user.student_id = generate_student_id()
            # Generate email address using first name and last name
            email = f"{slugify(user.first_name)}.{slugify(user.last_name)}@uha.fr"
            user.email = email
            user.save()
            messages.success(request, 'User has been created successfully.')
            return redirect('userslist')
    else:
        form = UserForm()
    roles = Roles.objects.all()
    specialities = Speciality.objects.all()
    return render(request, 'createuser.html', {'form': form, 'roles': roles, 'specialities': specialities})
    
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

def importusers(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Please upload a CSV file.')
            return redirect('importusers')

        try:
            decoded_file = csv_file.read().decode('latin-1').splitlines()
            reader = csv.DictReader(decoded_file)
            for row in reader:
                print(row)
                # Extract data from the CSV row
                first_name = row.get('first_name')
                last_name = row.get('last_name')
                role = row.get('roles')
                date_of_birth = row.get('date_of_birth')
                speciality = row.get('speciality_id')
                email = row.get('email')
                password = row.get('password')
                year = row.get('year')
                # role = Roles.objects.get(name=role_name)
                # speciality = Speciality.objects.get(name=speciality_name)

                # Create user instance
                user = User(
                    first_name=first_name,
                    last_name=last_name,
                    roles=role,
                    date_of_birth=date_of_birth,
                    speciality_id=speciality,
                    email=email,
                    password=password,
                    year=year
                )
                # Save user instance
                # print(user)
                # user.save()

            messages.success(request, 'Users have been imported successfully.')
            return redirect('userslist')

        except Exception as e:
            messages.error(request, f'An error occurred while importing users: {e}')

    return render(request, 'userslist.html')

def generate_student_id():
    while True:
        student_id = random.randint(22300000, 23300000)
        if not User.objects.filter(student_id=student_id).exists():
            return student_id