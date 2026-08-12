mesaj = "Bu Çocuk Yapay Zekaya Savaş Açmaya Geldi Ayık OLUN" # bu çocuk kim ama demi iştee
cocuk = "Neo"
mesajIki = f"Bu {cocuk.upper()} ADAM BİZİN İÇİN";

if mesaj.find("Çocuk") :
    print(mesajIki.lower()) 
    # az çeşitlendircen çalışırken fazla çalış ama akıllı çalış hadi bakim 
    # 2 şey öğrendik burda mesaj ikide sen ne kadar upper atsan kod her zaman sonda bittiği için gene biat eder en aşşağıya

print(len(mesaj + cocuk)) # bu len toplam harfleri karakterleri sayıyor len dedinmi hemen yapar
print(mesaj.endswith("OLUN"))

if mesaj.startswith("bu"):
    print("başlangıcın bitişin olur")
elif mesaj.endswith("OLUN"):
    print("bazende bitişin başlangıç olur \n:)")
    print("#badvibeforever " * 2)

sayi1 = 2 * 2
sayi2 = 4
sayi3 = 30

if sayi1 == sayi2:
    print("DALLAMANIN TEKİ: EY CEG BOK GİBİSİN")

if sayi3 > (15 + 2) :
    print("CEG: BANA BOK GİBİSİN DE BU BANA VERİYOR OPTİMİZM")
