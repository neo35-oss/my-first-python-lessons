renkler = ["kırmızı","sarı","siyah","yeşil"]
print(type(renkler))
print(len(renkler))
print(renkler[0:2])

renkler.append("gri") # sona ekler
renkler.extend("Göztepe")#harfleri ayırarak sona ekler
renkler.insert(2,"Karşıyaka") # istediğin indexe ekliyor
renkler.remove("kırmızı")
print(renkler)

renkler2 = ["kırmızı","yeşil","sarı"]
renkler.extend(renkler2)
silinen = renkler2.pop() 
# son elamnı silme ve silinen elemanı alma
#terse çeviriyor biliyon zaten renkler2.reverse()
#renkler2.sort() alfabetik bir sıralama yapmakta
#renkler2.sort(reverse=True)
#eski yaptığın listeyi bozmadan listelemek için orjinal gibi bunu kullan liste2 = sorted(renkler)
print(renkler2)
print(silinen)