class Eagle:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"독수리의 나이는 {self.age}살 이름은 {self.name}"
