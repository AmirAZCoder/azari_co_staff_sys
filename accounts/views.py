from django.contrib.auth.views import LoginView

class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
