from django.urls import path
from courses.views import search, home
urlpatterns = [
    path('search/', search, name='search'),
    path('', home, name='home'),
]
