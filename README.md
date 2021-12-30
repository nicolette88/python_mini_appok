A program egy currency converter osztályban valósítja meg a konverziós függvényt.
A jobb tesztelhetőség kedvéért lett külön osztályban megvalósítva a feladat.

A program működése:
- először bekér egy átváltandó összeget számmal
- majd bekéri rövidítve azt, hogy milyen pénznemben van az összeg (pl. HUF, USD, EUR)
- ezután pedig azt a pénznemet kéri, amire át kell váltani az összeget (cél pénznem)
- végül pedig kiírja az átváltott összeget végeredményül.

A program nem tartalmaz hibakezelést.


Ezeket az API-kat használtam:
- requests library
- váltáshoz használt url: https://api.exchangerate-api.com/v4/latest/