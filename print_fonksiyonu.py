# Print fonksiyonu yazdigimiz seyleri ekrana bastirir

a=2536
b="Python programming"
print(a,b)

# \n - Bir satir asagiya indirir
# \t tab kadar bosluk birakir
# sep=" + " verilen degerleri + isareti ile ayirir

print(a,b,sep="*")
print("Python\nprogramming")
print("python\tProgramming")
print(*"Python") # basa * koyarsak her karakterin arasina bosluk koyar

# {} {}.format() daha guzel print fonksiyonu yazim seklidir
print("bu sayi {}, bu ise {} yazidir".format(a,b))

# type- degiskenin tipini gosterir

print(type(a))