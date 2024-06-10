from django import forms
from databaseprojet.models import Score, Course, User

class AddGradeForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['student_id', 'course_id', 'student_score']
        widgets = {
            'student_id': forms.Select(attrs={'class': 'form-control'}),
            'course_id': forms.Select(attrs={'class': 'form-control'}),
            'student_score': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(AddGradeForm, self).__init__(*args, **kwargs)
        student_role_name = 'Student'
        self.fields['student_id'].queryset = User.objects.filter(roles=student_role_name)
        self.fields['course_id'].queryset = Course.objects.all()
