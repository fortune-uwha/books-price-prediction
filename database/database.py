import os

from dotenv import load_dotenv
from psycopg2 import OperationalError, ProgrammingError, connect

load_dotenv()


class Database:
    def __init__(self) -> None:
        """
        Database class. This handles all connections to the PostgreSQL database on heroku.
        """
        self.__database_url = os.environ["DATABASE_URL"]

    def connect(self) -> None:
        """
        Connects to the database. Reads the credentials from .env.
        :return: Operational error if connection is unsuccessful.
        """
        try:
            connection = connect(self.__database_url)
            return connection
        except OperationalError as error:
            raise error

    def execute_query(self, query: str) -> None:
        """
        Executes SQL query. For queries which do not return any results, for example:
        INSERT, UPDATE, CREATE, ALTER, DROP, etc.
        :param query: SQL query
        :return: None
        """
        try:
            connection = self.connect()
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            connection.close()
        except ProgrammingError as error:
            raise error

    def execute_query_and_fetch(self, query: str) -> list:
        """
        Executes SQL query and fetches a response. For queries which return results, for example: SELECT.
        :param query: SQL query
        :return: array
        """
        try:
            connection = self.connect()
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            connection.close()
            return result
        except ProgrammingError as error:
            raise error
