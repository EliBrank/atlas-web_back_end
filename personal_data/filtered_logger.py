#!/usr/bin/env python3

"""Creates filter_datum function"""

import re
from typing import List
import logging
import os
import mysql.connector

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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
    for field in fields:
        pattern: str = f"{field}=([^{separator}]*)"
        repl: str = f"{field}={redaction}"
        message = re.sub(pattern, repl, message)
    return message


def get_logger() -> logging.Logger:
    """Creates logging object to handle data from csv"""
    logger: logging.Logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler: logging.Handler = logging.StreamHandler()
    formatter: logging.Formatter = RedactingFormatter(list(PII_FIELDS))

    # logger contains handler(s)
    # handler contains (has setting for) formatter
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Set up mysql database with csv info"""


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format, obfuscate input record using defined attributes"""
        message_formatted: str = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            message_formatted, self.SEPARATOR)
