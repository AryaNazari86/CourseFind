from django.urls import path
from courses.views import search, home
urlpatterns = [
    path('search/', search),
    path('', home),
]
