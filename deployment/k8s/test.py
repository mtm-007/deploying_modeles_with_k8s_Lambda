import requests

#url = 'http://localhost:9696/predict'
url = 'http://localhost:8080/predict'
data = {
    "url":'http://bit.ly/mlbookcamp-pants'
}

#print(requests.post(url, json=data))
result = requests.post(url, json=data).json()
print(result)


# response = requests.post(url, json=data)

# if response.status_code == 200:
#     try:
#         result = response.json()
#         print(result)
#     except json.decoder.JSONDecodeError as e:
#         print("Error decoding JSON:", e)
# else:
#     print("Error: Received status code", response.status_code)

