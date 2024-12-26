
#Dve promenlivi, brojkite da se vnesat vo prazna lsita, da se presmeta suma na listata,  da se proveri dali e pogolema od 10 ili da se proveri dali e paren toj broj

a = int(input("Vnesi broj a: "))
b = int(input("Vnesi broj b: "))
numbers = []
numbers.append(a)
numbers.append(b)
sum_numbers = sum(numbers)
if sum_numbers > 10 and sum_numbers % 2 == 0:
    print(f"Zbirot na brojkite e {sum_numbers} Brojot e pogolem  od 10 i e paren")
else:
    print(f"Zbiroto na brojkite e {sum_numbers} Brojot e pomal  od 10 i e neparen")


#Da se napishe programi koja prima broj od 1 do 5, dokolku se vnesi 1 da se ispechati nedovolon, 2 dovolen, 3 da se ispechati dovolen, 4 mn dobar, 5 odlichen, 6 7 8 ... se vnesi greshna brojka
poeni = int(input("Vnesi gi poenite: "))


if poeni >= 90:
    otcenka = 10
elif poeni >= 80:
    otcenka = 9
elif poeni >= 70:
    otcenka = 8
elif poeni >= 60:
    otcenka = 7
elif poeni >= 50:
    otcenka = 6
else:
    otcenka = 5
print(f"Uchenikot dobiva ocenka: {otcenka}")

a = int(input("Vnesi broj"))
b = int(input("Vnesi broj"))
c = input("Vnesi operatetor")
if c == "+":
    print(a+b)
elif c == "*":
    print(a*b)
elif c == "-":
    print(a-b)
elif c =="/":
    print(a/b)
else:
print("Vnesovte greshen operator")

broj1 = int(input("Внесете го првиот број: "))
broj2 = int(input("Внесете го вториот број: "))


if broj1 % 3 == 0 and broj1 % 5 == 0:
    print(f"Бројот {broj1} е делив и со 3 и со 5.")
elif broj1 % 3 == 0:
    print(f"Бројот {broj1} е делив со 3.")
elif broj1 % 5 == 0:
    print(f"Бројот {broj1} е делив со 5.")
else:
    print(f"Бројот {broj1} не е делив ни со 3 ни со 5.")

if broj2 % 3 == 0 and broj2 % 5 == 0:
    print(f"Бројот {broj2} е делив и со 3 и со 5.")
elif broj2 % 3 == 0:
    print(f"Бројот {broj2} е делив со 3.")
elif broj2 % 5 == 0:
    print(f"Бројот {broj2} е делив со 5.")
else:
    print(f"Бројот {broj2} не е делив ни со 3 ни со 5.")



gradovi = []


broj_na_gradovi = int(input("Vnesi kolku gradovi da se dodadat "))


for i in range(broj_na_gradovi):
    grad = input(f"Vnesi ime na grad {i+1}: ")
    gradovi.append(grad)


print("Lista na gradovi e :", gradovi)



parni_broevi = []
for i in range(0, 101, 2):
    parni_broevi.append(i)
print("Listata so parni broevi e", parni_broevi)

cities = [" New York", "London", "Tokyo", "Paris", "Sydney", "Berlin", "Toronto", "Barcelona", "Dubai", "Rome"]


grad = 0

# Use a while loop to print each city
while grad < len(cities):
    print(cities[grad])
    grad += 1


#cities = ["New York", "London", "Tokyo", "Paris", "Sydney", "Berlin", "Toronto", "Barcelona", "Dubai", "Rome"]


#for grad1 in cities:
    #print(grad1)

broj = 0
while broj <= 100:
    if broj % 2 == 0:
        broj += 1
        print(broj)




def zbir(a, b):
    return a + b


broj1 = int(input("Vnesi go prviot broј: "))
broj2 = int(input("Vnesi go vtoriot broj: "))


rezultat = zbir(broj1, broj2)
print(rezultat)


def kalkulator(broj1, broj2, znak):
    if znak == '+':
        return broj1 + broj2
    elif znak == '-':
        return broj1 - broj2
    elif znak == '*':
        return broj1 * broj2
    else:
        return "Nepoznat operator"

broj1 = int(input("Vnesi broj: "))
broj2 = int(input("Vnesi broj: "))
znak = input("Vnesi znak: ")

rezultat = kalkulator(broj1,broj2, znak)
print(rezultat)



def sredna_vrednost(lista):
    return sum(lista) / len(lista)

a = [1, 2, 3, 4, 5, 6]

rezultat = sredna_vrednost(a)
print(rezultat)

kvadrat = lambda broj: broj ** 2

broj = int(input("Vnesi broj: "))

print(kvadrat(broj))


def funkcija(**kwargs):

    for kluch, vrednost in kwargs.items():
        print(f"{kluch}: {vrednost}")


funkcija(ime="Dimitar", prezime="Mitrev", godini = 5)

a = [i for i in range(1, 100) if i % 3 == 0 and i % 5 == 0]
print(a)

