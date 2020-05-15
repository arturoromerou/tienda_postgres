from psycopg2 import connect, Error
from logger import escribir_al_log

###################### CONEXION Y CIERRE DE CONEXION CON BASE DE DATOS ######################
class ConexionPG:

    bd = None
    cursor = None

    def __init__(self, **parametros):
        try:
            self.db = connect(
                host=parametros['direccion_servidor'],
                user=parametros['usuario'],
                password=parametros['contrasenia'],
                database=parametros['base_datos']
            )
            self.cursor = self.db.cursor()
        except Error as e:
            escribir_al_log(e, "ocurrio un error al conectar a la base de datos")

################################ EJECUTAR SENTENCIAS SQL ################################
    def _ejecutar_sql(
        self, sentencia_sql, parametros=None, 
        escribir_en_db=True
    ):
        try:
            self.cursor.execute(sentencia_sql, parametros) # execute corre las sentencias sql
            if escribir_en_db:
                self.db.commit()
        except Exception as e:
             escribir_al_log(e, f"Ocurrio un error al ejecutar la sentencia SQL:\n\n{sentencia_sql}\n")
        if escribir_en_db:
                self.db.rollback()

################################## LECTOR DE CODIGO SQL ##################################
    def _leer_desde_sql(self):
        try:
            registros = self.cursor.fetchall()
            for x in registros:
                print(x)
        except Exception as e:
            escribir_al_log(e, f'Un error ocurrió al momento de leer desde la BD')
        return registros

################################## CREAR TABLA ALMACEN EN BD ###################################
    def crear_tabla(self):  
        self._ejecutar_sql(
            """
            CREATE TABLE almacen (
                codigo_articulo SERIAL,
                nombre_articulo VARCHAR(50) NOT NULL,
                fecha TIMESTAMP,
                cantidad INT,
                precio DECIMAL,
                PRIMARY KEY (codigo_articulo)
            )
            """
        )
#################################### INSERTAR BD ALMACEN ####################################
    def insertar_articulos(self, nombre_articulo, cantidad, precio):
        self._ejecutar_sql(
            """INSERT INTO almacen (nombre_articulo, fecha, cantidad, precio) 
            VALUES (%s, CURRENT_DATE, %s, %s)""",
            (nombre_articulo, cantidad, precio)
    )
################################ VER ARTICULOS EN BD ALMACEN ################################
    def ver_articulos(self):
        self._ejecutar_sql(
            "SELECT * FROM almacen",
            escribir_en_db=False
        )
        self._leer_desde_sql()

################################ MODIFICAR ARTICULOS EN BD ALMACEN ################################

    def modificar_articulos(self, nombre_articulo, cantidad, precio, codigo_articulo):
        self._ejecutar_sql(
            """UPDATE almacen 
            SET nombre_articulo=%s,
                cantidad=%s,
                precio=%s
            WHERE
                codigo_articulo = %s""",
            (nombre_articulo, cantidad, precio, codigo_articulo)
        )

################################ ELIMINAR ARTICULOS EN BD ALMACEN ################################
    def eliminar_articulo_almacen(self, codigo_articulo):
        self._ejecutar_sql(
            "DELETE FROM almacen WHERE codigo_articulo=%s",
            (codigo_articulo,)
        )

################################## CREAR TABLA CLIENTES EN BD ###################################

    def crear_tabla_clientes(self):
        self._ejecutar_sql(
            """
            CREATE TABLE clientes (
                num_factura SERIAL,
                articulo VARCHAR (50) NOT NULL,
                fecha TIMESTAMP,
                cantidad INT,
                subtotal DECIMAL,
                igv DECIMAL,
                total DECIMAL,
                PRIMARY KEY (num_factura)
            )
            """
        )


#################################### INSERTAR BD CLIENTES ####################################

    def insertar_articulos_clientes(self, articulo, cantidad, subtotal, igv, total):
        self._ejecutar_sql(
            """INSERT INTO clientes (articulo, fecha, cantidad, subtotal, igv, total) 
            VALUES (%s, CURRENT_DATE, %s, %s, %s, %s)""",
            (articulo, cantidad, subtotal, igv, total)
        )

################################ VER ARTICULOS EN BD CLIENTES ################################
    def ver_articulos_clientes(self):
        self._ejecutar_sql(
            "SELECT * FROM clientes",
            escribir_en_db=False
        )
        self._leer_desde_sql()

################################ ELIMINAR ARTICULOS EN BD CLIENTES ################################
    def eliminar_articulo_usuarios(self, num_factura):
        self._ejecutar_sql(
            "DELETE FROM clientes WHERE num_factura=%s",
            (num_factura,)
        )