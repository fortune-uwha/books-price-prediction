from database.database import Database


class Queries:
    def __init__(self):
        self.__database = Database()

    def create_tables(self) -> None:
        """
        Builds table structure if it doesn't exist.
        :return: None
        """
        self.__database.execute_query('''
        CREATE TABLE IF NOT EXISTS history (
            id serial PRIMARY KEY,
            author varchar(255),
            edition varchar(255),
            category varchar(255),
            predicted_price FLOAT
        ); ''')

    def log_prediction(self, input_data, response) -> None:
        """
        Writes the request and prediction data to a database.
        :param input_data: validated json
        :param response: item price prediction json
        :return: None
        """
        query = f'''
            INSERT INTO history(
                author, edition, category, predicted_price) 
                VALUES('{input_data["author"]}', '{input_data["edition"]}', '{input_data["category"]}',
                '{response["predicted_price"]}'); '''
        self.__database.execute_query(query)

    def get_last_records(self, number_of_records: int = 10) -> list:
        """
        Gets a specified number of predictions from the database.
        :param predictions_to_show:
        :return: list
        """
        return self.__database.execute_query_and_fetch(f'''
            SELECT * FROM history ORDER BY id DESC LIMIT {number_of_records}''')
