from urllib import response
from django.shortcuts import render, HttpResponse
from courses.models import Course


def home(request):
    return render(request, 'index.html')


def search(request):
    query = Course.objects.filter(name__icontains=request.GET['name'])

    # Order
    if 'order' in request.GET.keys():
        query.order_by(request.GET['order'])
    else:
        query.order_by('price')

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

    return render(request, 'search.html', {'courses': query})


def course_details(request, course_id):
    context = {'details': Course.objects.get(id=course_id)}
    return render(request, '')
