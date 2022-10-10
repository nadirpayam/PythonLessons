from re import X


name = 'Nadir Payam'

for letter in name:
    if letter == 'a':
        break #continue deseydik a atlardı devam ederdi, ama a görünce kırıldı döngü hemen breakle
    print(letter)


result = 0
x=0
while x<=100:
    x+=1
    if x% 2 ==1:
        continue
    result +=X
   
print(f'toplam: {result}')
    
   