# Игра отгадай число!

# Данный блок я заимствовал из Интернета (в "Блоке 0" такому не учили)
import numpy as np
num_random = np.random.randint(1, 101)

'''print(f'Загадано число - {num_random}') # Подсказка, какое число загадано (для контроля)'''

def number_search(num):
    count = 0 # Переменная счетчик попыток
    num_list = []
    while True: # Бесконечный цикл ввода чисел для сравнения с загаданным числом
        count +=1
        num = input('Давайте еще раз  - ')
        num = int(num)
        
        if num > num_random:
            num_list.append(num)
            print(f'Число {num} больше загаданного, введенные числа {num_list}')
        elif num < num_random:
            num_list.append(num)
            print(f'Число {num} меньше загаданного, введенные числа {num_list}')
        else:
            return print(f'Поздравляю!!! Загаданное число {num_random}, вы отгадали за {count} попыток(ки)')

number_search(input('Начнем игру, введите число от 1 до 100 - '))