# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       incrustarImagenes.py
# Autor:        Miguel Andres Garcia Niño
# Creado:       23 de Mayo 2018
# Modificado:   23 de Mayo 2018
# Copyright:    (c) 2018 by Miguel Andres Garcia Niño, 2018
# License:      Apache License 2.0
# ----------------------------------------------------------------------------

__versión__ = "1.0"

"""
El módulo *incrustarImagenes* permite incrustar imágenes en una aplicación, con el objetivo
de evitar la distribución de las imágenes junto con la aplicación.
"""

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

import imagenes


# =================== CLASE ventanaPrincipal =======================

class ventanaPrincipal(QMainWindow):
    def __init__(self, parent=None):
        super(ventanaPrincipal, self).__init__(parent)
        
        self.setWindowTitle("Incrustar imágenes en PyQt5 por: ANDRES NIÑO")
        self.setWindowIcon(QIcon(":imagenes/Qt.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(400, 400)

        self.initUI()

    def initUI(self):

      # ===================== WIDGET QLABEL ======================

        label = QLabel(self)
        label.setGeometry(20, 20, 100, 100)
        label.setPixmap(QPixmap(":imagenes/Python.png").scaled(100, 100, Qt.KeepAspectRatio,
                                                               Qt.SmoothTransformation))


# ================================================================

if __name__ == '__main__':
    
    import sys
    
    aplicacion = QApplication(sys.argv)
    
    ventana = ventanaPrincipal()
    ventana.show()
    
    sys.exit(aplicacion.exec_())
