from django.urls import path
from xojimuhammad.views import home_page, about_page, post_form, post_detail, post_coniform_delete, user_post, login_page, logout_page, register_page

app_name = 'xojimuhammad'

urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('post_form/', post_form, name='post_form'),
    path('post_detail/', post_detail, name='post_detail'),
    path('post_coniform_delete/', post_coniform_delete, name='post_coniform_delete'),
    path('user_post/', user_post, name='user_post'),
    path('login_page/', login_page, name='login_page'),
    path('logout_page/', logout_page, name='logout_page'),
    path('register/', register_page, name='register_page'),
]