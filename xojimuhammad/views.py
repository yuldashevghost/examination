from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from xojimuhammad.forms import RegistrationForm, LoginForm

from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from xojimuhammad.models import Post
from .forms import PostForm


# Create your views here.
# def home_page(request):
#     return render(request, 'home.html')

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
    # form_class = PostForm
    template_name = 'update_post.html'
    fields = ['title', 'body']
    success_url = reverse_lazy('xojimuhammad:home')

class DeletePostView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('xojimuhammad:home')


def about_page(request):
    return render(request, 'about.html')



def user_post(requset):
    return render(requset, 'user_posts.html')



def logout_page(request):
    return render(request, 'logout.html')



def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('xojimuhammad:login_page')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})





def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('xojimuhammad:home')
            else:

                pass
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

