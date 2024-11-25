from django.shortcuts import render
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm  # Or UserCreationForm if you're not using a custom form


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Log the user in
            return redirect('forum:index')  # Redirect to the home page or dashboard
        else:
            # Invalid credentials
            return render(request, 'forum/login.html', {'error': 'Invalid credentials'})

    return render(request, 'forum/login.html')

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

