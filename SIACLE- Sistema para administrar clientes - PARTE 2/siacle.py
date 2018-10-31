# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       siacle.py
# Autor:        Miguel Andres Garcia Niño
# Creado:       30 de Octubre 2018
# Modificado:   30 de Octubre 2018
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

from PyQt5.QtGui import QFont, QIcon, QPalette, QBrush, QColor, QPixmap, QRegion, QClipboard
from PyQt5.QtCore import (Qt, QFile, QTime, QSize, QTimer, QRect, QTranslator, QLocale,
                          QLibraryInfo)
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QDialog, QPushButton, QMenu,
                             QTableWidget, QTableWidgetItem, QAbstractItemView, QLineEdit,
                             QActionGroup, QAction, QMessageBox, QFrame, QStyle, QGridLayout,
                             QVBoxLayout, QHBoxLayout, QLabel, QToolButton)


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

        labelAcerca = QLabel("SIACLE: sistema para administrar clientes, diseñado y\ndesarrollado "
                             "por ANDRES NIÑO con fines educativos.", self)
        labelAcerca.move(10, 460)

        botonCerrar = QPushButton("Cerrar", self)
        botonCerrar.setFixedSize(80, 32)
        botonCerrar.move(360, 457)

      # ========================= EVENTO =========================

        botonCerrar.clicked.connect(self.close)


# ========================= CLASE Boton ============================

class Boton(QToolButton):
    def __init__(self, parent=None):
        super(Boton, self).__init__(parent)

        self.setMask(QRegion(QRect(2, 2, 220, 36), QRegion.Rectangle))
        self.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.setIconSize(QSize(26, 26))
        self.setIcon(QIcon("Imagenes/Qt.png"))
        self.setFixedSize(224, 40)


# ========================= CLASE Widgets ==========================

