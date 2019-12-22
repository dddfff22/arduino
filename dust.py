import serial
import json
from urllib import request, parse
import time

ser=serial.Serial("/dev/ttyACM0",9600)
username="dddfff22"
while True:
    try:
      res= ser.readline()
      print(res.decode())
      temp=res.decode().split(" ")
      if len(temp)>2:
        hu = temp[2]
        tu = temp[0].split("C")[0]
      else:
        du=temp[0].split("\r")[0]
      res= ser.readline()
      print(res.decode())
      temp=res.decode().split(" ")
      if len(temp)>2:
        hu = temp[2]
        tu = temp[0].split("C")[0]
      else:
        du=temp[0].split("\r")[0]
      

      data = {
        "user_id": username,
        "rooms": [
          {
            "dust": str(du),
            "humidity": str(hu),
            "roomId": "dd",
            "roomName": "Living Room",
            "temp": str(tu)
        }
        ],
        "timestamp": "2019-12-21T13:33:36.328Z"
      }

      data["rooms"].append({
            "dust": "100",
            "humidity": "60",
            "roomId": "string",
            "roomName": "Inner Room",
            "temp": "35"
      })
      
      data = json.dumps(data)
      data = str(data)
      data = data.encode('utf-8')
      req = request.Request('http://45.119.146.82:8082/dust/addDustInfo/', data=data)
      req.add_header('Content-Type', 'application/json')
      response = request.urlopen(req)
      print (response.read())
      time.sleep(5)
      ser.flushInput()
      ser.flushOutput()
    except:
      print("error")

ser.close()
