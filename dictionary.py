# Sozlukler
dic=dict()
dic1={ }

sozluk={'bir':1,'iki':2,'uc':3}

# sozluklere dinamik eleman ekle
sozluk['dord']=4

# degistirilebilir
sozluk['uc']=45

# ic ice sozlukler
sozluk1={'sayilar':{'bir':1,'iki':2},'meyveler':{'yaz':'kiraz','kis':'elma'}}

# sozluk elemanlarina erisme ex: kiraz
a=sozluk1['meyveler']["yaz"]

# sozluk methodlari
sozluk1.keys()  # sozlugun ilk degeri
sozluk1.values() # sozlugun ikinci degeri
sozluk1.items() # sozlugun tum degerleri



