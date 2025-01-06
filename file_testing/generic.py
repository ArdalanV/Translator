def greet(name):
    print(f"Hello, {name}!")

def calculate_sum(a, b):
    return a + b

def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        if self.species == "Dog":
            return "Woof!"
        elif self.species == "Cat":
            return "Meow!"
        else:
            return "Unknown sound"

if __name__ == "__main__":
    greet("World")
    print(calculate_sum(3, 5))
    print(print([1, 2, 3, 4, 5]))
    dog = Animal("Buddy", "Dog")
    print(dog.speak())
