from django.db import models

from django.utils.translation import ugettext_lazy as _


class BlogPost(models.Model):

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')

        ordering = ['-published']

    title = models.CharField(
        verbose_name=_('title'),
        max_length=200,
    )

    image = models.ImageField(
        verbose_name=_('image'),
        upload_to='blog/blogpost',
    )

    text = models.TextField(
        verbose_name=_('text'),
    )

    published = models.DateTimeField(
        verbose_name=_('piblished at'),
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self._meta.verbose_name} "{self.title}"'

