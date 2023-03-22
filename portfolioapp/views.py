from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm, ApplicationForm, ProjectForm
from .models import Review, Service, Application, Project


def index(request):
    messages.info(request, 'Welcome to my portfolio, I am Leroy Eugene Oroni.')
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
            messages.success(request, 'Your review has been successfully submitted. Thank you for your opinion')
            return redirect(reverse('index') + '#reviews')
    else:
        messages.error(request, 'Sorry there was an error with processing your review. Please try again.')
        form = ReviewForm()
    return render(request, 'reviews.html', {'form': form})


def submit_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.save()
            messages.success(request, 'Your application was submitted successfully. We will get back to you shortly.')
            messages.info(request, 'Thank you for choosing to work with us.')
            return redirect(reverse('index') + '#home')
    else:
        messages.success(request, 'Sorry there was a problem uploading your application')
        form = ApplicationForm()
    return render(request, 'admin usage/requests.html', {'form': form})


def reviews(request):
    messages.info(request, 'On this page, it is our humble request that you leave us your opinion of your experience '
                           'with us.')
    services = Service.objects.values('name')
    return render(request, 'reviews.html', {'services': services})


def submit_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            messages.success(request, 'Your project was submitted successfully.')
            return redirect(reverse('index') + '#work')
    else:
        form = ProjectForm()
        messages.error(request, 'Sorry there was an error uploading your project. Please try again.')
    return render(request, 'index.html', {'form': form})


@login_required(login_url='admin:login')
def applications(request):
    messages.info(request, 'Welcome to the applications page. Here you will find applications pending to be reviewed.')
    applications = Application.objects.order_by('-created_at')
    context = {'applications': applications}
    return render(request, 'admin usage/requests.html', context)


@login_required(login_url='admin:login')
def projects(request):
    messages.info(request, 'Welcome to the project entry page. Here you can upload the projects you have completed '
                           'for other potential customers to view. Please note that only completed projects are to be'
                           ' submitted here.')
    services = Service.objects.all()
    return render(request, 'admin usage/projects.html', {'services': services})
