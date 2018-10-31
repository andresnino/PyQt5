# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       crearDB.py
# Autor:        Miguel Andres Garcia Niño
# Creado:       27 de Octubre 2018
# Modificado:   27 de Octubre 2018
# Copyright:    (c) 2018 by Miguel Andres Garcia Niño, 2018
# License:      Apache License 2.0
# ----------------------------------------------------------------------------

__version__ = "1.0"

"""
El módulo *crearDB* permite crear la Base de Datos de la aplicación SIACLE.
"""

# Versión Python: 3.5.2

import sqlite3

# Crear base de datos fisica (reside en el disco)

"""Crear objeto de conexión, si la base de datos no existe se creara automáticamente y estará alojada en la misma
ubicación de este script"""
conexion = sqlite3.connect("DB_SIACLE.db")

# Crear cursor
cursor = conexion.cursor()

try:
    # Crear tabla si no existe
    cursor.execute("CREATE TABLE IF NOT EXISTS CLIENTES (ID INTEGER PRIMARY KEY, NOMBRE TEXT, APELLIDO TEXT, "
                   "SEXO TEXT, FECHA_NACIMIENTO TEXT, PAIS TEXT, TELEFONO_CELULAR TEXT)")

    datos_insertar = [("Andres", "Niño", "Masculino", "06/12/2019", "Colombia", "3104187394"),
                      ("Alex", "Garcia", "Masculino", "26/01/2019", "Colombia", "3114187394"),
                      ("Donald", "Trump", "Masculino", "06/12/1950", "Estados Unidos", "3124187394"),
                      ("María Fernanda", "Espinosa", "Femenino", "06/10/1980", "Ecuador", "3134187394"),
                      ("Alberto", "Canosa", "Masculino", "04/05/1876", "España", "3144187394"),
                      ("Virtud", "Pontes", "Femenino", "23/18/1965", "España", "3154187394"),
                      ("Elon", "Musk", "Masculino", "06/12/1960", "Estados Unidos", "3164187394"),
                      ("Richard", "Branson", "Masculino", "14/12/1956", "Reino Unido", "3174187394"),
                      ("Gabriel", "Garcia Marquez", "Masculino", "19/11/1948", "Colombia", "3184187394"),
                      ("Valentina", "Tereshkova", "Femenino", "06/03/1937", "Rusia", "3194187394"),
                      ("Artur", "Fischer", "Masculino", "31/12/1919", "Alemania", "32014187394"),
                      ("Grace", "Murray Hopper", "Femenino", "09/12/1906", "Estados Unidos", "3214187394"),
                      ("Guido van", "Rossum", "Masculino", "31/01/1956", "Países Bajos", "3224187394")]

    # Insertar multiples filas o datos
    cursor.executemany("INSERT INTO CLIENTES VALUES (NULL,?,?,?,?,?,?)", datos_insertar)

    # Guardar los cambios en la base de datos
    conexion.commit()

    print("Base de datos creada con éxito.")

# Capturar cualquier error que genere sqlite3
except sqlite3.Error as error:
    print("Error inseperado: {}".format(error))

# Cerrar conexión
conexion.close()
