# neliti-test-q3

This project is for neliti test purpose only. A weather app powered by Django and Angular.

## How to start the UI
- cd neliti-weather-ui
- run npm install
- run npm start

## How to start the Backend
- cd nelititest
- activate python virtual environment
- run pip install -r nelititest/requirements.txt
- run python manage.py runserver


## API Documentation

### API search country

- URL: https://localhost:8000/api/countries
- METHOD: GET
- URL PARAMS: {country_name: string}
- RESPONSE CODE: 200 OK
```
GET https://localhost:8000/api/countries?country_name=indon
[
    {
        "code": "ID",
        "name": "Indonesia",
        "timezones": [
            "Asia/Jakarta",
            "Asia/Pontianak",
            "Asia/Makassar",
            "Asia/Jayapura"
        ],
        "point": {
            "lat": "-5.0",
            "lon": "120.0"
        }
    }
]
```


### API check weather 
- URL: https://localhost:8000/api/weathers/
- METHOD: POST
- RESPONSE CODE: 200 OK
```
[
  {
    "date_time": "2021-06-19T09:00:00Z",
    "air_pressure_at_sea_level": "1012.2",
    "air_temperature": "24.6",
    "cloud_area_fraction": "82.8",
    "relative_humidity": "81.6",
    "wind_from_direction": "116.4",
    "wind_speed": "2.9",
    "symbol": "lightrainshowers_day"
  },
.....
]
```

