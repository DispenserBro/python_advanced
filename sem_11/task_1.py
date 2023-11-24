# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)

from time import time
from datetime import datetime

class MyStr(str):
    def __new__(cls, value: str, author: str):
        instance = super().__new__(cls, value)
        instance.value = value
        instance.author = author
        instance.creation_time = time()

        return instance
    
    def __str__(self) -> str:
        return f'{self.value} (Автор: {self.author}, Время создания: {datetime.fromtimestamp(self.creation_time).strftime("%Y-%m-%d %H:%M")})'
    
    def __repr__(self) -> str:
        return f'MyStr(\'{self.value}\', \'{self.author}\')'


mstr = MyStr("qwe", "Dis_Bro")
print(mstr)
print(repr(mstr))
mstr2 = eval(repr(mstr))
print(mstr2)
print(repr(mstr2))
