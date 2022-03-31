# listeler []
# sozlukler {anahtar:deger,}
# demetler (,)
# set (kumeler) {,}

bos_set = set()
print(bos_set)

yeni_set = {1, 2, 3, 4, 5, 6, }
print(type(yeni_set))

# ornek
liste = [1, 2, 4, 4, 1, 6, 1]
# yukarıdaki listedeki elemanların sadece bir tanesini
# içeren(tekrarları ortadan kaldıran) bir kod yazınız.

# 1. yol
yeni_liste = []
for k in liste:
    if k not in yeni_liste:
        yeni_liste.append(k)

print(yeni_liste)

# setlerde eleman tekrarı yoktur
# 2. yol
yeni_set = set(liste)
print(list(yeni_set))

gun_set = {"Pazartesi", "salı", "çarşamba", "perşembe"}

# add
gun_set.add("cuma")
print(gun_set)

gun_set.add("salı")
print(gun_set)

# set ifadelerinde indisler aracılığıyla ulaşımalaz
# print(gun_set[0])
# print(gun_set[0:3])

for k in gun_set:
    print(k)

# değerine göre eleman silme
gun_set.remove("salı")
print(gun_set)

u = {1, 2, 3, 4, 6}
k = {3, 4, 1, 5, 6}

birlesim_list = []
u_list = list(u)
k_list = list(k)

for ind in range(len(u_list)):  # 0,1,2,3,4
    if u_list[ind] not in birlesim_list:
        birlesim_list.append(u_list[ind])

    if k_list[ind] not in birlesim_list:
        birlesim_list.append(k_list[ind])

print(set(birlesim_list))

# union -> birleşim, intersection -> kesişim
birlesim = u.union(k)
print(birlesim)

# 1. yol
kelisim_list = []
for item in u_list:
    if item in k_list:
        kelisim_list.append(item)
print(kelisim_list)

# 2. yol
kesisim = u.intersection(k)
print(kesisim)

# fark
u_fark_k = u.difference(k)
k_fark_u = k.difference(u)
print(u_fark_k)
print(k_fark_u)

# u fark k
for k in k_list:
    if k in u_list:
        u_list.remove(k)

print(u_list)
