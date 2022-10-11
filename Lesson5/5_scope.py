#değişkenlerin local global olma durumu
#global scope
x ='global x'

def function():
    #local scope
    x='local x'
    return x

print(function()) #local x
print(x) #global x

