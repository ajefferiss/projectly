from typing import Any
from django.http import Http404
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Calendar, Project
from .serializers import CalendarSerializer

from datetime import datetime
from datetime import timedelta


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


class SearchBase(APIView):
    """
    Defines common base behaviour for the search views
    """

    def error(self, msg: str) -> Response:
        return Response(
            data={"error": msg},
            status=status.HTTP_400_BAD_REQUEST
        )


class CalendarSearchDetails(SearchBase):
    """
    Search for calendar entries between two given dates
    """

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    def post(self, request, format=None):
        start = request.data.get('start_date', None)
        end = request.data.get('end_date', None)
        exclude_completed = request.data.get('exclude_completed', False)

        if not start or not end:
            return self.error("Both start_date and end_date are required for search")

        start_date = datetime.strptime(start, '%Y-%m-%d').date()
        end_date = datetime.strptime(end, '%Y-%m-%d').date()

        if end_date < start_date:
            return self.error("end_date must be after start_date")

        query = (Q(start_date__gte=start_date))
        query.add(Q(end_date__lte=end_date), Q.AND)

        if exclude_completed:
            query.add(Q(completed=False), Q.AND)

        entries = Calendar.objects.filter(query)
        serializer = CalendarSerializer(entries, many=True)
        return Response(serializer.data)


class CalendarUpcomingDetails(SearchBase):
    """
    Upcoming entries for the calendar
    """

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    def post(self, request, format=None):
        try:
            date_offset = int(abs(request.data.get('days', 7)))
        except TypeError:
            return self.error("Days value invalid")
        exclude_completed = request.data.get('exclude_completed', False)

        today = datetime.today().strftime('%Y-%m-%d')
        end_date = datetime.strftime(
            datetime.today() + timedelta(days=date_offset),
            '%Y-%m-%d'
        )

        query = (Q(end_date__gte=today))
        query.add(Q(end_date__lte=end_date), Q.AND)

        if exclude_completed:
            query.add(Q(completed=False), Q.AND)

        entries = Calendar.objects.filter(query)
        serializer = CalendarSerializer(entries, many=True)
        return Response(serializer.data)
