class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} pravi nekakov zvuk. "

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{self.name} koj e {self.breed}, lae: 'Av, Av!'"

dog = Dog("Reks", "Labrador")
print(dog.speak())




