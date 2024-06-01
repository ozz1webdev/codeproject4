from .models import Comments
from .forms import AddCommentForm
from django.views.generic import (
    TemplateView, ListView,
    CreateView, UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin
)
# Create your views here.


class Comments(ListView):
    """
    This class is used to display all comments
    """
    template_name = 'comments/comments.html'
    model = Comments
    context_object_name = 'comments'
    form_class = AddCommentForm
    success_url = '/'

    def get_queryset(self):
        return Comments.model.objects.filter(post=self.kwargs['pk'])

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddComment, self).form_valid(form)


class AddComment(LoginRequiredMixin, CreateView):
    """
    This class is used to add comment
    """
    model = Comments
    template_name = 'comments/comments.html'
    form_class = AddCommentForm
    success_url = '/comments'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddComment, self).form_valid(form)


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
