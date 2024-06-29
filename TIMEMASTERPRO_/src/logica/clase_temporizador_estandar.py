import sqlite3
from datetime import datetime


class TemporizadorEstandar:
    def __init__(self, id=None, duration=None, started_at=None):
        self.id = id
        self.duration = duration
        self.started_at = started_at if started_at else datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def save_to_db(self):
        sql_update = 'UPDATE temporizadores_estandar SET duration=?, started_at=? WHERE id=?'
        sql_insert = 'INSERT INTO temporizadores_estandar (duration, started_at) VALUES (?, ?)'

        with sqlite3.connect('examen_final_temporizadores.db') as conn:
            cursor = conn.cursor()
            if self.id:
                cursor.execute(sql_update, (self.duration, self.started_at, self.id))
            else:
                cursor.execute(sql_insert, (self.duration, self.started_at))
                self.id = cursor.lastrowid
            conn.commit()

    @staticmethod
    def get_all_temporizadores():
        sql_select = 'SELECT * FROM temporizadores_estandar'

        with sqlite3.connect('examen_final_temporizadores.db') as conn:
            cursor = conn.cursor()
            cursor.execute(sql_select)
            temporizadores = cursor.fetchall()

        return [TemporizadorEstandar(id=row[0], duration=row[1], started_at=row[2]) for row in temporizadores]

    @staticmethod
    def get_temporizador_by_id(temporizador_id):
        sql_select_id = 'SELECT * FROM temporizadores_estandar WHERE id=?'

        with sqlite3.connect('examen_final_temporizadores.db') as conn:
            cursor = conn.cursor()
            cursor.execute(sql_select_id, (temporizador_id,))
            row = cursor.fetchone()

        if row:
            return TemporizadorEstandar(id=row[0], duration=row[1], started_at=row[2])
        return None

    def delete(self):
        sql_delete = 'DELETE FROM temporizadores_estandar WHERE id=?'

        with sqlite3.connect('examen_final_temporizadores.db') as conn:
            cursor = conn.cursor()
            cursor.execute(sql_delete, (self.id,))
            conn.commit()
