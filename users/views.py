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

# def upload(request):
#     if request.method == 'POST':
#         try:
#             user     = request.user
#             passport = request.FILES['passport']
#             File_St  = FileSystemStorage()
#             # file_ext = path.splitext(passport.name)[1]
#             File_St.save("{0}/{1}".format(user.id,passport.name), passport)
#         except( MultiValueDictKeyError ):
#             context = {
#                 'error':'С начала выберите документ!'
#             }
#             return render(request, 'upload.html', context)

            
#     return render(request, 'upload.html')
def upload(request):
    if request.method == 'POST':
        form = upload_files_form(request.POST, request.FILES)
        form.user = request.user
        form.save(commit = False)
        return redirect('profile')
    else:
        form = upload_files_form()
    return render (request, 'upload.html', {'form':form})


# profiles
def profile(request):
    return HttpResponse('ok')