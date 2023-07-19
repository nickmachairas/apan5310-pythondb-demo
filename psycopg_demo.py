import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect(
    "dbname=python_walkthrough user=postgres " 
    "password=123 host=localhost")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute(
    """
        CREATE TABLE IF NOT EXISTS customers (
        customer_id   integer,
        first_name    varchar(50) NOT NULL,
        last_name     varchar(50) NOT NULL,
        email         varchar(50) NOT NULL,
        cell_phone    varchar(20),
        PRIMARY KEY (customer_id)
    );
    """
)
# conn.commit()
# print('Table created successfully (probably).')

id = [1, 2, 3, 4, 5]
f_name = 'Jck'
l_name = 'Dulanty'
email = 'someemaiul'
cell = '1234567890'

# The process below will raise an error
for val in id:
    cur.execute(
        f"""
        INSERT INTO customers VALUES 
        ({id}, '{f_name}', '{l_name}', '{email}', '{cell}')
        """
    )


# Retrieve query results
# records = cur.fetchall()
conn.commit()
conn.close()

my_name = "Nick"

print(f"My name is {my_name}")
