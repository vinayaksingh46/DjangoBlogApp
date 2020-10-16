from . import views as registerViews
from django.urls import path, include

urlpatterns = [
    path('',registerViews.register,name = 'registrationPage')
]