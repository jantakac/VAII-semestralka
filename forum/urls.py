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
    #path('success/', lambda request: path.render(request, 'success.html'), name='success'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/add', views.post_add_view, name='post_add'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit', views.profile_edit_view, name='profile_edit'),
    path('profile/delete', views.profile_delete_view, name='profile_delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

htmx_urlpatterns = [
    path('like-post/', views.like_post, name='like_post'),
    path('add-comment/', views.add_comment, name='add_comment'),
    path('filter-categories/', views.filter_categories, name='filter_categories'),
]

urlpatterns += htmx_urlpatterns