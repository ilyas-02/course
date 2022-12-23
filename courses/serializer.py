from rest_framework import serializers

from .models import Students, Group, Course, Rooms, Mentor


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'start_date', 'end_date')


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = 'id name age phone email course group'.split()


class GroupSerializer(serializers.ModelSerializer):
    # student = StudentsSerializer(read_only=True, many=True)

    class Meta:
        model = Group
        fields = 'id name_group num room start_lesson end_lesson'.split()


class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = 'id name age phone email course group'.split()


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = 'id num_room'.split()
