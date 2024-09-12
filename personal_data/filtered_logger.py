#!/usr/bin/env python3
'''
module includes function for obfuscating log message
utilizing regex
'''
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
