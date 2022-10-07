name = 'Nadir' # tek, çift tırnak farketmez
#ve yukarda 5 karakterli bi bilgi tanımladık indekslerle karakterlerine ulaşabiliriz
surname="Payam"
age=36
greeting='My name is: ' + name + " " + surname + " and  \nI am " + str(age) +" years old"
print(greeting)

print(greeting[0]) #0.indeks=1.eleman 

length = len(greeting) #greeting'in boyutunu aldık

print(greeting[length-1]) #indeks 0'dan başladığı için 1 eksiğini yazdık toplam karakter 1 den başlıyor çünkü

#greeting[-1] bu da son indeksi verir.

print(greeting[2:5]) # 2-5 indeks arası yazdırıyor 5 dahil 

print(greeting[3:]) #3'ten başladı sonuna kadar gitti

print[greeting[:5]] #baştan başladı 5.indekse kadar gitti

print(greeting[2:40:5]) # 2'den 40' kadar git 5 indekste bi tane al