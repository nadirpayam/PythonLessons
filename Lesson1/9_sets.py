
#bu şekilde tanımlanan listelere sets denir ve elemanlarına indeks ile erişilemez
fruits = {'orange','apple','banana'}
# yanlış kullanım>>print(fruits[0])

#elemanlara ulaşmak için 
for x in fruits:
  print(x)

#eleman ekleme
fruits.add('cherry')

#birden fazla eleman ekleme, karışık bir şekilde eklenir
fruits.update(['mango','grape'])

print(fruits)

#tekrarlanan elemanları siler

#silme işlemi
fruits.remove('mango')

fruits.discard('apple')  # bu da siler

fruits.pop() #son eleman silinmez, elemanlar sıralı değil çünkü indekssiz rastgele

#tüm elemanları siler fruits.clear()