# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       barraTitulo.py
# Autor:        Miguel Andres Garcia Niño
# Creado:       17 de Mayo 2018
# Modificado:   17 de Mayo 2018
# Copyright:    (c) 2018 by Miguel Andres Garcia Niño, 2018
# License:      Apache License 2.0
# ----------------------------------------------------------------------------

__versión__ = "1.0"

"""
El módulo *barraTitulo* tiene como objetivo mostrar una Barra de Título personalizada
incluido un Menú.
"""

from PyQt5.QtGui import QPalette, QPixmap, QResizeEvent, QCursor, QMouseEvent
from PyQt5.QtCore import Qt, pyqtSignal, QPoint, QSize
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QWidget, QPushButton, QFrame,
                             QLabel, QToolButton, QHBoxLayout, QStyle, QMenu, QMessageBox)


# ===================== CLASE barraTitulo ==========================

class QLabelClickable(QLabel):
    clicked = pyqtSignal()
    
    def __init__(self, *args):
        QLabel.__init__(self, *args)
   
    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.clicked.emit()
        

class barraTitulo(QWidget):
    def __init__(self, parent):
        super(barraTitulo, self).__init__()
        
        self.parent = parent

        self.initUI()

    def initUI(self):

      # ======================= ESTILOS ==========================

        fuenteTitulo = self.font()
        fuenteTitulo.setPointSize(10)

        colorFrame = self.palette()
        colorFrame.setColor(QPalette.Background, Qt.yellow)

      # ======================= WIDGETS ==========================
      
        self.frameTitulo = QFrame()
        self.frameTitulo.setFrameStyle(QFrame.NoFrame)
        self.frameTitulo.setFixedHeight(30)
        self.frameTitulo.setAutoFillBackground(True)
        self.frameTitulo.setPalette(colorFrame)

        labelIcono = QLabelClickable()
        labelIcono.setObjectName("Icono")
        labelIcono.setPixmap(QPixmap("icono.png").scaled(18, 18, Qt.KeepAspectRatio,
                                                         Qt.SmoothTransformation))
        labelIcono.setAlignment(Qt.AlignCenter)
        labelIcono.setToolTip("Icono")
        labelIcono.setFixedWidth(32)
        labelIcono.setFixedHeight(24)
        labelIcono.setContextMenuPolicy(Qt.CustomContextMenu)
        labelIcono.customContextMenuRequested.connect(self.Menu)
        labelIcono.clicked.connect(self.Menu)

      # ================== QPUSHBUTTON QMENU =====================

        menuArchivo = QMenu()
        
        abrir = menuArchivo.addAction("Abrir proyecto", self.Abrir, "Ctrl+O")
        abrir.setShortcutVisibleInContextMenu(True)
        
        guardar = menuArchivo.addAction("Guardar el proyecto", self.Guardar, "Ctrl+S")
        guardar.setShortcutVisibleInContextMenu(True)
        
        guardarComo = menuArchivo.addAction("Guardar el proyecto como", self.guardarComo)
        
        menuArchivo.addSeparator()
        
        salir = menuArchivo.addAction("Salir", self.parent.close, "Alt+F4")
        salir.setShortcutVisibleInContextMenu(True)

        buttonArchivo = QPushButton("Archivo")
        buttonArchivo.setMenu(menuArchivo)
        buttonArchivo.setFixedWidth(70)
        buttonArchivo.setAutoDefault(False)

      # ==================== QLABEL TÍTULO =======================
        
        self.labelTitulo = QLabel("Barra de título con Menú por: ANDRES NIÑO")
        self.labelTitulo.setObjectName("Titulo")
        self.labelTitulo.setAlignment(Qt.AlignCenter)
        self.labelTitulo.setFont(fuenteTitulo)
        self.labelTitulo.setToolTip("Título")
        self.labelTitulo.setContextMenuPolicy(Qt.CustomContextMenu)
        self.labelTitulo.customContextMenuRequested.connect(self.Menu)

      # ============ QPUSHBUTTON MINIMIZAR - CERRAR ==============

        buttonMinimizar = QToolButton()
        buttonMinimizar.setToolTip("Minimizar")
        buttonMinimizar.setIconSize(QSize(38, 25))
        buttonMinimizar.setAutoRaise(True)
        buttonMinimizar.setIcon(QApplication.style().standardIcon(QStyle.SP_TitleBarMinButton))

        buttonCerrar = QToolButton()
        buttonCerrar.setToolTip("Cerrar")
        buttonCerrar.setIconSize(QSize(38, 25))
        buttonCerrar.setAutoRaise(True)
        buttonCerrar.setIcon(QApplication.style().standardIcon(QStyle.SP_TitleBarCloseButton))

      # ===================== DISEÑO (LAYOUT) ====================

        disenioFrame = QHBoxLayout()
        disenioFrame.setSpacing(0)
        disenioFrame.addWidget(labelIcono)
        disenioFrame.addWidget(buttonArchivo)
        disenioFrame.addWidget(self.labelTitulo)
        disenioFrame.addStretch()
        disenioFrame.addWidget(buttonMinimizar)
        disenioFrame.addWidget(buttonCerrar)
        disenioFrame.setContentsMargins(0, 0, 0, 0)

        self.frameTitulo.setLayout(disenioFrame)

        disenioFinal = QHBoxLayout()
        disenioFinal.addWidget(self.frameTitulo)
        disenioFinal.setContentsMargins(0, 0, 0, 0)

        self.setLayout(disenioFinal)

      # ==========================================================

        self.start = QPoint(0, 0)
        self.pressing = False

      # ================== EVENTOS QPUSHBUTTONS ==================

        buttonMinimizar.clicked.connect(self.Minimizar)
        buttonCerrar.clicked.connect(self.Cerrar)

  # ======================= FUNCIONES ============================

    def resizeEvent(self, QResizeEvent):
        super(barraTitulo, self).resizeEvent(QResizeEvent)
        self.frameTitulo.setFixedWidth(self.parent.width())
        self.labelTitulo.setFixedWidth(self.parent.width()-202)
        
    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end - self.start
            self.parent.setGeometry(self.mapToGlobal(self.movement).x(),
                                    self.mapToGlobal(self.movement).y(),
                                    self.parent.width(), self.parent.height())
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False

    def Menu(self, posicion=None):
        # Posicion del Mouse
        if self.sender().objectName() == "Icono":
            posicion = posicion if posicion else QPoint(0, 30)
        else:
            posicion = QPoint(posicion.x()+102, posicion.y())

        # Fuente
        fuente = self.font()
        fuente.setBold(True)

        # Crear menú
        menu = QMenu()
        
        restaurar = menu.addAction(QApplication.style().standardIcon(QStyle.SP_TitleBarNormalButton),
                                   "Restaurar")
        restaurar.setEnabled(False)
        
        mover = menu.addAction("Mover")
        mover.setEnabled(False)
        
        tamanio = menu.addAction("Tamaño")
        tamanio.setEnabled(False)
        
        minimizar = menu.addAction(QApplication.style().standardIcon(QStyle.SP_TitleBarMinButton),
                                   "Minimizar", self.Minimizar)
        
        maximizar = menu.addAction(QApplication.style().standardIcon(QStyle.SP_TitleBarMaxButton),
                                   "Maximizar")
        maximizar.setEnabled(False)
        
        menu.addSeparator()

        cerrar = menu.addAction(QApplication.style().standardIcon(QStyle.SP_TitleBarCloseButton),
                                "Cerrar", self.Cerrar, "Alt+F4")
        cerrar.setShortcutVisibleInContextMenu(True)
        cerrar.setFont(fuente)

        # Abrir el menu de contexto  
        menu.exec(self.mapToGlobal(posicion))

    def Abrir(self):
        QMessageBox.information(self, "Abrir", "Has hecho clic en Abrir proyecto",
                                QMessageBox.Ok)

    def Guardar(self):
        QMessageBox.information(self, "Guardar", "Has hecho clic en Guardar el proyecto",
                                QMessageBox.Ok)

    def guardarComo(self):
        QMessageBox.information(self, "Guardar como", "Has hecho clic en Guardar el proyecto "
                                "como", QMessageBox.Ok)

    def Minimizar(self):
        self.parent.showMinimized()

    def Cerrar(self):
        self.parent.close()


# =================== CLASE ventanaPrincipal =======================

class ventanaPrincipal(QDialog):
    def __init__(self, parent=None):
        super(ventanaPrincipal, self).__init__(parent)

        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowSystemMenuHint)
        self.setFixedSize(800, 400)
        self.pressing = False

        # Aplicar Barra de Título personalizada
        tituloBarra = QVBoxLayout()
        tituloBarra.addWidget(barraTitulo(self))
        tituloBarra.setContentsMargins(0, 0, 0, 0)
        tituloBarra.addStretch(-1)

        self.setLayout(tituloBarra)

        self.initUI()

    def initUI(self):

      # ======================= WIDGETS ==========================

        button = QPushButton("Desarrollo avanzado de GUI (PyQt5) en Python", self)
        button.setGeometry(15, 45, 300, 28)


# ================================================================

if __name__ == '__main__':
    
    import sys
    
    aplicacion = QApplication(sys.argv)
    
    ventana = ventanaPrincipal()
    ventana.show()
    
    sys.exit(aplicacion.exec_())
