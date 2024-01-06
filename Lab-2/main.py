import csv
from random import randint

FILE_PATH = 'books-en.csv'
NEWLINE = ''

# task 1
NAME_COL = 'Book-Title'
MAX_CHAR_COUNT = 30

# task 2
BOOK_AUTHOR_COL = 'Book-Author'
COST_LIMIT = 200
COST_COL = 'Price'

# task 3
YEAR_COL = 'Year-Of-Publication'


def find_col_idx(col_name):
    with open(FILE_PATH, newline=NEWLINE, encoding='latin-1', mode='r') as file:
        rows = csv.reader(file)
        header_row = next(rows)[0]
        header_cells = str(header_row).split(";")

        for i in range(len(header_cells)):
            if header_cells[i].lower() == col_name.lower():
                return i

        return -1


def task_1():
    with open(FILE_PATH, newline=NEWLINE, encoding='latin-1', mode='r') as file:
        rows = csv.reader(file)
        result = 0

        book_title_idx = find_col_idx(NAME_COL)

        if (book_title_idx == -1):
            return '[TASK 1]: Failed'

        for row in rows:
            book_title = str(row).split(";")[book_title_idx]
            if len(book_title) > MAX_CHAR_COUNT:
                result += 1

        print('[TASK 1]: Вывести количество записей, у которых в поле Название строка длиннее 30 символов:', result)


def task_2():
    print('[TASK 2]: Реализовать поиск книги по автору, использовать ограничение на выдачу (до 200 р):')
    print('Введите имя автора:')
    author_name = input()

    with open(FILE_PATH, newline=NEWLINE, encoding='latin-1', mode='r') as file:
        rows = csv.reader(file)
        author_name_idx = find_col_idx(BOOK_AUTHOR_COL)
        book_title_idx = find_col_idx(NAME_COL)
        cost_idx = find_col_idx(COST_COL)

        next(rows)

        for row in rows:
            try:
                parsed_row = str(row[0]).split(";")
                current_author = parsed_row[author_name_idx]
                current_book = parsed_row[book_title_idx]
                current_cost = float(parsed_row[cost_idx])

                if current_author == author_name and current_cost < COST_LIMIT:
                    print(current_book)
            except:
                pass


def task_3():
    print('[TASK 3]: Реализовать генератор библиографических ссылок вида <автор>. <название> - <год> для 20 записей. Записи выбрать произвольно. Список сохраняется как отдельный файл текстового формата с нумерацией строк.')
    with open(FILE_PATH, newline=NEWLINE, encoding='latin-1', mode='r') as file:
        rows = csv.reader(file)
        next(rows)

        result = ''

        author_name_idx = find_col_idx(BOOK_AUTHOR_COL)
        book_title_idx = find_col_idx(NAME_COL)
        year_idx = find_col_idx(YEAR_COL)

        count = 0
        pos = 0

        for row in rows:
            if (count >= 20):
                break
            try:
                parsed_row = str(row[0]).split(";")
                current_author = parsed_row[author_name_idx]
                current_book = parsed_row[book_title_idx]
                current_year = int(parsed_row[year_idx])

                pos = count + 1
                result += f'({pos}). {current_author}. {current_book} - {current_year}\n'
                count += 1
            except:
                pass

        result_file = open("links.txt", "w")
        result_file.write(result)
        result_file.close()

        print("Данные были сохранены в файл links.txt")


task_1()
task_2()
task_3()
