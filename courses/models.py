from django.db import models


class CourseSource(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()


class Course(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(
        upload_to='Course-Images/', default='default-course.png')
    url = models.URLField()
    source = models.ForeignKey(
        CourseSource, related_name='courses', on_delete=models.CASCADE)
