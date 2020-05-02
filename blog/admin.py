from django.contrib import admin

from blog.models import BlogPost


@admin.register(BlogPost)
class BlogPostModelAdmin(admin.ModelAdmin):
    pass
