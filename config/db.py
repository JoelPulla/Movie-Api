from sqlmodel import SQLModel, create_engine, Session
from contextlib import contextmanager

""" Creamos el nombre, ruta y cracion del motor de la base de datos """
sqlite_file_name = "database.db"  
sqlite_url = f"sqlite:///{sqlite_file_name}"  
engine = create_engine(sqlite_url)  

""" Funcion para la creacion de la BDD segun los modelos"""
def init_db():
    SQLModel.metadata.create_all(engine)
    
"""
Proporciona una sesión para interactuar con la base de datos.
Uso de contextmanager para asegurar el cierre correcto de la sesión.
"""
@contextmanager
def get_session():
    with Session(engine) as session:
        yield session