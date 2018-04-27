from django.contrib import admin
from .models import Project, ActivityJournal, Registry


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'description', )


class RegistryAdmin(admin.ModelAdmin):
    list_filter = ('start',)
    list_display = ('user', 'start', 'end')


class ActivityJournalAdmin(admin.ModelAdmin):
    list_filter = ('start', 'end', 'project',)
    list_display = ('user', 'project', 'start', 'end')


admin.site.register(Registry, RegistryAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ActivityJournal, ActivityJournalAdmin)
