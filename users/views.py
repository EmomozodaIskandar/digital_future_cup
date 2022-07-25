from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from users.forms import UserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from users.token_generator import account_activation_token
from users.forms import User
from django.core.mail import EmailMessage



# Create your views here.
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

