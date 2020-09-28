# Listeler

# 2 sekilde bos liste olusturabiliriz
liste=[]
liste1=list()

# Listeler her veri tipinden olusabilir
liste=[1,2,5,"Python"]

# string veri tipinin liste veri tipine cevrilmesi

liste=list("Python")

# Listeler degistirilebilirler

liste2=[2,3,4,5,6]
#indexleme

liste2[2]=95  # degistirilebilir

# parcalama
x=liste2[: : 4]
#print(x)

# listelerin toplanmasi

a=liste+liste2 # iki listedeki elamanlari bir listede toplar
#print(a)


# Liste metodlar
# append - listeye eleman ekler
liste2.append(5)
# pop - listeden eleman siler, index yazmazsak en son elemani siler
liste2.pop()

# sort- listeyi kucukten buyuye veya alfabetik siralar
liste2.sort()

# iC ICE LISTELER

liste4=[[1,2],["a","ag"],[3,"python"]]