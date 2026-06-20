from abc import ABC, abstractmethod


class DBDriver(ABC):
    """
    Abstract Base Class (Interface) representing a Database Driver.

    All concrete database implementations (e.g., SQL, NoSQL) must implement
    this interface to ensure they can be used interchangeably by client code.
    """

    @abstractmethod
    def find(self, id: str) -> None:
        """
        Retrieve a record by its identifier.

        Args:
            id (str): The unique identifier of the record.
        """
        pass

    @abstractmethod
    def update(self, id: str, new_value: str) -> None:
        """
        Update an existing record with a new value.

        Args:
            id (str): The unique identifier of the record.
            new_value (str): The new value to set.
        """
        pass

    @abstractmethod
    def delete(self, id: str) -> None:
        """
        Delete a record by its identifier.

        Args:
            id (str): The unique identifier of the record to delete.
        """
        pass


class SqlDB(DBDriver):
    """
    Concrete implementation of DBDriver for a Relational (SQL) Database.
    """

    def find(self, id: str) -> None:
        print(f"find in sql called for id : {id}")

    def update(self, id: str, new_value: str) -> None:
        print(f"update called in sql for {id} and new value {new_value}")

    def delete(self, id: str) -> None:
        print(f"delete called in sql for {id}")


class NoSqlDB(DBDriver):
    """
    Concrete implementation of DBDriver for a Document/NoSQL Database.
    """

    def find(self, id: str) -> None:
        print(f"find in no sql called for id : {id}")

    def update(self, id: str, new_value: str) -> None:
        print(f"update called in no sql for {id} and new value {new_value}")

    def delete(self, id: str) -> None:
        print(f"delete called in no sql for {id}")


class DBFactory:
    """
    Factory class responsible for instantiating database driver objects.

    By centralizing object creation here, client code does not need to know
    the concrete classes (SqlDB, NoSqlDB) or their initialization details.
    """

    def get_db(self, db_name: str) -> DBDriver:
        """
        Factory method to create and return a database driver instance.

        Args:
            db_name (str): The type of database driver needed ('sql' or 'nosql').

        Returns:
            DBDriver: A concrete database driver instance implementing DBDriver.

        Raises:
            ValueError: If an unsupported or invalid db_name is provided.
        """
        normalized_name = db_name.strip().lower()
        if normalized_name == "sql":
            return SqlDB()
        elif normalized_name == "nosql":
            return NoSqlDB()
        else:
            raise ValueError(
                f"Unsupported database type: '{db_name}'. Supported types are 'sql', 'nosql'."
            )


if __name__ == "__main__":
    # Initialize the factory
    factory = DBFactory()

    # Create and interact with the SQL database driver
    sql = factory.get_db("sql")
    print(f"Obtained driver: {sql}")
    sql.find("123")
    sql.update("123", "Alice")
    sql.delete("123")

    print("-" * 40)

    # Create and interact with the NoSQL database driver
    nosql = factory.get_db("nosql")
    print(f"Obtained driver: {nosql}")
    nosql.find("456")
    nosql.update("456", "Bob")
    nosql.delete("456")