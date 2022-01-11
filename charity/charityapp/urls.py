from django.urls import path
from .views import *

app_name = 'charityapp'

urlpatterns = [
    path('', LandingPageView.as_view(), name='base'),
    path('adddonation/', AddDonationView.as_view(), name='adddonation-form'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]