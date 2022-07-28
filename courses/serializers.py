from rest_framework import serializers
from django.db import models
from courses.models import Course, CourseSource


class Course(serializers.ModelSerializer):
    name = serializers.CharField()
    price = serializers.IntegerField()
    image_url = serializers.URLField()
    participants = serializers.IntegerField()
    teacher = models.CharField(max_length=50)
    url = serializers.URLField()
    source = CourseSource()
    description = serializers.CharField()

    class Meta:
        model = Course
        fields = ('name', 'price', 'image_url', 'source', 'teacher',
                  'url', 'price', 'participants', 'description')
