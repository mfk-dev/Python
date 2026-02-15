class Bank:
    def __init__(self, balance):
        self.__balance = balance # This is secret, so u cant see it directly!

    def balance(self):
        print(f"Balance: {self.__balance}")

hesap = Bank(1000)

# print(hesap.__balance)  <-- This will give an error.

hesap.balance()    # We can only see it this way.
