from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, resolve_url
from django.contrib.auth.views import redirect_to_login
from base.models import Solicitud
# from django.core.exceptions import PermissionDenied


# add: user.has_perm('foo.add_bar')
# change: user.has_perm('foo.change_bar')
# delete: user.has_perm('foo.delete_bar')
# view: user.has_perm('foo.view_bar')

# @login_required(login_url='/login/')
# @custom_permission_validation('user.add_blog')
# @user_is_blog_author

def login_required(function):
    def wrap(request, *args, **kwargs):

        # checks if user is logged in
        if not request.user.is_authenticated:
            messages.info(request, settings.REQUIRED_LOGIN_MESSAGE)
            path = request.get_full_path() # request.build_absolute_uri()
            resolved_login_url = resolve_url(settings.LOGIN_URL)
            # return redirect('Backend:login')
            return redirect_to_login(path, resolved_login_url)
        else:
            return function(request, *args, **kwargs)

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def user_is_solicitud_author(function):
    def wrap(request, *args, **kwargs):

        # checks if user is logged in
        if not request.user.is_authenticated:
            messages.info(request, settings.REQUIRED_LOGIN_MESSAGE)
            path = request.get_full_path() # request.build_absolute_uri()
            resolved_login_url = resolve_url(settings.LOGIN_URL)
            # return redirect('Backend:login')
            return redirect_to_login(path, resolved_login_url)

        else:
            solicitud = Solicitud.objects.get(pk=kwargs['solicitud_pk'])
            if solicitud.autor == request.user:
                return function(request, *args, **kwargs)
            else:
                messages.error(request, settings.PERMISSION_MESSAGE)
                url = request.META.get('HTTP_REFERER')
                if (url is None) or ('?next=' in url):
                    url = settings.WEBSITE_HOME

                return redirect(url)
                # return redirect('Backend:blog')
                # raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def custom_permission_validation(permission):
    def wrapper(decorator_func):
        def wrapped(request, *args, **kwargs):

            # checks if user is logged in
            if not request.user.is_authenticated:                
                messages.info(request, settings.REQUIRED_LOGIN_MESSAGE)
                path = request.get_full_path() # request.build_absolute_uri()
                resolved_login_url = resolve_url(settings.LOGIN_URL)
                # return redirect('Backend:login')
                return redirect_to_login(path, resolved_login_url)

            # checks if user has permissions to access that view (parameter)
            if permission != '':
                if not request.user.has_perm(permission):
                    # if the user doesn't have permission
                    messages.error(request, settings.PERMISSION_MESSAGE + ' (' + permission + ')')
                    url = request.META.get('HTTP_REFERER')
                    if (url is None) or ('?next=' in url):
                        url = settings.WEBSITE_HOME
                    return redirect(url)

            return decorator_func(request, *args, **kwargs)
        wrapped.__doc__ = decorator_func.__doc__
        wrapped.__name__ = decorator_func.__name__
        return wrapped
    return wrapper
