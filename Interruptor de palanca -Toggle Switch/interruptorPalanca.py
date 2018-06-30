# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       interruptorPalanca.py
# Autores:      Miguel Andres Garcia Niño - Ángel Iván Hernández
# Creado:       29 de Junio 2018
# Modificado:   29 de Junio 2018
# Copyright:    (c) 2018 by Miguel Andres Garcia Niño - Ángel Iván Hernández, 2018
# License:      Apache License 2.0
# ----------------------------------------------------------------------------

__versión__ = "1.0"

"""
El módulo *interruptorPalanca* tiene como objetivo imitar las funciones de un
Toggle Switch (Interruptor de palanca).
"""

# Versión Python: 3.5.2
# Versión PyQt5: 5.10.0

from PyQt5.QtGui import QIcon, QFont, QPalette, QColor
from PyQt5.QtCore import Qt, QPoint, pyqtSignal, QTimer, QPropertyAnimation, QAbstractAnimation
from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QFrame, QLabel


# ========================= CLASE Frame ===========================

class Frame(QFrame):
    clicked = pyqtSignal(str)

    MIN_VALOR = 1
    MAX_VALOR = 101
    VALOR = MAX_VALOR + MIN_VALOR
    
    def __init__(self, parent=None):
        super(Frame, self).__init__(parent)

        self.parent = parent
        self.mover = QPoint()
        self.habilitado = False

    def actualizarEstado(self):
        # Si la posicion x del boton mas la mitad de su ancho
        # es menor que la mitad del ancho del widget padre,
        # entonces esta apagado (NO)
        if (self.parent.button.x() + (self.parent.button.width() / 2)) < Frame.VALOR / 2:
            self.habilitado = False
            
        # Si la posicion x del boton mas la mitad de su ancho
        # es mayor que la mitad del ancho del widget padre,
        # entonces esta encendido (SI)
        if (self.parent.button.x() + (self.parent.button.width() / 2)) > Frame.VALOR / 2:
            self.habilitado = True
            
        if self.habilitado:
            self.parent.button.setText("SI")
            color = QColor(206, 61, 59)
        elif not self.habilitado:
            self.parent.button.setText("NO")
            color = QColor(147, 183, 89)

        colorFrame = self.palette()
        colorFrame.setColor(QPalette.Background, color)
        self.setPalette(colorFrame)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mover.setY(1)
            
            if event.pos().x() < Frame.VALOR / 2:
                self.mover.setX(Frame.MIN_VALOR)
            elif event.pos().x() > Frame.VALOR / 2:
                self.mover.setX(Frame.MAX_VALOR - self.parent.button.width())

            self.animacion = QPropertyAnimation(self.parent.button, b"pos")
            self.animacion.setDuration(150)
            self.animacion.setEndValue(self.mover)
            self.animacion.valueChanged.connect(self.actualizarEstado)
            self.animacion.finished.connect(self.emitirEstado)
            self.animacion.start(QAbstractAnimation.DeleteWhenStopped)

    def emitirEstado(self):
        self.clicked.emit(self.parent.button.text())

        
# ====================== CLASE PushButton =========================

