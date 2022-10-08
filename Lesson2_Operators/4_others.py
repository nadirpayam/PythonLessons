# identity operator : is

x = y = [1,2,3]
z = [1,2,3] 

print(x==y)
print(x==z) #değer karşılaştırması yaptık

print(x is z) # adres karşılaştırması yapar



#membership operator: in

x = ['apple','banana']

print('banana' in x) # listede banana var mı diye sorduk

name = 'Nadir'

print('ad' not in name)
