from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from forum import views

app_name = 'forum'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('categories/', views.CategoriesView.as_view(), name='categories'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/add', views.post_add_view, name='post_add'),
    path('my-posts/', views.my_posts_view, name='my_posts'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit', views.profile_edit_view, name='profile_edit'),
    path('profile/delete', views.profile_delete_view, name='profile_delete'),
    path('browse-profiles/', views.browse_profiles_view, name='browse_profiles'),
    path('browse-profiles/<int:profile_id>/', views.browse_profile_view, name='browse_profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

htmx_urlpatterns = [
    #POST ajax
    path('like-post/', views.like_post, name='like_post'),
    path('add-comment/', views.add_comment, name='add_comment'),
    path('edit-comment/', views.edit_comment, name='edit_comment'),
    path('delete-comment/', views.delete_comment, name='delete_comment'),
    path('edit-my-post/', views.edit_my_post, name='edit_my_post'),
    path('delete-my-post/', views.delete_my_post, name='delete_my_post'),

    #GET ajax
    path('categories/filter/', views.filter_categories, name='filter_categories'),
    path('my-posts/sort/', views.sort_my_posts, name='sort_my_posts'),
]

urlpatterns += htmx_urlpatterns