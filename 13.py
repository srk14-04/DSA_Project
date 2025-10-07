from tableauhyperapi import HyperProcess, Connection, TableDefinition, CreateMode, Telemetry, TableName, SqlType, Inserter
import random

def generate_sample_data():
    names = ["John", "Jane", "Alice", "Bob", "Michael", "Emily"]
    email_domains = ["gmail.com", "yahoo.com", "outlook.com", "example.com"]
    years = [2020, 2021, 2022, 2023, 2024]
    titles = ["Engineer", "Analyst", "Manager", "Designer", "Developer"]

    data = []
    for _ in range(10):  
        name = random.choice(names)
        email = f"{name.lower()}_{random.randint(1, 100)}@{random.choice(email_domains)}"
        year = random.choice(years)
        title = random.choice(titles)
        data.append([name, email, year, title])

    return data

with HyperProcess(telemetry=Telemetry.SEND_USAGE_DATA_TO_TABLEAU) as hyper:
    with Connection(endpoint=hyper.endpoint, database="tabl.hyper", create_mode=CreateMode.CREATE_AND_REPLACE) as connection:
        table_definition = TableDefinition(
            table_name=TableName("Extract", "Extract"),
            columns=[
                TableDefinition.Column("name", SqlType.text()),
                TableDefinition.Column("email", SqlType.text()),
                TableDefinition.Column("year", SqlType.int()),
                TableDefinition.Column("title", SqlType.text())
            ]
        )

        connection.catalog.create_schema("Extract")
        connection.catalog.create_table(table_definition)

        data = generate_sample_data()

        with Inserter(connection, table_definition) as inserter:
            inserter.add_rows(data)
            inserter.execute()
print("Generating sample data...")
data = generate_sample_data()
print("Sample data generated successfully.")

with HyperProcess(telemetry=Telemetry.SEND_USAGE_DATA_TO_TABLEAU) as hyper:
    print("HyperProcess started.")
    with Connection(endpoint=hyper.endpoint, database="tabl.hyper", create_mode=CreateMode.CREATE_AND_REPLACE) as connection:
        print("Connection established.")
        table_definition = TableDefinition(
            table_name=TableName("Extract", "Extract"),
            columns=[
                TableDefinition.Column("name", SqlType.text()),
                TableDefinition.Column("email", SqlType.text()),
                TableDefinition.Column("year", SqlType.int()),
                TableDefinition.Column("title", SqlType.text())
            ]
        )

        connection.catalog.create_schema("Extract")
        print("Schema created.")
        connection.catalog.create_table(table_definition)
        print("Table created.")

        with Inserter(connection, table_definition) as inserter:
            inserter.add_rows(data)
            inserter.execute()
            print("Data inserted into the table.")
