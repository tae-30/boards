from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'original/post_list.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'original/post_edit.html', {'form': form})


def original_view(request):
    return render(request, 'original.html')