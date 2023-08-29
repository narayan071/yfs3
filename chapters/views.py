from django.shortcuts import render,redirect,get_object_or_404
from .forms import NewChapterForm, JoinChapterForm
from django.contrib import messages
from .models import AllChapter, NewChapterApplication, JoinChapterApplication
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.


def chapters(request):
    allchapters = AllChapter.objects.all().order_by('established_on')

    context = {
        "pname":"chapters",
        "allchapters" : allchapters
    }
    return render(request, "chapters/index.html", context)

def new_chapter(request):
    context={
        "pname":"newChapter",
    }
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
            return redirect('chapters')

    context['form'] = form
    return render(request, 'chapters/newchapter.html', context)

# def chpterprofile(request):
#     chapter = get_object_or_404(Chapter)

#     context = {
#         'pname':'Chapter Profile'

#     }
#     return render(request,'chapters/chapterprofile.html',context)


def join_chapter(request):
    context = {
        "pname":"joinChapter",
    }

    if not request.user.is_authenticated:
        messages.error(request, "Please log into your account before applying to join a chapter.")
        return redirect('signin')

    form = JoinChapterForm(instance=request.user)
    form.name = "Join Chapter Form"
    context['form'] = form

    if request.method == "POST":
        form = JoinChapterForm(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            # Here you can link the institution_name to the corresponding NewChapterApplication instance
            institution_name = form.cleaned_data['institution_name']
            try:
                new_chapter_instance = NewChapterApplication.objects.get(institution_name=institution_name)
            except ObjectDoesNotExist:
                messages.error(request, "The selected institution does not exist.")
                return redirect('join-chapter')
            obj.institution_name = new_chapter_instance
            obj.user = request.user
            obj.save()
            
            messages.success(
                request, "You have successfully applied to join a chapter. We will contact you for further updates.")
            return redirect('profile')

    context['form'] = form
    return render(request, 'chapters/joinchapter.html', context)