#format kullanımında tip dönüşümü yapmamıza gerek kalmaz, paramterleri sırayla kabul eder süslü parantezler
name = 'Cem'
surname = 'Filiz'
age = 41

print('He name is {} {}'.format(name,surname)) 

print('He name is {1} {0}'.format(name,surname)) #indekslerin yerini değiştirdik

print('He name is {n} {s}'.format(n=name,s=surname))  # değişkenleri kısalttık

print('He name is {} {} and He is {} years old.'.format(name,surname,age)) #age 'de int to string yapmamıza gerek kalmadı format bunu kendisi yapıyor

result = 200/700
print("result is {r:9.3} ".format(r=result)) # format float to str yaptı
#3 virgülden sonra kaç basamak olacağını gösteriyor, 1 ise tam kısım için kaç tane boşluk bırakacağını söylüypr önceki kelimeyle arasında


print(f"He name is {name} {surname} and He is {age} years old.")
#fstring tırnak başına f eklersen değişkenleridirekt yazabilirsin {} içlerine




