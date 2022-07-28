from django.urls import path
from courses.views import search, home, course_details, CourseList, SourceDel
urlpatterns = [
    path('search/', search, name='search'),
    path('', home, name='home'),
    path('course/', course_details, name='course'),
    path('add/', CourseList.as_view()),
    path('del/', SourceDel)
]
