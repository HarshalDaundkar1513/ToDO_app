import sqlite3
from flask import g

def open_to_database():
    sql = sqlite3.connect('todoapp.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_database():
    if not hasattr(g, 'todo_db'):
        g.todo_db = open_to_database()
    return g.todo_db