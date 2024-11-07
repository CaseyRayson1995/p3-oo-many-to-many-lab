class Author:
    # Create an Author class that has the following attributes: name (string)
    def __init__(self, name: str):
        self.name = name
        self._contracts = []
        self._books = set()

    def contracts(self):
        """Returns a list of contracts associated with the author."""
        return self._contracts

    def books(self):
        """Returns a list of books associated with the author."""
        return list(self._books)

    def sign_contract(self, book, date, royalties):
        """Creates a contract for an author and book."""
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        self._books.add(book)
        return contract

    def total_royalties(self):
        """Calculates the total royalties across all contracts for the author."""
        return sum(contract.royalties for contract in self._contracts)


class Book:
    # Create a Book class that has the following attributes: title (string)
    def __init__(self, title: str):
        self.title = title
        self._contracts = []
        self._authors = set()

    def contracts(self):
        """Returns a list of contracts associated with the book."""
        return self._contracts

    def authors(self):
        """Returns a list of authors associated with the book."""
        return list(self._authors)


class Contract:
    # Static list to keep track of all contracts created
    all = []

    # Create a Contract class that has the following properties: author (Author object), book (Book object), date (string), and royalties (int)
    def __init__(self, author, book, date, royalties):
        # Validates that the author is an instance of Author
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of the Author class.")
        
        # Validates that the book is an instance of Book
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of the Book class.")
        
        # Validates that the date is of type str
        if not isinstance(date, str):
            raise TypeError("date must be a string.")
        
        # Validates that royalties is an integer
        if not isinstance(royalties, int):
            raise TypeError("royalties must be an integer.")

        # Setting attributes
        self._author = author
        self._book = book
        self._date = date
        self._royalties = royalties

        # Add contract to both author and book's lists of contracts
        author._contracts.append(self)
        author._books.add(book)
        book._contracts.append(self)
        book._authors.add(author)

        # Append to the list of all contracts
        Contract.all.append(self)

    @property
    def author(self):
        """Returns the author associated with the contract."""
        return self._author

    @property
    def book(self):
        """Returns the book associated with the contract."""
        return self._book

    @property
    def date(self):
        """Returns the date of the contract."""
        return self._date

    @property
    def royalties(self):
        """Returns the royalties for the contract."""
        return self._royalties

    @staticmethod
    def contracts_by_date(date):
        """Returns a list of contracts that match a given date."""
        return [contract for contract in Contract.all if contract.date == date]
