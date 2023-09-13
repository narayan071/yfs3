from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from chapters.models import NewChapterApplication, JoinChapterApplication, AllChapter
from chapters.forms import  EventForm, AllChapterForm

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
            messages.success(request, f"Signed in as {user}")
            login(request, user)
            return redirect('profile')
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
            messages.error(request,'username is already taken, try with a new username')
            user_exists=True
        if User.objects.filter(email=email).exists():
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


def profile(request):
    chapters = AllChapter.objects.filter(chapter_lead=request.user)
    members = JoinChapterApplication.objects.filter(user=request.user)
    print(members)
    add_event = EventForm()

    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.chapter = chapters[0]
            obj.save()
    if len(chapters) > 0:
        chapters = NewChapterApplication.objects.filter(user=request.user)[0]
    if(chapters):
        context = {
        "pname": "profile",
        "chapters": chapters,
        "members": members,
        "add_event_form":add_event,
    }
    elif (len(members)!=0 and len(chapters)==0):
        context = {
            "pname": "profile",
            "members": members,
        }
    else :
        context = {
            "pname": "profile",
            "chapters": chapters,
        }
    
    return render(request, 'user/profile.html', context)