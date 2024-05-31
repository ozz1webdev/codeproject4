from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Profile
from .forms import ProfileForm


class Profiles(TemplateView):
    """User Profile View"""
    template_name = 'profiles/profile.html'

    def get_context_data(self, **kwargs):
        profile = Profile.objects.get(user=self.kwargs['pk'])
        context = {
            'profile': profile,
            'form': ProfileForm(instance=profile),
        }
        return context


class EditProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a profile"""

    model = Profile
    form_class = ProfileForm

    def form_valid(self, form):
        self.success_url = f'/profiles/user/{self.kwargs["pk"]}/'
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().user
