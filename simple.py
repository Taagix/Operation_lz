n= int(input("Введите число для проверки")) # ввод искомого числа
answer = True # переменная
for number in range (2, int(n**(1/2))+1): # запускает диапазон от 2 до квадратного корня из n
    answer = True # переменная
    if n % number == 0: # сравнивает остаток от деления с нулем
        answer = False # переменная
        break # переменная
if answer == True: #
    print (f"Искомое число {n} - четное Y")
else:
    print (f"Искомое число {n} - нечетное N")