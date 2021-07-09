class Library:
    bookshelf = []

    def new_book(self, book_name: str, year_of_writing: int, name: str, country: str, birthday: int):
        author = Author(name, country, birthday)
        book = Book(book_name, year_of_writing, author)
        if len(self.bookshelf) < 1:
            self.bookshelf.append(book)
            book.bookshelf_length += 1
            print(f'"{book.book_name}" was added to bookshelf')
            for book_in_bookshelf in self.bookshelf:
                if author.name == book_in_bookshelf.author.name:
                    author.books.append(book)
                    return author.books
            return self.bookshelf
        else:
            for book_in_bookshelf in self.bookshelf:
                if book.book_name == book_in_bookshelf.book_name:
                    return f'"{book.book_name}" already in shelf!'
            else:
                self.bookshelf.append(book)
                book.bookshelf_length += 1
                print(f'"{book.book_name}" was added to bookshelf')
                for book_in_bookshelf in self.bookshelf:
                    if author.name == book_in_bookshelf.author.name:
                        author.books.append(book)
                        return author.books

    def group_by_author(self, author):
        grouped_list = []
        if len(self.bookshelf) < 1:
            return 'Empty bookshelf!'
        else:
            for b in self.bookshelf:
                if b.author.name == author:
                    grouped_list.append(b)
                else:
                    return 'Book with this author not found!'
                return grouped_list

    def group_by_year(self, year):
        grouped_list = []
        if len(self.bookshelf) < 1:
            return 'Empty bookshelf!'
        else:
            for b in self.bookshelf:
                if b.year_of_writing == year:
                    grouped_list.append(b)
                else:
                    return 'Book with this year of writing not found!'
                return grouped_list

    def __repr__(self):
        return 'Library'

    def __str__(self):
        return f'{len(self.bookshelf)} books in bookshelf'


class Book:
    bookshelf_length = 0

    def __init__(self, book_name, year_of_writing, author):
        self.book_name = book_name
        self.year_of_writing = year_of_writing
        self.author = author

    def __repr__(self):
        return f'{self.book_name}, {self.year_of_writing}, {self.author.name}'

    def __str__(self):
        return f'{self.book_name}, {self.year_of_writing}'


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f'{self.name}, {self.country}, {self.birthday}'

    def __str__(self):
        return f'{self.books}'


l1 = Library()


def user_interface():
    while True:
        user_choice = input('''\tLibrary\nChoice your action!\n
1 - add new book
2 - group by author
3 - group by year of writing\n''')
        if user_choice == '1':
            print(l1.new_book(book_name=input('Enter book name: '),
                              year_of_writing=int(input('Enter year of writing: ')),
                              name=input('Enter author name: '),
                              country=input('Enter author country: '),
                              birthday=int(input('Enter author year of birthday: '))))
        elif user_choice == '2':
            print(l1.group_by_author(input('Enter witch author books you wanna search: ')))
        elif user_choice == '3':
            print(l1.group_by_year(year=int(input('Enter year of writing: '))))
        else:
            print('Something went wrong!')
            break


user_interface()
