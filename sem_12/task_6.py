class Value:
    @classmethod
    def check_value(cls, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Value must be a number')
        if not value > 0:
            raise ValueError('Value must be greater than 0')
    
    def __set_name__(self, owner, name):
        self.name = '_' + name
    
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        self.check_value(value)
        setattr(instance, self.name, value)


value = Value()
value = -1
