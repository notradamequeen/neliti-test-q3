from datetime import datetime
from dateutil.parser import parse
from typing import List
from pytz import country_timezones, timezone
from typing import List
from django.db import models

# Create your models here.
class Point:
    lat: str
    lon: str

    def __init__(self, lat=None, lon=None):
        self.lat = lat
        self.lon = lon
    
    def to_dict(self):
        return dict(lat=self.lat, lon=self.lon)


class Country:
    code: str
    name: str
    point: Point
    timezones: List[str]

    def __init__(self, code: str, name: str, point: List):
        self.code = code
        self.name = name
        self.point = Point(*point)
        self.timezones = country_timezones[code]
    
    def to_dit(self):
        return dict(
            code=self.code,
            name=self.name,
            point=self.point.to_dict(),
            timezones=self.timezones
        )


class Weather:
    date_time: datetime
    air_pressure_at_sea_level: float
    air_temperature: float
    cloud_area_fraction: float
    relative_humidity: float
    wind_from_direction: float
    wind_speed:	float
    symbol: str


    def __init__(self, **kwargs) -> None:
        self.date_time = parse(kwargs.get('time')).astimezone(kwargs.get('timezone'))
        self.air_pressure_at_sea_level = kwargs.get('air_pressure_at_sea_level')
        self.air_temperature = kwargs.get('air_temperature')
        self.cloud_area_fraction = kwargs.get('cloud_area_fraction')
        self.relative_humidity = kwargs.get('relative_humidity')
        self.wind_from_direction = kwargs.get('wind_from_direction')
        self.wind_speed = kwargs.get('wind_speed')
        self.symbol = kwargs.get('symbol')
