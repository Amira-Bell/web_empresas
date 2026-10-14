from django.shortcuts import render, get_object_or_404
from .models import Category, Post


def blog(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    current_category = None

    if category_id:
        current_category = get_object_or_404(Category, id=category_id)
        posts = Post.objects.filter(category=current_category)
    else:
        posts = Post.objects.all()

    return render(
        request,
        'blog/blog.html',
        {
            'posts': posts,
            'categories': categories,
            'current_category': current_category,
        }
    )


def category(request, category_id):
    current_category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=current_category)
    categories = Category.objects.all()

    return render(
        request,
        'blog/blog.html',
        {
            'posts': posts,
            'categories': categories,
            'current_category': current_category,
        }
    )
