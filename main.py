import requests
from data import *

pixela_endpoint = "https://pixe.la/v1/users "

user_params = {
    'token': MY_TOKEN,

}
requests.post(pixela_endpoint)