from django.contrib import admin

from .models import Project, Note, Script

admin.site.register(Project)
admin.site.register(Note)
admin.site.register(Script)
