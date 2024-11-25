from django.shortcuts import render
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'forum/index.html'

class CategoriesView(generic.TemplateView):
    template_name = 'forum/categories.html'

class AboutView(generic.TemplateView):
    template_name = 'forum/about.html'

class RegisterView(generic.TemplateView):
    template_name = 'forum/register.html'