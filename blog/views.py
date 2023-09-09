from django.shortcuts import render,get_object_or_404

# Create your views here.

def blogs(request):
    context = {
        'pname' : 'blogs',
    }
    return render(request, 'blog/blogs.html', context)

