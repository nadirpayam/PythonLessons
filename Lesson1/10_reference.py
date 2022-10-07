#value type , string number

x=5
y=25

x=y

y=10

"""
burda y 10 olunca x 25 kaldı çünkü value type,değerin kendisiyle ilgileniyoruz
"""

#reference type => list
 #adres bilgisi taşır reference types, değerin adresiyle ilgileniyoruz
a = ['apple','banana']
b = ['muz', 'elma']

a = b #ikisi de aynı oldu artık b'de yapılan değişiklik a'yı da etkileyecek
b[0] = 'üzüm'

print(a,b)