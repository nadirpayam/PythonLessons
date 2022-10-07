a = input("1.sayı: ") #input'tan gelen değer string olarak alınır
b = input("2.sayı:" )


print(type(a))
print(type(b))

toplam = int(a) + int(b) # string to int

print(toplam)

#Type conversion

x = 5
y = 2.5
name="Cem"
isOnline= True

#int to float
x=float(x)
print(x) #5 int idi, float oldu 5.0

#float to int
y = int(y)
print(y) #çıktısı 2, ondalıklı kısmı yazılmıyor sadece tam kısmı yazılıyor

#float,int to str
result = str(y) + str(x)
print(result) 

#bool to str

isOnline =str(isOnline)
print(isOnline)

#bool to int
isOnline = int(isOnline)
print(isOnline) #çıktısı 1 oldu, true= 1

#print'te print("değer :" + float + "değer2" + float) yapamazsınız birleştirmelerdeki değerler string olmalı