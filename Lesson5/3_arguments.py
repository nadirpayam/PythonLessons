 # 2 parametreli, 3 parametreli fonksiyon aynı anda çalışması için

def add(a,b,c=0):
  return sum((a,b))

print(add(10,20))
print(add(10,20,30))

#sınırsızca 

def add2(*params): # tek yıldız ile listeyi belirttik
    return sum((params))

print(add2(5,6,34,62,61,4))

#
def displayUser(**args): #** ile dictionary'i belirttik
    for key, value in args.items():
        print('{} is {}' .format(key,value))
displayUser(name='çınar', age=3,city='İstanbul')
displayUser(name='çınar', age=3,city='İstanbul', phone='android')
