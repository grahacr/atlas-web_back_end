#!/usr/bin/env python3
'''
module includes function for obfuscating log message
utilizing regex
'''
import logging
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
