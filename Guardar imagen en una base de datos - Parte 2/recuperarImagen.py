# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       recuperarImagen.py
# Autor:        Miguel Andres Garcia Niño
# Creado:       07 de Mayo 2018
# Modificado:   07 de Mayo 2018
# Copyright:    (c) 2018 by Miguel Andres Garcia Niño, 2018
# License:      Apache License 2.0
# ----------------------------------------------------------------------------

__versión__ = "1.0"

"""
El módulo *recuperarImagen* permite mostrar una foto en un QLabel y un nombre de usuario
en un QLineEdit que están almacenados en una Base de Datos (SQLite).
"""

from os import getcwd
from sqlite3 import connect

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal, QByteArray, QIODevice, QBuffer
from PyQt5.QtWidgets import (QApplication, QDialog, QLabel, QPushButton, QFileDialog,
                             QLabel, QLineEdit)


# ===================== CLASE QLabelClickable ======================

class QLabelClickable(QLabel):
    clicked = pyqtSignal()
    
    def __init__(self, parent=None):
        super(QLabelClickable, self).__init__(parent)

    def mousePressEvent(self, event):
        self.clicked.emit()


# ==================== CLASE recuperarImagen =======================

class recuperarImagen(QDialog):
    def __init__(self, parent=None):
        super(recuperarImagen, self).__init__(parent)
        
        self.setWindowTitle("Recuperar imagen por: ANDRES NIÑO")
        self.setWindowIcon(QIcon("icono.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(400, 511)

        self.initUI()

    def initUI(self):

      # ==================== WIDGET QLABEL =======================
        
        self.labelImagen = QLabelClickable(self)
        self.labelImagen.setGeometry(15, 15, 168, 180)
        self.labelImagen.setToolTip("Imagen")
        self.labelImagen.setCursor(Qt.PointingHandCursor)

        self.labelImagen.setStyleSheet("QLabel {background-color: white; border: 1px solid "
                                       "#01DFD7; border-radius: 2px;}")
        
        self.labelImagen.setAlignment(Qt.AlignCenter)

      # ==================== WIDGETS QLABEL ======================

        labelNombre = QLabel("Nombre de usuario", self)
        labelNombre.move(193, 15)

      # ================== WIDGETS QLINEEDIT =====================

        self.lineEditNombre = QLineEdit(self)
        self.lineEditNombre.setGeometry(193, 30, 192, 25)

      # ================= WIDGETS QPUSHBUTTON ====================

        buttonSeleccionar = QPushButton("Seleccionar", self)
        buttonSeleccionar.setToolTip("Seleccionar imagen")
        buttonSeleccionar.setCursor(Qt.PointingHandCursor)
        buttonSeleccionar.setGeometry(15, 200, 168, 25)

        buttonBuscar = QPushButton("Buscar", self)
        buttonBuscar.setToolTip("Buscar usuario")
        buttonBuscar.setCursor(Qt.PointingHandCursor)
        buttonBuscar.setGeometry(193, 60, 93, 25)

        buttonGuardar = QPushButton("Guardar", self)
        buttonGuardar.setToolTip("Guardar usuario")
        buttonGuardar.setCursor(Qt.PointingHandCursor)
        buttonGuardar.setGeometry(292, 60, 93, 25)

      # ===================== EVENTO QLABEL ======================

      # Llamar función al hacer clic sobre el label
        self.labelImagen.clicked.connect(self.seleccionarImagen)

      # ================== EVENTOS QPUSHBUTTON ===================

        buttonSeleccionar.clicked.connect(self.seleccionarImagen)
        buttonBuscar.clicked.connect(self.Buscar)
        buttonGuardar.clicked.connect(self.Guardar)
     

  # ======================= FUNCIONES ============================

    def seleccionarImagen(self):
        imagen, extension = QFileDialog.getOpenFileName(self, "Seleccionar imagen", getcwd(),
                                                        "Archivos de imagen (*.png *.jpg)",
                                                        options=QFileDialog.Options())
          
        if imagen:
            # Adaptar imagen
            pixmapImagen = QPixmap(imagen).scaled(166, 178, Qt.KeepAspectRatio,
                                                  Qt.SmoothTransformation)

            # Mostrar imagen
            self.labelImagen.setPixmap(pixmapImagen)

    def Buscar(self):
        # Obtener nombre de usuario
        nombre = " ".join(self.lineEditNombre.text().split()).title()

        if nombre:
            # Establecer conexión con la base de datos
            conexion = connect("DB_USUARIOS.db")
            cursor = conexion.cursor()

            # Buscar usuario en la base de datos
            cursor.execute("SELECT * FROM Usuarios WHERE NOMBRE = ?", (nombre,))
            resultado = cursor.fetchone()

            # Validar si se encontro algún resultado
            if resultado:
                # Cargar foto a un QPixmap
                foto = QPixmap()
                foto.loadFromData(resultado[1], "PNG", Qt.AutoColor)
                
                # Insertar foto en el QLabel
                self.labelImagen.setPixmap(foto)

                # Insertar nombre de usuario en el QLineEdit
                self.lineEditNombre.setText(resultado[0])
            else:
                self.labelImagen.clear()
                print("El usuario {} no existe.".format(nombre))
                
            # Cerrar la conexión con la base de datos
            conexion.close()

            self.lineEditNombre.setFocus()
        else:
            self.lineEditNombre.clear()
            self.lineEditNombre.setFocus()

    def Guardar(self):
        pass
            

# ================================================================

if __name__ == '__main__':
    
    import sys
    
    aplicacion = QApplication(sys.argv)
    
    ventana = recuperarImagen()
    ventana.show()
    
    sys.exit(aplicacion.exec_())
