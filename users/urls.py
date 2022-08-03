from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from users.views import Register, activate_account, upload, profile 
# from django.contrib.auth import urls
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register, name='register'), 
    path('activate_account/<uidb64>/<token>/',  
        activate_account, name='activate'),
    path('upload/',upload, name = 'upload'),
    path('upload/profile/<uidb64>/',profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

