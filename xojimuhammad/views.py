from django.contrib import messages
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.



from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from xojimuhammad.models import Post
from .forms import PostForm, EditForm
from django.contrib.auth import logout


from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    # fields = "__all__"


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title', 'body']
    success_url = reverse_lazy('xojimuhammad:home')



class DeletePostView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('xojimuhammad:home')


def about_page(request):
    return render(request, 'about.html')



def user_post(requset):
    return render(requset, 'user_posts.html')




class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')




class CustomLoginView(LoginView):
    template_name = 'login.html'

class LogoutView(LogoutView):
    template_name = 'logged_out.html'

    def form_valid(self, form):

        response = super().form_valid(form)

        return response

    def form_invalid(self, form):

        return super().form_invalid(form)
