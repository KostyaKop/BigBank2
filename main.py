
class Bank:
    def __init__(self):
        self.users = {}

    def add_user(self, name, balance):
        self.users[name] = balance
        print(f"User {name} with balance {balance} added.")

    def show_balance(self, name):
        if name in self.users:
            print(f"User {name} has balance {self.users[name]}.")
        else:
            print(f"User {name} not found.")
    def show_all_list(self):
        for name, balance in self.users.items():
            print(f"User {name} has balance {balance}.")

bank = Bank()

while True:
    print("Enter 'add' to add a user, 'balance' to show user balance, 'all' to show all list or 'exit' to quit.")
    command = input()
    if command == 'add':
        name = input("Enter user name: ")
        balance = int(input("Enter user balance: "))
        bank.add_user(name, balance)
    elif command == 'balance':
        name = input("Enter user name: ")
        bank.show_balance(name)
    elif command == 'all':
        bank.show_all_list()
    elif command == 'exit':
        break
    else:
        print("Invalid command.")


