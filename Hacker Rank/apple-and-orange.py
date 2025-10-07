s, t = 7, 10 #Casa
a = 4 #Manzano
b= 12 #Naranjo
manzanas = [2, 3, -4]
naranjas = [3, -2, -4]

c_manzanas = 0
for manzana in manzanas:
    if s <= a+manzana <= t:
        c_manzanas += 1

c_naranjas = 0
for naranja in naranjas:
    if s <= b+naranja <= t:
        c_naranjas += 1

print(f"Total manzanas: {c_manzanas} \nTotal naranjas: {c_naranjas}")
