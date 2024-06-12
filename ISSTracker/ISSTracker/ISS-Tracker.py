#Gerçek zamanlı ISS izleyici

import json, turtle, urllib.request, time

#Uzaydaki tüm astronotların isimlerini çekmek için ilk JSON isteği.
url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print("Şu anda " + str(result["number"]) + " uzayda ki astronotlar:")
print("")

people = result["people"]
for p in people:
  print(p["name"] + " Gemide " + p["craft"])

#Python Turtle kullanarak dünya haritası hakkında bilgi görüntüleme
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)

#Dünya haritası resmini ISS görselini ekler
screen.bgpic("img/world-map.gif")
screen.register_shape("img/iss.gif")
iss = turtle.Turtle()
iss.shape("img/iss.gif")
iss.setheading(45)
iss.penup()

while True:
  #IIS uzay istasyonunun geçerli boylamını ve enlemini almak için bir JSON isteği (gerçek zamanlı)
  url = "http://api.open-notify.org/iss-now.json"
  response = urllib.request.urlopen(url)
  result = json.loads(response.read())
    
  #Konum bilgilerini ayıklama
  location =result["iss_position"]
  y = float(location['latitude'])
  x = float(location['longitude'])
  #y = location["latitude"]
  #x = location["longitude"]
    
  #Çıktı bilgisi
  print("\nX-Boylam: " +str(x))
  print("Y-Enlem: " + str(y))
 
  #ISS'yi haritaya çiz
  iss.goto(x, y)

  #Her 2 saniyede bir yenile
  time.sleep(2)