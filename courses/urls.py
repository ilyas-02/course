from django.urls import path, include
from rest_framework import routers
from .views import *

app_name = 'courses'


router = routers.SimpleRouter()
router.register(r'group', GroupViewSet)
router.register(r'student', StudentViewSet)
router.register(r'mentor', MentorViewSet)
router.register(r'course', CourseViewSet)


urlpatterns = [
    path('', include(router.urls), name='group'),
    path('', include(router.urls), name='student'),
    path('', include(router.urls), name='mentor'),
    path('', include(router.urls), name='course'),
    path('room/', RoomsList.as_view(), name='room-list'),
    path('api/v1/', include(router.urls)),
]
