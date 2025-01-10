from django.forms import ModelForm
from .models import *

class Register_form(ModelForm):

    class Meta:
        model=Reg
        fields='__all__'



class Event_form(ModelForm):

    class Meta:
        model=event
        fields='__all__'

class News_form(ModelForm):

    class Meta:
        model=news
        fields='__all__'




