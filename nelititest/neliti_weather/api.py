from rest_framework.response import Response
from rest_framework.views import APIView

from neliti_weather.models import Point
from neliti_weather.serializers import CountrySerializer, CheckWeatherSerializer, WeatherSerializer
from neliti_weather.services import fetch_countries, fetch_weathers



class CountriesAPIView(APIView):
    def get(self, request):
        country_name = request.GET.get('country_name', None)
        res = fetch_countries(country_name)
        print(res)
        return Response(CountrySerializer(res, many=True).data)


class WeathersAPIView(APIView):
    def post(self, request):
        data = request.data
        serializers = CheckWeatherSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        validated_data = serializers.validated_data
        point = Point(**validated_data.get('country').get('point'))
        res = fetch_weathers(point, validated_data.get('timezone'))
        print(res)
        return Response(WeatherSerializer(res, many=True).data)
