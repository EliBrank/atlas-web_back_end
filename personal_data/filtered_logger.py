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


def get_db() -> (mysql.connector.CMySQLConnection |
    mysql.connector.connection.MySQLConnection):
    """Set up mysql database"""
    user = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    # development password is pw
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD")
    host_name = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME", "my_db")

    connector_obj = mysql.connector.connect(
        user=user,
        password=password,
        host=host_name,
        database=db_name,
    )

    return connector_obj


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
