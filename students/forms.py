from django import forms
from students.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'department': 'Department',
            'gender': 'Gender',
            'city': 'City',
            'state': 'State',
            'email': 'E-mail'
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['department'].empty_label = "Select"
        self.fields['gender'].empty_label = "Select"
        self.fields['city'].required = False
        self.fields['state'].required = False
