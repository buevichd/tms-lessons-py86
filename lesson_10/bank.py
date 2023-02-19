import random
import json
import os


def generate_random_digits(count) -> str:
    return ''.join([str(random.randint(0, 9)) for i in range(count)])


class BankAccount:
    def __init__(self, card_holder, money=0.0, card_number=None, account_number=None):
        self.card_holder: str = card_holder.upper()
        self.money: float = money
        self.card_number: str = generate_random_digits(16) if card_number is None else card_number
        self.account_number: str = generate_random_digits(20) \
            if account_number is None else account_number


def convert_bank_account_to_dict(bank_account: BankAccount) -> dict:
    return {
        'card_holder': bank_account.card_holder,
        'money': bank_account.money,
        'card_number': bank_account.card_number,
        'account_number': bank_account.account_number
    }


def save_accounts(bank_accounts: dict[str, BankAccount], file_name: str):
    data = {number: convert_bank_account_to_dict(account)
            for number, account in bank_accounts.items()}
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=2)


def load_accounts(file_name) -> dict[str, BankAccount]:
    if not os.path.exists(file_name):
        return {}
    with open(file_name, 'r') as file:
        return {number: BankAccount(**data) for number, data in json.load(file).items()}


class Bank:
    def __init__(self, bank_accounts=None):
        self.bank_accounts: dict[str, BankAccount] = bank_accounts or {}

    def open_account(self, card_holder) -> BankAccount:
        account = BankAccount(card_holder)
        self.bank_accounts[account.account_number] = account
        return account

    def add_money(self, account_number, money):
        account = self.bank_accounts[account_number]
        account.money += money

    def transfer_money(self, from_account_number, to_account_number, money):
        self.bank_accounts[from_account_number].money -= money
        self.bank_accounts[to_account_number].money += money

    def external_transfer(self, from_account_number, to_external_number, money):
        self.bank_accounts[from_account_number].money -= money
        print(f'Банк перевёл {money}$ с вашего счёта {from_account_number} '
              f'на внешний счёт {to_external_number}')


class Controller:
    def __init__(self, data_file_name):
        self.data_file_name = data_file_name
        bank_accounts: dict[str, BankAccount] = load_accounts(data_file_name)
        self.bank = Bank(bank_accounts)

    def run(self):
        print('Здравствуйте, наш банк открылся!')
        while True:
            print('Выберите действие:')
            print('0. Завершить программу')
            print('1. Открыть новый счёт')
            print('2. Просмотреть открытые счета')
            print('3. Положить деньги на счёт')
            print('4. Перевести деньги между счетами')
            print('5. Совершить платёж')
            action = int(input())
            if action == 0:
                save_accounts(self.bank.bank_accounts, self.data_file_name)
                print('До свидания!')
                break
            elif action == 1:
                card_holder = input('Введите имя и фамилию держателя карты (на английском): ')
                account = self.bank.open_account(card_holder)
                print(f'Счёт {account.account_number} создан.')
            elif action == 2:
                self.show_accounts()
            elif action == 3:
                account_number = input('Введите номер cчёта: ')
                money = float(input(f'Количество денег: '))
                self.bank.add_money(account_number, money)
            elif action == 4:
                from_account_number = input('Введите номер cчёта-отправителя: ')
                to_account_number = input('Введите номер cчёта-получателя: ')
                money = float(input(f'Количество денег: '))
                self.bank.transfer_money(from_account_number, to_account_number, money)
            elif action == 5:
                from_account_number = input('Введите номер cчёта-отправителя: ')
                to_external_number = input('Введите номер счёта внешнего получателя: ')
                money = float(input(f'Количество денег: '))
                self.bank.external_transfer(from_account_number, to_external_number, money)
            else:
                print('Не поддерживаемая операция.')
            print()

    def show_accounts(self):
        print('Ваши открытые счета:')
        for account_number, account in self.bank.bank_accounts.items():
            print(f'Cчёт: {account_number}')
            print(f'   Остаток на счету: {account.money}$')
            print(f'   Номер карты: {account.card_number}')
            print(f'   Держатель карты: {account.card_holder}')


if __name__ == '__main__':
    controller = Controller('data.json')
    controller.run()

