class Animal:
    speaking = 'rrruff'
    speaking1 = 'mmaaaayy'
    def __init__(self, name: str = 'Default name'):
        self.Name = name
    def __str__(self):
        return (f'Name: {self.Name}\n'
                f'Speaking: {self.speaking1}')