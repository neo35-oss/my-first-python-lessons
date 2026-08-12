mesaj = "Merhaba Bacını sikim"
mesajTwo = " Yarrak"
isim = "Ali"
yas = 20

print(mesaj.upper())
print(mesaj.lower())
print(mesaj.capitalize())
print(mesaj.startswith("Me")) # Metin başında bundan kullanıldımı
print(mesaj.endswith("im")) # Metin sonunda bundan kullanıldımı
print(len(mesaj + mesajTwo))
print("merhaba" * 10)
print("{} , {} yaşındadır".format(isim,yas))
print(f"{isim} {yas} bu mal bu yaşta")