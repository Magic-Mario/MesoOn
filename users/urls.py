from django.urls import path

from users.views import Profile, solicitud

app_name = 'users'

urlpatterns = [
    path('profile/', Profile, name='profile'),
    path('solicitud/', solicitud, name='solicitud')

]
