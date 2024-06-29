import sqlite3

# Inicializar la bd y crear las tablas necesarias
def initialize_database():
    conn = sqlite3.connect('examen_final_temporizadores.db')
    cursor = conn.cursor()

    # Crear tabla para alarmas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alarms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            alarm_time TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    ''')

    # Crear tabla para temporizadores estándar
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS temporizadores_estandar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            duration INTEGER NOT NULL,
            started_at TEXT NOT NULL
        )
    ''')

    # Crear tabla para temporizadores Pomodoro
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS temporizadores_pomodoro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            work_duration INTEGER NOT NULL,
            break_duration INTEGER NOT NULL,
            cycles INTEGER NOT NULL,
            started_at TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    initialize_database()
