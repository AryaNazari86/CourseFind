from urllib import response
from django.shortcuts import render, HttpResponse
from courses.models import Course


def test(request):
    response = ''
    response += '<ul>'.join(Course.objects.all().values_list('name', flat=True))
    response += '</ul>'
    return HttpResponse(response)


def search(request):
    query = Course.objects.filter(name__icontains=request.GET['name'])
    return HttpResponse(query[0].name)
