
def flip_numbers(num):
    if  num % 10 > 0:
        num1 = str(num)
        num2 = num1[::-1]
        print(int(num2))
    else:
        print('Ошибка! Введите число не оканчивающееся на 0')

flip_numbers(1230)
flip_numbers(123456789)