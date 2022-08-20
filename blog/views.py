from django.shortcuts import render
from .models import Post
from .forms import CommentForm

# Create your views here.

def home(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, "blog/home.html", context)


def detail(request, slug):
    post = Post.objects.get(slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.product = product
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    context = {
        'post': post
    }
    return render(request, 'blog/detail.html', context)


