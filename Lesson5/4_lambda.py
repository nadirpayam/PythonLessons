#map ile dizi üzerindeki her elemana ulaşabiliyoruz


numbers=[1,2,3,5,9]

result = list(map(lambda num:num**2,numbers))#methodun adını yaz direkt, çalıştırma

print(result)

#filter

def check_even(num): return num%2==0

result = list(filter(check_even,numbers))
print(result)