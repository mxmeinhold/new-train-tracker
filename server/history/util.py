import psycopg2
import os

import server.secrets as secrets

HISTORY_TABLE_NAME = "newtrains_history"

HISTORY_DB_SCHEMA = f"""
CREATE TABLE IF NOT EXISTS {HISTORY_TABLE_NAME} (
    id SERIAL,
    is_new BOOLEAN NOT NULL,
    line VARCHAR(255) NOT NULL,
    car VARCHAR(5) NOT NULL,
    seen_start TIMESTAMP WITH TIME ZONE NOT NULL,
    seen_end TIMESTAMP WITH TIME ZONE NOT NULL,
    PRIMARY KEY (id)
);

CREATE INDEX {HISTORY_TABLE_NAME}_car ON {HISTORY_TABLE_NAME}(car);
""".strip()


def get_history_db_connection(with_db_name=True):
    db_host = os.getenv("POSTGRES_HOST", "localhost")

    dbname = secrets.POSTGRES_DB if with_db_name else None
    if secrets.POSTGRES_PASS == '':
        return psycopg2.connect(user=secrets.POSTGRES_USER, dbname=dbname, host=db_host)
    else:
        return psycopg2.connect(user=secrets.POSTGRES_USER, password=secrets.POSTGRES_PASS, dbname=dbname, host=db_host)
