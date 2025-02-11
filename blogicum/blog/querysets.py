from django.db import models
from django.utils import timezone
from django.conf import settings


class PostQuerySet(models.QuerySet):
    def published(self):
        """Возвращает опубликованные посты."""
        return self.filter(
            is_published=True,
            pub_date__lte=timezone.now(),
            category__is_published=True
        )

    def latest_posts(self):
        """Возвращает последние опубликованные посты."""
        return self.published().order_by('-pub_date')[:settings.POSTS_PER_PAGE]

    def get_post_by_id(self, id):
        """Возвращает пост по ID, если он опубликован."""
        return self.published().filter(id=id).first()
