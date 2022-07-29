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
    price = models.IntegerField(default=-1)
    image_url = models.URLField(
        default='https://learning.unv.org/theme/image.php/mb2aofk/theme/1647859262/course-default')
    participants = models.IntegerField(default=-1)
    rating = models.FloatField(default=-1)
    teacher = models.CharField(max_length=50, default='Teacher')
    url = models.URLField()
    source = models.ForeignKey(
        CourseSource, related_name='courses', on_delete=models.CASCADE)
    description = models.TextField(default='No Information')

    def __str__(self):
        return self.name
