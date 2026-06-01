from books.models import Book

# Lazy evaluation
books = Book.objects.filter(published=True)

# Query executes here
for book in books:
    print(book.title)

# View generated SQL
print(books.query)

# Count vs len
count = Book.objects.filter(published=True).count()
length = len(Book.objects.filter(published=True))

# Exists
exists = Book.objects.filter(published=True).exists()

# select_related
books = Book.objects.select_related("author")
for book in books:
    print(book.author.name)

# iterator
for book in Book.objects.iterator():
    print(book.title)
