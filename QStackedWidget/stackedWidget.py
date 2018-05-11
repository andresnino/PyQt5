# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       stackedWidget.py
# Autor:        Miguel Andres Garcia Niño
# Creado:       11 de Mayo 2018
# Modificado:   11 de Mayo 2018
# Copyright:    (c) 2018 by Miguel Andres Garcia Niño, 2018
# License:      Apache License 2.0
# ----------------------------------------------------------------------------

__versión__ = "1.0"

"""
El módulo *stackedWidget* proporciona una pila de widgets donde solo está visible un
widget a la vez.
"""

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QDialog, QComboBox, QStackedWidget, QWidget,
                             QPushButton, QLabel, QVBoxLayout)


# ======================== CLASE Boton ===========================

class Boton(QWidget):
    def __init__(self, parent=None):
        super(Boton, self).__init__(parent)

        self.initUI()

    def initUI(self):

      # ======================= WIDGETS ==========================

        button = QPushButton("Esto es un botón (QPushButton)")

      # ==================== DISEÑO (LAYOUT) =====================

        disenio = QVBoxLayout()
        disenio.setContentsMargins(0, 0, 0, 0)
        disenio.addWidget(button)

        self.setLayout(disenio)


# ====================== CLASE Etiqueta ==========================

class Etiqueta(QWidget):
    def __init__(self, parent=None):
        super(Etiqueta, self).__init__(parent)

        self.initUI()

    def initUI(self):

      # ======================= WIDGETS ==========================

        label = QLabel("Esto es una etiqueta (QLabel)")

      # ==================== DISEÑO (LAYOUT) =====================

        disenio = QVBoxLayout()
        disenio.setContentsMargins(0, 0, 0, 0)
        disenio.addWidget(label)
        disenio.setAlignment(label, Qt.AlignCenter)

        self.setLayout(disenio)


# ====================== CLASE ventanaHija =========================

class stackedWidget(QDialog):
    def __init__(self, parent=None):
        super(stackedWidget, self).__init__(parent)
        
        self.setWindowTitle("Pila de widgets (QStackedWidget) por : ANDRES NIÑO")
        self.setWindowIcon(QIcon("icono.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(400, 400)

        self.initUI()

    def initUI(self):

      # ======================= WIDGETS ==========================

        self.comboBox = QComboBox(self)
        self.comboBox.addItems(["Boton", "Etiqueta"])
        self.comboBox.setGeometry(20, 20, 360, 24)

        # Instancias
        self.boton = Boton(self)
        self.etiqueta = Etiqueta(self)

        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.addWidget(self.boton)
        self.stackedWidget.addWidget(self.etiqueta)
        self.stackedWidget.setGeometry(20, 84, 360, 25)

      # ==================== EVENTO QCOMBOBOX ====================

        self.comboBox.activated.connect(self.cambiarWidget)

  # ======================= FUNCIONES ============================

    def cambiarWidget(self):
        # Obtener el índice del item seleccionado en el QComboBox
        widget = self.comboBox.currentIndex()

        # Indicar el widget a visualizar
        self.stackedWidget.setCurrentIndex(widget)
            

# ================================================================

if __name__ == '__main__':
    
    import sys
    
    aplicacion = QApplication(sys.argv)
    
    ventana = stackedWidget()
    ventana.show()
    
    sys.exit(aplicacion.exec_())
