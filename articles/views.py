from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied 
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView

from django.urls import reverse_lazy
from .models import Article

# Create your views here.


class ArticleListView(LoginRequiredMixin ,ListView):
    model= Article
    template_name = 'article_list.html'
    # ordering = ['-id']
    login_url= 'login'

class ArticleDetailView(LoginRequiredMixin ,DetailView):  
    model = Article
    template_name = 'article_detail.html'
    login_url= 'login'

class ArticleUpdateView(LoginRequiredMixin ,UpdateView):  
    model = Article
    fields = ('title', 'body', 'img_field_name', 'file_field_name',)
    template_name = 'article_edit.html'
    success_url = reverse_lazy('article_list')
    login_url= 'login'

    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ArticleDeleteView(LoginRequiredMixin ,DeleteView):  
 
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url= 'login'

    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ArticleCreateView(LoginRequiredMixin ,CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body' , 'img_field_name', 'file_field_name',)
    login_url= 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)