from django import forms
from classes.models import Classes


class ClassesForm(forms.ModelForm):

    class Meta:
        model = Classes
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-border'
