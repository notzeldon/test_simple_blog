from django.views import generic

from blog.forms import BlogPostModelForm
from blog.models import BlogPost


class BlogMainPageView(generic.TemplateView):
    template_name = 'blog/main_page_view.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        posts = BlogPost.objects.order_by('-published')[0:10]

        if posts:
            ctx['main_post'] = posts[0]
            ctx['posts'] = posts[1:]

        return ctx


class BlogCreateView(generic.CreateView):
    model = BlogPost
    form_class = BlogPostModelForm

    def get_success_url(self):
        return '/'