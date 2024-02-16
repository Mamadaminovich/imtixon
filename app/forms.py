from django.forms import ModelForm
from .models import data

class dataForm(ModelForm):
    class Meta:
        model = data
        fields = '__all__'