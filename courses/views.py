from urllib import response
from django.shortcuts import render, HttpResponse
from courses.models import Course
from rest_framework.generics import ListCreateAPIView
from courses import serializers


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

# API


class CourseList(ListCreateAPIView):
    serializer_class = serializers.Course
    queryset = Course.objects.all()


def SourceDel(request):
    # TODO:Change this to post
    Course.objects.filter(source__id=request.GET['id']).delete()
    return HttpResponse('!')


# Courses
def search(request):
    query = Course.objects.filter(name__icontains=request.GET['name'])

    # Order
    query = query.order_by(request.GET.get('order') or 'price')

    # Filter by price
    if 'min-price' in request.GET.keys() and 'max-price' in request.GET.keys():
        query.filter(price__lte=request.GET['min-price'],
                     price__gte=request.GET['max-price'])

    # Filter By participants
    if 'max-participants' in request.GET.keys() and 'min-participants' in request.GET.keys():
        query.filter(participants__lte=request.GET['min-participants'],
                     participants__gte=request.GET['max-participants'])

    # Filter By rating
    if 'max-rating' in request.GET.keys() and 'min-rating' in request.GET.keys():
        query.filter(rating__lte=request.GET['min-rating'],
                     rating__gte=request.GET['max-rating'])

    return render(request, 'searchResult.html', {'courses': query})


def course_details(request, id):
    query = Course.objects.get(id=id)
    print(query.price)
    return render(request, 'courseDetails.html', {'course': query})
