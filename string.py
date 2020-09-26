# Stringlerin yazim sekilleri asagidaki gibidir
# Stringlerimizi a,b,c,d degiskenlerine atiyoruz

a="Bilgisayar"
b='Bilgisayar'
c="""
Bilgisayar
"""
d="Bilgisayar'n gucu"

# String'lerin indexlenmesi(0'dan basliyor) ve parcalanmasi

# indexleme islemi

a='Merhaba'
a[0] # a-nin 0ci indexi 'M' -dir
a[1] # a-nin 1'ci indexi 'e'-dir.... ve boyle devam eder
a[-1] # a-nin sonunci indexidir , yani, 'a'-dir
a[-2] # a-nin sondan 2'ci indexidir yani, 'b'-dir

# parcalama islemi

# [ baslama indexi, bitis indexi, atlama degeri ]
x= 'Ben python ogreniyorum'
x[3,10] # burada 3'cu indexten 10'cu indexe kadar olan karakterleri ekrana getirir
x[3,10,2] # burada 3'cu indexten 10'cu indexe kadar olan karakterleri iki-iki atlayarak ekrana getirir
x[4,:] # 4'cu indexten basla sona kadar git
x[:, 12] # ilk indexten basla 12'ci indexe kadar git
x[:,:,2] # ilk indexten son indexe iki-iki atlayarak git
x[:,:,-1] # stringi ters dondurecek

# String ozellikleri

# len() - String uzunlugunu bulur

a="Sevda"
len(a)

# Onemli bir ozellik stringlerin degerleri degistirilemez
a[3]='t' # a'nin 3'cu indexi yani, 'd'-i degistirip 't' yapamayiz













