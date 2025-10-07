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
