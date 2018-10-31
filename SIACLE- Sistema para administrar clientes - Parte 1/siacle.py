# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       siacle.py
# Autor:        Miguel Andres Garcia Niño
# Creado:       27 de Octubre 2018
# Modificado:   27 de Octubre 2018
# Copyright:    (c) 2018 by Miguel Andres Garcia Niño, 2018
# License:      Apache License 2.0
# ----------------------------------------------------------------------------

__version__ = "1.0"

"""
La aplicación SIACLE (Sistema para administrar clientes) fue diseñada y desarrollada
por ANDRES NIÑO (Python developer) con fines educativos. Sientase libre de usarla.
"""

# Versión Python: 3.5.2
# Versión PyQt5: 5.11.3

import sqlite3

from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt, QTime, QTimer, QTranslator, QLocale, QLibraryInfo
from PyQt5.QtWidgets import (QApplication, QMainWindow, QDialog, QMenu, QPushButton, QAction,
                             QMessageBox, QStyle, QLabel)


# ========================= CLASE Ayuda ============================

class Ayuda(QDialog):
    def __init__(self, parent=None):
        super(Ayuda, self).__init__()

        self.setWindowTitle("Ayuda")
        self.setWindowFlags(Qt.WindowTitleHint | Qt.CustomizeWindowHint |
                            Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(450, 500)

        self.initUI()

    def initUI(self):
        label = QLabel(self)
        label.setPixmap(QPixmap("Imagenes/siacle.jpg").scaled(450, 450, Qt.KeepAspectRatio,
                                                              Qt.SmoothTransformation))
        label.move(0, 0)

        botonCerrar = QPushButton("Cerrar", self)
        botonCerrar.setFixedSize(430, 32)
        botonCerrar.move(10, 457)

      # ========================= EVENTO =========================

        botonCerrar.clicked.connect(self.close)


# ========================= CLASE Acerca ===========================

class Acerca(QDialog):
    def __init__(self, parent=None):
        super(Acerca, self).__init__()

        self.setWindowTitle("Acerca de Siacle")
        self.setWindowFlags(Qt.WindowTitleHint | Qt.CustomizeWindowHint |
                            Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(450, 500)

        self.initUI()

    def initUI(self):
        label = QLabel(self)
        label.setPixmap(QPixmap("Imagenes/siacle.jpg").scaled(450, 450, Qt.KeepAspectRatio,
                                                              Qt.SmoothTransformation))
        label.move(0, 0)

        labelAcerca = QLabel("SIACLE: sistema para administrar clientes, diseñado y\n"
                             "desarrollado por ANDRES NIÑO con fines educativos.", self)
        labelAcerca.move(10, 460)

        botonCerrar = QPushButton("Cerrar", self)
        botonCerrar.setFixedSize(80, 32)
        botonCerrar.move(360, 457)

      # ========================= EVENTO =========================

        botonCerrar.clicked.connect(self.close)


# ========================= CLASE Siacle ===========================

class Siacle(QMainWindow):
    def __init__(self, parent=None):
        super(Siacle, self).__init__(parent)

        self.setWindowIcon(QIcon("Imagenes/Qt.png"))
        self.setWindowTitle("SIACLE (Sistema para administrar clientes por: ANDRES NIÑO)")
        self.setMinimumSize(820, 302)

        self.initUI()

    def initUI(self):
    
      # ======================= ITEMS MENÚ =======================

        salir = QAction(self.style().standardIcon(QStyle.SP_MessageBoxCritical),
                        " Salir", self)
        salir.setShortcut("ESC")
        salir.triggered.connect(self.close)

        ayuda = QAction(self.style().standardIcon(QStyle.SP_MessageBoxQuestion),
                        " Ver la Ayuda", self)
        ayuda.setShortcut("Ctrl+A")
        ayuda.triggered.connect(lambda: Ayuda(self).exec_())

        acercaDe = QAction(self.style().standardIcon(QStyle.SP_MessageBoxInformation),
                           " Acerca de", self)
        acercaDe.setShortcut("Ctrl+D")
        acercaDe.triggered.connect(lambda: Acerca(self).exec_())

      # ========================= MENÚ ===========================
        
        menu = self.menuBar()
        
        siacleMenu = menu.addMenu("&Siacle")
        siacleMenu.addAction(salir)

        ayudaMenu = menu.addMenu("&Ayuda")
        ayudaMenu.addAction(ayuda)
        ayudaMenu.addSeparator()
        ayudaMenu.addAction(acercaDe)

      # ============== BARRA DE ESTADO (STATUSBAR) ===============

        labelVersion = QLabel(self)
        labelVersion.setText("Siacle versión beta: 1.0  ")

        hora = QTime.currentTime().toString("hh:mm:ss A ")

        self.labelHora = QLabel(self)
        self.labelHora.setText("Hora: {}".format(hora))

        statusBar = self.statusBar()
        statusBar.addPermanentWidget(self.labelHora, 1)
        statusBar.addPermanentWidget(labelVersion, 0)

        # Actualizar la hora cada segundo (1000 milisegundos)
        self.hora = QTimer(self)
        self.hora.setInterval(1000)
        self.hora.timeout.connect(self.Hora)
        self.hora.start()

  # ========================= FUNCIONES ==========================

    def Hora(self):
        hora = QTime.currentTime().toString("hh:mm:ss A ")
        self.labelHora.setText("Hora: {}".format(hora))

    def closeEvent(self, event):
        cerrar = QMessageBox(self)

        cerrar.setWindowTitle("¿Salir de Siacle?")
        cerrar.setIcon(QMessageBox.Question)
        cerrar.setText("¿Estás seguro que desea cerrar Siacle?   ")
        botonSalir = cerrar.addButton("Salir", QMessageBox.YesRole)
        botonCancelar = cerrar.addButton("Cancelar", QMessageBox.NoRole)
            
        cerrar.exec_()
            
        if cerrar.clickedButton() == botonSalir:
            event.accept()
        else:
            event.ignore()
        
                                
# ===============================================================           

if __name__ == "__main__":

    import sys

    aplicacion = QApplication(sys.argv)

    traductor = QTranslator(aplicacion)
    lugar = QLocale.system().name()
    path = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    traductor.load("qtbase_%s" % lugar, path)
    aplicacion.installTranslator(traductor)

    fuente = QFont()
    fuente.setPointSize(10)
    aplicacion.setFont(fuente)

    ventana = Siacle()
    ventana.showMaximized()

    sys.exit(aplicacion.exec_())
