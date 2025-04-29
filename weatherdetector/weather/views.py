from django.shortcuts import render
import json
import urllib.request
from urllib.error import URLError, HTTPError
from django.conf import settings




def index(request):
    data = {}
    city = ''
    error_message = None
    
    if request.method == 'POST':
        city = request.POST.get('city', '').strip()
        
        if not city:  # Check for empty search
            error_message = "Please enter a city name"
        else:
            try:
                # Make API request
                api_key = settings.OPENWEATHERMAP_API_KEY
                api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
                with urllib.request.urlopen(api_url) as response:
                    json_data = json.loads(response.read().decode('utf-8'))
                    
                    # Prepare weather data
                    data = {
                        'country_code': str(json_data['sys']['country']),
                        'coordinate': f"{json_data['coord']['lon']} longitude & {json_data['coord']['lat']} latitude",
                        'temp': f"{round(json_data['main']['temp'] - 273.15, 2)}°C",
                        'pressure': f"{json_data['main']['pressure']} hPa",
                        'humidity': f"{json_data['main']['humidity']}%",
                        'description': str(json_data['weather'][0]['description']).capitalize(),
                        'icon': str(json_data['weather'][0]['icon']),
                        'wind_speed': f"{round(json_data['wind']['speed'] * 3.6, 2)} km/h",  # Convert m/s to km/h
                        'wind_degree': f"{json_data['wind']['deg']}°",
                        'visibility': f"{json_data.get('visibility', 'N/A')} meters",
                    }
                    
            except HTTPError as e:
                error_message = f"City not found. Please try another location. (Error: {e.code})"
            except URLError as e:
                error_message = "Network error. Please check your internet connection."
            except KeyError as e:
                error_message = f"Missing weather data: {str(e)}"
            except Exception as e:
                error_message = f"An unexpected error occurred: {str(e)}"
    
    context = {
        'data': data,
        'city': city,
        'error_message': error_message,
        'has_data': bool(data) and not error_message
    }
    return render(request, 'index.html', context)