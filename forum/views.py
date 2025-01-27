from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .forms import CustomUserCreationForm, LoginForm, UserEditForm, ProfileEditForm
from .models import Post, PostLikedbyUser, Profile


def login_view(request):
    if request.method == 'POST': # ak uz submitol
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect('forum:index')
            else:
                form.add_error(None, 'Invalid username or password')
    else: # ak si este len loadol form
        form = LoginForm()

    return render(request, 'forum/login.html', {'form': form})


def logout_view(request):
    logout(request)  # Log the user out
    return redirect('forum:index')


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return redirect('forum:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'forum/register.html', {'form': form})


def index_view(request):
    most_liked_posts = Post.objects.all().order_by('-like_count')[:5]

    most_recent_posts = Post.objects.all().order_by('-created_at')[:5]

    return render(request, 'forum/index.html', {
        'most_liked_posts': most_liked_posts,
        'most_recent_posts': most_recent_posts,
    })


class CategoriesView(generic.TemplateView):
    template_name = 'forum/categories.html'


class AboutView(generic.TemplateView):
    template_name = 'forum/about.html'


def post_list(request):
    return None


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'forum/post_detail.html', {'post': post})


@require_POST
@login_required
def add_comment(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    content = request.POST.get('content')
    if content:
        comment = post.comments.create(content=content, user_id=request.user.id, post_id=post.id)
        post.comments.add(comment)
        return render(request, 'forum/partials/post_comments.html', {'post': post})


@login_required
def profile_view(request):
    profile = request.user.profile
    return render(request, 'forum/profile.html', {'profile': profile})


@login_required
def profile_edit_view(request):
    user = request.user
    profile = user.profile
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=user)
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('forum:profile')
    else:
        user_form = UserEditForm(instance=user)
        profile_form = ProfileEditForm(instance=profile)

    return render(request, 'forum/profile_edit.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def profile_delete_view(request):
    user = request.user
    if request.method == 'POST':
        logout(request)
        user.delete()
        return redirect('forum:index')
    return render(request, 'forum/profile_edit.html')


def post_add_view(request):
    return None


def like_post(request):
    return None


@login_required
def like_post(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    like = PostLikedbyUser.objects.filter(post_id=post, user_id=request.user)
    if like.exists():
        like.delete()
        post.like_count -= 1
    else:
        like = PostLikedbyUser(post_id=post.id, user_id=request.user.id)
        like.save()
        post.like_count += 1
    post.save()
    return HttpResponse(post.like_count)
