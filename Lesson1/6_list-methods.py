numbers = [1,10,5,16,4,9,10]
letters = ['a','g','s','b','y','a','s']

#min max kullanımı böyle, listeden eleman tarar
val = min(numbers)
val = max(numbers)
val = min(letters) #alfabetik olarak min değerini yazar
print(val)


val = numbers[3:6] #3-6 arası yazdırır
val = numbers[3:] #3'ten itibaren yazdırır

numbers[4] = 40 #eleman değiştirdik

numbers.append(49) #listeye eleman ekledik en sona ekleniyor

numbers.insert(3,78) #3.indekse 78 elemanını ekledi

numbers.pop() #eleman siler en sondan, içine indekste verebilirsin

numbers.remove(9) #indeks değil silmek istediğin karakteri yazarsın

numbers.sort() #liste sayısal olarak sıralanır
letters.sort() #alfabetik olarak sıralar

numbers.reverse()  #listeyi tersine çevirir, büyükten küçüğe
letters.reverse() #z'den a'ya sıralar

print(len(letters))

print(numbers.count(10)) # içerisinde kaç tane 10 olduğunu söyler

numbers.clear() # elemanları temizler

letters.index('a')  #indeks buluyoruz

print('b' in letters) #listenin içinde mi değil mi

#karakter dizisini listeye çevirme
str="Naber,Gelmedi"
print(str.split(',')) #virgülden itibaren ayırdı listeye eleman ekledi