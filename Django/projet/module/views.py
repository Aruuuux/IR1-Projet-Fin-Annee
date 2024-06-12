# module/views.py

from django.shortcuts import get_object_or_404, render, redirect
from .forms import *
from databaseprojet.models import *
from django.contrib import messages

def create_module(request):
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            module = form.save()
            messages.success(request, 'Module has been created successfully.')
            return redirect('module:create_module')
        else:
            messages.error(request, 'There were errors in the form. Please correct them and try again.')
    else:
        form = ModuleForm()
    
    modules = Module.objects.all()  # Retrieve all modules from the database
    return render(request, 'create_module.html', {'form': form, 'modules': modules})

def edit_module(request, module_id):
    module = get_object_or_404(Module, pk=module_id)
    modules = Module.objects.all()  # Fetch all modules
    if request.method == 'POST':
        form = ModuleForm(request.POST, instance=module)
        if form.is_valid():
            form.save()
            messages.success(request, 'Module has been updated successfully.')
            return redirect('module:create_module')  # Redirect to create_module
        else:
            messages.error(request, 'There were errors in the form. Please correct them and try again.')
    else:
        form = ModuleForm(instance=module)
        # Fill the form with existing module data
        form.fields['name'].initial = module.name
        form.fields['year'].initial = module.year
        form.fields['speciality_id'].initial = module.speciality_id
    return render(request, 'create_module.html', {'form': form, 'modules': modules})  # Render create_module template with table data



def delete_module(request, module_id):
    modules = Module.objects.all()
    module = get_object_or_404(Module, pk=module_id)
    module.delete()
    form = ModuleForm()
    messages.success(request, 'Module has been deleted successfully.')
    return render(request, 'create_module.html', {'modules': modules, 'form': form})

    

def create_course(request, module_id):
    module = get_object_or_404(Module, id=module_id)

    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.module_id = module
            course.Speciality_id = module.speciality_id.id  # Set speciality_id from module
            course.save()
    else:
        form = CourseForm()

    teachers = User.objects.filter(roles='Teacher')
    courses = Course.objects.filter(module_id=module)
    return render(request, 'courses.html', {'form': form, 'module': module, 'courses': courses, 'teachers': teachers})

def manage_course(request, course_id):
    course = get_object_or_404(Course, course_id=course_id)
    absences = Absence.objects.filter(course_id=course)
    scores = Score.objects.filter(course_id=course)
    students = User.objects.filter(roles='Student')

    if request.method == "POST":
        absence_form = AbsenceForm(request.POST)
        score_form = ScoreForm(request.POST)
        student_id = get_object_or_404(User, id=request.POST.get('student_id'))
        if absence_form.is_valid():
            absence = absence_form.save(commit=False)
            absence.course_id = course
            absence.student_id = student_id
            absence.save()
            return redirect('module:manage_course', course_id=course_id)
        if score_form.is_valid():
            score = score_form.save(commit=False)
            score.course_id = course
            score.student_id = student_id
            score.save()
            return redirect('module:manage_course', course_id=course_id) 
    else:
        absence_form = AbsenceForm()
        score_form = ScoreForm()

    return render(request, 'manage_course.html', {
        'course': course,
        'absences': absences,
        'scores':scores,
        'absence_form': absence_form,
        'score_form': score_form,
        'students':students
    })
    
    
def editabsence(request, pk):
    absence = get_object_or_404(Absence, pk=pk)
    course = get_object_or_404(Course, pk=absence.course_id.course_id)
    absences = Absence.objects.filter(course_id=course)
    scores = Score.objects.filter(course_id=course)
    students = User.objects.filter(roles='Student')

    if request.method == 'POST':
        form = AbsenceForm(request.POST, instance=absence)
        if form.is_valid():
            form.save()
            messages.success(request, 'Absence updated successfully.')
            return redirect('module:manage_course', course_id=course.course_id)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = AbsenceForm(instance=absence)

    return render(request, 'manage_course.html', {
        'course': course,
        'absences': absences,
        'scores': scores,
        'form': form,
        'students': students,
        'absence':absence
    })

def deleteabsence(request, absence_id):
    absence = get_object_or_404(Absence, pk=absence_id)
    absence.delete()
    messages.success(request, 'Absence deleted successfully.')
    return redirect('module:manage_course', course_id=absence.course_id.course_id) 



def editscore(request, pk):
    score = get_object_or_404(Score, pk=pk)
    course = get_object_or_404(Course, pk=score.course_id.course_id)
    absences = Absence.objects.filter(course_id=course)
    scores = Score.objects.filter(course_id=course)
    students = User.objects.filter(roles='Student')
    if request.method == 'POST':
        form = ScoreForm(request.POST, instance=score)
        if form.is_valid():
            form.save()
            messages.success(request, 'Score updated successfully.')
            return redirect('module:manage_course', course_id=score.course_id.course_id)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ScoreForm(instance=score)
    return render(request, 'manage_course.html', {
        'course': course,
        'absences': absences,
        'scores': scores,
        'form': form,
        'students': students,
        'score':score
    })

def deletescore(request, score_id):
    score = get_object_or_404(Score, pk=score_id)
    score.delete()
    messages.success(request, 'Score deleted successfully.')
    return redirect('module:manage_course', course_id=score.course_id.course_id)


def editcourse(request, course_id):
    # Retrieve the course object
    course = get_object_or_404(Course, course_id=course_id)
    
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('module:create_course',course.module_id.id)  # Adjust this URL as needed
    else:
        form = CourseForm(instance=course)
    teachers = User.objects.filter(roles='Teacher')
    courses = Course.objects.filter(module_id=course.module_id)
    return render(request, 'courses.html', {'form': form, 'course': course, 'teachers':teachers,'courses':courses})


def deletecourse(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    module = course.module_id
    course.delete()
    messages.success(request, 'Score deleted successfully.')
    return redirect('module:create_course',module.id)  # Replace 'module_view_name' with the name of the view you want to redirect to
