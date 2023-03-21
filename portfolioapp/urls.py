from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reviews', views.reviews, name='reviews'),
    path('submit_review', views.submit_review, name='submit_review'),
    path('submit_application', views.submit_application, name='submit_application'),
    path('applications', views.applications, name='applications'),
    path('projects', views.projects, name='projects'),
    path('submit_project', views.submit_project, name='submit_project'),
]
