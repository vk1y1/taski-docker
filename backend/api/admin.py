from django.contrib import admin

from api.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
