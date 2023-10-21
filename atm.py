# Напишите программу банкомат
# ✔Начальная сумма равна нулю
# ✔Допустимые действия: пополнить, снять, выйти
# ✔Сумма пополнения и снятия кратны 50 у.е.
# ✔Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔Нельзя снять больше, чем на счёте
# ✔При превышении суммы в 5 млн,
# вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔Любое действие выводит сумму денег

class ATM:
    def __init__(self, balance: float = 0, value_divider = 50,
                 wealth_tax_limit = 5_000_000,
                 wealth_tax_percent = 10,
                 interest_operations = 3,
                 interest_percent = 3):
        self.__balance = balance
        self.__operations_count = 0
        self.__value_divider = value_divider
        self.__wealth_tax_limit = wealth_tax_limit
        self.__wealth_tax_percent = wealth_tax_percent
        self.__interest_operations = interest_operations
        self.__interest_percent = interest_percent

    def add_balance(self, value: str) -> None:
        self.__check_balance()

        if self.__check_value(value):
            self.__balance += value
            self.__interest_bearing()
        else:
            print("Operation failed!")

        self.get_balance()

    def withdraw_balance(self, value: str) -> int:
        self.__check_balance()
        withdraw_sum = value + self.__get_taxes(1.5, value, 30, 600)
        withdraw = 0

        if not self.__check_value(value) or self.__balance < withdraw_sum:
            print("Operation failed!")
        else:
            self.__balance -= withdraw_sum
            withdraw = value
            self.__interest_bearing()

        self.get_balance()
        return withdraw

    def get_balance(self) -> None:
        print(self.__balance)

    def __check_balance(self) -> None:
        if self.__balance > self.__wealth_tax_limit:
            self.__balance -= self.__get_taxes(self.__wealth_tax_percent)

    # TODO: Replace with more correct calcultions && taxes calculations here
    def __get_taxes(self, percent: int, value: int = None,
                  min_tax: int = 0, max_tax: int = 0) -> float:

        tax_value = self.__balance if value is None else value
        tax_value *= (percent / 100)

        if not max_tax:
            return tax_value if tax_value > min_tax else min_tax
        else:
            if tax_value < min_tax:
                return min_tax
            elif tax_value > max_tax:
                return max_tax
            else:
                return tax_value

    def __check_value(self, value: int) -> bool:
        return value % self.__value_divider == 0

    def __interest_bearing(self) -> None:
        self.__operations_count += 1
        if self.__operations_count % self.__interest_operations == 0:
            self.__balance += self.__balance * (self.__interest_percent / 100)
