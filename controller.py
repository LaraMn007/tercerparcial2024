import time
import sqlite3 as sql

def createDB():
    conn = sql.connect("autoconocimiento.db")
    print("Base de datos de autoconocimiento creada")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("autoconocimiento.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE preguntas (
    id_pregunta INTEGER PRIMARY KEY AUTOINCREMENT,
    texto_pregunta TEXT NOT NULL,
    respuesta_a TEXT NOT NULL,
    respuesta_b TEXT NOT NULL,
    inteligencia_relacionada TEXT NOT NULL
    );
    """)    
    print("Tabla creada")
    conn.commit()
    conn.close()

if __name__=="__main__":
    createDB()
    createTable()

