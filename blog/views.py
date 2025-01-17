from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def feed(request):
    posts = Post.objects.all().order_by('-date_posted')
    paginator = Paginator(posts, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "feed.html", {"posts": page_obj, "user": request.user})

@login_required(login_url='login')
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, "create-post.html", {"form": form})

@login_required(login_url='login')
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()

    return render(request, "post_detail.html", {
        "post": post,
        "comments": comments,
        "form": form,
    })