import pymysql
import configparser
from DBUtils.PooledDB import PooledDB

###########################################################
class DB_Connector:
    '''
    MySQL Database connector.
    Providing services like inserting, updateing, deleting from the database
    '''
    def __init__(self, db_host, db_port, db_name, db_username, db_password):
        #Maintaining a database connection pool
        self.db_connection_pool = self.config(db_host, db_port, db_name, db_username, db_password)

        try:
            self.conn = self.db_connection_pool.get_connection()
            self.cur = self.conn.cursor()
            self.cur.execute("set names utf8;")
            self.commit()
        except Exception as e:
            raise e

    def __del__(self):
        self.cur.close()
        self.conn.close()


    #APIs
    def config(self, db_host, db_port, db_name, db_username, db_password):
        '''
        If no configuration is specified, it will do auto config,
        otherwise, it will do customized configuration

        '''
        #Do customized configuration
        conn_args = {
            'host': db_host,
            'port': db_port,
            'db': db_username,
            'user': db_username,
            'passwd': db_password,
            'charset': 'utf8mb4',
            'cursorclass': pymysql.cursors.DictCursor
        }

        #Setup DB connection pool done!
        db_connection_pool = DB_ConnectionPool(conn_args)
        return db_connection_pool

    def fetchone(self, sql):
        '''
        Fetch one record from database
        '''
        try:
            self.execute(sql)
            result = self.cur.fetchone()
        except Exception as err:
            print("fetchone()/" + sql)
            raise err
        return result

    def fetchall(self, sql):
        '''
         Fetch all records from database
         '''
        try:
            self.execute(sql)
            result = self.cur.fetchall()
        except Exception as err:
            print("fetchall()/" + sql)
            raise err
        return result

    def execute(self, sql):
        try:
            self.cur.execute(sql)
            self.commit()
        except Exception as err:
            print("execute()/" + sql)
            raise err

    def commit(self):
        try:
            self.conn.commit()
        except Exception as err:
            print("commit()")
            raise err

    def rollback(self):
        try:
            self.conn.rollback()
        except Exception as err:
            print("rollback()")
            raise err

###########################################################
class DB_ConnectionPool:
    '''
    A pool of thread safe connection
    '''
    def __init__(self, **conn_args):
        self.__pool = PooledDB(creator=pymysql, mincached=5, maxcached=20, **conn_args)

    # Implement singleton pattern with __new__
    def __new__(cls, *args, **kwargs):
        if not hasattr(DB_ConnectionPool, "_instance"):
            DB_ConnectionPool._instance = object.__new__(cls)
        return DB_ConnectionPool._instance

    ##### APIs #####
    # Return a database connection pool to the database
    def get_connection(self):
        conn = self.__pool.connection()
        return conn

