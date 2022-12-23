from django.contrib import admin
from .models import Students, Group, Course, Rooms, Mentor


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'course', 'group', 'phone', 'email')
    list_display_links = ('id', 'name', 'course', 'group')
    search_fields = ('id', 'name', 'course')


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_group', 'num', 'room', 'start_lesson', 'end_lesson')
    list_display_links = ('id', 'name_group',)
    search_fields = ('id', 'name_group')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_date', 'end_date')
    list_display_links = ('id', 'name',)
    search_fields = ('id', 'name')


class MentorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'phone', 'email', 'course')
    list_display_links = ('id', 'name', 'course')
    search_fields = ('id', 'name', 'course')


class RoomsAdmin(admin.ModelAdmin):
    list_display = ('id', 'num_room')
    list_display_links = ('id', 'num_room')
    search_fields = ('id', 'num_room')


admin.site.register(Students, StudentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Rooms, RoomsAdmin)
admin.site.register(Mentor, MentorAdmin)

# Register your models here.
