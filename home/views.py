from django.shortcuts import render, HttpResponse
# Create your views here.

def home(request):
    context={
        'pname':"home",
    }
    return render(request, 'home/home.html', context)