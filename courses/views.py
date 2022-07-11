from urllib import response
from django.shortcuts import render, HttpResponse
from courses.models import Course


def home(request):
    return render(request, 'index.html')


def search(request):
    query = Course.objects.filter(name__icontains=request.GET['name'])

    if 'order' in request.GET.keys():
        query.order_by(request.GET['order'])
    else:
        query.order_by('price')

    return HttpResponse(query[0])
