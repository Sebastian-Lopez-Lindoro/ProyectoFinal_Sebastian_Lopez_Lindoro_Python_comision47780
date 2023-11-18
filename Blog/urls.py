from django.urls import path
from Blog.views import (
    inicio,
    about,
)
from django.views.generic.base import TemplateView


from Blog.class_views import (
    BlogListView,
    BlogCreateView,
    BlogDetailView,
    BlogDeleteView,
    BlogUpdateView,
)


urlpatterns = [
    path("", TemplateView.as_view(template_name="Blog/index.html"), name="Inicio"),
    path("pages/", BlogListView.as_view(), name="Pages"),
    path("about/", about, name="Acerca De"),
    path(
        "new-blog/",
        BlogCreateView.as_view(),
        name="Nuevo Blog",
    ),
    path("blog-detail/<int:pk>/", BlogDetailView.as_view(), name="Blog Detail"),
    path(
        "blog-delete/<int:pk>/",
        BlogDeleteView.as_view(),
        name="Blog Delete",
    ),
    path(
        "blog-update/<int:pk>/",
        BlogUpdateView.as_view(),
        name="Blog Update",
    ),
]
