import requests


# külön hibakezelést nem implementáltam feltételezem, hogy a lekérés a valuta pénznemének rövidítésével türténik pl: HUF mint forint
# minimális konverziókat használok, hogy helyes bemeneti adatok esetén mégis stabil legyen a program
class CurrencyConverter():

    def __init__(self, url):
        self._url = url

    def converter(self, in_curr, out_curr, osszeg):
        # a stringeket nagybetűre vagy float-tá konvertálom, hogy mindíg a megfelelő formátumben kezelje a program az árfolyamot
        osszeg = float(osszeg)
        tmp_url = self._url + str(in_curr.upper())
        response_data = requests.get(tmp_url).json()
        currencies = response_data['rates']
        osszeg = round(osszeg * currencies[out_curr.upper()], 4)
        return osszeg


osszeg = input("Kérem adja meg a(z) átváltandó összeget: ")
input_penznem = input("Kérem adja meg a(z) pénznemet: ")
output_penznem = input("Kérem adja meg a cél pénznemet: ")

url = 'https://api.exchangerate-api.com/v4/latest/'
converter = CurrencyConverter(url)
print("az átváltott összeg: " +
      str(converter.converter(input_penznem, output_penznem, osszeg)) + " " +
      output_penznem)

# teszt kód, hogy ne kelljen külön beirogatni
# print(converter.converter('EUR', 'HUF', 1))
