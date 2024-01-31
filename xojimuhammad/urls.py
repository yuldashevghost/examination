from django.urls import path
from xojimuhammad.views import HomeView, about_page, AddPost, ArticleDetailView, DeletePostView, user_post, login_page, logout_page, register_page, UpdatePostView

app_name = 'xojimuhammad'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', about_page, name='about'),
    path('post_form/', AddPost.as_view(), name='post_form'),
    # path('post_detail/', post_detail, name='post_detail'),
    path('post_coniform_delete/', DeletePostView.as_view(), name='post_coniform_delete'),
    path('user_post/', user_post, name='user_post'),
    path('login_page/', login_page, name='login_page'),
    path('logout_page/', logout_page, name='logout_page'),
    path('register/', register_page, name='register_page'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='post_detail'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_epost'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete_epost')
]