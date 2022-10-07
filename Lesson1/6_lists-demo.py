arabalar = ["BMW", "Mercedes","Opel","Mazda"]
#listenin ilk ve son elemanını bulun
print(arabalar[0])
print(arabalar[-1])

#Mercedes listenin bir elemanı mıdır?
print('Mercedes' in arabalar) #true false döner

#listenin son iki elemanı yerine "toyota" ve "renault" atayın
arabalar[-2:] = ["toyota","renault"]
print(arabalar)

#listenin üzerine "audi" be "nissan" değerlerini ekleyin
arabalar + ["audi","nissan"]

#listenin son elemanını sil
del arabalar[-1]

#liste elemanını tersten yazdır
print(arabalar[::-1])

student = ["yiğit","bilgi",2010, [70,60,70]] #yani list içerisinde parantez bilgileri ekledik
print(student)