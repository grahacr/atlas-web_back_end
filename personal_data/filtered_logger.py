#!/usr/bin/env python3
'''
module includes function for obfuscating log message
utilizing regex
'''
import logging
import re
from typing import List


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
