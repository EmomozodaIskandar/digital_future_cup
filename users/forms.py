from dataclasses import field, fields
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.utils.translation import gettext_lazy as _
from users.models import Users_profile

User = get_user_model()

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name','email','password1', 'password2')



class upload_files_form(forms.ModelForm):
    passport                 = forms.FileField()
    tech_passport            = forms.FileField(required=False, )
    tech_osmotr              = forms.FileField()
    tax                      = forms.FileField()
    tonirovka                = forms.FileField()
    strakhovka               = forms.FileField()
    ecology                  = forms.FileField()
    talon                    = forms.FileField()
    med_spravka              = forms.FileField()  
    udost_von_gas_balon_auto = forms.FileField()
    
    class Meta:
        model = Users_profile
        fields = ['is_driver',]
    
