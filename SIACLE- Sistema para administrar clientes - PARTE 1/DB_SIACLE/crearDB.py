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

"""Crear objeto de conexión, si la base de datos no existe se creara automáticamente y
estará alojada en la misma ubicación de este script"""
conexion = sqlite3.connect("DB_SIACLE.db")

# Crear cursor
cursor = conexion.cursor()

try:
    # Crear tabla si no existe
    cursor.execute("CREATE TABLE IF NOT EXISTS CLIENTES (ID INTEGER PRIMARY KEY, NOMBRE TEXT, "
                   "APELLIDO TEXT, SEXO TEXT, FECHA_NACIMIENTO TEXT, PAIS TEXT, "
                   "TELEFONO_CELULAR TEXT)")

    # Guardar los cambios en la base de datos
    conexion.commit()

    print("Base de datos creada con éxito.")

# Capturar cualquier error que genere sqlite3
except sqlite3.Error as error:
    print("Error inseperado: {}".format(error))

# Cerrar conexión
conexion.close()
