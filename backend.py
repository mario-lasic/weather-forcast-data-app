from api_key import API_key
import requests

def get_data(place, forecast_days=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}&units=metric"
    response = requests.get(url=url)
    data = response.json()
    filtered_data = data["list"]
    filtered_data = filtered_data[:8*forecast_days]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))