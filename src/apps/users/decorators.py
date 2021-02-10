from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user and hasattr(request.user, "type"):
                if request.user.type in allowed_roles:
                    return view_func(request, *args, **kwargs)

            return HttpResponseRedirect(reverse_lazy("users:login_view"))

        return wrapper_func

    return decorator
