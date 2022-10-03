#değişken tanımlarken tipini belirtmemize gerek yok
maasAli = 5000
vergi = 0.27

print(maasAli -(maasAli * vergi))

# Değişken tanımlama kuralları
# rakam ile başlayamaz değişken adı
# Python'da büyük küçük harf duyarlılığı vardır
# değişken tanımlarken türkçe karakter kullanmamaya dikkat edelim
# değişken adı tanımlarken space kullanma
x = 1   # int
y = 2.0 #float
name = 'Yusuf' #string
isStudent = True # boolean, T ve F büyük olmalı

firstName = "Nadir"
lastName = ' Payam'
print(firstName + lastName)

#tek satırda birden fazla değer tanımlamak için

o, n, d , job = (9,5.8,False,'Software Engineer')
print(job)