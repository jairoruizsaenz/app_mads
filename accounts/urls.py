from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'accounts_app'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_with_email_authentication_view, name='signup'),
    # path('signup_without_authentication/', views.signup_without_email_authentication_view, name='signup2'),
    path('registration_email/', views.registration_email_view, name='registration_email'),
    path('account_activation_done/', views.account_activation_done_view, name='account_activation_done'),
    path('account_activation_failed/', views.account_activation_failed_view, name='account_activation_failed'),
    path('email_test/', views.email, name='email_test'),
    # url(r'^activate_user_account/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate_user_account_view, name='activate_user_account')
    path('activate_user_account/<uidb64>/<token>/', views.activate_user_account_view, name='activate_user_account')
]
