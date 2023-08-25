from django.shortcuts import render,redirect
from .forms import NewChapterForm
from django.contrib import messages

# Create your views here.


def chapters(request):
    context = {
        "pname":"chapters",
    }
    return render(request, "chapters/index.html", context)

def new_chapter(request):
    context = {}
    if not request.user.is_authenticated:
        messages.info(
            request, "Please log into your account before applying to volunteer")

        return redirect('signin')

    form = NewChapterForm(instance=request.user)
    form.name = "New Chapter Form"

    if request.method == "POST":
        form = NewChapterForm(request.POST or None)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(
                request, "You have successfully applied for a new chapter. We will contact you for further updates.")
            return redirect('profile')

    context['form'] = form
    return render(request, 'chapters/newchapter.html', context)