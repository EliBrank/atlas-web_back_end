#!/usr/bin/env python3

"""Creates filter_datum function"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Obfuscates log message

    Args:
        fields: List of all fields (strings) to obfuscate
        redaction: String used to for obfuscating fields
        message: String for the log line
        separator: Character separating all fields in the log line (message)

    Returns:
        Log message string with obfuscation
    """
    filtered_string: str = ""
    for field in fields:
        pattern: str = f"{field}=([^{separator}]*)"
        repl: str = f"{field}={redaction}"
        filtered_string += re.sub(pattern, repl, message)
    return filtered_string
