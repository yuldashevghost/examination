from django.urls import path
from xojimuhammad.views import HomeView, LogoutView, CustomLoginView, about_page, AddPost, ArticleDetailView, DeletePostView, user_post, UpdatePostView, RegisterView

app_name = 'xojimuhammad'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', about_page, name='about'),
    path('post_form/', AddPost.as_view(), name='post_form'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('post_coniform_delete/', DeletePostView.as_view(), name='post_coniform_delete'),
    path('user_post/', user_post, name='user_post'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='post_detail'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_epost'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete_epost')
]