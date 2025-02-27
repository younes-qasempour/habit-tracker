import requests
from data import *

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    'token': MY_TOKEN,
    'username': 'qasempouryounes',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
