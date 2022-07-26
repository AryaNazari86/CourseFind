from django.urls import path
from courses.views import search, home, CourseList, SourceDel
urlpatterns = [
    path('search/', search, name='search'),
    path('', home, name='home'),
    path('add/', CourseList.as_view()),
    path('del/', SourceDel)
]
