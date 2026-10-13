from collections import Counter
import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

def save_to_db(frequencies: Counter):
    database_url = os.getenv("database_url")
    if not database_url:
        print(database_url)
        return
    try:
        with psycopg.connect(database_url) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS  colour_frequencies(
                    colour VARCHAR(50) PRIMARY KEY,
                    frequency INTEGER NOT NULL
                    )
                    """
                )
                for colour, frequency in frequencies.items():
                    cursor.execute(
                        """
                        INSERT INTO colour_frequencies (colour, frequency)
                        VALUES (%s, %s)
                        ON CONFLICT (colour)
                        DO UPDATE SET frequency = EXCLUDED.frequency
                        """, (colour, frequency))
            print("Colour frequencies saved successfully.")

    except psycopg.Error as error:
        print("Database error:", error)
