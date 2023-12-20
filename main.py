import requests
import json
from jsonpath_ng import jsonpath, parse

response = requests.get(
    'https://api.weatherbit.io/v2.0/current?lat=55.751244&lon=37.618423&key=056eb184043541ba8b80094a08db6431&include=minutely')
print(response.json())

with open('data.json', 'w') as outfile:
    json.dump(response.json(), outfile)

with open("data.json", 'r') as json_file:
    json_data = json.load(json_file)

jsonpath_expression = parse('data[*].weather[*].description')
jsonpath_expression2 = parse('data[*].temp')

print(jsonpath_expression)
for match in jsonpath_expression.find(json_data):
    x = str(match.value)
    # print(f'w desc: {match.value}')
for match2 in jsonpath_expression2.find(json_data):
    y = str(match2.value)
print('desc:' + ' ' + x + ' ' + 'temp:' + ' ' + y)
