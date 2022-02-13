from . models import Task
from django import forms

class avodhaclassforms(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','post','datetime']
