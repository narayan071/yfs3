from django.shortcuts import render,redirect,get_object_or_404
from .forms import NewChapterForm
from django.contrib import messages
from .models import AllChapter

# Create your views here.


def chapters(request):
    allchapters = AllChapter.objects.all().order_by('established_on')

    context = {
        "pname":"chapters",
        "allchapters" : allchapters
    }
    return render(request, "chapters/index.html", context)

def new_chapter(request):
    context={}
    if not request.user.is_authenticated:
        messages.error(request, "Please log into your account before applying to volunteer")
        return redirect('signin')

    form = NewChapterForm(instance=request.user)
    form.name = "New Chapter Form"
    context['form'] = form
    if request.method == "POST":
        form = NewChapterForm(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            chapter = AllChapter(
                institution_name = request.POST.get('institution_name'),
                chapter_lead = request.user,
                established_on = request.POST.get('applied_at')
            )
            chapter.save()
            messages.success(
                request, "You have successfully applied for a new chapter. We will contact you for further updates.")
            return redirect('profile')

    context['form'] = form
    return render(request, 'chapters/newchapter.html', context)

# def chpterprofile(request):
#     chapter = get_object_or_404(Chapter)

#     context = {
#         'pname':'Chapter Profile'

#     }
#     return render(request,'chapters/chapterprofile.html',context)