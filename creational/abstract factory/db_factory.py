import os
import sys
from abc import ABC, abstractmethod

# Add the parent folder to the system path to allow importing from the neighboring 'factory' directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from factory.DBfactory import DBDriver, SqlDB, NoSqlDB
from db_connection import DBConnection, SqlConnection, NoSqlConnection
from query_builder import QueryBuilder, SqlQueryBuilder, NoSqlQueryBuilder

class AbstractDatabaseFactory(ABC):
    """
    The Abstract Factory interface.
    
    It declares a set of factory methods that return a family of related products.
    In this case, the family of products includes:
      1. A Database Driver (DBDriver)
      2. A Database Connection (DBConnection)
      3. A Database Query Builder (QueryBuilder)
    """

    @abstractmethod
    def create_driver(self) -> DBDriver:
        pass

    @abstractmethod
    def create_connection(self) -> DBConnection:
        pass

    @abstractmethod
    def create_query_builder(self) -> QueryBuilder:
        pass


class SqlDatabaseFactory(AbstractDatabaseFactory):
    """
    Concrete SQL Factory.
    
    Creates a family of objects compatible with a Relational (SQL) Database stack.
    """

    def create_driver(self) -> DBDriver:
        # Reuses the SQL Database Driver from the factory implementation
        return SqlDB()

    def create_connection(self) -> DBConnection:
        return SqlConnection()

    def create_query_builder(self) -> QueryBuilder:
        return SqlQueryBuilder()


class NoSqlDatabaseFactory(AbstractDatabaseFactory):
    """
    Concrete NoSQL Factory.
    
    Creates a family of objects compatible with a Document/NoSQL Database stack.
    """

    def create_driver(self) -> DBDriver:
        # Reuses the NoSQL Database Driver from the factory implementation
        return NoSqlDB()

    def create_connection(self) -> DBConnection:
        return NoSqlConnection()

    def create_query_builder(self) -> QueryBuilder:
        return NoSqlQueryBuilder()
