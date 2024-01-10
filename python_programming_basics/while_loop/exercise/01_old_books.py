# Книгите в библиотеката са свършили щом получите текст "No More Books".
# •	Ако не открие търсената книгата да се отпечата на два реда:
# o	"The book you search is not here!"
# o	"You checked {брой} books."
# •	Ако открие книгата си се отпечатва един ред:
# o	"You checked {брой} books and found it."

search_book = input()
curr_book = input()
book_num = 0

while curr_book != 'No More Books':

    if search_book == curr_book:
        print(f'You checked {book_num} books and found it.')
        break

    else:
        curr_book = input()
        book_num += 1

if curr_book == 'No More Books':
    print(f'The book you search is not here!')
    print(f'You checked {book_num} books.')




