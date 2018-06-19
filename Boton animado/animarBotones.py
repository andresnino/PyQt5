# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       animarBotones.py
# Autor:        Miguel Andres Garcia Niño
# Creado:       18 de Junio 2018
# Modificado:   18 de Junio 2018
# Copyright:    (c) 2018 by Miguel Andres Garcia Niño, 2018
# License:      Apache License 2.0
# ----------------------------------------------------------------------------

__versión__ = "1.0"

"""
El módulo *animarBotones* tiene como objetivo aumentar el tamaño de los botones al
pasar el cursor sobre ellos.
"""

# Versión Python: 3.5.2
# Versión PyQt5: 5.10.0

from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect, QAbstractAnimation
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QMessageBox


# ====================== CLASE hoverButton =========================

class hoverButton(QPushButton):
    def __init__(self, parent=None):
        QPushButton.__init__(self, parent)
        
        self.setMouseTracking(True)

        self.fuente = self.font()

        self.posicionX = int
        self.posicionY = int

    def enterEvent(self, event):
        self.posicionX = self.pos().x()
        self.posicionY = self.pos().y()
        
        self.animacionCursor = QPropertyAnimation(self, b"geometry")
        self.animacionCursor.setDuration(100)
        self.animacionCursor.setEndValue(QRect(self.posicionX-15, self.posicionY-6, 170, 38))
        self.animacionCursor.start(QAbstractAnimation.DeleteWhenStopped)
        
        self.fuente.setPointSize(11)
        self.setFont(self.fuente)

    def leaveEvent(self, event):
        self.fuente.setPointSize(10)
        self.setFont(self.fuente)
        
        self.animacionNoCursor = QPropertyAnimation(self, b"geometry")
        self.animacionNoCursor.setDuration(100)
        self.animacionNoCursor.setEndValue(QRect(self.posicionX, self.posicionY, 140, 28))
        self.animacionNoCursor.start(QAbstractAnimation.DeleteWhenStopped)


# ====================== CLASE animarBotones =======================

class animarBotones(QDialog):
    def __init__(self, parent=None):
        super(animarBotones, self).__init__(parent)
        
        self.setWindowTitle("Animar botones en PyQt5 por: ANDRES NIÑO")
        self.setWindowIcon(QIcon("Qt.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(400, 400)

        self.initUI()

    def initUI(self):

      # ======================== WIDGETS =========================

        self.button = hoverButton(self)
        self.button.setText("Suscribete...")
        self.button.setCursor(Qt.PointingHandCursor)
        self.button.setAutoDefault(False)
        self.button.setGeometry(40, 30, 140, 28)

        self.buttonUno = hoverButton(self)
        self.buttonUno.setText("Suscribete...")
        self.buttonUno.setCursor(Qt.PointingHandCursor)
        self.buttonUno.setAutoDefault(False)
        self.buttonUno.setGeometry(40, 70, 140, 28)

        self.buttonDos = hoverButton(self)
        self.buttonDos.setText("Suscribete...")
        self.buttonDos.setCursor(Qt.PointingHandCursor)
        self.buttonDos.setAutoDefault(False)
        self.buttonDos.setGeometry(220, 30, 140, 28)

        self.buttonTres = hoverButton(self)
        self.buttonTres.setText("Suscribete...")
        self.buttonTres.setCursor(Qt.PointingHandCursor)
        self.buttonTres.setAutoDefault(False)
        self.buttonTres.setGeometry(220, 70, 140, 28)

      # ================== EVENTOS QPUSHBUTTON ===================

        self.button.clicked.connect(self.Mensaje)
        self.buttonUno.clicked.connect(self.Mensaje)
        self.buttonDos.clicked.connect(self.Mensaje)
        self.buttonTres.clicked.connect(self.Mensaje)

  # ======================= FUNCIONES ============================

    def Mensaje(self):
        mensaje = QMessageBox(self)
        mensaje.setWindowTitle("Mensaje")
        mensaje.setText("Si no se ha suscrito al canal, l@ invito a que lo haga...")
        mensaje.move(self.pos().x()+33, self.pos().y()+150)
        mensaje.exec_()


# ================================================================

if __name__ == '__main__':
    
    import sys
    
    aplicacion = QApplication(sys.argv)

    fuente = QFont()
    fuente.setPointSize(10)
    fuente.setFamily("Bahnschrift Light")

    aplicacion.setFont(fuente)
    
    ventana = animarBotones()
    ventana.show()
    
    sys.exit(aplicacion.exec_())
