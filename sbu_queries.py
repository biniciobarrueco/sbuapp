from bbdd_connections import database_connection



class Queries:
    def __init__(self):
        self.connection = database_connection()
        self.cursor = self.connection.cursor()

        #------------CODE ONLY FOR CREATE TABLE------------

        #for tbl_query in createtbls:
        #    self.cursor.execute(tbl_query)
        #self.cursor.execute("SHOW TABLES")
        #tables = self.cursor.fetchall()
        #print(tables)
        #---------------------------------------------------

    def insert_data(self,columns, values):
        
        place_holders=','.join(['%s']*len(values))
        query_insert="""INSERT INTO proyectos ({}) VALUES ('{}') """.format(columns,place_holders)
        self.cursor.execute(query_insert,list(values))
        self.connection.commit()
        pass

    def delete_data(self, query):
        pass

    def read_data(self, query):
        pass

    def update_data(self, query):
        pass


############################################################
# ---------------- QUERY INSTRUCTIONS --------------------
############################################################

''' 
# 1)     --------------CREATE TABLES-------------------------

proy_tbl = """CREATE TABLE IF NOT EXISTS proyectos (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NOMBRE_PROYECTO VARCHAR(80),
    MANDANTE VARCHAR(60),
    RUT_MANDANTE VARCHAR(14) UNIQUE,
    NOMBRE_CONTACTO VARCHAR(60),
    FONO_CONTACTO VARCHAR(20),
    CODIGO_OC VARCHAR (40),
    NETO INT,
    IVA INT,
    TOTAL_OC INT)"""

trab_tbl = """CREATE TABLE IF NOT EXISTS trabajadores (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    APELLIDOS VARCHAR(80),
    NOMBRES VARCHAR(60),
    FECHA_NACIMIENTO VARCHAR(20),
    EDAD INT,
    RUT VARCHAR(25) UNIQUE,
    TIPO_CONTRATO VARCHAR (25),
    CARGO VARCHAR (20),
    SUELDO_BASE INT,
    COLACION INT,
    MOVILIZACION INT,
    ASIGNACION_FAMILIAR INT,
    AFP VARCHAR (30),
    PREVISION_SALUD VARCHAR (30),
    FECHA_CONTRATO VARCHAR (25),
    FECHA_DESVINCULO VARCHAR (25),
    BANCO VARCHAR (30),
    TIPO_CUENTA VARCHAR (25),
    NUMERO_CUENTA VARCHAR (40),
    CORREO VARCHAR (90) 
        )"""

fact_tbl = """CREATE TABLE IF NOT EXISTS facturas (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    FOLIO VARCHAR(100),
    TIPO_FACTURA VARCHAR(14),
    ID_PROYECTO SMALLINT,
    RUT VARCHAR(25) UNIQUE,
    MONTO_NETO INT,
    MONTO_IVA INT,
    MONTO_TOTAL INT
    )"""
afp_tbl = """CREATE TABLE IF NOT EXISTS afp (
    AFP VARCHAR (25),
    TASA_INDEPENDIENTE FLOAT,
    TASA_DEPENDIENTE FLOAT,
    SIS FLOAT
    )"""

asig_tbl = """CREATE TABLE IF NOT EXISTS asignacion_familiar (
    TRAMO VARCHAR(10),
    MONTO INT,
    REQUISITO_RENTA VARCHAR (50)
    )"""
ces_tbl = """CREATE TABLE IF NOT EXISTS seguro_cesantia (   
    TIPO_CONTRATO VARCHAR (20),
    FINANCIAMIENTO_EMPLEADOR FLOAT,
    FINANCIAMIENTO_TRABAJADOR FLOAT
    )"""

createtbls = [proy_tbl, afp_tbl, ces_tbl, asig_tbl, fact_tbl, trab_tbl]

# 2)     --------------INSERT INSTRUCTIONS-------------------------


'''

instance = Queries()