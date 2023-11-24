# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков-архивов
# list-архивы также являются свойствами экземпляра

class Archive:
    '''Archive class that holds data of previous archives
    :param num: number value
    :param name: string value
    
    '''
    _instance = None
    archive_text = []
    archive_number = []
    
    def __new__(cls, text: str, number: int):
        if cls._instance is None:
            instance = super().__new__(cls)
            cls._instance = instance
        instance = cls._instance
        instance.text = text
        instance.number = number
        cls.archive_text.append(text)
        cls.archive_number.append(number)
        
        return instance

    def __repr__(self) -> str:
        return f"Archive({self.text}, '{self.number}')"

    def __str__(self) -> str:
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'


archive1 = Archive("First Text", 1)

print(archive1)

archive2 = Archive("Second Text", 2)

print(archive2)

archive3 = Archive("Third Text", 3)

print(archive1)
print(archive3)