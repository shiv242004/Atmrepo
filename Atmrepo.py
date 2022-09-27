import time
print('Insert your card!')
time.sleep(3)
password=1234
pin=int(input('enter your pin:'))
balance = 1500
print(balance)
if pin==password:
    while True:
        print('''
        1 == check balance
        2 == withdraw balance
        3 == deposite balance
        4 == Loan
        5 == exit''')
        op = int(input('Enter your choice:'))
        if op==1:
            print('Your balance is',balance)
        elif op==2:
            withdraw = int(input("Enter withdraw amount:"))
            balance-=withdraw
            print(withdraw," is debited from your account")
            print("Now your balance is:",balance)
        elif op == 3:
            print("OP3 ")
        elif op == 4:
            print("Option4 ")
        else:
            print("Wrong choice")
        