gradovi = ["Скопје", "Битола", "Прилеп", "Охрид", "Штип"]

nova_lista = [grad for grad in gradovi if not grad.startswith("П")]

print(nova_lista)



def presmetaj_suma(lista):
    suma = 0
    for broj in lista:
        suma += broj
    return suma

a = [1, 2, 4, 5, 6, 2, 35, 2]

rezultat = presmetaj_suma(a)
print(rezultat)
def grad_so_najgolem_broj_bukvi(lista):

    najgolem_grad = ""
    max_dolzina = 0


    for grad in lista:

        if len(grad) > max_dolzina:
            najgolem_grad = grad
            max_dolzina = len(grad)

    return najgolem_grad

cities = ["New York", "London", "Paris", "Tokyo", "Sydney", "Berlin", "Toronto", "Barcelona", "Moscow", "Dubai"]

rezultat = grad_so_najgolem_broj_bukvi(cities)
print(rezultat)


import math

def presmetaj_perimetar_i_ploshtina(radius):

    perimetar = 2 * math.pi * radius

    ploshtina = math.pi * radius ** 2

    return perimetar, ploshtina

radius = float(input("Vnesi radius na krug "))


perimetar, ploshtina = presmetaj_perimetar_i_ploshtina(radius)


print(f"{perimetar:.2f}")
print(f"{ploshtina:.2f}")



import math

perimetar = lambda radius: 2 * math.pi * radius

ploshtina = lambda radius: math.pi * radius ** 2

radius = float(input("Vnesi radius "))

print(f"Perimetar {perimetar(radius):.2f}")
print(f"Ploshtina {ploshtina(radius):.2f}")



a = ["Јаболко", "Банана", "Портокал", "Грозје", "Киви", "Круша", "Праска", "Ананас"]

ovoshja_so_a = [ovoshje for ovoshje in a if "а" in ovoshje.lower() or ovoshje.startswith("А")]

print(ovoshja_so_a)

