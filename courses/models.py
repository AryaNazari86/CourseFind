from distutils.command.upload import upload
from email.policy import default
from django.db import models


class CourseSource(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    image = models.ImageField(
        upload_to='CourseSources-Images/', default='default-course.png')


class Course(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image_url = models.URLField()
    participants = models.IntegerField(default=0)
    rating = models.FloatField(default=0)

    url = models.URLField()
    source = models.ForeignKey(
        CourseSource, related_name='courses', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
