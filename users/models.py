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

def user_directory_passport(instance, filename):
    return 'passport/{0}/{1}'.format(instance.user.id, filename)

#User's profile
# class Users_profile(models.Model):    
    # User = get_user_model()
    # user          = models.OneToOneField(User, on_delete=models.CASCADE, unique = True, )
    # is_driver     = models.BooleanField()
    # passport      = models.FileField(
    #     upload_to = user_directory_passport,
    # )
    # tech_passport = models.FileField(
    #     upload_to='tech_passports/{0}'.format(user_directory_path), 
    #     blank=True,
    #     null=True, 
    # )
    # tech_osmotr   = models.FileField(
    #     upload_to='tech_osmotr/{0}'.format(user_directory_path), 
    #     blank=True, 
    #     null=True,
    # )
    # tax           = models.FileField(
    #     upload_to='taxes/{0}'.format(user_directory_path), 
    #     blank=True,
    #     null=True, 
    # )
    # tonirovka     = models.FileField(
    #     upload_to='tonirovka/{0}'.format(user_directory_path), 
    #     blank=True,
    #     null=True, 
    # )
    # strakhovka    = models.FileField(
    #     upload_to='strakhovka/{0}'.format(user_directory_path), 
    #     blank=True,
    #     null=True, 
    # )
    # ecology       = models.FileField(
    #     upload_to='ecology/{0}'.format(user_directory_path), 
    #     blank=True,
    #     null=True, 
    # )
    # talon         = models.FileField(
    #     upload_to='talon/{0}'.format(user_directory_path), 
    #     blank=True,
    #     null=True, 
    # )
    # med_spravka   = models.FileField(
    #     upload_to='med_spravka/{0}'.format(user_directory_path), 
    #     blank=True,
    #     null=True, 
    # ) 
    # udost_von_gas_balon_auto = models.FileField(
    #     upload_to='udost_von_gas_balon_auto/{0}'.format(user_directory_path), 
    #     blank=True,
    #     null=True, 
    # )
    # def __str__(self):
        # return self.user.first_name + ' ' + self.user.last_name


class Users_profile(models.Model):    
    User = get_user_model()
    user          = models.OneToOneField(User, on_delete=models.CASCADE,)

    is_driver     = models.BooleanField()

    passport      = models.CharField(
        max_length=120, 
    )
    tech_passport = models.CharField( 
        blank=True, 
        max_length=120,
        null=True,
    )
    tech_osmotr   = models.CharField(
        blank=True,
        max_length=120, 
        null=True,
    )
    tax           = models.CharField( 
        blank=True, 
        max_length=120,
        null=True,
    )
    tonirovka     = models.CharField( 
        blank=True,
        max_length=120, 
        null=True,
    )
    strakhovka    = models.CharField(
        blank=True, 
        max_length=120,
        null=True,
    )
    ecology       = models.CharField(
        blank=True, 
        max_length=120,
        null=True,
    )
    talon         = models.CharField( 
        blank=True, 
        max_length=120,
        null=True,
    )
    med_spravka   = models.CharField(
        blank=True, 
        max_length=120,
        null=True,
    ) 
    udost_von_gas_balon_auto = models.CharField( 
        blank=True, 
        max_length=120,
        null=True,
    )
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
