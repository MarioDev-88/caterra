from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import LoginForm, CustomerForm
from .models import User


def login_view(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)

            return HttpResponseRedirect("/")

        messages.add_message(request, messages.ERROR, "Credenciales inválidas")

    ctx = {"form": form}

    return render(request, "users/login.html", ctx)


def logout_view(request):
    logout(request)

    return HttpResponseRedirect(reverse("ecommerce:home"))


def signup_view(request):
    form = CustomerForm(request.POST or None)
    print(request.POST)

    if request.method == "POST":
        print(form.is_valid())
        if form.is_valid():
            user = User()
            user.first_name = form.cleaned_data.get("first_name")
            user.first_surname = form.cleaned_data.get("first_surname")
            user.last_surname = form.cleaned_data.get("last_surname")
            user.email = form.cleaned_data.get("email")
            user.phone = form.cleaned_data.get("phone")
            user.type = "CUSTOMER"
            user.set_password(form.cleaned_data.get("password"))

            user.save()
            login(request, user)

            return HttpResponseRedirect(reverse("ecommerce:home"))
        return HttpResponseRedirect(reverse("ecommerce:home"))