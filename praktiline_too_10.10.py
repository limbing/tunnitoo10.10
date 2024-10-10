"""Matemaatilised tehted"""
import math
# midagi veel

# küsime kasutajalt ujuvkomaarvu kujul kolmnurga kaatetid a ja b
a = float(input("Sisesta oma a kaateti pikkus:"))
b = float(input("Sisesta oma b kaateti pikkus: "))
# koosta muutuja a, lisa võimalus kasutajal sisestada arv, muuda see ujuvkomaarvuks

# koosta muutuja b, lisa võimalus kasutajal sisestada arv, muuda see ujuvkomaarvuks

# meie ülesandeks on leida hüpoteenus c, kolmnurga ümbermõõt ja pindala NB(vastused peavad olema ümardatud sajandikeni)
c = math.sqrt((a ** 2) + (b ** 2))
print(f"Hüpoteenus c pikkus on: {round(c, 2)}")
p = (a + b + c)
print(f"kolmnurga pindala on: {round(p, 2)}")
s = ((a * b) / 2)
print(f"Kolmnurga pindala on: {round(s, 2)}")