import requests
from data import *
from datetime import datetime, timedelta

USER_NAME = 'qasempouryounes'
GRAPH_ID = 'graph1'

today = datetime.now()
yesterday = today - timedelta(days=1)

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
pixel_creation_endpoint = f'{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}'
pixel_update_endpoint = f'{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{yesterday.strftime('%Y%m%d')}'


headers = {
    'X-USER-TOKEN': MY_TOKEN,
}
user_params = {
    'token': MY_TOKEN,
    'username': USER_NAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}
graph_config = {
    'id': 'graph1',
    'name': 'Cycling Graph',
    'unit': 'Km',
    'type': 'float',
    'color': 'shibafu',
}
pixel_data = {
    'date': yesterday.strftime('%Y%m%d'),
    'quantity': '10.6'
}
pixel_data_update = {
    'quantity': '8.7'
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# response = requests.post(url=pixel_creation_endpoint, headers=headers, json=pixel_data)
# print(response.text)

# response = requests.put(url=pixel_update_endpoint, json=pixel_data_update, headers=headers)
# print(response.text)

response = requests.delete(url=pixel_update_endpoint, headers=headers)
print(response.text)
