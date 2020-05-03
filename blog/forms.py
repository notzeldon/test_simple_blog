from django import forms
from django.utils.translation import ugettext_lazy as _

from blog.models import BlogPost


class BlogPostModelForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ('title', 'text', 'image')

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': _('Put post title'),
            }),
            'text': forms.Textarea(attrs={
                'class': 'materialize-textarea faked-editor'
            }),
        }

    class Media:
        js = ('js/blog/image-picker.js',)


    # TODO: В идеале надо сделать виджет для image поля, но пока что нет времени