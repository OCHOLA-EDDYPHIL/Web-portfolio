from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm, ApplicationForm, ProjectForm
from .models import Review, Service, Application, Project


def index(request):
    services = Service.objects.all()
    reviews = Review.objects.order_by('-id')
    projects = Project.objects.order_by('-created_at')
    context = {'services': services, 'reviews': reviews, 'projects': projects}
    return render(request, 'index.html', context)


def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            return redirect(reverse('index') + '#reviews')
    else:
        form = ReviewForm()
    return render(request, 'reviews.html', {'form': form})


def submit_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.save()
            return redirect(reverse('index') + '#home')
    else:
        form = ApplicationForm()
    return render(request, 'admin usage/requests.html', {'form': form})


def reviews(request):
    services = Service.objects.values('name')
    return render(request, 'reviews.html', {'services': services})


def submit_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect(reverse('index') + '#work')
    else:
        form = ProjectForm()
    return render(request, 'index.html', {'form': form})


@login_required(login_url='admin:login')
def applications(request):
    applications = Application.objects.order_by('-created_at')
    context = {'applications': applications}
    return render(request, 'admin usage/requests.html', context)


@login_required(login_url='admin:login')
def projects(request):
    services = Service.objects.all()
    return render(request, 'admin usage/projects.html', {'services': services})
