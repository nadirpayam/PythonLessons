#bir liste tipidir
#key-value olarak çalıştır

#41=>kocaeli               34=>istanbul

syntax = {'key':'value'} 

plakalar ={'kocaeli':41,'Ankara':6}

print(plakalar['kocaeli'])

# value ataması yapabilirz plakalar['kocaeli] = 'new value'

#iç içe dictinoary
users = {
    'sadikturan':{
        'age':36,
        'email': 'mkjga@gmail.com'
     }
}
print(users['sadikturan']['age'])

#users.update methoduyla sözlüğü güncelleyebilirsin
