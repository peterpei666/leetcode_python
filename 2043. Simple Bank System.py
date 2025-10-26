from typing import List

class Bank:
    def __init__(self, balance: List[int]):
        self.temp = balance
        self.n = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 > self.n or account2 > self.n or self.temp[account1 - 1] < money:
            return False
        self.temp[account1 - 1] -= money
        self.temp[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account > self.n:
            return False
        self.temp[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account > self.n or self.temp[account - 1] < money:
            return False
        self.temp[account - 1] -= money
        return True
