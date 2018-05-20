# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       fuenteAplicacion.py
# Autor:        Miguel Andres Garcia Niño
# Creado:       20 de Mayo 2018
# Modificado:   20 de Mayo 2018
# Copyright:    (c) 2018 by Miguel Andres Garcia Niño, 2018
# License:      Apache License 2.0
# ----------------------------------------------------------------------------

__versión__ = "1.0"

"""
El módulo *fuenteAplicacion* permite asignarle el tipo y tamaño de fuente a toda
la aplicación.
"""

from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLineEdit, QPushButton, QComboBox,
                             QLabel)
        

# ==================== CLASE ventanaPrincipal ======================

class ventanaPrincipal(QMainWindow):
    def __init__(self, parent=None):
        super(ventanaPrincipal, self).__init__(parent)
        
        self.setWindowTitle("Asignar tipo y tamaño de fuente a toda la aplicación por: ANDRES NIÑO")
        self.setWindowIcon(QIcon("icono.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(600, 500)

        self.initUI()

    def initUI(self):

      # ======================= WIDGETS ==========================

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(20, 20, 560, 25)

        button = QPushButton("Cambiar el tipo y tamaño de la fuente", self)
        button.setGeometry(20, 54, 275, 25)

        comboBox = QComboBox(self)
        comboBox.addItems(["Cambiar el tipo de fuente", "Cambiar el tamaño de la fuente"])
        comboBox.setGeometry(305, 54, 275, 25)

      # =============== APLICAR FUENTE AL LABEL ==================

        fuente = self.font()
        fuente.setPointSize(12)
        fuente.setBold(True)
        fuente.setCapitalization(QFont.MixedCase) # Representación para el texto.

        label = QLabel("Cambiar el tipo y tamaño de la fuente a toda la aplicación...", self)
        label.setFont(fuente)
        label.setGeometry(20, 88, 480, 25)

      # =================== EVENTO QPUSHBUTTON ===================

        button.clicked.connect(self.cambiarFuente)

  # ======================= FUNCIONES ============================

    def cambiarFuente(self):
        fuente = self.font()
        fuente.setCapitalization(QFont.MixedCase)

        # Aplicar fuente al objeto QApplication 
        aplicacion.setFont(fuente)

        # Pasar el foco al lineEdit
        self.lineEdit.setFocus()
   
            
# ================================================================

if __name__ == '__main__':
    
    import sys

    # La clase QApplication administra el flujo de control de la aplicación
    # GUI y la configuración principal.
    aplicacion = QApplication(sys.argv)

    fuente = QFont()
    fuente.setPointSize(10) # Tamaño de la fuente
    fuente.setFamily("Bahnschrift Light") # Tipo de fuente
    fuente.setCapitalization(QFont.AllUppercase) # Texto en mayúsculas 
    
    aplicacion.setFont(fuente) # Aplicar fuente al objeto QApplication 
    
    ventana = ventanaPrincipal()
    ventana.show()
    
    sys.exit(aplicacion.exec_())
