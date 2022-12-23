from django.shortcuts import render
from rest_framework import generics, mixins, viewsets
from .models import Students, Group, Course, Rooms, Mentor
from .serializer import StudentsSerializer, GroupSerializer, CourseSerializer, RoomSerializer, MentorSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer


# class StudentDetail(generics.RetrieveAPIView):
#     queryset = Students.objects.all()
#     serializer_class = StudentsSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class RoomsList(generics.RetrieveAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomSerializer


class MentorViewSet(viewsets.ModelViewSet):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
