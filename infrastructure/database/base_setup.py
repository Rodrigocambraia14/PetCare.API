from abc import ABC, abstractmethod
import sqlite3, datetime
from infrastructure.database.constants import *

class BaseSetup(ABC):

    @staticmethod
    def create_tables():
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id TEXT PRIMARY KEY,
        name TEXT,
        email TEXT,
        password TEXT
    )
""")

        cur.execute("""
    CREATE TABLE IF NOT EXISTS {} (
        id TEXT PRIMARY KEY,
        name TEXT,
        race TEXT,
        age INTEGER,
        gender TEXT,
        color TEXT,
        user_id TEXT,
        FOREIGN KEY (user_id) REFERENCES {}(id)
    )
""".format(pet_TABLE, USER_TABLE))
        
        cur.execute("""
    CREATE TABLE IF NOT EXISTS {} (
        id TEXT PRIMARY KEY,
        name TEXT,
        portions INTEGER,
        pet_id TEXT,
        FOREIGN KEY (pet_id) REFERENCES {}(id)
    )
""".format(FOOD_ROUTINE_TABLE, pet_TABLE))
        
        cur.execute("""
    CREATE TABLE IF NOT EXISTS {} (
        id TEXT PRIMARY KEY,
        name TEXT,
        grams INTEGER,
        feed_time TEXT,
        food_routine_id TEXT,            
        FOREIGN KEY (food_routine_id) REFERENCES {}(id)
    )
""".format(PORTION_DETAIL_TABLE, FOOD_ROUTINE_TABLE))
        
       
        
    @staticmethod
    def insert(table_name : str, obj):
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        # Assumindo que atributos do objeto  correspondem �s colunas das tabelas
        placeholders = ','.join(['?'] * len(obj.__dict__.keys()))
        columns = ','.join(obj.__dict__.keys())
        values = tuple(obj.__dict__.values())
        
        cur.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})", values)
        
        conn.commit()
        conn.close()
        
    @abstractmethod
    def view(self):
        pass
    
    @staticmethod
    def connect():
        conn = sqlite3.connect(DB_NAME)
        return conn
   
    @staticmethod
    def close(conn: sqlite3.Connection):
        conn.close()
        
    @staticmethod
    def commitAndClose(conn: sqlite3.Connection):
        conn.commit()
        conn.close()

