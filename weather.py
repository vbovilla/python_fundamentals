import requests

# city = input('Enter city name:')
# if '' == city:
#     city = input('Please enter city name:')


city = ''
while city == '':
    city = input('Please enter city name:')

# city = 'London'
url = (
    'https://api.weatherapi.com/v1/current.json?key=41e5da5e83eb4183bc130625252311&q='
    + city
    + '&aqi=yes'
)
response = requests.get(url)
# print(response)

if response.status_code == 400:
    print('No weather report found for', city)
else:
    weather_json = response.json()
    print(weather_json)

    temp = weather_json.get('current').get('temp_f')
    description = weather_json.get('current').get('condition').get('text')

    # print(temp)
    # print(description)

    print("Today's weather in", city, "is",
          description, "and", temp, "degress")
