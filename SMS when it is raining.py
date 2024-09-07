import requests
from twilio.rest import Client

# OpenWeatherMap API setup (using city name Islamabad)
OWM_API_KEY = 'your_actual_api_key_here'  # Replace with your OpenWeatherMap API key
CITY = 'Islamabad'
# URL to get weather data for Islamabad
WEATHER_URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={OWM_API_KEY}&units=metric'

# Twilio API setup
TWILIO_SID = 'your_twilio_sid'  # Replace with your Twilio SID
TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'  # Replace with your Twilio Auth Token
TWILIO_PHONE_NUMBER = '+your_twilio_phone_number'  # Replace with your Twilio phone number in international format
TO_PHONE_NUMBER = '+923090090088'  # Your actual phone number in international format


# Function to fetch weather data
def get_weather_data():
    response = requests.get(WEATHER_URL)
    data = response.json()

    # Check if the API call was successful
    if data['cod'] != 200:
        raise Exception(f"Error fetching weather data: {data['message']}")

    return data


# Function to check if it is raining
def is_raining(weather_data):
    # Extract weather conditions
    weather_conditions = weather_data['weather']

    # Check if 'rain' is mentioned in the weather conditions
    for condition in weather_conditions:
        if 'rain' in condition['main'].lower():
            return True

    return False


# Function to send SMS using Twilio
def send_sms(message):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    # Send the SMS
    message = client.messages.create(
        body=message,
        from_=TWILIO_PHONE_NUMBER,  # Your Twilio phone number
        to=TO_PHONE_NUMBER  # Your recipient phone number
    )

    return message.sid


# Main function to check weather and send SMS if raining
def main():
    try:
        # Get current weather data
        weather_data = get_weather_data()

        # Check if it is raining
        if is_raining(weather_data):
            message = f"It is raining in {CITY}. Stay dry!"
            sms_sid = send_sms(message)
            print(f"SMS sent successfully: {sms_sid}")
        else:
            print(f"No rain in {CITY}.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
