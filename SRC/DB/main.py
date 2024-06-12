from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Time
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from datetime import time
import unittest

Base = declarative_base()


class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)

    alarmas = relationship('Alarma', back_populates='usuario')
    configuraciones = relationship('ConfigurarTiempo', back_populates='usuario')
    temporizadores_pomodoro = relationship('TemporizadorPomodoro', back_populates='usuario')
    temporizadores_estandar = relationship('TemporizadorEstandar', back_populates='usuario')


class Alarma(Base):
    __tablename__ = 'alarmas'
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'))
    hora_alarma = Column(Time, nullable=False)

    usuario = relationship('Usuario', back_populates='alarmas')


class ConfigurarTiempo(Base):
    __tablename__ = 'configurar_tiempo'
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'))
    duracion_trabajo_estandar = Column(Integer, nullable=False)
    duracion_temporizador_estandar = Column(Integer, nullable=False)
    duracion_trabajo_pomodoro = Column(Integer, nullable=False)
    duracion_descanso_pomodoro = Column(Integer, nullable=False)
    duracion_alarma = Column(Integer, nullable=False)

    usuario = relationship('Usuario', back_populates='configuraciones')


class TemporizadorPomodoro(Base):
    __tablename__ = 'temporizadores_pomodoro'
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'))
    duracion_trabajo = Column(Integer, nullable=False)
    duracion_descanso = Column(Integer, nullable=False)

    usuario = relationship('Usuario', back_populates='temporizadores_pomodoro')


class TemporizadorEstandar(Base):
    __tablename__ = 'temporizadores_estandar'
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'))
    duracion_temporizador = Column(Integer, nullable=False)

    usuario = relationship('Usuario', back_populates='temporizadores_estandar')


# Crear un motor
engine = create_engine('sqlite:///midatabase.db')

# Crear todas las tablas
Base.metadata.create_all(engine)

# Crear una nueva sesión
Session = sessionmaker(bind=engine)
session = Session()


# Función para agregar 24 registros por tabla con datos distintos
def agregar_datos():
    for i in range(1, 25):
        usuario = Usuario(nombre=f'Usuario {i}')
        session.add(usuario)
        session.commit()  # Necesitamos commit aquí para obtener el id del usuario

        alarma = Alarma(id_usuario=usuario.id, hora_alarma=time(8, 0, i % 60))
        session.add(alarma)

        configurar_tiempo = ConfigurarTiempo(
            id_usuario=usuario.id,
            duracion_trabajo_estandar=i * 5,
            duracion_temporizador_estandar=i,
            duracion_trabajo_pomodoro=i * 2,
            duracion_descanso_pomodoro=i,
            duracion_alarma=i % 10
        )
        session.add(configurar_tiempo)

        temporizador_pomodoro = TemporizadorPomodoro(
            id_usuario=usuario.id,
            duracion_trabajo=i * 3,
            duracion_descanso=i
        )
        session.add(temporizador_pomodoro)

        temporizador_estandar = TemporizadorEstandar(
            id_usuario=usuario.id,
            duracion_temporizador=i * 2
        )
        session.add(temporizador_estandar)

    session.commit()


# Llamar a la función para agregar los datos
agregar_datos()


# Pruebas unitarias
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.session = session

    def test_usuarios(self):
        usuarios = self.session.query(Usuario).count()
        self.assertEqual(usuarios, 24)

    def test_alarmas(self):
        alarmas = self.session.query(Alarma).count()
        self.assertEqual(alarmas, 24)

    def test_configuraciones(self):
        configuraciones = self.session.query(ConfigurarTiempo).count()
        self.assertEqual(configuraciones, 24)

    def test_temporizadores_pomodoro(self):
        temporizadores_pomodoro = self.session.query(TemporizadorPomodoro).count()
        self.assertEqual(temporizadores_pomodoro, 24)

    def test_temporizadores_estandar(self):
        temporizadores_estandar = self.session.query(TemporizadorEstandar).count()
        self.assertEqual(temporizadores_estandar, 24)


if __name__ == '__main__':
    unittest.main()
