from django.shortcuts import render
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, LoginForm


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
            form.save()  # Save the user to the database
            return redirect('forum:login')  # Redirect to login page
    else:
        form = CustomUserCreationForm()
    return render(request, 'forum/register.html', {'form': form})

class IndexView(generic.TemplateView):
    template_name = 'forum/index.html'

class CategoriesView(generic.TemplateView):
    template_name = 'forum/categories.html'

class AboutView(generic.TemplateView):
    template_name = 'forum/about.html'
