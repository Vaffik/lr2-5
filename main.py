s:int = 0
n = int(input("Введите 8-разрядное число: "))
s = n % 10 + n / 10 % 10 + n / 100 % 10 + n / 1000 % 10 + n / 10000 % 10 + n / 100000 % 10 + n / 1000000 % 10 + n / 10000000
print (f"Сумма всех цифр равна {int(s)}")