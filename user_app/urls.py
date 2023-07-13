from django.urls import path, include
from user_app import views

# user app urls.py

urlpatterns = [
    path('register/', views.RegisterView, name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path('captcha/', include('captcha.urls')),
    path('password_reset/done/', views.PasswordResetDone.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetComplete.as_view(), name='password_reset_complete'),
    path('profile/<str:user_name>', views.profile, name='profile'),
    path('accounts/signup/', views.RegisterView, name='register'),
    path('accounts/login/', views.Login.as_view(), name='login')
]