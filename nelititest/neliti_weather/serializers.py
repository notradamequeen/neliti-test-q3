from rest_framework import serializers


class PointSerializer(serializers.Serializer):
    lat = serializers.CharField()
    lon = serializers.CharField()


class CountrySerializer(serializers.Serializer):
    code = serializers.CharField()
    name = serializers.CharField()
    timezones = serializers.ListField(
        child=serializers.CharField()
    )
    point = PointSerializer()


class CheckWeatherSerializer(serializers.Serializer):
    country = CountrySerializer()
    timezone = serializers.CharField()


class WeatherSerializer(serializers.Serializer):
    date_time = serializers.DateTimeField()
    air_pressure_at_sea_level = serializers.CharField()
    air_temperature = serializers.CharField()
    cloud_area_fraction = serializers.CharField()
    relative_humidity = serializers.CharField()
    wind_from_direction = serializers.CharField()
    wind_speed = serializers.CharField()
    symbol= serializers.CharField()
