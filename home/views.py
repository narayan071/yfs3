from django.shortcuts import render, HttpResponse
# Create your views here.

def home(request):
    context={
        'pname':"home",
    }
    return render(request, 'home/home.html', context)
def contact(request):
    context={
        "pname":"contact"
    }
    return render(request,'home/contact.html',context)
def feedback(request):
    context={
        "pname":"feedback"
    }
    return render(request,'home/feedback.html',context)
