from dataclasses import dataclass, field


@dataclass(order=True, frozen= True)
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int
    strength: int = 100


    def __post_init__(self):
        self.sort_index = self.strength


person1 = Person("Geralt", "Witcher", 30, 99)
person2 = Person("Yennefer", "Sorceress", 25)
person3 = Person("Gary", "Accountant", 54)

print(id(person2))
print(id(person3))
print(person1)

print(person1 > person2)