def najgolem_od_trite(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


broj1 = (input("Vnesi go prviot broj "))
broj2 = (input("Vnesi go vtorio broj "))
broj3 = (input("Vnesi go tretior broj "))


najgolem_broj = najgolem_od_trite(broj1, broj2, broj3)
print(f"Najgolemiot broj e: {najgolem_broj}")


def faktoriel(n):

    if n == 0:
        return 1
    else:
        rezultat = 1
        for i in range(1, n + 1):
            rezultat *= i
        return rezultat


broj = int(input("Vnesi broj da se presmeta faktoriel: "))


print(faktoriel(broj))





a = []
for i in range(100, 1000):
    str_i = str(i)
    zbirCifri = int(str_i[0]) + int(str_i[1]) + int(str_i[2])
    if i % zbirCifri == 0:
        a.append(i)
print("Rezulatot e ", a)
print("Brojot na elementi vo a e:", len(a))


def delivi_so_3_i_15(lista):
    rezultat = [broj for broj in lista if broj % 3 == 0 and broj % 15 == 0]
    return rezultat

lista_broevi = [5, 16, 29, 15, 30, 45, 10, 20, 33, 50]
print(delivi_so_3_i_15(lista_broevi))


def find_largest(numbers):
    try:
        largest = numbers[0]
    except:
        print("listata koja ja isprativte e prazna")
        return
    for num in numbers:
        if num > largest:
            largest = num
    return largest

numbers_list = []
largest_number = find_largest(numbers_list)
print("The largest number is:", largest_number)


def podeli_broevi():
    try:
        broj1 = int(input("Vnesi go prviot broj: "))
        broj2 = int(input("Vnesi go vtoriot broj "))
        rezultat = broj1 // broj2
        return f"Резултатот од делењето е: {rezultat}"
    except ZeroDivisionError:
        return "Greshka delenje so nula ne e dozvoleno."

print(podeli_broevi())




def zbir_na_broevite():
    try:
        broj = input("Vnesi brojki ")
        broevi = broj.split(" ")

        zbir = sum(int(broj) for broj in broevi if broj)
        return zbir

    except ValueError:
        return "Greshka"

rezultat = zbir_na_broevite()
print("Zbirot e", rezultat)

with open("broevi.txt", "w") as data:
for broj in range(1, 31):
    if broj % 2 == 0:
        data.write(f"{broj}\n")





def zapisi():
    broj_ucenici = int(input("Vnesi ucenici"))
    with open("data.txt", 'a') as data:
        for i in range(broj_ucenici):
            ucenik = input("Vnesi go imeto na ucenikot")
            data.write(ucenik+"\n")

zapisi()


def zapishi():
    broj_na_uchenici = int(input("Vnesi kolku uchenici sakash da zapishesh "))


    with open("data.txt", "w") as data:
        for i in range(broj_na_uchenici):
            uchenik = input(f"Vnesi go imeto na uchenikot {i + 1}: ")

            if len(uchenik) < 4:
                data.write(uchenik + "\n")
                print(f"Imeto {uchenik} e zapishano.")
            else:
                print(f"Imeto {uchenik} ne e zapishano bidejki ima povekje od 3 bukvi")

zapishi()

def zapishi_broevi():
    broj_na_broevi = int(input("Vnesi kolku broevi sakash da zapishesh "))
    with open("broevi.txt", "w") as data:
        for i in range(broj_na_broevi):
            broj = input(f"Vnesi go brojot ")
            data.write(broj + "\n")

def presmetaj_suma_i_prosek():
    with open("broevi.txt", "r") as data:
        broevi = data.readlines()
        broevi = [int(broj.strip()) for broj in broevi]
        suma = sum(broevi)
        prosek = suma / len(broevi)
        print(f"Zbirot na broevite e {suma}")
        print(f"Prosekot na broevite e {prosek:.2f}")

zapishi_broevi()
presmetaj_suma_i_prosek()





import math
import csv
import os

def vnesi_uchenici():
    broj_na_uchenici = int(input("Kolku uchenici sakash da vnesesh "))

    uchenici = []

    for i in range(broj_na_uchenici):
        ime = input("Vnesi go imeto na uchenikot : ")
        prezime = input("Vnesi go prezimeto na uchenikot : ")
        godini = input("Vnesi gi godinite na uchenikot: ")


        uchenici.append([ime, prezime, godini])

    return uchenici

def zapishi_vo_csv(uchenici):
    file_name = "uchenici.csv"


    with open(file_name, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Ime", "Prezime", "Godini"])

        writer.writerows(uchenici)

    if os.path.exists(file_name):
        print(f"Podatocite se zapishani vo '{file_name}'.")
    else:
        print("Greshka pri sozdavanje na datotekata")

uchenici = vnesi_uchenici()
zapishi_vo_csv(uchenici)


def sortiraj(lista):
    lista.sort()
    with open("data.txt", 'w') as d:
        for broj in lista:
            d.write(str(broj) + "\n")
sortiraj([5,2,1,4])

import math

def kvadrat(lista):
    n_list = []
    for i in lista:
        n_list.append(math.pow(i, 2))
    return n_list

print(kvadrat([2,4,5]))


import random

def gradovi(num_cities, filename):
    with open(filename, 'w') as file:
        for i in range(num_cities):
            city = input(f"Vnesi go {i + 1}-ot grad: ")
            file.write(city + "\n")

def random_grad(filename):
    with open(filename, 'r') as file:
        cities = file.readlines()

    cities = [city.strip() for city in cities]

    random_city = random.choice(cities)
    print(f"Sledno patuvanje kje bide vo {random_city}")



num_cities = int(input("Kolku gradovi sakash da vnesesh? "))
filename = "gradovi.txt"

gradovi(num_cities, filename)

random_grad(filename)


import random
def generate_password():
    a = [1, 2, 3, 4, 5]
    b = ["a", "b", "c", "d", "e"]

    chosen_numbers = random.sample(a, 3)
    chosen_letters = random.sample(b, 3)

    combined = chosen_numbers + chosen_letters

    random.shuffle(combined)

    password = ''.join(map(str, combined))

    return password

print("Generirana lozinka:", generate_password())

import numpy as np
a=[1,2,3]
b=[4,5,6]
c=[7,8,9]
all=(a,b,c)
niza_od_a=np.array([a,b,c])
print(np.min(all))



def count_letter(letter, sentence):

    letter = letter.lower()
    sentence = sentence.lower()

    count = sentence.count(letter)

    return count

letter = input("Vnesi bukva ")
sentence = input("Vnesi ja rechenicata: ")

count = count_letter(letter, sentence)
print(count)


def count_letter(letter, sentence):

    letter = letter.lower()
    sentence = sentence.lower()

    brojac = 0

    for char in sentence:
        if char == letter:
            brojac += 1

    return brojac

letter = input("Vnesi bukva ")
sentence = input("Vnesi rechenica ")

brojac = count_letter(letter, sentence)
print(brojac)

def palindrome(word):
    word = word.lower()

    return word == word[::-1]

word = input("Vnesi zbor: ")

if palindrome(word):
    print(f"Zborot '{word}' e palindrom.")
else:
    print(f"Zborot '{word}' ne e palindrom.")




def palindrome(word):

    word = word.lower()


    length = len(word)

    for i in range(length // 2):
        if word[i] != word[length - i - 1]:
            return False

    return True

word = input("Vnesi zbor ")

if palindrome(word):
    print(f"Zborot '{word}' e palindrom.")
else:
    print(f"Zborot '{word}' ne e palindrom")


def najdi_najmal(numbers):

    index = 0
    smallest = numbers[0]


    while index < len(numbers):
        if numbers[index] < smallest:
            smallest = numbers[index]
        index += 1

    return smallest


numbers = [1,2,3,4,5,6]
najmal_broj = najdi_najmal(numbers)

print(najmal_broj)


