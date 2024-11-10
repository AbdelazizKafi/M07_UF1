# Importo les  funcions del fitxer per poder accedir a la bbdd.
from conn import conn, connection

# Abans de crear la taula he tingut que implementar aquesta funció per evitar errors que he tingut.
# El que fa es comprobar la connexio a la bbdd ha sigut exitosa i que el cursor s'ha creat correctament.
# Creo una taula que tractarà de jugadors de futbo amb 6 columnes diferents.
if conn is not None and connection is not None:
    sql = '''
    CREATE TABLE JUGADORS(
        abreviacio VARCHAR(10) PRIMARY KEY,
        nom VARCHAR(255) NOT NULL,
        equip VARCHAR(255),
        posicio VARCHAR(50),
        gols INTEGER,
        trofeus INTEGER
    )
    '''
# Executo la consulta SQL per crear la taula.
    try:
        connection.execute(sql)
        conn.commit()
        print("Tabla JUGADORS creada correctament.")
    except Exception as error:
        print("Error al crear la taula:", error)
    finally:
        connection.close()
        conn.close()
# Si les funcions conn i connection no funcionen correctament, s'imprimirà aquest text.
# Faig això per poder identificar l'error concret en cas de rebre algún.
else:
    print("No s'ha pogut establir la connexió a la base de dades.")
