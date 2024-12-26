class Student:
    def __init__(self, ime, prezime, ocenki):
        self.ime = ime
        self.prezime = prezime
        self.ocenki = ocenki

    def prosek(self):
        return sum(self.ocenki) / len(self.ocenki)

    def popravi_ocenka(self, index, nova_ocenka):
        self.ocenki[index] = nova_ocenka

    def dodadi_ocenka(self, ocenka):
        self.ocenki.append(ocenka)

    def __str__(self):
        return f"Ime: {self.ime} {self.prezime}\nOcenki: {self.ocenki}\nProsek: {self.prosek()}"


class Fakultet:
    def __init__(self, ime, studenti=None):
        self.ime = ime
        self.studenti = studenti if studenti else []

    def prosek(self):
        prosek_na_studenti = [student.prosek() for student in self.studenti]
        return sum(prosek_na_studenti) / len(prosek_na_studenti)

    def najdobar_student(self):
        return max(self.studenti, key=lambda student: student.prosek()) if self.studenti else None

    def najlosh_student(self):
        return min(self.studenti, key=lambda student: student.prosek()) if self.studenti else None

    def dodadi_student(self, student):
        self.studenti.append(student)

    def izbrishi_student(self, ime, prezime):
        self.studenti = [student for student in self.studenti if not (student.ime == ime and student.prezime == prezime)]

    def __str__(self):
        my_str = f"Fakultet: {self.ime}\n"
        for student in self.studenti:
            my_str += str(student) + "\n"
        return my_str



def kreiraj_studenti(broj_na_studenti):
    studenti_lista = []
    for i in range(broj_na_studenti):
        print(f"\nVnesuvanje na student {i+1}:")
        ime = input("Vnesete ime na studentot: ")
        prezime = input("Vnesete prezime na studentot: ")

        broj_na_ocenki = int(input("Kolku ocenki sakate da vnesete? "))
        ocenki = []
        for j in range(broj_na_ocenki):
            ocenka = int(input(f"Vnesete ocenka {j+1}: "))
            ocenki.append(ocenka)

        student = Student(ime, prezime, ocenki)
        studenti_lista.append(student)

    return studenti_lista

if __name__ == "__main__":
    ime_fakultet = input("Vnesete ime na fakultetot: ")
    broj_na_studenti = int(input("Kolku studenti sakate da vnesete? "))


    studenti_lista = kreiraj_studenti(broj_na_studenti)


    fakultet = Fakultet(ime_fakultet, studenti_lista)


    print("\nFakultetot so site studenti:")
    print(fakultet)


    najdobar = fakultet.najdobar_student()
    najlosh = fakultet.najlosh_student()

    print(f"\nNajdobar student:\n{najdobar}")
    print(f"Najlosh student:\n{najlosh}")
