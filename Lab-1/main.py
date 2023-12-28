# Кладницкий Матвей, R3137
import os
import time

END_COLOR = '\u001b[0m'
RED_COLOR = '\u001b[41m'
PERCENT_COLOR = '\u001b[42m'
WHITE_COLOR = '\u001b[47m'


## Общие функции
def clear_screen():
    os.system('cls')

def wait(sec):
    time.sleep(sec * 1000)

def start_task(task_name):
    print(task_name + "\n")

def task_1():
    start_task('Сгенерировать при помощи escape-символов в консоли изображение флага, соответственно варианту (столбец "Страна"): Poland')
    
    LINE_SIZE = 30

    print(f'{WHITE_COLOR}{"  " * LINE_SIZE}{END_COLOR}')
    print(f'{WHITE_COLOR}{"  " * LINE_SIZE}{END_COLOR}')
    print(f'{WHITE_COLOR}{"  " * LINE_SIZE}{END_COLOR}')
    print(f'{RED_COLOR}{"  " * LINE_SIZE}{END_COLOR}')
    print(f'{RED_COLOR}{"  " * LINE_SIZE}{END_COLOR}')
    print(f'{RED_COLOR}{"  " * LINE_SIZE}{END_COLOR}')
    print('\n')

def task_2(width, height):
    start_task('Сгенерировать в консоли повторяющийся узор (столбец "Узор"): d')
    matrix = []
    for row in range(height):
        if row == 0 or row == height - 1 or row == 2:
            matrix.append('*' * width)

        else:
            row_string = ''
            for col in range(width):
                if row == 1 and col % 9 == 0:
                    row_string += '*'
                if row == 3 and col % 7 == 0 and col > 0:
                    row_string += '*'
                
                else:
                    row_string += ' '
            matrix.append(row_string)

    for row in matrix:
        print(row)

def task_3(HEIGHT, WIDTH):
    start_task('Сгенерировать в консоли график функции (1 четверти) при помощи escape-символов, минимум 9 строк в высоту (столбец "Функция"):')
    print("y=x^0.5")

    def func(x):
        return x ** 2
    
    for x_cursor in range(HEIGHT -1, -1, -1):
        y_row = ""
        for y_cursor in range(WIDTH):
            x = func(x_cursor)
            if x % 1 == 0 and x == y_cursor:
                y_row += "*"
            else:
                y_row += "_"
        print(y_row)

def task_4():
    start_task('Используя прилагаемый файл с числовой последовательностью sequence.txt, вывести диаграмму процентного соотношения согласно варианту:')
    print('Среднее по модулю первых 125 и вторых 125 чисел')

    with open('sequence.txt', 'r') as sequence:
        file = sequence.readlines()

    first_half = 0
    second_half = 0

    for number in file[:125]:
        first_half += abs(float(number))
    
    for number in file[125:]:
        second_half += abs(float(number))
    
    first_half = first_half / 125
    second_half = second_half / 125

    halfs_sum = first_half + second_half

    first_percent = first_half * 50 / halfs_sum
    second_percent = second_half * 50 / halfs_sum

    print(f'{first_half}/{second_half}')

    print(f'{PERCENT_COLOR}{"  " * int(first_percent)}{WHITE_COLOR}{"  " * int(second_percent)}{END_COLOR}')


task_1()
task_2(50, 5)
task_3(15, 100)
task_4()