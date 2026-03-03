class Tabungan:
    def __init__(self, tabungan_awal):
        self.__balance = tabungan_awal
    
    def get_balance(self):
        return self.__balance
        
    def deposit(self, money):
        self.__balance += money
    
    def withdraw(self, money):
        if self.__balance > money:
            self.__balance -= money
        else:
            raise Exception("Damn, broke ass")
        
    def transfer(self, tabungan_lain, money):
        self.withdraw(money)
        tabungan_lain.deposit(money)

tabungan_awal = int(input('masukkan tabungan awal: '))
tabungan = Tabungan(tabungan_awal)
tabungan2 = Tabungan(50000)
while True:
    pilihan = int(input('pilihan: '))
    match pilihan:
        case 1:
            print(tabungan.get_balance())
        case 2:
            deposit = int(input('uang yg mau dideposit: '))
            tabungan.deposit(deposit)
        case 3:
            withdrawal = int(input('uang yg mau diambil: '))
            tabungan.withdraw(withdrawal)
        case 4:
            transferred = int(input('uang yg mau ditransfer: '))
            tabungan.transfer(tabungan2, transferred)
        case 5:
            print(tabungan2.get_balance())
        case _:
            print('pilih yg bener')