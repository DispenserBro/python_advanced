from atm import ATM


# add_balance method adds value to balance and calls interest_bearing method
def test_add_balance_adds_value_and_calls_interest_bearing():
    atm = ATM()
    atm.deposit(100)
    assert atm._ATM__balance == 100
    assert atm._ATM__operations_count == 1


# withdraw_balance method subtracts value and taxes from balance and calls interest_bearing method
def test_withdraw_balance_subtracts_value_and_taxes_and_calls_interest_bearing():
    atm = ATM(balance=100)
    assert atm.withdraw_balance(50) == 50
    assert atm._ATM__balance == 20
    assert atm._ATM__operations_count == 1


# get_balance method prints current balance
def test_get_balance_prints_current_balance(capsys):
        atm = ATM(balance=100)
        atm.get_balance()
        captured = capsys.readouterr()
        assert captured.out == "100\n"


# add_balance method fails if value is not divisible by value_divider
def test_add_balance_fails_if_value_not_divisible_by_value_divider(capsys):
        atm = ATM()
        atm.deposit(75)
        captured = capsys.readouterr()
        assert captured.out == "Operation failed!\n0\n"


# withdraw_balance method fails if value is not divisible by value_divider or balance is less than withdraw sum
def test_withdraw_balance_fails_if_value_not_divisible_by_value_divider_or_balance_less_than_withdraw_sum(capsys):
    atm = ATM(balance=100)
    atm.withdraw_balance(75)
    captured = capsys.readouterr()
    assert captured.out == "Operation failed!\n100\n"


# withdraw tax don't have upper limit if withdraw_balance is None or equals 0
def test_withdraw_balance_returns_unlimited_tax_if_max_tax_is_not_set():
    atm1 = ATM(balance=1_000_000)
    atm2 = ATM(balance=1_000_000, withdraw_max_tax=None)
    atm3 = ATM(balance=1_000_000, withdraw_max_tax=0)

    assert atm1.withdraw_balance(100_000) == atm2.withdraw_balance(100_000) == atm3.withdraw_balance(100_000)
    assert atm1._ATM__balance != atm2._ATM__balance
    assert atm2._ATM__balance == atm3._ATM__balance


def test_iterest_bearing_triggers():
    atm = ATM()
    test_balance = 30_000

    atm.deposit(test_balance / 3)
    atm.deposit(test_balance / 3)
    atm.deposit(test_balance / 3)

    assert atm._ATM__balance > test_balance










