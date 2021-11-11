from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'school', 'is_active', 'price', 'duration', 'max_students']
