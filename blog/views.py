from django.shortcuts import render,get_object_or_404

# Create your views here.

def blog(request):
    context = {
        'blog' : 'blog',
    }
    return render(request, 'blog/index.html', context)