class PushButton(QPushButton):
    clicked = pyqtSignal(str)
    
    MIN_VALOR = 1
    MAX_VALOR = 101
    VALOR = MAX_VALOR + MIN_VALOR
    
    def __init__(self, parent=None):
        super(PushButton, self).__init__(parent)
        self.parent = parent
        
        self.pressing = False
        self.inicio = QPoint()
        self.mover = QPoint()
        self.habilitado = False
        self.arrastrado = False
        
        self.actualizarEstado()
        self.actualizarPosicion()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.ultimo = True
            self.inicio = event.pos()
            self.pressing = True
            self.actualizarEstado()

    def actualizarEstado(self):
        # Si la posicion x del boton mas la mitad de su ancho
        # es menor que la mitad del ancho del widget padre,
        # entonces esta apagado (NO)
        if (self.x() + (self.width() / 2)) < PushButton.VALOR / 2:
            self.habilitado = False
            
        # Si la posicion x del boton mas la mitad de su ancho
        # es mayor que la mitad del ancho del widget padre,
        # entonces esta encendido (SI)
        if (self.x() + (self.width() / 2)) > PushButton.VALOR / 2:
            self.habilitado = True
            
        if self.habilitado:
            self.setText("SI")
            color = QColor(206, 61, 59)
        elif not self.habilitado:
            self.setText("NO")
            color = QColor(147, 183, 89)

        colorFrame = self.palette()
        colorFrame.setColor(QPalette.Background, color)
        self.parent.setPalette(colorFrame)

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.mover = self.mapToParent(event.pos() - self.inicio)
            self.mover.setY(1)
            self.move(self.mover)

            self.arrastrado = True
            self.restringirMovimiento()
            self.actualizarEstado()

    def actualizarPosicion(self):
        self.mover.setY(1)

        if self.habilitado:
            self.mover.setX(PushButton.MAX_VALOR - self.width())
        else:
            self.mover.setX(PushButton.MIN_VALOR)

        self.animacion = QPropertyAnimation(self, b"pos")
        self.animacion.setDuration(150)
        self.animacion.setEndValue(self.mover)
        self.animacion.finished.connect(self.emitirEstado)
        self.animacion.start(QAbstractAnimation.DeleteWhenStopped)

    def restringirMovimiento(self):
        self.mover.setY(1)
        
        # Restringir lado izquierdo
        if self.x() < PushButton.MIN_VALOR:
            self.mover.setX(PushButton.MIN_VALOR)
            self.move(self.mover)
            return
        
        # Restringir lado derecho
        if (self.x() + self.width()) > PushButton.MAX_VALOR:
            self.mover.setX(PushButton.MAX_VALOR - self.width())
            self.move(self.mover)
            return

    def mouseReleaseEvent(self, event):
        if self.pressing:
            self.pressing = False
            self.actualizarEstado()
            self.actualizarPosicion()

            if not self.arrastrado and self.ultimo:
                # QApplication.instance().doubleClickInterval()
                QTimer.singleShot(100, self.performSingleClickAction)
            else:
                self.arrastrado = False

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.ultimo = False
    
    def performSingleClickAction(self):
        if self.ultimo:
            self.mover.setY(1)

            if self.habilitado:
                self.mover.setX(PushButton.MIN_VALOR)
            else:
                self.mover.setX(PushButton.MAX_VALOR - self.width())

            self.animacion = QPropertyAnimation(self, b"pos")
            self.animacion.setDuration(150)
            self.animacion.setEndValue(self.mover)
            self.animacion.valueChanged.connect(self.actualizarEstado)
            self.animacion.finished.connect(self.emitirEstado)
            self.animacion.start(QAbstractAnimation.DeleteWhenStopped)

    def emitirEstado(self):
        self.clicked.emit(self.text())


# =================== CLASE interruptorPalanca ====================

class interruptorPalanca(QDialog):
    def __init__(self, parent=None):
        super(interruptorPalanca, self).__init__(parent)

        self.setWindowIcon(QIcon("Qt.png"))
        self.setWindowTitle("Toggle Switch (Interruptor de palanca) en PyQt5")
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(400, 240)

        self.initUI()

    def initUI(self):

      # ========================= WIDGETS =========================

        fuenteLabel = self.font()
        fuenteLabel.setBold(True)

        self.frame = Frame(self)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFixedSize(102, 32)
        self.frame.setAutoFillBackground(True)
        self.frame.move(149, 84)

        self.button = PushButton(self.frame)
        self.button.setFixedSize(50, 30)
        self.button.setAutoDefault(False)
        self.button.move(1, 1)

        self.labelEstado = QLabel("ESTADO INTERRUPTOR: NO", self)
        self.labelEstado.setFont(fuenteLabel)
        self.labelEstado.move(112, 126)

      # =============== EVENTOS QFRAME - QPUSHBUTTON ==============

        self.frame.clicked.connect(self.estadoInterruptor)
        self.button.clicked.connect(self.estadoInterruptor)


  # ======================== FUNCIONES ============================

    def estadoInterruptor(self, texto):
        self.labelEstado.setText("ESTADO INTERRUPTOR: {}".format(texto))



# =================================================================

if __name__ == '__main__':

    import sys

    aplicacion = QApplication(sys.argv)

    fuente = QFont()
    fuente.setPointSize(10)
    fuente.setFamily("Bahnschrift Light")

    aplicacion.setFont(fuente)

    ventana = interruptorPalanca()
    ventana.show()

    sys.exit(aplicacion.exec_())
