from django.shortcuts import get_object_or_404, render, redirect
from .forms import UserForm,FilterForm
from databaseprojet.models import Speciality, Roles, User
import random, csv
from django.contrib import messages
from django.template.defaultfilters import slugify

def admin(request):
    return render(request, 'admin.html')

def main(request):
    roles = Roles.objects.all()
    specialities = Speciality.objects.all()
    users = User.objects.all()  
    if request.method == 'POST':
        form = FilterForm(request.POST, request.FILES)
        
        if form.is_valid():
            
            selected_years = request.POST.getlist('year')
            selected_lessons = request.POST.getlist('lesson')
            selected_specialities = request.POST.getlist('cursus')
            selected_identifications = request.POST.getlist('identification')
            users = User.objects.all()

            if selected_years:
                users = users.filter(year__in=selected_years)
                
            if selected_lessons:
                users = users.filter(lesson__id=selected_lessons)
            if selected_specialities:
                users = users.filter(speciality_id=selected_specialities)
            if selected_identifications:
                if '1' in selected_identifications:
                    print("select 1")
                if '2' in selected_identifications:
                    print("select 2")
            if not selected_years and not selected_lessons and not selected_specialities and not selected_identifications:
                print("rien")
            form = UserForm()
            print(users)
            return render(request, 'main.html', {
        'form': form,
        'roles': roles,
        'specialities': specialities,
        'users': users
    })

    else:
        form = FilterForm()
    return render(request, 'main.html', {
        'form': form,
        'roles': roles,
        'specialities': specialities,
        'users': users
    })
    

def tableau_list(request):
    first_name = request.GET.get('first_name', '')
    last_name = request.GET.get('last_name', '')
    role_id = request.GET.get('roles', '')
    speciality_id = request.GET.get('speciality_id', '')
    year = request.GET.get('year', '')
    
    users = User.objects.all()
    
    selected_filters = []
    if first_name:
        users = users.filter(first_name__icontains=first_name)
        selected_filters.append('first_name')
    if last_name:
        users = users.filter(last_name__icontains=last_name)
        selected_filters.append('last_name')
    if role_id:
        users = users.filter(roles__id=role_id)
        selected_filters.append('roles')
    if speciality_id:
        users = users.filter(speciality_id=speciality_id)
        selected_filters.append('speciality_id')
    if year:
        users = users.filter(year=year)
        selected_filters.append('year')
    
    # Get all roles and specialities for the filters
    roles = Roles.objects.all()
    specialities = Speciality.objects.all()
    
    context = {
        'users': users,
        'roles': roles,
        'specialities': specialities,
        'selected_filters': selected_filters,
    }
    return render(request, 'main.html', context)

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
        print(form.errors)
        if form.is_valid():
            
            user = form.save(commit=False)
            user.student_id = generate_student_id()
            # Generate email address using first name and last name
            email = f"{slugify(user.first_name)}.{slugify(user.last_name)}@uha.fr"
            user.email = email
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
            
            messages.success(request, 'User has been created successfully.')
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
    return render(request, 'createuser.html', {'form': form, 'roles': roles, 'specialities': specialities, 'users': users})

def edituser(request, user_id):
   return render(request, 'index.html')
    # return render(request, 'admin.html', {'user': user})

def deleteuser(request, user_id):
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
            # Decode the file and split lines for the CSV reader
            decoded_file = csv_file.read().decode('latin-1').splitlines()
            reader = csv.reader(decoded_file)

            # Extract the header
            header = next(reader)
            header = header[0].split(',')  # Split header into individual columns
            print(header)  # Debugging header

            for row in reader:
                row = row[0].split(',')  # Split row into individual columns
                print(row)  # Debugging row

                # Create a dictionary to map column names to values
                row_data = dict(zip(header, row))

                # Extract data from the CSV row
                first_name = row_data['first_name'].strip()
                last_name = row_data['last_name'].strip()
                role_name = row_data['roles'].strip()
                date_of_birth = row_data['date_of_birth'].strip()
                speciality_name = row_data['speciality_id'].strip()
                email = row_data['email'].strip()
                password = row_data['password'].strip()
                year = row_data['year'].strip()
                student_id = generate_student_id()

                # Debugging print statements to check values
                print(f"first_name: {first_name}, last_name: {last_name}, role_name: {role_name}, date_of_birth: {date_of_birth}, speciality_name: {speciality_name}, email: {email}, password: {password}, year: {year}")

                # Retrieve role and speciality objects
                try:
                    role = Roles.objects.get(name=role_name)
                except Roles.DoesNotExist:
                    messages.error(request, f'Role "{role_name}" does not exist.')
                    return redirect('importusers')

                try:
                    speciality = Speciality.objects.get(name=speciality_name)
                except Speciality.DoesNotExist:
                    messages.error(request, f'Speciality "{speciality_name}" does not exist.')
                    return redirect('importusers')

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
                user.save()

            messages.success(request, 'Users have been imported successfully.')
            return redirect('userslist')

        except UnicodeDecodeError:
            messages.error(request, 'Error decoding file. Please make sure the file is encoded in Latin-1.')
        except Exception as e:
            messages.error(request, f'An error occurred while importing users: {e}')

    roles = Roles.objects.all()
    specialities = Speciality.objects.all()
    users = User.objects.all()
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
