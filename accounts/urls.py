from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserLoginView, DashboardView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', DashboardView.as_view(), name='dashboard'), # صفحه اصلی به عنوان داشبورد
]
