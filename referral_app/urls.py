from django.urls import path
from .views import *


urlpatterns = [
    path('auth/phone/', AuthView.as_view(), name='auth'),
    path('auth/verify/', AuthVerifyView.as_view(), name='authverify'),
    path('profile/', ProfileView.as_view(), name='profile'),

]

