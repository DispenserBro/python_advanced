from atm import ATM


# add_balance method adds value to balance and calls interest_bearing method
def test_add_balance_adds_value_and_calls_interest_bearing():
    atm = ATM()
    atm.add_balance(100)
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
        atm.add_balance(75)
        captured = capsys.readouterr()
        assert captured.out == "Operation failed!\n0\n"


# withdraw_balance method fails if value is not divisible by value_divider or balance is less than withdraw sum
def test_withdraw_balance_fails_if_value_not_divisible_by_value_divider_or_balance_less_than_withdraw_sum(capsys):
    atm = ATM(balance=100)
    atm.withdraw_balance(75)
    captured = capsys.readouterr()
    assert captured.out == "Operation failed!\n100\n"













