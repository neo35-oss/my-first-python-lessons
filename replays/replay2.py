renkler = ["Kırmızı","Sarı","Mavi","Bordo","Pembe"]
renkler2 = ["Turkuaz","Gri","Turuncu","Mor"]
sayilar = [39,4,3,7,8]

renkler.append("Karşıyaka")
# renkler.extend("Göztepe") her harfi indexlere ayırarak sonuncu indexe ekler
renkler.insert(3,"Göztepe")
renkler.remove("Sarı")
# renkler.extend(renkler2) bu renkler listinin sonuna renkler 2 listesini ekler

removed = renkler.pop()
print(renkler)
print(f"Silinen Sonuncu Index Buydu:{removed}")

print(min(sayilar))
print(max(sayilar))
print(sum(sayilar)) # toplamı

for i in renkler2:
    print(i)

print(list(enumerate(renkler2, 1)))

rengdeigisk = "-".join(renkler2)
print(rengdeigisk)