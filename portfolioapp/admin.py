from django.contrib import admin
from .models import Service, Review, Application, Project


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'service', 'opinion', 'location', 'created_at')


# admin.site.register(Request, RequestAdmin)

admin.site.register(Review, ReviewAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


admin.site.register(Service, ServiceAdmin)


class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'subject', 'message', 'location', 'created_at')


admin.site.register(Application, RequestAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'service', 'location', 'description')


admin.site.register(Project, ProjectAdmin)
