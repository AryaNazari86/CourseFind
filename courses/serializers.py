from rest_framework import serializers
from django.db import models
from courses.models import Course, CourseSource


class Course(serializers.ModelSerializer):
    name = serializers.CharField()
    price = serializers.IntegerField()
    image_url = serializers.URLField()
    participants = serializers.IntegerField()

    url = serializers.URLField()
    source = CourseSource()

    class Meta:
        model = Course
        fields = ('name', 'price', 'image_url', 'source',
                  'url', 'price', 'participants')
