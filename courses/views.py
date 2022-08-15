from django.shortcuts import render, HttpResponse
from courses.models import Course
from rest_framework.generics import ListCreateAPIView
from courses import serializers
from django.core.paginator import Paginator
from django.contrib.auth.decorators import permission_required


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
    if request.GET.get('name') != None:
        query = Course.objects.filter(name__icontains=request.GET.get('name'))
    else:
        query = Course.objects.all()

    # Order
    query = query.order_by(request.GET.get('order') or 'price')

    # Filter by price
    if 'max-price' in request.GET.keys():
        query = query.filter(price__lte=request.GET['max-price'])

    # # Filter By participants
    # if 'max-participants' in request.GET.keys():
    #     query.filter(participants__gte=request.GET['max-participants'])

    # Filter By rating
    '''if 'max-rating' in request.GET.keys() and 'min-rating' in request.GET.keys():
        query.filter(rating__lte=request.GET['min-rating'],
                     rating__gte=request.GET['max-rating'])'''
    # All courses count
    coursesCount = query.count()
    # Pagination
    page = Paginator(query, 20)


    return render(request, 'searchResult.html', 
    {
        'courses': page.page(request.GET.get('page') or 1).object_list,
        'coursesCount': coursesCount,
        'searchName': request.GET.get('name') or '',
        'searchOrder': request.GET.get('order') or 'price',
        'searchMaxPrice': request.GET.get('max-price') or '2500000',
        'currentPage': int(request.GET.get('page') or 1),
        'pages': page.page_range
    })


def course_details(request, id):
    query = Course.objects.get(id=id)
    return render(request, 'courseDetails.html', {'course': query})
