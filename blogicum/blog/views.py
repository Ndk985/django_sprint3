from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from blog.models import Post
from blog.models import Category
from django.utils import timezone


def index(request):
    posts = Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    ).order_by('-pub_date')[:5]
    return render(request, 'blog/index.html', {'post_list': posts})


def post_detail(request: HttpRequest, id: int) -> HttpResponse:
    post = get_object_or_404(
        Post,
        id=id,
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request: HttpRequest, category_slug: str) -> HttpResponse:
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now()
    )
    return render(
        request, 'blog/category.html',
        {'category': category, 'post_list': posts}
    )
