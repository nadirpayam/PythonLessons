
#range() methodu 0'dan verilen sayıya kadarını yazar
for item in range(2,10,3): #başlangıç,finish,artış miktarı
    print(item)

print(list(range(50,100,20))) # liste şeklinde eleman yapmak

#enumerate , indeks veriyor
greeting = "Hello There"

for index,letter in enumerate(greeting):
    print(f'index: {index} letter: {letter}')

#zip, dictionary'e benzer

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']

print(list(zip(list1, list2)))
 
for item in zip(list1, list2):
      print(item)