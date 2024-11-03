from csv import reader
import random 

output = open('result.txt', 'w')

with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
    tbl = reader(csvfile, delimiter=';')
    tbl = list(tbl)
    for i in range(1, 21):
        row = random.choice(tbl)
        output.write(f'{i}. {row[2]}. {row[1]} - {row[3]}\n')
            
output.close()
print('Done')
