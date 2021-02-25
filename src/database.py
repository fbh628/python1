import mysql.connector


class Database():
    def __init__(self, host, user, password, db_name):
        self.db = self.connect(host, user, password, db_name)

    def connect(self, host, user, password, db_name):
        return mysql.connector.connect(host=host, user=user, password=password, database=db_name)

    def get_cursor(self):
        return self.db.cursor()

    def get_books(self):
        cursor = self.get_cursor()
        cursor.execute("SELECT * FROM Books")
        data = cursor.fetchall()
        books = []
        for book in data:
            books.append((book[0], book[1]))
        return books

    def get_authors(self):
        cursor = self.get_cursor()
        cursor.execute("SELECT * FROM Authors")
        data = cursor.fetchall()
        authors = []
        for author in data:
            authors.append((author[0], author[1]))
        return authors

    def get_publishers(self):
        cursor = self.get_cursor()
        cursor.execute("SELECT * FROM Publishers")
        data = cursor.fetchall()
        publishers = []
        for publisher in data:
            publishers.append((publisher[0], publisher[1]))
        return publishers


if __name__ == "__main__":
    db = Database("localhost", "root", "LZhwH2sC9y6Hbk3eiwT", "schulepython")
    books = db.get_books()
    print(books)
