from django.urls import path

from .views import HomePage, PostPage, PostsByCategory, PostsByTags


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
    path('post/<str:slug>/', PostPage.as_view(), name='post'),
    path('tag/<slug:slug>/', PostsByTags.as_view(), name='tag'),
]
