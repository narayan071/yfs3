from django.shortcuts import render, HttpResponse, redirect
from .models import num_counts, what_we_do
from .forms import FeedbackForm
from django.contrib import messages
from .forms import FeedbackForm

# Create your views here.

def home(request):
    count_instance = num_counts.objects.first() 
    what_we_do_inst = what_we_do.objects.all()[:3]


    context = {
        'pname': "home",
        'count_instance': count_instance,
        'what_we_do' : what_we_do_inst,
    }
    return render(request, 'home/home.html', context)
# def contact(request):
#     context={
#         "pname":"contact"
#     }
#     return render(request,'home/contact.html',context)

def projects(request):
    return render(request, "home/projects.html")

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