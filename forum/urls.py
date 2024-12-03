from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
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

]