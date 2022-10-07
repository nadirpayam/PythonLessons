from email import message

message = "Hello There. My name is Nadir Payam"

print(message.upper()) # methodlarda () bulunmalı mutlaka, upper karakterli büyük harfe çevirir

print(message.lower()) #küçük harfe çevirir

print(message.title()) #her kelimenin baş harfi büyük hale gelir

print(message.capitalize()) #sadece ilk harfi büyütür

print(message.strip()) #baştaki boşluk karakterini atar, lstrip() soldan siler, rstrip() sağdan siler
# lstrip("/:pth") istediğimiz karakterleri sildi
print(message.split()) # messajı böler karakter dizisine ekler, boşluklardan böler

print(message.split('.')) #istediğimiz karakterden ayırır

print(' '.join(message)) #parça parça olan şeyleri birleştirir araya istediğimiz karakterleri ekleyerek

print(message.find('Nadir')) #aramak istediğin şeyi find methodun içine yaz,ve indeksini döner kelimenin ilk harfiin indeksini

print(message.startswith('H')) #message H ile mi başlıyor? true false döner

print(message.endswith('n')) #message n karakteri ile mi bitiyor? true false döner

print(message.replace('Nadir','Cem')) # eski, yeni  ard arda replace yapabilirsin

print(message.center(100,'-')) #100 karakterlik bir alan içerisine ortalar mesajımızı
  # message.center(100,'*') bu şekilde de boşluklara yıldız koyar
# rjust() ljust() sağa sola yaslar

print(message.count('a')) # kaç tane a var onu söylüyor 
#count('a',0,10) burda da  0-10 karakteri arasındaki a'ları sayar find()'de de var bu tarama
#rfind() sağdan başlatır 

print('hashasf'.isalpha()) #alfabetik mi değil mi onu söylüyor yani tüm karakterler harf mi

# isdigit() rakamsalm ı değil mi onu söylüyor

