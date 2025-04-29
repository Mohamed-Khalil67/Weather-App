# Weather Detector Application

A lightweight Django web application that provides real-time weather information for locations worldwide using the OpenWeatherMap API.

## Features
- Current weather conditions for any city  
- Temperature in °C  
- Atmospheric pressure in hPa  
- Humidity percentage  
- Wind speed in km/h with direction  
- Geographic coordinates (latitude/longitude)  
- Visual weather icons  
- Responsive design works on all devices  
- Clear error messages for invalid searches  
- Bookmarkable city URLs  

## Installation Steps

1. Clone the repository:
git clone https://github.com/yourusername/weather-detector.git  
cd weather-detector  

2. Create virtual environment:
python -m venv venv  
# Linux/Mac:  
source venv/bin/activate  
# Windows:  
venv\Scripts\activate  

3. Install requirements:
pip install django requests python-dotenv  

4. Get API key from OpenWeatherMap website  

5. Create .env file with:
API_KEY=your_api_key_here  

6. Run the server:
python manage.py runserver  

## How to Use

1. Enter a city name in the search box  
2. View all weather details  
3. Share or bookmark specific city weather pages  

## API Information

The app uses this API endpoint:
https://api.openweathermap.org/data/2.5/weather  
Required parameters:  
- q={city_name}  
- appid={your_api_key}  
- units=metric  

## Deployment

For production:  
1. Use Gunicorn as WSGI server  
2. Configure Nginx/Apache  
3. Set DEBUG=False  
4. Add domain to ALLOWED_HOSTS  

## Contributing

1. Fork the repository  
2. Create your feature branch  
3. Commit your changes  
4. Push to the branch  
5. Create Pull Request  

## License
MIT License - free to use and modify  
