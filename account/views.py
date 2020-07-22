from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User  # superuser database
from context.models import Context
from django.http import HttpResponse

# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are logged in!")
            return redirect("dashboard")
        else:
            messages.error(request, "User not found")
            return redirect("login")

    else:
        return render(request, "accounts/login.html")


def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password != password2:
            messages.error(request, "password does not matched")
            return redirect("register")
        else:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, "username is already exitst")
                return redirect("register")
            else:
                # check email
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email is already used")
                    return redirect("register")
                else:
                    # login
                    user = User.objects.create_user(
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        email=email,
                        password=password,
                    )
                    user.save()
                    messages.success(request, "You are Register!!")
                    return redirect("login")

    else:
        return render(request, "accounts/register.html")


def dashboard(request):
    user_contacts = Context.objects.order_by("-contact_date").filter(
        user_id=request.user.id
    )
    context = {"contacts": user_contacts}
    return render(request, "accounts/dashboard.html", context)


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are Logged Out !")
        return redirect("index")
