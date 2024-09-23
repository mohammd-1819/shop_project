from blog.models import Post, Category


def recent_posts(request):
    recent_posts = Post.objects.all().order_by('-created_at')[:3]

    return {'recent_posts': recent_posts}


def categories(request):
    categories = Category.objects.all()

    return {'categories': categories}

