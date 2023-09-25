import pymysql
import logging


class Database:

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        # self.db = db
        self.connection = None
        self.connect()

    def connect(self):
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                # database=self.db,
                # cursorclass=pymysql.cursors.DictCursor
            )
            self.connection._write_timeout = 10000
            logging.info('Database connection succeed')
        except Exception as e:
            logging.error(f'DB error: {str(e)}')
            self.connection = None

    def __del__(self):
        if self.connection:
            self.connection.close()

    def execute_query(self, query, args=None):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, args)
                result = cursor.fetchall()
                return result
        except (pymysql.err.InterfaceError, pymysql.err.OperationalError):
            # Переподключение к базе данных в случае ошибки
            self.connect()
            self.execute_query(query, args)

        except Exception as e:
            logging.error(f'DB error: {str(e)}')