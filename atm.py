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
    def __init__(self, balance: float = 0,
                 value_divider: int = 50,
                 withdraw_tax_percent: float=1.5,
                 withdraw_min_tax: int = 30,
                 withdraw_max_tax: int =600, 
                 wealth_tax_limit: int = 5_000_000,
                 wealth_tax_percent: float = 10,
                 interest_operations: int = 3,
                 interest_percent: float = 3):
        self._balance = balance
        self._operations_count = 0
        self._value_divider = value_divider
        self._withdraw_tax_percent = withdraw_tax_percent
        self._withdraw_min_tax = withdraw_min_tax
        self._withdraw_max_tax = withdraw_max_tax
        self._wealth_tax_limit = wealth_tax_limit
        self._wealth_tax_percent = wealth_tax_percent
        self._interest_operations = interest_operations
        self._interest_percent = interest_percent

    def deposit(self, value: int) -> None:
        self._check_balance()

        if self._check_value(value):
            self._balance += value
            self._interest_bearing()
        else:
            print("Operation failed!")

        self.get_balance()

    def withdraw_balance(self, value: int) -> int:
        self._check_balance()
        withdraw_sum = value + self._get_taxes(self._withdraw_tax_percent, value,
                                                self._withdraw_min_tax,
                                                self._withdraw_max_tax)
        withdraw = 0

        if not self._check_value(value) or self._balance < withdraw_sum:
            print("Operation failed!")
        else:
            self._balance -= withdraw_sum
            withdraw = value
            self._interest_bearing()

        self.get_balance()
        return withdraw

    def get_balance(self) -> None:
        print(self._balance)

    def _check_balance(self) -> None:
        if self._balance > self._wealth_tax_limit:
            self._balance -= self._get_taxes(self._wealth_tax_percent)

    def _get_taxes(self, percent: float, value: int = None,
                  min_tax: int = 0, max_tax: int = 0) -> float:

        tax_value = self._balance if value is None else value
        tax_value *= (percent / 100)

        if not max_tax:
            return tax_value if tax_value < min_tax else min_tax
        else:
            if tax_value < min_tax:
                return min_tax
            elif tax_value > max_tax:
                return max_tax
            else:
                return tax_value

    def _check_value(self, value: int) -> bool:
        return value % self._value_divider == 0

    def _interest_bearing(self) -> None:
        self._operations_count += 1
        if self._operations_count % self._interest_operations == 0:
            self._balance += self._balance * (self._interest_percent / 100)
