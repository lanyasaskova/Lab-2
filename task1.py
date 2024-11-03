from csv import reader

with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
    book = reader(csvfile, delimiter=';')
    flag = 0 #метка на количество названий более 30 символов
    for row in book:
        if len(row[1])>30:
            flag +=1

    print(f'Найдено {flag} книг с названиями длиной более 30 символов.')
