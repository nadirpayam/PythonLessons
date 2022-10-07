website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sonra Python Programlama Rehberiniz (40 saat)"

#1- karakter uzunluğu bulma
lengthCourse = len(course)
print(lengthCourse)

#2- website içinden www karakterlerini alın
print(website[7:10])

#3- website içinden com karakterlerini bulun 
print(website[22:25]) #baştan saydık
length = len(website)
print(website[length-3:length]) #sondan başladık

#4- course içinden ilk 15 ve son 15 karakteri alın
print(course[0:15]) 

#5 course ifadesindeki karakterleri tersten yazdırın
print(course[::-1])

#6 'Hello World' ifadesindeki w harfini 'W' ile değiştirin
s = 'Hello World'
s = s[0:6] + 'W' + s[-4:]
print(s)

#7 abc kelimesini 3 defa ard arda yazdırın
print('abc' * 3)