from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post, Tag


def home(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    """
    Class for showing all post of this blog, by 5 post at every page
    """
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    """
    Class for filter posts by picked user
    """
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by('-date_posted')


class TagPostListView(ListView):
    """
    class  for filter posts by selected tag
    """
    model = Post
    template_name = 'blog/tag_detail.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        t_tag = get_object_or_404(Tag, title=self.kwargs.get("title"))
        return Post.objects.filter(tags=t_tag).order_by('-date_posted')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_tag"] = get_object_or_404(Tag, title=self.kwargs.get("title"))
        return context




class PostDetailView(DetailView):
    """
    View about detail of every post
    """
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    creating new post
    """
    model = Post
    fields = ['title', 'content', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    updating existing post
    """
    model = Post
    fields = ['title', 'content', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    deleting existing post
    """
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class TagListView(ListView):
    """
    class with list of all tags
    """
    model = Tag
    template_name = 'blog/tags.html'
    context_object_name = 'tags'


# class TagDetailView(DetailView):
#     model = Tag


def about(request):
    return render(request, "blog/about.html", {'title': 'About'})
