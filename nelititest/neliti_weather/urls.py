from django.conf.urls import include, url

from neliti_weather.api import CountriesAPIView, WeathersAPIView

urlpatterns = [
    url(r'^countries/', CountriesAPIView.as_view(), name='get_countries'),
    url(r'^weathers/', WeathersAPIView.as_view(), name='check_weathers'),

]
