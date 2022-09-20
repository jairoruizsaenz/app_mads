from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from .models import CustomUser
from django.core.mail import EmailMessage
from django.contrib import messages

# from django.shortcuts import render, redirect
# from django.contrib.auth import login
# from django.contrib.auth import authenticate
# from .forms import SignupForm
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import logout
# from django.urls import reverse_lazy
# from django.views import generic

def email(request):
    # function to send emails
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['receiver@gmail.com']
    send_mail(subject, message, email_from, recipient_list)
    return redirect('website:home')


def registration_email_view(request):
    return render(request, 'accounts/registration_email_sent.html')


def account_activation_done_view(request):
    return render(request, 'accounts/account_activation_done.html')


def account_activation_failed_view(request):
    return render(request, 'accounts/account_activation_failed.html')


def signup_without_email_authentication_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log user in
            # login(request, user)
            message = 'mensaje de prueba'
            return render(request, 'website/home.html', {'message': message})
            # return redirect('persuasivo_app:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup2.html', {'form': form})


def signup_with_email_authentication_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activación de cuenta'
            message = render_to_string('accounts/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            # return HttpResponse('Please confirm your email address to complete the registration')
            return redirect('accounts_app:registration_email')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def activate_user_account_view(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # log user in
        # login(request, user)
        # return redirect('home')
        return redirect('accounts_app:account_activation_done')
        # return HttpResponse('Thank you for your email confirmation. Now you can login to your account.')
    else:
        return redirect('accounts_app:account_activation_failed')
        # return HttpResponse('Activation link is invalid!')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            user = form.get_user()
            if user.is_active_by_admin:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                return redirect('baseApp:solicitudes')
            else:
                messages.error(request, settings.ACTIVATION_REQUIRED)
                return redirect(settings.LOGIN_URL)
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


'''
# in urls.py > path('signup/', views.SignUp.as_view(), name='signup'),
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('persuasivo_app:index')
    template_name = 'accounts/signup.html'

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            user = form.get_user()
            login(request, user)
            return redirect('persuasivo_app:index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('persuasivo_app:index')
'''
