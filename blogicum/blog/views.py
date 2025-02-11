from django.shortcuts import render, get_object_or_404, Http404
from django.http import HttpRequest, HttpResponse
from blog.models import Post, Category
from django.utils import timezone


def index(request):
    posts = Post.objects.latest_posts()
    return render(request, 'blog/index.html', {'post_list': posts})


def post_detail(request: HttpRequest, id: int) -> HttpResponse:
    post = Post.objects.get_post_by_id(id)
    if post is None:
        raise Http404
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request: HttpRequest, category_slug: str) -> HttpResponse:
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts = category.posts.filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now()
    )
    return render(
        request, 'blog/category.html',
        {'category': category, 'post_list': posts}
    )
