from django.contrib import messages
from django.shortcuts import render, redirect

from xojimuhammad.forms import UserRegisterModelForm


# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def about_page(request):
    return render(request, 'about.html')

def post_coniform_delete(request):
    return render(request, 'post_confirm_delete.html')

def post_detail(request):
    return render(request, 'post_detail.html')

def post_form(requset):
    return render(requset, 'post_form.html')

def user_post(requset):
    return render(requset, 'user_posts.html')

def login_page(request):
    return render(request, 'login.html')

def logout_page(request):
    return render(request, 'logout.html')

def register_page(request):

    if request.method == 'GET':
        form = UserRegisterModelForm()
        return render(request, "register.html", {"form": form})

    elif request.method == 'POST':
        form = UserRegisterModelForm(data=request.POST)
        if form.is_valid():
            messages.success(request, "User successfully registered")
            form.save()
            return redirect("bookshop:login")
        else:
            return render(request, "register.html", {"form": form})

    return render(request, 'register.html')

