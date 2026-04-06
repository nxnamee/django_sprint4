from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'pages/about.html'


class RulesView(TemplateView):
    template_name = 'pages/rules.html'


def csrf_failure(request, reason=""):
    return render(request, 'pages/403csrf.html')


def page_not_found(request, exception):
    return render(request, 'pages/404.html')


def server_error(request):
    return render(request, 'pages/500.html')


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog:profile', username=user.username)
    else:
        form = UserCreationForm()
    return render(request, 'registration/registration_form.html', {'form': form})
