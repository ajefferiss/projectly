from rest_framework import serializers
from .models import Project, Note, Script, Calendar


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name_text', 'pub_date']


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'project', 'note_text']


class ScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Script
        fields = ['id', 'project', 'script_text']


class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = ['id', 'project', 'start_date', 'end_date', 'completed']
