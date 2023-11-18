from Blog.models import Blog
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class BlogListView(ListView):
    model = Blog
    template_name = "Blog/pages.html"


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = "Blog/new_blog.html"
    success_url = reverse_lazy("Pages")
    fields = ["title", "subtitle", "body", "author", "date", "image"]


class BlogDetailView(DetailView):
    model = Blog
    template_name = "Blog/blog_detail.html"


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy("Pages")
    template_name = "Blog/blog_confirm_delete.html"


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = "Blog/blog_edit.html"
    success_url = reverse_lazy("Pages")
    fields = ["title", "subtitle", "body", "author", "date", "image"]
