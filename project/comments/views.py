from .models import Comments
from home.models import Post
from .forms import AddCommentForm
from django.views.generic import (
    TemplateView, ListView,
    CreateView, UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin
)
from django.urls import reverse_lazy
from django.utils import timezone


class Comments(TemplateView):
    """
    This class is used to display all comments
    """
    template_name = 'comments/comments.html'
    model = Comments
    context_object_name = 'comments'
    form_class = AddCommentForm
    form = AddCommentForm()
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(Comments, self).get_context_data(**kwargs)
        context['comments'] = Comments.model.objects.filter(post=self.kwargs['pk'])
        context['title'] = Post.objects.get(id=self.kwargs['pk']).title
        context['image'] = Post.objects.get(id=self.kwargs['pk']).image
        context['post'] = Post.objects.get(id=self.kwargs['pk']).pk
        context['user_id'] = self.request.user.id
        return context

    def get_queryset(self):
        return Comments.model.objects.filter(post=self.kwargs['pk'])


class AddComment(LoginRequiredMixin, CreateView):
    model = Comments
    template_name = 'comments/addComment.html'
    form_class = AddCommentForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.created_on = timezone.now()
        form.instance.user_id = self.request.user.id
        form.instance.post_id = self.kwargs['pk']
        return super(AddComment, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AddComment, self).get_context_data(**kwargs)
        context['post_id'] = Post.objects.get(id=self.kwargs['pk']).pk
        return context

    def get_queryset(self):
        return Comments.model.objects.filter(post=self.kwargs['pk'])


class DeleteComment(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    This class is used to delete comment
    """
    model = Comments
    success_url = '/'
    template_name = 'comments/comment_confirm_delete.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.user


class EditComment(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    This class is used to edit comment
    """
    model = Comments
    template_name = 'comments/edit_comment.html'
    form_class = AddCommentForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EditComment, self).form_valid(form)

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.user
