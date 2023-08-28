from django.shortcuts import render, HttpResponse, redirect
from .forms import FeedbackForm
from django.contrib import messages
from .forms import FeedbackForm

# Create your views here.

def home(request):
    context={
        'pname':"home",
    }
    return render(request, 'home/home.html', context)
# def contact(request):
#     context={
#         "pname":"contact"
#     }
#     return render(request,'home/contact.html',context)

def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your feedback has been shared with us successfully")
            return redirect('contact')  # This line should be here

    else:
        form = FeedbackForm()

    context = {
        'form': form,
        'pname': 'contact'
    }
    return render(request, 'home/feedback.html', context)