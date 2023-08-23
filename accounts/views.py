from django.shortcuts import render

# Create your views here.


def login(request):
    context={
        "pname": "login",
    }

    return render(request, "user/login.html", context)

def signup(request):
    context={
        "pname": "signup",
    }

    return render(request, "user/signup.html", context)
