import requests


class WeatherManager():

    OW_ENDPOINT_URL = 'https://api.openweathermap.org/data/2.5/forecast'
    APP_ID = '8fc4096ef9c9e23174b8c8f7c0f24e3e'

    def __init__(self, lat, lng) -> None:
        self.lat = lat
        self.lng = lng
        self.data: list[int]
        self.load_data()

    def load_data(self):
        response = requests.get(url=self.OW_ENDPOINT_URL, params={
            'lat': self.lat,
            'lon': self.lng,
            'appid': self.APP_ID,
            'cnt': 5
        })
        response.raise_for_status()
        w_list = response.json()['list']
        self.data = [int(row['weather'][0]['id']) for row in w_list]

    def check_for_rain(self) -> bool:
        will_rain = False
        for condition_code in self.data:
            if condition_code < 700:
                will_rain = True
        return will_rain
