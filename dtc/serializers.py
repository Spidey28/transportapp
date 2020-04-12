from rest_framework import serializers
from dtc.models import Booking, Route


class RouteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Route
        fields = (
            'id',
            'route_no',
            'source',
            'destination'
        )


class BookingSerializer(serializers.ModelSerializer):
    # route = RouteSerializer()
    bus_id = serializers.IntegerField(allow_null=True, write_only=True)
    route_id = serializers.IntegerField(allow_null=True, write_only=True)
    class Meta:
        model = Booking
        fields = (
            'id',
            'bus',
            'bus_id',
            'route',
            'route_id',
            'source',
            'destination'
        )
