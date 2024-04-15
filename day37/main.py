import requests
from datetime import datetime

TOKEN = "md3qk6sajd83bsfb2kj34"
USERNAME = "sharry"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
# account creation
params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# resp = requests.post(url=pixela_endpoint, json=params)
# print(resp.text)

# creating a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# resp = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(resp.text)

# adding an entry to the graph (creating a pixel)
graph_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
graph_pixel_config = {
    "date": str(datetime.now().strftime("%Y%m%d")),
    "quantity": "2.74"
}

# resp = requests.post(url=graph_pixel_endpoint, json=graph_pixel_config, headers=headers)
# print(resp.text)

# updating a pixel
edit_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{graph_pixel_config['date']}"
edit_config = {
    "quantity": 5,
}

# resp = requests.put(url=edit_endpoint, json=edit_config, headers=headers)
# print(resp.text)

# deleting an entry
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{graph_pixel_config['date']}"

# resp = requests.delete(url=delete_endpoint, headers=headers)
# print(resp.text)