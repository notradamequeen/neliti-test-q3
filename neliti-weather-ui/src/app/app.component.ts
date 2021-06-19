import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { FormControl } from '@angular/forms';
import { BehaviorSubject, Observable } from 'rxjs';
import { take } from 'rxjs/operators';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'neliti-weather-ui';
  countryName: FormControl = new FormControl('');
  selectedCountry: any;
  countries: BehaviorSubject<any[]> = new BehaviorSubject([]);
  isCountryOptionShow: boolean = true;
  weathers: any[];

  constructor(private http: HttpClient) {}

  fetchCountries(countryName: string): Observable<any> {
    return this.http.get<any>(`http://localhost:8000/api/countries?country_name=${countryName}`)
  }

  checkWeathers(data: any): Observable<any> {
    return this.http.post<any>(`http://localhost:8000/api/weathers/`, data)
  }

  searchCountry(event: any) {
    this.isCountryOptionShow = true
    this.fetchCountries(this.countryName.value).pipe(take(1)).subscribe(
      (data) => {
        this.countries.next(data)
        console.log(data)
      },
      (err) => {
        console.log('err', err);
        this.countries.next([])
      }
    )
  }

  selectCountry(country) {
    this.isCountryOptionShow = false
    console.log(country)
    this.selectedCountry = country
  }

  checkWeather() {
    const data: any = {
      country: this.selectedCountry,
      timezone: this.selectedCountry.timezones[0]
    }
    this.checkWeathers(data).pipe(take(1)).subscribe(
      (res) => {
        console.log(res)
        this.weathers = res.map((w) => {
          w.date_time = new Date(w.date_time)
          return w
        })
      }, (err) => {
        console.log('err', err)
      }
    )
  }

  getWeatherIcon(symbol: string) {
    switch(symbol) {
      case 'partlycloudy_day':
        return `<i class="fas fa-cloud-sun weather-symbol"></i> <small>${symbol}</small>`;
      case 'rainshowers_day':
        return `<i class="fas fa-cloud-sun-rain weather-symbol"></i> <small>${symbol}</small>`
      case 'lightrainshowers_day':
        return `<i class="fas fa-cloud-sun-rain weather-symbol"></i> <small>${symbol}</small>`
      case 'cloudy':
        return `<i class="fas fa-cloud weather-symbol"></i> <small>${symbol}</small>`
      case 'heavyrain':
        return `<i class="fas fa-cloud-sun-rain weather-symbol"></i> <small>${symbol}</small>`
      case 'partlycloudy_night':
        return `<i class="fas fa-cloud-moon weather-symbol"></i> <small>${symbol}</small>`
      case 'fair_night':
        return `<i class="far fa-moon weather-symbol"></i> <small>${symbol}</small>`
      default:
        return `<i class="fas fa-sun weather-symbol"></i> <small>${symbol}</small>`
      
    }
  }
}
