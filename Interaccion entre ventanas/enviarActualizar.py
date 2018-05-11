# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       enviarActualizar.py
# Autor:        Miguel Andres Garcia Niño
# Creado:       10 de Mayo 2018
# Modificado:   10 de Mayo 2018
# Copyright:    (c) 2018 by Miguel Andres Garcia Niño, 2018
# License:      Apache License 2.0
# ----------------------------------------------------------------------------

__versión__ = "1.0"

"""
El módulo *enviarActualizar* permite enviar y actualizar información entre ventanas.
"""

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QDialog, QLineEdit, QPushButton,
                             QLabel)


# ====================== CLASE ventanaHija =========================

class ventanaHija(QDialog):
    def __init__(self, texto, parent=None):
        super(ventanaHija, self).__init__()

        self.parent = parent
        self.texto = texto
        
        self.setWindowTitle("Ventana hija por: ANDRES NIÑO")
        self.setWindowIcon(QIcon("icono.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(400, 400)

        self.initUI()

    def initUI(self):

      # ======================= WIDGETS ==========================

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setText(self.texto)
        self.lineEdit.setGeometry(20, 20, 360, 24)

        buttonLineEdit = QPushButton("Actualizar QLineEdit de la ventana principal", self)
        buttonLineEdit.setGeometry(20, 54, 360, 25)

        buttonLabel = QPushButton("Actualizar QLabel de la ventana principal", self)
        buttonLabel.setGeometry(20, 85, 360, 25)

        buttonFuncion = QPushButton("Actualizar QLineEdit de la ventana principal desde una\n"
                                    "función de la ventana principal", self)
        buttonFuncion.setGeometry(20, 120, 360, 50)

      # ================== EVENTOS QPUSHBUTTONS ==================

        buttonLineEdit.clicked.connect(self.actualizarLineEdit)
        buttonLabel.clicked.connect(self.actualizarLabel)
        buttonFuncion.clicked.connect(self.funcionVentanaPrincipal)

        # lambda: self.parent.lineEdit.setText(self.lineEdit.text())

  # ======================= FUNCIONES ============================

    def actualizarLineEdit(self):
        # Obtener texto del QLineEdit
        texto = self.lineEdit.text()

        # Insertar texto en el QLineEdit de la ventana principal
        self.parent.lineEdit.setText(texto)

    def actualizarLabel(self):
        # Obtener texto del QLineEdit
        texto = self.lineEdit.text()

        # Insertar texto en el QLabel de la ventana principal
        self.parent.label.setText(texto)

    def funcionVentanaPrincipal(self):
        # Obtener texto del QLineEdit
        texto = self.lineEdit.text()

        # Llamar función de la ventana principal pasandolé como parametro el texto
        # del QLineEdit
        self.parent.modificarTexto(texto)

        

# ==================== CLASE ventanaPrincipal ======================

class ventanaPrincipal(QMainWindow):
    def __init__(self, parent=None):
        super(ventanaPrincipal, self).__init__(parent)
        
        self.setWindowTitle("Interacción entre ventanas por: ANDRES NIÑO")
        self.setWindowIcon(QIcon("icono.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(500, 500)

        self.initUI()

    def initUI(self):

      # ======================= WIDGETS ==========================

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(20, 20, 354, 24)

        button = QPushButton("enviar y abrir", self)
        button.setGeometry(380, 20, 104, 25)

        self.label = QLabel("Esta información se actualizará desde otra ventana...", self)
        self.label.setGeometry(20, 54, 480, 20)

      # =================== EVENTO QPUSHBUTTON ===================

        button.clicked.connect(self.enviarAbrir)

  # ======================= FUNCIONES ============================

    def enviarAbrir(self):
        # Obtener texto del QLineEdit
        texto = self.lineEdit.text()

        # Llamar la ventana hija pasandole un parametro
        ventanaHija(texto, self).exec_()

    def modificarTexto(self, texto):
        # Insertar texto en el QLineEdit
        self.lineEdit.setText(texto)
            

# ================================================================

if __name__ == '__main__':
    
    import sys
    
    aplicacion = QApplication(sys.argv)
    
    ventana = ventanaPrincipal()
    ventana.show()
    
    sys.exit(aplicacion.exec_())
