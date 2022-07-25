from django.urls import include, path
from users.views import Register, activate_account
# from django.contrib.auth import urls
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register, name='register'), 
    path('activate_account/<uidb64>/<token>/',  
        activate_account, name='activate'),
]