from django.shortcuts import render, HttpResponse, redirect
from .models import num_counts
from .forms import FeedbackForm
from django.contrib import messages
from .forms import FeedbackForm

# Create your views here.

def home(request):
    count_instance = num_counts.objects.first() 

    context = {
        'pname': "home",
        'count_instance': count_instance,
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