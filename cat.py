from animal import Animal
class Cat(Animal):
    def __init__(self, name: str = 'Default cat name'):
        super().__init__(name)
    def __str__(self):
        return (f'Cat name: {self.Name}\n'
                f'Speaking: {self.speaking1}')