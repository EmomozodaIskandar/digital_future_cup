from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

class User(AbstractUser):
    email = models.EmailField(
        _('email address'), 
        unique=True,
    )
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=False,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        )
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

#User's profile
# class Users_profile(models.Model):    
#     User = get_user_model()
#     user          = models.ForeignKey(User, on_delete=models.CASCADE)
#     is_driver     = models.BooleanField()
#     passport      = models.FileField(
#         upload_to='passports'
#     )
#     tech_passport = models.FileField(
#         upload_to='tech_passports', 
#         blank=True, 
#     )
#     tech_osmotr   = models.FileField(
#         upload_to='tech_osmotr', 
#         blank=True, 
#     )
#     tax           = models.FileField(
#         upload_to='taxes', 
#         blank=True, 
#     )
#     tonirovka     = models.FileField(
#         upload_to='tonirovka', 
#         blank=True, 
#     )
#     strakhovka    = models.FileField(
#         upload_to='strakhovka', 
#         blank=True, 
#     )
#     ecology       = models.FileField(
#         upload_to='ecology', 
#         blank=True, 
#     )
#     talon         = models.FileField(
#         upload_to='talon', 
#         blank=True, 
#     )
#     med_spravka   = models.FileField(
#         upload_to='med_spravka', 
#         blank=True, 
#     ) 
#     udost_von_gas_balon_auto = models.FileField(
#         upload_to='udost_von_gas_balon_auto', 
#         blank=True, 
#     )
#     def __str__(self):
#         return self.user.first_name + ' ' + self.user.last_name


class Users_profile(models.Model):    
    User = get_user_model()
    user          = models.ForeignKey(User, on_delete=models.CASCADE)

    is_driver     = models.BooleanField()
    
    passport      = models.CharField(
        max_length=120
    )
    tech_passport = models.CharField( 
        blank=True, 
        max_length=120,
    )
    tech_osmotr   = models.CharField(
        blank=True,
        max_length=120, 
    )
    tax           = models.CharField( 
        blank=True, 
        max_length=120,
    )
    tonirovka     = models.CharField( 
        blank=True,
        max_length=120, 
    )
    strakhovka    = models.CharField(
        blank=True, 
        max_length=120,
    )
    ecology       = models.CharField(
        blank=True, 
        max_length=120,
    )
    talon         = models.CharField( 
        blank=True, 
        max_length=120,
    )
    med_spravka   = models.CharField(
        blank=True, 
        max_length=120,
    ) 
    udost_von_gas_balon_auto = models.CharField( 
        blank=True, 
        max_length=120,
    )
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
