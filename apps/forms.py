from django import forms
from .models import *


class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = '__all__'


class MyCapsForm(forms.ModelForm):
    class Meta:
        model = MyCaps
        fields = ('name','color')
        CHOICES = [('select1', 'select 1'),
                   ('select2', 'select 2')]

        MY_CHOICES = (
            ('opt0', 'Option zero'),
            ('opt1', 'Option one'),
        )
        myfield = forms.ChoiceField(widget=forms.RadioSelect, choices=MY_CHOICES)


        # def __init__(self, *args, **kwargs):
        #     super(ColorForm, self).__init__(*args, **kwargs)
        #     self.fields['type'].widget = forms.RadioSelect