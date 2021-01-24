from django import forms 
from .models import *
  
class ImagesForm(forms.ModelForm): 
    class Meta: 
        model = Images 
        fields = ['city', 'country', 'imageUploaded'] 

class SignupForm(forms.ModelForm): 
    class Meta: 
        model = User 
        fields = ['username', 'password', 'first_name', 'last_name'] 