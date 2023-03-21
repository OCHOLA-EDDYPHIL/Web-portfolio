from django import forms

from .models import Review, Application, Project


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['email', 'service', 'opinion', 'location', 'description']
        widgets = {
            'service': forms.Select(
                attrs={'class': 'form-select form-control', 'aria-label': 'Default select example'}),
            'opinion': forms.Select(
                attrs={'class': 'form-select form-control opinion', 'aria-label': 'Default select example'}),
            'description': forms.Textarea(attrs={'class': 'form-control textarea', 'placeholder': 'Briefly describe'
                                                                                                  'your experience'})
        }


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'email', 'subject', 'message', 'location']
        widgets = {
            'subject': forms.Select(
                attrs={'class': 'form-select form-control', 'aria-label': 'Default select example'}),
            'message': forms.Textarea(attrs={'class': 'form-control textarea', 'placeholder': 'Enter your message'})
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['service', 'location', 'description']
        widgets = {
            'service': forms.Select(
                attrs={'class': 'form-select form-control', 'aria-label': 'Default select example'}),
            'description': forms.Textarea(attrs={'class': 'form-control textarea', 'placeholder': 'Describe the '
                                                                                                  'project and the '
                                                                                                  'outcome of your '
                                                                                                  'participation'})
        }
