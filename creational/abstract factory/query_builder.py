from abc import ABC, abstractmethod

class QueryBuilder(ABC):
    """
    Abstract Base Class (Interface) representing a Query Builder.
    """

    @abstractmethod
    def build_query(self, table: str, conditions: dict) -> str:
        """
        Build and return a database query string based on the given table and conditions.
        """
        pass


class SqlQueryBuilder(QueryBuilder):
    """
    Concrete implementation of QueryBuilder for a Relational (SQL) Database.
    """

    def build_query(self, table: str, conditions: dict) -> str:
        cond_str = " AND ".join(f"{k}='{v}'" for k, v in conditions.items())
        return f"SELECT * FROM {table} WHERE {cond_str};"


class NoSqlQueryBuilder(QueryBuilder):
    """
    Concrete implementation of QueryBuilder for a Document/NoSQL Database.
    """

    def build_query(self, table: str, conditions: dict) -> str:
        cond_str = ", ".join(f"'{k}': '{v}'" for k, v in conditions.items())
        return f"db.{table}.find({{{cond_str}}});"
