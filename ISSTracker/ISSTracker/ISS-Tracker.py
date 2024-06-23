import json, turtle, urllib.request, time

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print("Right now" + str(result["number"]) + " Astronaut in Space")
print("")

people = result["people"]
for p in people:
  print(p["name"] + " on board " + p["craft"])

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)

screen.bgpic("img/world-map.gif")
screen.register_shape("img/iss.gif")
iss = turtle.Turtle()
iss.shape("img/iss.gif")
iss.setheading(45)
iss.penup()

while True:
  url = "http://api.open-notify.org/iss-now.json"
  response = urllib.request.urlopen(url)
  result = json.loads(response.read())
    
  
  location =result["iss_position"]
  y = float(location['latitude'])
  x = float(location['longitude'])
  #y = location["latitude"]
  #x = location["longitude"]
    
  
  print(str(x))
  print(str(y))
 
  
  iss.goto(x, y)

  
  time.sleep(2)
