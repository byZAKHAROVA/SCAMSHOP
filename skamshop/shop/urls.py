from . import views
from django.urls import path

urlpatterns = [
    path('', views.main, name='index.html'),
    path('registration', views.register, name='register.html')
]
