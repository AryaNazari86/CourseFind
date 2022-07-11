from django.urls import path
from courses.views import test, search
urlpatterns = [
    path('results/', test),
    path('search/', search),
]
