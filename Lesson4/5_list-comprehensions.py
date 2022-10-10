#for ve while döngülerine alternatif yöntem

#1
numbers = [x for x in range(10)] #x içine 1'den 10'a akdar olan değerleri atıyorsun onlar da diziyi temsil ediyor
print(numbers)

#2
for x in range(10):
    print(x**2)
numbers = [x**2 for x in range(10)]
print(numbers)


#3
numbers =  [x for x in range(10) if x%3==0] #sadece 3 bölünenler geldi
print(numbers)

#4
myString ='Hello'
myList = []

for letter in myString:
    myList.append(letter)
    print(myList)

#5
myList = [letter for letter in myString]
print(myList)

#6
years = [1980,1993,1994,2001]
ages = [2022 -year for year in years]
print(ages)

#7
results = [x if x%2 == 0 else 'TEK' for x in range(1,10)]
print(results)

#8
result = []

for x in range(3):
    for y in range(3):
        result.append((x,y))
print(result)  

#9
numbes = [ (x,y) for x in range(3) for y in range(3)]
print(numbers)

