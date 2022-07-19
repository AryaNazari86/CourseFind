from django.urls import path
from courses.views import search, home, CourseList
urlpatterns = [
    path('search/', search, name='search'),
    path('', home, name='home'),
    path('a/', CourseList.as_view()),
]
