class Chapter:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

class Book:
    def __init__(self):
        self.chapters = []

    def add_chapter(self, chapter):
        self.chapters.append(chapter)

    def total_pages(self):
        return sum(chapter.page_count for chapter in self.chapters)

# Create book and add chapters
book = Book()
book.add_chapter(Chapter("Introduction to Python", 25))
book.add_chapter(Chapter("Object-Oriented Programming", 40))
book.add_chapter(Chapter("Advanced Topics", 35))

# Display total page count
print("Total pages in the book:", book.total_pages())
