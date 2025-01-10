from django.forms import ModelForm
from .models import *

class Register_form(ModelForm):

    class Meta:
        model=Reg
        fields=['company_name','company_logo','email','password','youtube_URL',]




class Event_form(ModelForm):

    class Meta:
        model=event
        fields='__all__'

class News_form(ModelForm):

    class Meta:
        model=news
        fields='__all__'




