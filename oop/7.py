
class Weather:
    def __init__(self, weather_params):
        self.weather_params = weather_params
        
    def __contains__(self, item):
        return item in self.weather_params