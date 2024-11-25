from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from forum import views
from forum.views import RegisterView

app_name = 'forum'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('categories/', views.CategoriesView.as_view(), name='categories'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('login/', LoginView.as_view(template_name='forum/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]