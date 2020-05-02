from django.views import generic

from blog.models import BlogPost


class BlogMainPageView(generic.TemplateView):
    template_name = 'blog/main_page_view.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        posts = BlogPost.objects.all()[0:10]

        if posts:
            ctx['main_post'] = posts[0]
            ctx['posts'] = posts[1:]

        return ctx
