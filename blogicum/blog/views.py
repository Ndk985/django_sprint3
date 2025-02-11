from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from blog.models import Post, Category
from django.conf import settings


def index(request):
    posts = (
        Post.objects.published()
        .order_by('-pub_date')[:settings.POSTS_PER_PAGE]
    )
    return render(request, 'blog/index.html', {'post_list': posts})


def post_detail(request: HttpRequest, id: int) -> HttpResponse:
    post = get_object_or_404(
        Post.objects.published(),
        id=id
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request: HttpRequest, category_slug: str) -> HttpResponse:
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts = category.posts.published()
    return render(
        request, 'blog/category.html',
        {'category': category, 'post_list': posts}
    )
