from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Note, Project
from .serializers import NoteSerializer


class NoteList(APIView):
    """
    List all Notes, or create a new Note, for a given Project.
    """

    def get_project(self, project_id):
        try:
            return Project.objects.get(pk=project_id)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, project_id, format=None):
        project = self.get_project(project_id)
        notes = Note.objects.filter(project=project)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    def post(self, request, project_id, format=None):
        self.get_project(project_id)
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteDetail(APIView):
    """
    Retrieve, update or delete a Note.
    """

    def get_project(self, project_id):
        try:
            return Project.objects.get(pk=project_id)
        except Project.DoesNotExist:
            raise Http404

    def get_note(self, note_id):
        try:
            return Note.objects.get(pk=note_id)
        except Note.DoesNotExist:
            raise Http404

    def get(self, request, project_id, note_id, format=None):
        self.get_project(project_id)

        serializer = NoteSerializer(self.get_note(note_id))
        return Response(serializer.data)

    def put(self, request, project_id, note_id, format=None):
        project = self.get_project(project_id)
        note = self.get_note(note_id)
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, project_id, note_id, format=None):
        self.get_project(project_id)
        note: Project = self.get_note(note_id)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
