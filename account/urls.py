from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    
    # path('login/', views.user_login, name='login')
    #login / logout
    
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # # Change password urls
    # path('change-password/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('change-password-done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    
    # # reset password urls
    # path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    # include the default auth urls (login, logout, password change, password reset)
    path('', include('django.contrib.auth.urls')),
    
    path('dashboard/',views.dashboard, name='dashboard'),
 
]