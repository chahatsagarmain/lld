from abc import ABC, abstractmethod

class DBConnection(ABC):
    """
    Abstract Base Class (Interface) representing a Database Connection.
    """

    @abstractmethod
    def connect(self) -> None:
        """
        Establish a database connection.
        """
        pass


class SqlConnection(DBConnection):
    """
    Concrete implementation of DBConnection for a Relational (SQL) Database.
    """

    def connect(self) -> None:
        print("SQL database connection established successfully.")


class NoSqlConnection(DBConnection):
    """
    Concrete implementation of DBConnection for a Document/NoSQL Database.
    """

    def connect(self) -> None:
        print("NoSQL database connection established successfully.")
