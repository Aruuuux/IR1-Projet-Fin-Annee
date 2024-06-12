# module/forms.py

from django import forms
from databaseprojet.models import *

class ModuleForm(forms.ModelForm):
    YEAR_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
    ]

    year = forms.ChoiceField(choices=YEAR_CHOICES, required=True)

    class Meta:
        model = Module
        fields = ['speciality_id', 'name', 'year']
        

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'Number_of_credits', 'Year', 'coefficient', 'semester',  'teacher_id']
    
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['teacher_id'].queryset = User.objects.filter(roles='Teacher')
        
class AbsenceForm(forms.ModelForm):
    class Meta:
        model = Absence
        fields = ['date']

    def __init__(self, *args, **kwargs):
        super(AbsenceForm, self).__init__(*args, **kwargs)
        
class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = [ 'student_score']
        widgets = {
            'student_score': forms.NumberInput(attrs={'type': 'range', 'step': 0.1, 'min': 0, 'max': 20}),
        }