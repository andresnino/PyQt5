# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       botonCircular.py
# Autor:        Miguel Andres Garcia Niño
# Creado:       10 de Julio 2018
# Modificado:   10 de Julio 2018
# Copyright:    (c) 2018 by Miguel Andres Garcia Niño, 2018
# License:      Apache License 2.0
# ----------------------------------------------------------------------------

__versión__ = "1.0"

"""
El módulo *botonCircular* permite pintar un botón circular perfecto e insertarle texto.
"""

# Versión Python: 3.5.2
# Versión PyQt5: 5.10.0

from PyQt5.QtGui import QIcon, QPainter, QColor, QFont, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QMessageBox


# ======================= CLASE PushButton =========================

class PushButton(QPushButton):
    def __init__(self, icono, parent=None):
        super(PushButton, self).__init__(parent)

        self.icono = QPixmap(icono)
        self.opacidad = QColor(0, 0, 0, 0)

        self.etiqueta = ""

        self.setMouseTracking(True)

    def paintEvent(self, event):
        ancho, altura = self.width(), self.height()
        icono = self.icono.scaled(ancho, altura, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        pintor = QPainter()
        
        pintor.begin(self)
        pintor.setRenderHint(QPainter.Antialiasing, True)
        pintor.setPen(Qt.NoPen)
        pintor.drawPixmap(0, 0, icono, 0, 0, 0, 0)
        pintor.setPen(Qt.white)
        pintor.drawText(event.rect(), Qt.AlignCenter, self.etiqueta)
        pintor.setPen(Qt.NoPen)
        pintor.setBrush(self.opacidad)
        pintor.drawEllipse(0, 0, ancho, altura)
        pintor.end()

        self.setMask(icono.mask())

    def enterEvent(self, event):
        self.opacidad = QColor(0, 0, 0, 26)

    def leaveEvent(self, event):
        self.opacidad = QColor(0, 0, 0, 0)

    def setText(self, texto):
        self.etiqueta = texto
        self.update()


# ====================== CLASE botonCircular =======================

class botonCircular(QDialog):
    def __init__(self, parent=None):
        super(botonCircular, self).__init__(parent)

        self.setWindowTitle("Botón circular en PyQt5 por: ANDRES NIÑO")
        self.setWindowIcon(QIcon("Qt.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(400, 400)

        self.initUI()

    def initUI(self):
        self.boton = PushButton("logoQt.png", self)
        # self.boton.setText("BOTÓN")
        self.boton.setToolTip("Botón")
        self.boton.setFixedSize(60, 60)
        self.boton.move(170, 100)

      # =================== EVENTO QPUSHBUTTON ===================
        
        self.boton.clicked.connect(self.Mensaje)

  # ======================= FUNCIONES ============================

    def Mensaje(self):
        mensaje = QMessageBox(self)
        mensaje.setWindowTitle("Mensaje")
        mensaje.setText("Si no se ha suscrito al canal, l@ invito a que lo haga...")
        mensaje.move(self.pos().x()+33, self.pos().y()+150)
        mensaje.exec_()


if __name__ == '__main__':

    import sys

    aplicacion = QApplication(sys.argv)

    fuente = QFont()
    fuente.setPointSize(10)
    fuente.setFamily("Bahnschrift Light")

    aplicacion.setFont(fuente)

    ventana = botonCircular()
    ventana.show()

    sys.exit(aplicacion.exec_())
