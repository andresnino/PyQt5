# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       botonRedondo.py
# Autor:        Miguel Andres Garcia Niño
# Creado:       10 de Mayo 2018
# Modificado:   10 de Mayo 2018
# Copyright:    (c) 2018 by Miguel Andres Garcia Niño, 2018
# License:      Apache License 2.0
# ----------------------------------------------------------------------------

__versión__ = "1.0"

"""
El módulo *botonRedondo* tiene como objetivo mostrar un botón redondo que solo sea clickable
la parte visual.
"""

from PyQt5.QtGui import QIcon, QRegion
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QMessageBox


# ====================== CLASE botonRedondo ========================

class botonRedondo(QDialog):
    def __init__(self, parent=None):
        super(botonRedondo, self).__init__(parent)
        
        self.setWindowTitle("Botón redondo por: ANDRES NIÑO")
        self.setWindowIcon(QIcon("icono.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(400, 511)

        self.initUI()

    def initUI(self):

      # ================== WIDGET QPUSHBUTTON ====================

        buttonRedondo = QPushButton("2019", self)
        buttonRedondo.setToolTip("Botón redondo")
        buttonRedondo.setCursor(Qt.PointingHandCursor)

        buttonRedondo.setFixedWidth(58)
        buttonRedondo.setFixedHeight(58)
        buttonRedondo.setMask(QRegion(QRect(-1, -1, 59, 59), QRegion.Ellipse))

        buttonRedondo.setStyleSheet("QPushButton {background-color: yellow; border: 1.8px solid black; "
                                    "border-radius: 29.4px} QPushButton:pressed "
                                    "{background-color: white;}")
        
        buttonRedondo.move(171, 80)

      # =================== EVENTO QPUSHBUTTON ===================

        buttonRedondo.clicked.connect(self.botonPresionado)

  # ======================= FUNCIONES ============================

    def botonPresionado(self):
        QMessageBox.information(self, "Botón redondo", "Hiciste clic sobre el botón   ",
                                QMessageBox.Ok)
            

# ================================================================

if __name__ == '__main__':
    
    import sys
    
    aplicacion = QApplication(sys.argv)
    
    ventana = botonRedondo()
    ventana.show()
    
    sys.exit(aplicacion.exec_())
