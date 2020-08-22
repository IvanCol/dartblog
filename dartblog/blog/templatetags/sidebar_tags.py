from django import template

from blog.models import Post, Tag


register = template.Library()


@register.inclusion_tag('blog/tags/popular_posts.html')
def show_popular_posts(cnt=3):
    posts = Post.objects.order_by('-views')[:cnt]
    context = {
        'posts': posts
    }
    return context


@register.inclusion_tag('blog/tags/tags.html')
def show_tags(cnt=10):
    tags = Tag.objects.all()
    context = {
        'tags': tags
    }
    return context
