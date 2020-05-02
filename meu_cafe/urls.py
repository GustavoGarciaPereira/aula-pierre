from .views import boas_vindas



from django.urls import path, include

from .views import home

app_name = 'landpage'
urlpatterns = [
    path('', boas_vindas, name='home'),
]