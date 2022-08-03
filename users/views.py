from msilib.schema import File
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from users.forms import UserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from users.token_generator import account_activation_token
from users.forms import User #, upload_files_form
from django.core.mail import EmailMessage
from django.core.files.storage import FileSystemStorage
from os import path
from django.utils.datastructures import MultiValueDictKeyError
from users.forms import upload_files_form
from users.models import Users_profile

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render (request, 'home.html')
    else:
        return redirect('register')
        



def Register (request):
    if request.method == 'GET':
        context = {
            'form':UserCreationForm()
        }
        return render(request, 'registration/register.html', context )
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            current_site = get_current_site(request)
            email_subject = 'Activate Your Account'
            message = render_to_string('activate_account.html', {
                'user':user,
                'domain':current_site.domain,
                'uid':user.pk,
                'token': account_activation_token.make_token(user),
            })
            
            to_email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            email = EmailMessage(email_subject, message, to = [to_email])
            email.send()
            user = authenticate(email = to_email, password = password)
            return HttpResponse('We have sent you an email, please confirm your email address to complete registration')
        else:
            context = {
                'form':form
            }
            return render(request, 'registration/register.html', context)


#activate account

def activate_account(request, *_args, **kwargs):
    # try:
    uid = kwargs["uidb64"]
    user = User.objects.get(pk=uid)
    print(uid)
    # except(TypeError, ValueError, OverflowError, User.DoesNotExist):
    #     print('Eror. A bigest eror!!')
    #     user = None
    print(account_activation_token.check_token(user, kwargs["token"]), user,user.password, sep = ' ')
    if user is not None and account_activation_token.check_token(user, kwargs["token"]):
        user.is_active = True
        user.save()
        login(request, user)
        return render(request, 'account_activated_successfully.html')
    else:
        return HttpResponse('Activation link is invalid!')

def upload(request):
    if request.method == 'POST':
        try:
            form     = upload_files_form(request.POST, request.FILES)
            # is_driver = form.is_driver
            if form.is_valid():
                    
                form.user = request.user 
                driver    = form.cleaned_data.get('is_driver')
                user      = request.user
                # 
                # passport
                # 
                passport      = request.FILES['passport']
                File_St       = FileSystemStorage()
                passport_path = "passport/{0}/{1}".format(user.id,passport.name)
                File_St.save(passport_path, passport)
                try:
                    # 
                    # tech_passport
                    # 
                    tech_passport      = request.FILES['tech_passport']
                    File_St            = FileSystemStorage()
                    tech_passport_path = "tech_passport/{0}/{1}".format(user.id, tech_passport.name)
                    File_St.save(tech_passport_path, tech_passport)
                    # 
                    # tech_osmotr
                    # 
                    tech_osmotr      = request.FILES['tech_osmotr']
                    File_St          = FileSystemStorage()
                    tech_osmotr_path = "tech_osmotr/{0}/{1}".format(user.id, tech_osmotr.name)
                    File_St.save(tech_osmotr_path, tech_osmotr)
                    # 
                    # tax
                    # 
                    tax      = request.FILES['tax']
                    File_St  = FileSystemStorage()
                    tax_path = "tax/{0}/{1}".format(user.id, tax.name)
                    File_St.save(tax_path, tax)
                    # 
                    # tonirovka
                    # 
                    tonirovka      = request.FILES['tonirovka']
                    File_St        = FileSystemStorage()
                    tonirovka_path = "tonirovka/{0}/{1}".format(user.id, tonirovka.name)
                    File_St.save(tonirovka_path, tonirovka)
                    # 
                    # strakhovka
                    # 
                    strakhovka      = request.FILES['strakhovka']
                    File_St         = FileSystemStorage()
                    strakhovka_path = "strakhovka/{0}/{1}".format(user.id, strakhovka.name)
                    File_St.save(strakhovka_path, strakhovka)
                    # 
                    # ecology
                    # 
                    ecology       = request.FILES['ecology']
                    File_St       = FileSystemStorage()
                    ecology_path  = "ecology/{0}/{1}".format(user.id, ecology.name)
                    File_St.save(ecology_path, ecology)
                    # 
                    # talon
                    # 
                    talon         = request.FILES['talon']
                    File_St       = FileSystemStorage()
                    talon_path    = "talon/{0}/{1}".format(user.id, talon.name)
                    File_St.save(talon_path, talon)
                    # 
                    # med_spravka
                    #
                    med_spravka      = request.FILES['med_spravka']
                    File_St          = FileSystemStorage()
                    med_spravka_path = "med_spravka/{0}/{1}".format(user.id, med_spravka.name)
                    File_St.save(med_spravka_path, med_spravka)
                    # 
                    # udost_von_gas_balon_auto
                    # 
                    udost_von_gas_balon_auto      = request.FILES['udost_von_gas_balon_auto']
                    File_St                       = FileSystemStorage()
                    udost_von_gas_balon_auto_path = "udost_von_gas_balon_auto/{0}/{1}".format(user.id, udost_von_gas_balon_auto.name)
                    File_St.save(udost_von_gas_balon_auto_path, udost_von_gas_balon_auto)
                    # 
                    # saving in database
                    # 
                    Users_profile.objects.create(
                        user                     = user,
                        is_driver                = driver,
                        passport                 = passport_path,
                        tech_passport            = tech_passport_path, 
                        tech_osmotr              = tech_osmotr_path,
                        tax                      = tax_path,
                        tonirovka                = tonirovka_path,
                        strakhovka               = strakhovka_path,
                        ecology                  = ecology_path,
                        talon                    = talon_path,
                        med_spravka              = med_spravka_path,
                        udost_von_gas_balon_auto = udost_von_gas_balon_auto_path
                    )
                except(MultiValueDictKeyError):
                    Users_profile.objects.create(user = user, is_driver = driver, passport = passport_path)

                return HttpResponse("ok")
        except( MultiValueDictKeyError ):
        
            context = {
                'error':'С начала выберите документ!'
            }
            return render(request, 'upload.html', context)
    if request.method == 'GET':
        form = upload_files_form()
        return render(request, 'upload.html', {'form':form} )
            
#     return render(request, 'upload.html')
# def upload(request):
#     if request.method == 'POST':
#         form = upload_files_form(request.POST, request.FILES)
#         form.user = request.user
#         form.save(commit = False)
#         return redirect('profile')
#     else:
#         form = upload_files_form()
#     return render (request, 'upload.html', {'form':form})


# profiles
def profile(request, uidb64):
    uidb64 = request.user
    return HttpResponse('ok')