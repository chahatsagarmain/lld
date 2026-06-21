from db_factory import AbstractDatabaseFactory, SqlDatabaseFactory, NoSqlDatabaseFactory

def client_code(factory: AbstractDatabaseFactory) -> None:
    """
    The client code works with factories and products solely through their 
    abstract interfaces (AbstractDatabaseFactory, DBDriver, DBConnection, QueryBuilder).
    This keeps the client completely decoupled from concrete subclasses.
    """
    print(f"\n[Client] Initializing Database Suite using {factory.__class__.__name__}")
    
    # 1. Create the family of products
    connection = factory.create_connection()
    query_builder = factory.create_query_builder()
    driver = factory.create_driver()

    # 2. Use the products
    print("[Client] Activating connection...")
    connection.connect()
    
    # Generate query using query builder
    table = "users"
    conditions = {"status": "active", "role": "admin"}
    query = query_builder.build_query(table, conditions)
    print(f"[Client] Built Query: {query}")
    
    # Simulate DB operations using the driver
    print("[Client] Executing operations via driver:")
    driver.find("user_101")
    driver.update("user_101", "Developer")
    driver.delete("user_101")


if __name__ == "__main__":
    print("=== Abstract Factory Pattern Demo ===")
    
    # Test with SQL Database Stack
    sql_factory = SqlDatabaseFactory()
    client_code(sql_factory)
    
    print("\n" + "=" * 60 + "\n")
    
    # Test with NoSQL Database Stack
    nosql_factory = NoSqlDatabaseFactory()
    client_code(nosql_factory)
