from django.views.generic import (
        TemplateView, ListView,
        CreateView, UpdateView,
        DeleteView, DetailView,
        RedirectView
    )
from django.views import View
from django.contrib.auth.mixins import (
        LoginRequiredMixin, UserPassesTestMixin
    )
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from .forms import CreatePost, AddCommentForm
from .models import Post, Comment

# Create your views here.


class home(ListView):
    """
    This class is used to display all posts
    """
    template_name = 'home/home.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all().order_by('-created_on')


# @login_required(login_url="accounts/login")
class addPost(LoginRequiredMixin, CreateView):
    """
    This class is used to add post
    """

    template_name = 'home/add_post.html'
    model = Post
    form_class = CreatePost
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(addPost, self).form_valid(form)


class postView(DetailView):
    """
    This class is used to display post
    """
    template_name = 'home/postView.html'
    model = Post
    context_object_name = 'post'


class postView2(DetailView):
    """
    This class is used to display post
    """
    template_name = 'home/postView.html'
    model = Post
    context_object_name = 'post'


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    This class is used to delete post
    """
    model = Post
    success_url = '/'
    template_name = 'home/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.user


class EditPost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    This class is used to edit post
    """
    model = Post
    template_name = 'home/edit_post.html'
    form_class = CreatePost
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EditPost, self).form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.user


class PostLike(RedirectView):
    """
    This class is used to like post
    """
    model = Post

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, id=kwargs.get('pk'))
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user.id)
        else:
            post.likes.add(request.user.id)
        post.save()

        return HttpResponseRedirect(reverse('home'))


class Comments(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    This class is used to add comment
    """
    model = Comment
    template_name = 'home/comments.html'
    form = AddCommentForm
    context_object_name = 'comments'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Comments, self).form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.user
