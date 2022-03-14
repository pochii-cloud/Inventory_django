from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from core.forms import RegistrationForm


class LoginPageView(LoginView):
    template_name = 'login.html'


class RegisterView(View):
    def get(self, request):
        form = RegistrationForm(request.POST)
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'account was created for ' + user)
            return redirect('LoginPageView')
        return render(request, 'register.html', {'form': form})


class ForgotPasswordView(TemplateView):
    template_name = 'forgot-password.html'


class ProfilePage(TemplateView):
    template_name = 'profilepage.html'
