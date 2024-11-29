from animal import Animal
class Dog(Animal):
    def __init__(self, name: str = 'Default dog name'):
        super().__init__(name)
    def __str__(self):
        return (f'Dog name: {self.Name}\n'
                f'Speaking: {self.speaking}')