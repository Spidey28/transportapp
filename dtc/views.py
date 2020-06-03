from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
from dtc.models import Booking, Route
from dtc.serializers import BookingSerializer
from django.core.exceptions import ObjectDoesNotExist


def hello_world(request):

    return render(request, 'hello_world.html', {})


def dashboard(request):

    return render(request, 'dashboard.html', {})


def maps(request):

    return render(request, 'maps.html', {})


def welcome(request):

    return render(request, 'welcome.html', {})


def find_route(request):
    # import ipdb; ipdb.set_trace()
    request_data = request.GET
    if request_data:
        source = request_data['source']
        destination = request_data['destination']

        try:
            route_obj = Route.objects.get(
                source=source,
                destination=destination
            )

        except ObjectDoesNotExist:

            return HttpResponse("<h1> Sorry! No Routes Found <h1>")

    return render(request, 'findroute.html', {})


def routes(request):

    request_data = request.GET
    route_id = request_data.get('id')
    routes = Route.objects.get(id=route_id)
    routes_all = Route.objects.all()
    response = {
        'source': routes.source,
        'destination': routes.destination,
        'routes': []
    }
    for routee in routes_all:
        response.get('routes').append(
            {
                routee.id: routee.route_no
            }
        )
    # return render(request, 'routes.html', {'routes': routes})
    return JsonResponse(response)
    # return HttpResponse(response, content_type='application/json')


def exampleSerializer(request):

    if request.method == 'GET':
        booking = Booking.objects.all()
        serializer = BookingSerializer(booking, many=True)

        return JsonResponse(serializer.data, status=200, safe=False)
