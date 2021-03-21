from django import forms
from .models import Packages, Category


class PackagesForm(forms.ModelForm):

    class Meta:
        model = Packages
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        names = [(c.id, c.get_name()) for c in categories]

        self.fields['category'].choices = names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'
