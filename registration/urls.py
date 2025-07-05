from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.register, name='register'),
    path('success/', views.success, name='success'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='admin_login'), name='logout'),
    path('generate-pdf/', views.generate_pdf, name='generate_pdf'),
]