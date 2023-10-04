# 1․ Գրել BankUser class, որը․
#    - __init__() -ում կընդունի մարդու անունը, ազգանունը, տարիքը, հաշվեհամարը, գումարը հաշվեհամարի վրա, գաղտնաբառը,
#    - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտները ճիշտ են մուտքագրված՝
#      -- անունը և ազգանունը - տառերից բաղկացած,
#      -- տարիքը - բնական թիվ,
#      -- հաշվեհամարը - 16 թվանշանից բաղկացած (xxxx xxxx xxxx xxxx կամ xxxxxxxxxxxxxxxx ֆորմատով),
#      -- գումարը - դրական թիվ,
#      -- գաղտնաբառը - ամենաքիչը 8 սիմվոլից բաղկացած տեքստ,
#    - անունը, ազգանունը և տարիքը կլինեն այնպիսի ատրիբուտներ, որոնց ուղիղ հասանելիությունը կլինի պաշտպանված,
#    - հաշվեհամարը, գումարը և գաղտնաբառը կլինեն այնպիսի ատրիբուտներ, որոնց ուղիղ հասանելիությունը կլինի արգելված,   
#    - կունենա մեթոդ, որը կվերադարձնի մարդու անունը և ազգանունը,
#    - կունենա մեթոդ, որը կվերադարձնի մարդու տարիքը,
#    - կունենա մեթոդ, որը կվերադարձնի հաշվեհամարը և գումարը, բայց միայն ճիշտ գաղտնաբառ հավաքելուց հետո,
#    - կունենա մեթոդ, որը կավելացնի գումար հաշվին,
#    - կունենա մեթոդ, որը կհանի գումար հաշվից, հաշվի առեք, որ գումարը բացասական չի կարող լինել,
#    - 3 անգամ սխալ գաղտնաբառ հավաքելուց հետո տվյալ user-ի համար հասանելիությունը class-ի ամբողջ ֆունկցիոնալությանը կլինի արգելված։

import string
class BankUser:
    PASSWORD_COUNT = 0
    def __init__(self, name, surname, age, account, amount, password):
        if not (self.validate_name(name) and self.validate_surname(surname) and self.validate_age(age) and \
        self.validate_account(account) and self.validate_amount(amount) and self.validate_password(password)):
            raise ValueError
        self._name = name
        self._surname = surname
        self._age = age
        self.__account = account
        self.__amount = amount
        self.__password = password

    @staticmethod
    def validate_name(text_name: str) -> bool:
        for i in text_name:
            if i not in string.ascii_letters:
                return False
        return True

    @staticmethod
    def validate_surname(text_surname: str) -> bool:
        for i in text_surname:
            if i not in string.ascii_letters:
                return False
        return True

    @staticmethod
    def validate_age(int_age: int) -> bool:
        return type(int_age) == int and int_age > 0
    
    @staticmethod
    def validate_account(str_account: str) -> bool:
        if len(str_account) == 16:
            for i in str_account:
                if i not in string.digits:
                    return False
        elif len(str_account) == 19:
            for i in str_account.split():
                if i not in string.digits:
                    return False
            if not (str_account[4] == ' ' and str_account[9] == ' ' and str_account[14] == ' '):
                return False
        else: 
            return False
        return True
    
    @staticmethod
    def validate_amount(int_amount: int) -> bool:
        return int_amount > 0

    @staticmethod
    def validate_password(str_pass: str) -> bool:
        return len(str_pass) >= 8 

    def name_surname(self):
        if self.pass_not_pass():
            return False
        return (self._name, self._surname)

    def user_age(self):
        if self.pass_not_pass():
            return False
        return self._age
    
    def user_account_details(self):
        if self.pass_not_pass():
            return False
        is_not_correct = True
        while is_not_correct and self.PASSWORD_COUNT < 3:
            user_password = input('Enter your password: ')
            if user_password != self.__password:
                self.PASSWORD_COUNT += 1
                print('Wrong password')
            else:
                is_not_correct = False
                return (self.__account, self.__amount)
        
    def add_money(self, money_in: int|float) -> int|float:
        if self.pass_not_pass():
            return False
        if type(money_in) is int or type(money_in) is float:
            self.__amount += money_in
            return self.__amount
        else:
            raise ValueError
    
    def take_money(self, money_out: int|float) -> int|float:
        if self.pass_not_pass():
            return False
        if self.__amount - money_out >= 0:
            self.__amount -= money_out
            return self.__amount
        else:
            raise ValueError

    @classmethod
    def pass_not_pass(cls):
        return cls.PASSWORD_COUNT == 3

User_3 = BankUser('Anna', 'Amiryan', 26, '1234567891011214', 1300, 'qwerty123')
print(User_3.pass_not_pass())
print(User_3.name_surname())
# print(User_3.user_age())
# print(User_3.add_money(120))
# print(User_3.take_money(10))
print(User_3.user_account_details())
print(User_3.name_surname())

       





