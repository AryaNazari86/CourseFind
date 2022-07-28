from django.urls import path
from courses.views import search, home, course_details, CourseList, SourceDel
urlpatterns = [
    path('search/', search, name='search'),
    path('', home, name='home'),
    path('course/<int:id>', course_details, name='course'),
    path('api/', CourseList.as_view()),
    path('del/', SourceDel)
]
