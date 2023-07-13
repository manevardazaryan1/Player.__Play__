from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.views import (LoginView, LogoutView)
from user_app.forms import RegisterForm, LoginForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import BadHeaderError
from django.db.models.query_utils import Q
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django.contrib.auth.views import (PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView)
from .forms import RegisterForm
from django.http import JsonResponse
from user_app.tokens import account_activation_token
from player_project.helpers import SITE_NAME
from .tasks import send_email
from .models import Profile
from music_app.models import Playlist
from music_app.forms import CreatePlaylistForm
User = get_user_model()


class SuccessUrlMixin:
    """Success mixin class"""

    def get_success_url(self):
        return reverse("base_app:index")
    

class PasswordResetDone(PasswordResetDoneView):
    template_name = '../templates/user_app/password_reset_done.html'

class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = '../templates/user_app/password_reset_confirm.html'

class PasswordResetComplete(PasswordResetCompleteView):
    template_name = '../templates/user_app/password_reset_complete.html'


def RegisterView(request):
    if request.method == 'POST':  
        form = RegisterForm(request.POST)  
        if form.is_valid():  
            # save form in the memory not in database  
            user = form.save(commit=False)  
            user.is_active = False  
            user.save()  
            # to get the domain of the current site  
            current_site = get_current_site(request)  
            mail_subject = 'Activation link has been sent to your email id'  
            email_template_name = '../templates/user_app/acc_active_email.html'
            message = render_to_string(email_template_name, {  
                'user': user,  
                'domain': current_site.domain, 
                'site_name': SITE_NAME,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
                'protocol': 'http', 
            })  
            to_email = form.cleaned_data.get('email')  
            send_email(mail_subject, message, to_email)
            return render(request, '../templates/user_app/email_confirmation.html')
    else:  
        form = RegisterForm()  
    return render(request, '../templates/user_app/register.html', {'form': form})  


def activate(request, uidb64, token):  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return render(request,'../templates/user_app/email_confirmation_done.html')
    else:  
        return render(request,'../templates/user_app/email_confirmation_done.html', {'error': 'Activation link is invalid!'})

def password_reset_request(request):
    if request.method == 'POST':
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            to_email = password_reset_form.cleaned_data['email']
            mail_subject = 'Password Reset Requested'
            current_site = get_current_site(request)
            email_template_name = '../templates/user_app/password_reset_email.txt'
            associated_users = User.objects.filter(Q(email=to_email))

            if associated_users.exists():
                for user in associated_users:
                    message = render_to_string(email_template_name,{
                        'email': user.email,
                        'domain': current_site.domain,
                        'site_name': SITE_NAME,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'user': user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    })

                    try:
                        send_email(mail_subject, message, to_email)
                    except BadHeaderError:
                        return render(request, '../templates/user_app/password_reset_except.html')
                    
                    return render(request, '../templates/user_app/password_reset_done.html')
    password_reset_form = PasswordResetForm()
    return render(request, '../templates/user_app/password_reset.html', {'password_reset_form':password_reset_form})


class Login(SuccessUrlMixin, LoginView):
    """Login class"""

    form_class = LoginForm
    template_name = "../templates/user_app/login.html"

    def form_valid(self, form):

        remember_me = form.cleaned_data['remember_me']

        login(self.request, form.get_user())

        if remember_me:
            self.request.session.set_expiry(1209600)

        return super().form_valid(form)


class Logout(LogoutView):
    """Log out class"""

    next_page = "base_app:index"


def profile(request, user_name):
    """Profile function"""

    if user_name != request.user.username:
        return redirect('base_app:index')
    user = User.objects.get(username=request.user.username)
    return render(request, '../templates/user_app/profile.html', {'user': user})
