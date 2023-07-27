from django import forms
#from django import ValidationError

from .models import Food

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['title','text','calories']

    # def clean_title(self):
    #     title= self.cleaned_data['title']
    #     if 'Django' not in title:
    #         raise ValidationError('We only accept food about Django') 
    #     return title  