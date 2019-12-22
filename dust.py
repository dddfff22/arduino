import serial
import json
from urllib import request, parse
import time

ser=serial.Serial("dev/ttyACM0",9600)
username="dddfff22"
while True:
    res= ser.readline()
    print(res.decode())
    data = {
      "user_id": username,
      "rooms": [
        
      ],
      "timestamp": "2019-12-21T13:33:36.328Z"
    }
    data["rooms"].append({
          "dust": "string",
          "humidity": "string",
          "roomId": "string",
          "roomName": "string",
          "temp": "string"
      })
    data = json.dumps(data)
    data = str(data)
    data = data.encode('utf-8')
    req = request.Request('http://45.119.146.82:8082/dust/addDustInfo/', data=data)
    req.add_header('Content-Type', 'application/json')
    response = request.urlopen(req)
    print (response.read())
    time(100000)

ser.close()
