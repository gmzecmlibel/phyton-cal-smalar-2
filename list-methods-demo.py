names=["Osman", "Burkan", "Yunus", "Enes"]
dateOf=(2000, 2001, 1995)

# 1-  "Cenk" ismini listenin sonuna ekleyiniz.

# names.append("Cenk")
# print(names)
#or
names.insert(len(names),"Cenk")

# 2-  "Sena" ismini listenin başına ekleyiniz.

names.insert(0,"Sena")
print(names)

# 3-  "Enes" ismini listeden siliniz.

names.remove("Enes")
print(names)
# 4-  "Osman" isminin indeks nedir.

a=names.index("Osman")
print(a)
# 5-  "Ayşe" listenin bir elemanı mıdır?
asd="Ayşe" in names
print(asd)
# 6-  Liste elemanlarını ters çeviriniz.

names.reverse()
print(names)


# 7-  Liste elemanlarını alfabetik olarak sıralayınız.

names.sort()
print(names)


# 8-  str = "Chevrolet, Dacia" karakter dizisini listeye çeviriniz.
str = "Chevrolet,Dacia" 
result=str.split(",")
print(result)

# 9- Date dizisinin en büyük ve en küçük elemanı nedir?
maxx=max(dateOf)
print(maxx)

minn=min(dateOf)
print(dateOf)

# 10- Date dizisinde kaç tane 1998 değeri vardır?

aa=dateOf.count(1998)
print(aa)
# 11- Date dizisinin tüm elemanlarını siliniz.



# 12- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
marka1= input("Araba1= ")
marka2=input("Araba2= ")
marka3=input("Araba3= ")

bigdata=[marka1 , marka2, marka3]
print(bigdata)