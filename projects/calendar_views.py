from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Calendar, Project
from .serializers import CalendarSerializer


class CalendarProjectList(APIView):
    """
    List all Calendar Entries, or create a new Entry, for a given Project.
    """

    def get_project(self, project_id):
        try:
            return Project.objects.get(pk=project_id)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, project_id, format=None):
        project = self.get_project(project_id)
        entries = Calendar.objects.filter(project=project)
        serializer = CalendarSerializer(entries, many=True)
        return Response(serializer.data)

    def post(self, request, project_id, format=None):
        self.get_project(project_id)
        serializer = CalendarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CalendarProjectDetail(APIView):
    """
    Retrieve, update or delete a Calendar entry.
    """

    def get_project(self, project_id):
        try:
            return Project.objects.get(pk=project_id)
        except Project.DoesNotExist:
            raise Http404

    def get_entry(self, script_id):
        try:
            return Calendar.objects.get(pk=script_id)
        except Calendar.DoesNotExist:
            raise Http404

    def get(self, request, project_id, entry_id, format=None):
        self.get_project(project_id)

        serializer = CalendarSerializer(self.get_entry(entry_id))
        return Response(serializer.data)

    def put(self, request, project_id, entry_id, format=None):
        project = self.get_project(project_id)
        entry = self.get_entry(entry_id)
        serializer = CalendarSerializer(entry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, project_id, entry_id, format=None):
        self.get_project(project_id)
        entry = self.get_entry(entry_id)
        entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