class Widgets(QWidget):
    def __init__(self, parent=None):
        super(Widgets, self).__init__(parent)

        self.initUI()

    def initUI(self):

        fuenteSiacle = self.font()
        fuenteSiacle.setBold(True)
        fuenteSiacle.setPointSize(12)

      # ================= FRAME PANEL DE CONTROL ===================

        paletaBotones = self.palette()
        paletaBotones.setColor(QPalette.Background, QColor("#2EFEC8"))

        frameBotones = QFrame()
        frameBotones.setFrameStyle(QFrame.NoFrame)
        frameBotones.setAutoFillBackground(True)
        frameBotones.setPalette(paletaBotones)
        frameBotones.setFixedWidth(220)

      # ============================================================

        paletaPanel = self.palette()
        paletaPanel.setBrush(QPalette.Background, QBrush(QColor(255, 90, 0), Qt.SolidPattern))
        paletaPanel.setColor(QPalette.Foreground, Qt.white)

        labelSiacle = QLabel("PANEL DE CONTROL", frameBotones)
        labelSiacle.setAlignment(Qt.AlignCenter)
        labelSiacle.setFont(fuenteSiacle)
        labelSiacle.setAutoFillBackground(True)
        labelSiacle.setPalette(paletaPanel)
        labelSiacle.setFixedSize(220, 46)
        labelSiacle.move(0, 0)

      # ============================================================

        botonNuevo = Boton(frameBotones)
        botonNuevo.setText(" Nuevo")
        botonNuevo.setToolTip("Nuevo cliente")
        botonNuevo.setCursor(Qt.PointingHandCursor)
        botonNuevo.move(-2, 45)

        botonActualizar = Boton(frameBotones)
        botonActualizar.setText(" Actualizar")
        botonActualizar.setToolTip("Actualizar cliente")
        botonActualizar.setCursor(Qt.PointingHandCursor)
        botonActualizar.move(-2, 82)

        botonEliminar = Boton(frameBotones)
        botonEliminar.setText(" Eliminar")
        botonEliminar.setToolTip("Eliminar cliente")
        botonEliminar.setCursor(Qt.PointingHandCursor)
        botonEliminar.move(-2, 119)

        botonLimpiar = Boton(frameBotones)
        botonLimpiar.setText(" Limpiar tabla")
        botonLimpiar.setToolTip("Limpiar tabla")
        botonLimpiar.setCursor(Qt.PointingHandCursor)
        botonLimpiar.move(-2, 156)

      # ============================================================

        paletaSuscribete = self.palette()
        paletaSuscribete.setBrush(QPalette.Background, QBrush(QColor(135, 206, 250),
                                                              Qt.SolidPattern))

        fuenteSuscribete = self.font()
        fuenteSuscribete.setBold(True)
        fuenteSuscribete.setFamily("Arial")
        fuenteSuscribete.setPointSize(11)

        labelSuscribete = QLabel("<a href='https://www.youtube.com/c/AndresNiñoPython?"
                                 "sub_confirmation=1'>SUSCRIBETE.</a>", frameBotones)
        labelSuscribete.setAlignment(Qt.AlignCenter)
        labelSuscribete.setOpenExternalLinks(True)
        labelSuscribete.setFont(fuenteSuscribete)
        labelSuscribete.setAutoFillBackground(True)
        labelSuscribete.setPalette(paletaSuscribete)
        labelSuscribete.setFixedSize(220, 46)
        labelSuscribete.move(0, 210)

      # ============ FRAME BIENVENIDO - CONFIGURACIÓN ==============

        paletaFrame = self.palette()
        paletaFrame.setColor(QPalette.Background, QColor("blue"))

        frameBienvenido = QFrame()
        frameBienvenido.setFrameStyle(QFrame.NoFrame)
        frameBienvenido.setAutoFillBackground(True)
        frameBienvenido.setPalette(paletaFrame)
        frameBienvenido.setFixedHeight(46)

      # ============================================================

        paletaTitulo = self.palette()
        paletaTitulo.setColor(QPalette.Foreground, Qt.yellow)

        labelBienvenido = QLabel("BIENVENIDO A SIACLE")
        labelBienvenido.setAlignment(Qt.AlignCenter)
        labelBienvenido.setFont(fuenteSiacle)
        labelBienvenido.setPalette(paletaTitulo)

        botonConfiguracion = QPushButton()
        botonConfiguracion.setIcon(QIcon("Imagenes/configuracion.png"))
        botonConfiguracion.setIconSize(QSize(24, 24))
        botonConfiguracion.setToolTip("Configurar Siacle")
        botonConfiguracion.setCursor(Qt.PointingHandCursor)
        botonConfiguracion.setFixedWidth(36)

      # Primero, creamos los widgets que queremos en el diseño. Luego, creamos el
      # objeto QHBoxLayout y agregamos los widgets en el diseño. Finalmente, llamamos
      # a QWidget.setLayout(diseño) para instalar el objeto QHBoxLayout en el widget.

        disenioFrame = QHBoxLayout()
        disenioFrame.addWidget(labelBienvenido, Qt.AlignCenter)
        disenioFrame.addStretch()
        disenioFrame.addWidget(botonConfiguracion)
        disenioFrame.setContentsMargins(0, 0, 5, 0)

        frameBienvenido.setLayout(disenioFrame)

      # ============================================================

        self.buscarLineEdit = QLineEdit()
        self.buscarLineEdit.setObjectName("Enter")
        self.buscarLineEdit.setPlaceholderText("Nombre del cliente")
        self.buscarLineEdit.setMinimumSize(200, 26)

        botonBuscar = QPushButton("Buscar")
        botonBuscar.setObjectName("Buscar")
        botonBuscar.setCursor(Qt.PointingHandCursor)
        botonBuscar.setMinimumSize(60, 26)

        separadorTodos = QFrame()
        separadorTodos.setFrameShape(QFrame.VLine)
        separadorTodos.setFrameShadow(QFrame.Raised)
        separadorTodos.setFixedSize(1, 26)

        botonTodos = QPushButton("Todos")
        botonTodos.setObjectName("Todos")
        botonTodos.setCursor(Qt.PointingHandCursor)
        botonTodos.setMinimumSize(60, 26)

        nombreColumnas = ("Id", "Nombre", "Apellido", "Sexo", "Fecha de nacimiento", "País",
                          "Teléfono o celular")

        menuMostrarOcultar = QMenu()
        for indice, columna in enumerate(nombreColumnas, start=0):
            accion = QAction(columna, menuMostrarOcultar)
            accion.setCheckable(True)
            accion.setChecked(True)
            accion.setData(indice)

            menuMostrarOcultar.addAction(accion)

        botonMostrarOcultar = QPushButton("Motrar/ocultar columnas")
        botonMostrarOcultar.setCursor(Qt.PointingHandCursor)
        botonMostrarOcultar.setMenu(menuMostrarOcultar)
        botonMostrarOcultar.setMinimumSize(180, 26)

      # Crear el objeto QHBoxLayout y agregar los widgets en el diseño.
      
        disenioBuscar = QHBoxLayout()
        disenioBuscar.setSpacing(10)
        disenioBuscar.addWidget(self.buscarLineEdit)
        disenioBuscar.addWidget(botonBuscar)
        disenioBuscar.addWidget(separadorTodos)
        disenioBuscar.addWidget(botonTodos)
        disenioBuscar.addWidget(botonMostrarOcultar)

      # =================== WIDGET  QTableWidget ===================
      
        self.tabla = QTableWidget()

        # Deshabilitar edición
        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Deshabilitar el comportamiento de arrastrar y soltar
        self.tabla.setDragDropOverwriteMode(False)

        # Seleccionar toda la fila
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Seleccionar una fila a la vez
        self.tabla.setSelectionMode(QAbstractItemView.SingleSelection)

        # Especifica dónde deben aparecer los puntos suspensivos "..." cuando se muestran
        # textos que no encajan
        self.tabla.setTextElideMode(Qt.ElideRight)# Qt.ElideNone

        # Establecer el ajuste de palabras del texto 
        self.tabla.setWordWrap(False)

        # Deshabilitar clasificación
        self.tabla.setSortingEnabled(False)

        # Establecer el número de columnas
        self.tabla.setColumnCount(7)

        # Establecer el número de filas
        self.tabla.setRowCount(0)

        # Alineación del texto del encabezado
        self.tabla.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|
                                                          Qt.AlignCenter)

        # Deshabilitar resaltado del texto del encabezado al seleccionar una fila
        self.tabla.horizontalHeader().setHighlightSections(False)

        # Hacer que la última sección visible del encabezado ocupa todo el espacio disponible
        self.tabla.horizontalHeader().setStretchLastSection(True)

        # Ocultar encabezado vertical
        self.tabla.verticalHeader().setVisible(False)

        # Dibujar el fondo usando colores alternados
        self.tabla.setAlternatingRowColors(True)

        # Establecer altura de las filas
        self.tabla.verticalHeader().setDefaultSectionSize(20)
        
        # self.tabla.verticalHeader().setHighlightSections(True)

        # Establecer las etiquetas de encabezado horizontal usando etiquetas
        self.tabla.setHorizontalHeaderLabels(nombreColumnas)
        
        # Menú contextual
        self.tabla.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tabla.customContextMenuRequested.connect(self.menuContextual)
        
        # Establecer ancho de las columnas
        for indice, ancho in enumerate((80, 240, 240, 140, 150, 130), start=0):
            self.tabla.setColumnWidth(indice, ancho)

      # ============================================================

        disenioBuscarTabla = QVBoxLayout()
        disenioBuscarTabla.addLayout(disenioBuscar)
        disenioBuscarTabla.addWidget(self.tabla)
        disenioBuscarTabla.setSpacing(8)
        disenioBuscarTabla.setContentsMargins(10, 10, 10, 0)

      # ===================== LAYOUT DERECHO =======================

        disenioDerecho = QVBoxLayout()
        disenioDerecho.addWidget(frameBienvenido)
        disenioDerecho.addLayout(disenioBuscarTabla)
        disenioDerecho.setContentsMargins(0, 0, 0, 0)

      # ====================== LAYOUT FINAL ======================
        
        disenioFinal = QGridLayout()
        disenioFinal.addWidget(frameBotones, 0, 0)
        disenioFinal.addLayout(disenioDerecho, 0, 1)
        disenioFinal.setSpacing(0)
        disenioFinal.setContentsMargins(0, 0, 0, 0)
        
        self.setLayout(disenioFinal)

      # ========= GUARDAR INFORMACIÓN EN EL PORTAPAPELES =========

        self.copiarInformacion = QApplication.clipboard()

  # ======================== FUNCIONES ===========================

    def menuContextual(self, posicion):
        indices = self.tabla.selectedIndexes()

        if indices:
            menu = QMenu()

            itemsGrupo = QActionGroup(self)
            itemsGrupo.setExclusive(True)
            
            menu.addAction(QAction("Copiar todo", itemsGrupo))

            columnas = [self.tabla.horizontalHeaderItem(columna).text()
                        for columna in range(self.tabla.columnCount())
                        if not self.tabla.isColumnHidden(columna)]

            copiarIndividual = menu.addMenu("Copiar individual") 
            for indice, item in enumerate(columnas, start=0):
                accion = QAction(item, itemsGrupo)
                accion.setData(indice)
                
                copiarIndividual.addAction(accion)

            itemsGrupo.triggered.connect(self.copiarTableWidgetItem)
            
            menu.exec(self.tabla.viewport().mapToGlobal(posicion))

    def copiarTableWidgetItem(self, accion):
        filaSeleccionada = [dato.text() for dato in self.tabla.selectedItems()]
            
        if accion.text() == "Copiar todo":
            filaSeleccionada = tuple(filaSeleccionada)
        else:
            filaSeleccionada = filaSeleccionada[accion.data()]

        self.copiarInformacion.clear(mode = QClipboard.Clipboard)
        self.copiarInformacion.setText(str(filaSeleccionada), QClipboard.Clipboard)


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

      # =================== LLAMAR WIDGETS =======================
      
        self.widgets = Widgets(self)
        self.setCentralWidget(self.widgets)

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
