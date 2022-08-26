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
    passport                 = forms.FileField(
        
    )
    tech_passport            = forms.FileField(
        required=False,
    )
    tech_osmotr              = forms.FileField(
        required=False,
    )
    tax                      = forms.FileField(
        required=False,
    )
    tonirovka                = forms.FileField(
        required=False,
    )
    strakhovka               = forms.FileField(
        required=False,
    )
    ecology                  = forms.FileField(
        required=False,
    )
    talon                    = forms.FileField(
        required=False,
    )
    med_spravka              = forms.FileField(
        required=False,
    )
    udost_von_gas_balon_auto = forms.FileField(
        required=False,
    )
    class Meta:
        model = Users_profile
        fields = [
            'is_driver',
            # 'passport', 
            # 'tech_passport', 
            # 'tech_osmotr', 
            # 'tax','tonirovka',
            # 'strakhovka',
            # 'ecology',
            # 'talon', 
            # 'med_spravka', 
            # 'udost_von_gas_balon_auto',
            ]
    
