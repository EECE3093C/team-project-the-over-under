import bitdotio
import pandas as pd

# Connect with bit.io API key credentials.
b = bitdotio.bitdotio("v2_3zxXD_wujECdYdhKwuU7nzWFG8M57")

# Define queries as below.
insert_test_row = """
    INSERT INTO matchups(home, away, competition)
    VALUES
        ('Bournemouth', 'Liverpool', 'Premier League')
    """

delete_test_row = """
    DELETE FROM matchups
    WHERE home = 'Bournemouth'
    """

# Execute queries with cursor.
with b.get_connection("ciminibb/mainline") as conn:
    cursor = conn.cursor()
    cursor.execute(insert_test_row)