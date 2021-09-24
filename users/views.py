from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import CustomUserChangeForm, CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class EditProfileView(UpdateView):
    form_class= CustomUserChangeForm
    success_url = reverse_lazy('home')
    template_name = 'edit_profile.html'

    def get_object(self):
        return self.request.user