from django import forms
#from django import ValidationError

from .models import Food

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['title','text','calories']
        style = 'display: block'
        widgets ={
            'title': forms.TextInput(attrs={'style': style}),
            'text': forms.Textarea(attrs={'style': style}),
            'calories': forms.TextInput(attrs={'style': style}),

        }
        labels = {
            'title':'Enter food name ',
            'text': 'Enter description of food ',
            'calories': 'Calorie Count '
        }

    # def clean_title(self):
    #     title= self.cleaned_data['title']
    #     if 'Django' not in title:
    #         raise ValidationError('We only accept food about Django') 
    #     return title  