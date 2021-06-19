import datetime
import requests
import json
import pytz

from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from typing import List
from django.utils import timezone

from neliti_weather.models import Weather
from neliti_weather.models import Country, Point

def fetch_countries(country_name: str) -> List[Country]:
    print(country_name)
    res = requests.get(f"https://restcountries.eu/rest/v2/name/{country_name}")
    if res.status_code != 200:
        return []

    res = res.json()
    return list(map(
        lambda country: Country(country['alpha2Code'], country['name'], country['latlng']),
        res))

def fetch_weathers(point: Point, tz_info: str) -> List[Weather]:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64;"}
    res = requests.get(f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={point.lat}&lon={point.lon}", headers=headers)
    if res.status_code != 200:
        return []

    res = res.json()
    one_hour_before = timezone.now().replace(minute=0, second=0, microsecond=0) - relativedelta(hours=1)
    raw_weathers = list(filter(
        lambda x: parse(x['time']) >= one_hour_before and parse(x['time']).date() == one_hour_before.date(),
        res['properties']['timeseries']))
    weathers = []
    for i in range(0, len(raw_weathers)):
        if i < len(raw_weathers) - 1:
            weathers.append(
                Weather(
                    **dict(
                        timezone=pytz.timezone(tz_info),
                        time=raw_weathers[i+1]['time'],
                        symbol=raw_weathers[i]['data'].get('next_1_hours', {}).get('summary', {}).get('symbol_code', ''),
                        **raw_weathers[i+1]['data']['instant']['details']
                    )
                )
            )
    return weathers
