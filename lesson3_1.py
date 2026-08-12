renkler = ["Siyah","Beyaz","Sarı","Mavi","Yeşil"]
sayilar = [1,2,39,4,3,7,8]

print(min(renkler)) # alfabetik olarak en düşük
print(min(sayilar)) # sayi olarak en düşük tersi max
print(sum(sayilar)) #toplam

for i in renkler: # olum for atmak ne kadar kolay aq burda :D
    print(i)

print(list(enumerate(renkler,start=3))) 
# sayarak ekliyor  
# start kısmıda hangi sayıdan başlayarak saysın

print("Siyah" in renkler) # siyah renkler listesinde varmı

stringrenkler = "|".join(renkler) # aralara istedin işareti atıyor
print(stringrenkler)

adamolsun = stringrenkler.split("|")
print(adamolsun) 
# eğer liste normala dönsün dersen liste görünümüne split atcan