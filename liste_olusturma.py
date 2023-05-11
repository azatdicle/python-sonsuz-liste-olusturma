#AZAT DİCLE
# Kullanıcı listeyi boş bırakana kadar kadar liste oluşturuma
ekle="a"
liste=[]
print(" boş bırakırsanız programdan çıkılır")
while True:
    if ekle=="":
        break
    else:
        ekle=input("Değer Giriniz:")
        liste.append(ekle)
sayac=0
for x in liste:
    sayac+=1    
sayac=-1
liste.pop(sayac)
print(liste)
    