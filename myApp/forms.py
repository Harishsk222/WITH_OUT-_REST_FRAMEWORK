from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    def clean_marks(self):
        m=self.cleaned_data['marks']
        if m<35:
            raise forms.ValidationError("marks is under 35")
        return m 
    class Meta:
        model = Student
        fields = "__all__"
