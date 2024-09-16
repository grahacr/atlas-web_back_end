#!/usr/bin/env python3
'''
module includes function for obfuscating log message
utilizing regex
'''
import logging
import os
import mysql.connector
import re
from typing import List

'''
tuple containing PII from user_data.csv which need to
be obfuscated from logger messaging
'''
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    '''
    filter_datum takes 4 arguments:
    - fields (a list of strings)
    - redaction (string) - to replace sensitive info
    - message (string) - full string to replace PII
    - separator (string) - separator to search for
    Returns:
    - String: obfuscated using redaction string
    '''
    pattern = ('|'.join(f'(?<={field}=)[^;]*?(?={separator}|$)'
                        for field in fields))
    return re.sub(pattern, redaction, message)


def get_db() -> mysql.connector.connection.MySQLConnection:
    '''
    get_db function - takes no arguments
    returns:
    mysql.connector connection
    set up connection to secure database
    using environmental variables for sensitive info credentials
    '''
    db_username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    db_password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    db_host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')

    connection = mysql.connector.connect(
        user=db_username,
        password=db_password,
        host=db_host,
        database=db_name
    )
    return connection


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        '''
        constructor method takes 2 args:
        - self
        - fields (list of strings)
        '''
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        '''
        format class method takes 2 arguments:
        - self
        - record (log record using logging module)
        Returns:
        - string, which will be a filtered message using filter_datum
        global method
        '''
        og_message = super().format(record)

        filtered_message = filter_datum(self.fields, self.REDACTION,
                                        og_message, self.SEPARATOR)
        return filtered_message


def get_logger() -> logging.Logger:
    '''
    get_logger function takes no arguments.
    Returns: logger object
    function creates logging object with formatted message
    stream and fields from global variable PII_FIELDS
    '''
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


def main():
    '''
    main function which will execute all other functions
    to set up database connection and execute logging
    '''
    db = get_db()
    if db:
        cursor = db.cursor(dictionary=True)
        cursor.execute(
            "SELECT name, email, phone, ssn, password, ip, last_login, user_agent FROM users")

        logger = get_logger()
        for row in cursor:
            message = (
                f"name={row['name']}; email={row['email']}; phone={row['phone']}; "
                f"ssn={row['ssn']}; password={row['password']}; ip={row['ip']}; "
                f"last_login={row['last_login']}; user_agent={row['user_agent']}"
            )
            logger.info(message)
        
        cursor.close()
        db.close()
    else:
        print("Database connection failed.")
        
if __name__ == '__main__':
    main()
