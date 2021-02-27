import requests

BASE= "http://127.0.0.1:5000/"

response = requests.get(BASE + "users?email=yassine.elzaart@lau.edu&name=yus&phoneNumber=81899268&city=barja&street=kroom&password=hihi2020")
response2 = requests.post(BASE + "/login?email=idk&password=idktoo", {"email":"hey"})
print(response.json())
print(response2.json())