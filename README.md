# Weather Alert Program
A Python program that checks the current weather in Islamabad and sends an SMS alert if it's raining.

# Table of Contents
- Overview
- Requirements
- Setup
- Usage
- Code Structure
- API Documentation
# Overview
This program uses the OpenWeatherMap API to fetch the current weather data for Islamabad and checks if it's raining. If it is, it sends an SMS alert using the Twilio API.

# Requirements
- Python 3.x
- requests library
- twilio library
- OpenWeatherMap API key
- Twilio SID and Auth Token
- Twilio phone number
- Setup
- Replace your_actual_api_key_here with your OpenWeatherMap API key in weather.py.
- Replace your_twilio_sid and your_twilio_auth_token with your Twilio SID and Auth Token in weather.py.
- Replace your_twilio_phone_number with your Twilio phone number in international format in weather.py.
- Install the required libraries by running pip install requests twilio.
# Usage
- Run the program by executing python weather.py.
- The program will check the current weather in Islamabad and send an SMS alert if it's raining.
# Code Structure
- The program consists of the following files:

- weather.py: The main program file that contains the logic for fetching weather data and sending SMS alerts.
- README.md: This file, which provides an overview of the program and its usage.
# API Documentation
The program uses the following APIs:

- OpenWeatherMap API: https://openweathermap.org/api
- Twilio API: https://www.twilio.com/docs/api
Note: This is just a sample README file, you should adjust it according to your needs and the specifics of your project.
