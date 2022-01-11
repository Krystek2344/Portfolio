from django.views import View
from django.shortcuts import render

# Create your views here.


class LandingPageView(View):
    def get(self, request):
        ctx = {}
        return render(request, 'charityapp/base.html', ctx)


class AddDonationView(View):
    def get(self, request):
        ctx = {}
        return render(request, 'charityapp/form.html', ctx)


class LoginView(View):
    """Login page view """
    def get(self, request):
        ctx = {}
        return render(request, 'charityapp/login.html', ctx)


class RegisterView(View):
    def get(self, request):
        ctx = {}
        return render(request, 'charityapp/register.html', ctx)
