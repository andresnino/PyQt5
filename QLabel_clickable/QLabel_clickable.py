# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       QLabel_clickable.py
# Autor:        Miguel Andres Garcia Niño
# Creado:       11 de Abril 2018
# Modificado:   11 de Abril 2018
# Copyright:    (c) 2018 by Miguel Andres Garcia Niño, 2018
# License:      Apache License 2.0
# ----------------------------------------------------------------------------

__versión__ = "1.0"

"""
El módulo *QLabel_clickable* permite llamar a una función al hacer clic o doble clic sobre
un QLabel
"""

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal, QTimer
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QMessageBox


# ===================== CLASE QLabelClickable ======================

class QLabelClickable(QLabel):
    clicked = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super(QLabelClickable, self).__init__(parent)

    def mousePressEvent(self, event):
        self.ultimo = "Clic"
    
    def mouseReleaseEvent(self, event):
        if self.ultimo == "Clic":
            QTimer.singleShot(QApplication.instance().doubleClickInterval(),
                              self.performSingleClickAction)
        else:
            # Realizar acción de doble clic.
            self.clicked.emit(self.ultimo)
    
    def mouseDoubleClickEvent(self, event):
        self.ultimo = "Doble Clic"
    
    def performSingleClickAction(self):
        if self.ultimo == "Clic":
            self.clicked.emit(self.ultimo)


# ===================== CLASE labelClickable =======================

class labelClickable(QDialog):
    def __init__(self, parent=None):
        super(labelClickable, self).__init__(parent)
        
        self.setWindowTitle("Label clickable por: ANDRES NIÑO")
        self.setWindowIcon(QIcon("icono.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(400, 511)

        self.initUI()

    def initUI(self):

      # ==================== WIDGET QLABEL =======================
        
        self.labelImagen = QLabelClickable(self)
        self.labelImagen.setGeometry(15, 15, 118, 130)
        self.labelImagen.setToolTip("Imagen")
        self.labelImagen.setCursor(Qt.PointingHandCursor)

        self.labelImagen.setStyleSheet("QLabel {background-color: white; border: 1px solid "
                                       "#01DFD7; border-radius: 5px;}")

        self.pixmapImagen = QPixmap("Qt.png").scaled(112, 128, Qt.KeepAspectRatio,
                                                     Qt.SmoothTransformation)
        self.labelImagen.setPixmap(self.pixmapImagen)
        self.labelImagen.setAlignment(Qt.AlignCenter)

      # ===================== EVENTO QLABEL ======================

      # Llamar función al hacer clic o doble clic sobre el label
        self.labelImagen.clicked.connect(self.Clic)

  # ======================= FUNCIONES ============================

    def Clic(self, accion):
        QMessageBox.information(self, "Tipo de clic",
                                "Hiciste {}.                         ".format(accion))


# ================================================================

if __name__ == '__main__':
    
    import sys
    
    aplicacion = QApplication(sys.argv)
    
    ventana = labelClickable()
    ventana.show()
    
    sys.exit(aplicacion.exec_())
