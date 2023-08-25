from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def signin(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid signin credentials')
            return render(request, 'user/signin.html')
        else:
            login(request, user)
            return redirect('home')
    context={
        "pname": "signin",
    }
    return render(request, "user/signin.html", context)

def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_exists=False
        if User.objects.filter(username=username).exists():
            # print("username is already taken")
            messages.error(request,'username is already taken, try with a new username')
            user_exists=True
        if User.objects.filter(email=email).exists():
            # print("email is already existing")
            messages.error(request,'email is already taken, try with a new email id')
            user_exists=True
        if user_exists:
            return render (request, 'user/signup.html')
        
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password
        )
        user.save()
        messages.success(request, "Account Created successfuly, signin to Continue")
    
        print(first_name, last_name,email, username, password)  #to be removed
    context={
        "pname":"signup",
    }
    return render(request, "user/signup.html",context)

def signout(request):
    logout(request)
    context = {
        "pname":"signin"
    }
    return render(request, 'user/signin.html',context)

