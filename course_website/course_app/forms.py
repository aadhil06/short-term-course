from django import forms
from .models import *

class ShortTermCourseForm(forms.ModelForm):
    class Meta:
        model = ShortTermCourse
        fields = ['title', 'subtitle', 'description', 'amount', 'textarea', 'status']
