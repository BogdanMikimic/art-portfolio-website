from django import forms
from .models import ReceivedEmails

class MyContactForm(forms.ModelForm):
    class Meta():
        model = ReceivedEmails
        fields = ['first_name', 'last_name', 'email', 'question']
        widgets = {
          'first_name': forms.TextInput(attrs={'class':'input_text_form'}),
          'last_name': forms.TextInput(attrs={'class':'input_text_form'}),
          'email': forms.TextInput(attrs={'class':'input_text_form'}),
          'question': forms.Textarea(attrs={'rows':5, 'cols':25, 'class':'input_text_form'}),
        }
