from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Rooms(models.Model):
    num_room = models.CharField(max_length=50)

    def __str__(self):
        return self.num_room


class Group(models.Model):
    name_group = models.CharField(max_length=50)
    num = models.IntegerField()
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name='group')
    start_lesson = models.CharField(max_length=50)
    end_lesson = models.CharField(max_length=50)

    def __str__(self):
        return self.name_group


class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.IntegerField()
    email = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='students')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name


class Mentor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.IntegerField()
    email = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='mentor')
    group = models.ManyToManyField(Group, blank=True, related_name='mentor')

    def __str__(self):
        return self.name


