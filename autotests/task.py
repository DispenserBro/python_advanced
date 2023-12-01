class InvalidNameError(Exception):
    pass


class InvalidAgeError(Exception):
    pass


class InvalidIdError(Exception):
    pass


class StringValue:
    @classmethod
    def check_value(cls, value):
        if not isinstance(value, str):
            raise InvalidNameError('Value must be a string')
        if value == '':
            raise InvalidNameError(f'Invalid name: {value}. Name should be a non-empty string.')
    
    def __set_name__(self, owner, name):
        self.name = '_' + name
    
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        self.check_value(value)
        setattr(instance, self.name, value)


class AgeValue:
    def check_value(self, value):
        if not isinstance(value, (int, float)):
            raise InvalidAgeError('Value must be a number')
        if not value > 0:
            raise InvalidAgeError(f'Invalid {self.name[1:]}: {value}. Age should be a positive integer.')
    
    def __set_name__(self, owner, name):
        self.name = '_' + name
    
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        self.check_value(value)
        setattr(instance, self.name, value)


class IdValue:
    def check_value(self, value):
        if not isinstance(value, (int, float)):
            raise InvalidIdError('Value must be a number')
        if not 999_999 > value > 100_000:
            raise InvalidIdError(f'Invalid id: {value}. Id should be a 6-digit positive integer between 100000 and 999999.')
    
    def __set_name__(self, owner, name):
        self.name = '_' + name
    
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        self.check_value(value)
        setattr(instance, self.name, value)


class Person:
    last_name = StringValue()
    first_name = StringValue()
    surname = StringValue()
    age = AgeValue()
    
    def __init__(self, last_name, first_name, surname, age):
        self.last_name = last_name
        self.first_name = first_name
        self.surname = surname
        self.age = age
    
    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age


class Employee(Person):
    id = IdValue()
    def __init__(self, last_name, first_name, surname, age, id):
        super().__init__(last_name, first_name, surname, age)
        self.id = id
    
    def get_level(self):
        return sum(map(int, str(self.id))) % 7
