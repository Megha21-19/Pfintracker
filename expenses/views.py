# expenses/views.py

from django.shortcuts import redirect,render
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from .forms import SignUpForm, LoginForm
from django.contrib.auth.views import LogoutView
def root_view(request):
    return redirect('signup_login')

class SignUpView(CreateView):
    template_name = 'signup_login.html'
    form_class = SignUpForm
    success_url = '/login/'

class CustomLoginView(LoginView):
    template_name = 'signup_login.html'
    authentication_form = LoginForm

def user_dashboard_view(request):
    return render(request, 'user_dashboard.html')
def reports_view(request):
    return render(request, 'reports.html')
def contactus_view(request):
    return render(request,'contact_us.html')
def graphics_view(request):
    return render(request,'graphics.html')

class CustomLogoutView(LogoutView):
    next_page = 'signup_login'






