First = input('Введите первое число: ')
Second = input('Введите второе число: ')
Third = input('Введите третье число: ')
if First == Second and Second == Third:
    print(3, " Все числа равны")
elif First == Second or First == Third or Second == Third:
    print(2, " Два числа равны")
else:
    print(0, " Числа не равны друг другу")