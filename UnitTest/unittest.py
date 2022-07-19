import requests

start_time = input('Enter the start time "YYYY-MM-DD": ')
end_time = input('Enter the end time "YYYY-MM-DD": ')
latitude = input('Enter the latitude: ')
longitude = input('Enter the longitude: ')
max_radius_km = input('Enter the max radius in km: ')
min_magnitude = input('Enter the min magnitude: ')

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
response = requests.get(url, headers={'Accept': 'application/json'}, params={
    'format': 'geojson',
    'starttime': start_time,
    'endtime': end_time,
    'latitude': latitude,
    'longitude': longitude,
    'maxradiuskm': max_radius_km,
    'minmagnitude': min_magnitude
})

data = response.json()
place_and_magnitude_list = []

for x in data['fuatures']:
    place_and_magnitude_list.append((x['properties']['place'], x['properties']['mag'] ))

print(place_and_magnitude_list)
