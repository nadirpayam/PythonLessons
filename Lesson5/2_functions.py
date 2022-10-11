#fonksiyon tanımlama

def sayHello():
    print('Hello')


sayHello()

#parametreli function

def sayName(name): #name='user' dersen parametresiz çağrılabilir bu fonk ve name kısmı default user olarak gelir
    print(f'Hello {name}')

sayName('Nadir')

#return ile kullanımı
def sayNumber(number):
    return number

numberr = sayNumber(5)

print(numberr)