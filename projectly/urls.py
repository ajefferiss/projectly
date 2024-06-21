"""
URL configuration for projectly project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from projects import projects_views, note_views, scripts_views, calendar_views

urlpatterns = [
    path('projects', projects_views.ProjectList.as_view()),
    path('projects/<int:pk>', projects_views.ProjectDetail.as_view()),
    path('projects/<int:project_id>/notes', note_views.NoteList.as_view()),
    path(
        'projects/<int:project_id>/notes/<int:note_id>',
        note_views.NoteDetail.as_view()
    ),
    path(
        'projects/<int:project_id>/scripts',
        scripts_views.ScriptList.as_view()
    ),
    path(
        'projects/<int:project_id>/scripts/<int:script_id>',
        scripts_views.ScriptDetail.as_view()
    ),
    path(
        'projects/<int:project_id>/calendar',
        calendar_views.CalendarProjectList.as_view()
    ),
    path('projects/<int:project_id>/calendar/<int:entry_id>',
         calendar_views.CalendarProjectDetail.as_view()
         ),
    path('calendar/search', calendar_views.CalendarSearchDetails.as_view()),
    path('admin/', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)
