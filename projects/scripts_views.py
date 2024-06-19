from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Script, Project
from .serializers import ScriptSerializer


class ScriptList(APIView):
    """
    List all Scripts, or create a new Script, for a given Project.
    """

    def get_project(self, project_id):
        try:
            return Project.objects.get(pk=project_id)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, project_id, format=None):
        project = self.get_project(project_id)
        scripts = Script.objects.filter(project=project)
        serializer = ScriptSerializer(scripts, many=True)
        return Response(serializer.data)

    def post(self, request, project_id, format=None):
        self.get_project(project_id)
        serializer = ScriptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ScriptDetail(APIView):
    """
    Retrieve, update or delete a Script.
    """

    def get_project(self, project_id):
        try:
            return Project.objects.get(pk=project_id)
        except Project.DoesNotExist:
            raise Http404

    def get_script(self, script_id):
        try:
            return Script.objects.get(pk=script_id)
        except Script.DoesNotExist:
            raise Http404

    def get(self, request, project_id, script_id, format=None):
        self.get_project(project_id)

        serializer = ScriptSerializer(self.get_script(script_id))
        return Response(serializer.data)

    def put(self, request, project_id, script_id, format=None):
        project = self.get_project(project_id)
        script = self.get_script(script_id)
        serializer = ScriptSerializer(script, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, project_id, script_id, format=None):
        self.get_project(project_id)
        script: Project = self.get_script(script_id)
        script.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
