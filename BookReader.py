'''
Created on Dec 6, 2016

@author: Monica
'''

def get_data(books, ratings):
    book_list = []
    author_book = {}
    d = {}
    
    f = open(books)
    for row in f:
        info = row.split(",")
        author = info[0]
        book = info[1].strip()
        book_list.append(book)
        if author not in author_book:
            author_book[author] = []
        author_book[author].append(book)
        
    f_rates = open(ratings)
    for row in f_rates:
        info = row.split()
        user = info[0].strip()
        rating = info[1:]
        if user not in d:
            d[user] = rating
    
    return book_list, author_book, d