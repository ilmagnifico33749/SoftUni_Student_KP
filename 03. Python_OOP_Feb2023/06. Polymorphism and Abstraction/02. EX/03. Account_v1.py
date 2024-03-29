class Account:
    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions = list()

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def handle_transaction(self, transaction_amount):
        if self.balance + transaction_amount < 0:
            raise ValueError("sorry cannot go in debt!")
        self._transactions.append(transaction_amount)
        return f"New balance: {self.balance}"

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        return self.handle_transaction(amount)

    def __add__(self, other):
        new_account_name = self.owner + "&" + other.owner
        new_account_starting_amount = self.amount + other.amount
        new_account = Account(new_account_name, new_account_starting_amount)
        new_account._transactions = self._transactions + other._transactions
        return new_account

    # Below follow comparative function
    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, transaction_index):
        return f"{self._transactions[transaction_index]}"

    def __reversed__(self):
        # not sure whether only to reverse the order or also to return it
        return reversed(self._transactions)

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance


# ###################################################
# Test_Code_1:
acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)

print(f"ACC Balance: {acc.balance}")
print(f"ACC2 Balance: {acc2.balance}")
acc2.add_transaction(-30)
print(f"ACC2 Balance: {acc2.balance}")
print(acc != acc2)
# ---------------------------------------------------
# Output_1:
# Account of bob with starting amount: 10
# Account(bob, 10)
# 40
# 3
# 20
# -20
# 30
# -20
# [30, -20, 20]
# False
# False
# True
# True
# False
# True
# Account of bob&john with starting amount: 10
# [20, -20, 30, 10, 60]
# ###################################################
