# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       visorImagenes.py
# Autor:        Miguel Andres Garcia Niño
# Creado:       15 de Noviembre 2018
# Modificado:   15 de Noviembre 2018
# Copyright:    (c) 2018 by Miguel Andres Garcia Niño, 2018
# License:      Apache License 2.0
# ----------------------------------------------------------------------------

__nombre__ = "Vima"
__versión__ = "1.0"

"""
El módulo *visorImagenes* permite seleccionar una imagen (png, jpg, ico, bmp) y
visualizarla, e igualmente visualizar las demás imágenes que se encuentren en la
carpeta de la imagen seleccionada.
"""

# Versión Python: 3.6.0
# Versión PyQt5: 5.11.3

from random import randint

from PyQt5.QtGui import QIcon, QFont, QPalette, QImage, QPixmap
from PyQt5.QtCore import (Qt, QDir, QFile, QFileInfo, QPropertyAnimation, QRect,
                          QAbstractAnimation, QTranslator, QLocale, QLibraryInfo)
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton, QMessageBox,
                             QFrame, QLabel, QFileDialog)


# ========================= CLASE Widgets ==========================

class Widgets(QWidget):
    def __init__(self, parent=None):
        super(Widgets, self).__init__(parent)

        self.parent = parent
        
        self.initUI()

    def initUI(self):

      # ======================== WIDGETS ===========================

        framePrincipal = QFrame(self)
        framePrincipal.setFrameShape(QFrame.Box)
        framePrincipal.setFrameShadow(QFrame.Sunken)
        framePrincipal.setAutoFillBackground(True)
        framePrincipal.setBackgroundRole(QPalette.Light)
        framePrincipal.setFixedSize(662, 503)
        framePrincipal.move(10, 10)

        frame = QFrame(framePrincipal)
        frame.setFixedSize(640, 480)
        frame.move(10, 10)

        self.labelImagen = QLabel(frame)
        self.labelImagen.setAlignment(Qt.AlignCenter)
        self.labelImagen.setGeometry(0, 0, 640, 480)
        # self.labelImagen.setScaledContents(True)

        self.labelImagenUno = QLabel(frame)
        self.labelImagenUno.setAlignment(Qt.AlignCenter)
        self.labelImagenUno.setGeometry(-650, 0, 640, 480)

      # =================== BOTONES (QPUSHBUTTON) ==================

        self.buttonCargar = QPushButton("Cargar imagen", self)
        self.buttonCargar.setCursor(Qt.PointingHandCursor)
        self.buttonCargar.setFixedSize(325, 30)
        self.buttonCargar.move(10, 519)

        self.buttonEliminar = QPushButton("Eliminar imagen", self)
        self.buttonEliminar.setCursor(Qt.PointingHandCursor)
        self.buttonEliminar.setFixedSize(255, 30)
        self.buttonEliminar.move(345, 519)
        
        self.buttonAnterior = QPushButton("<", self)
        self.buttonAnterior.setObjectName("Anterior")
        self.buttonAnterior.setToolTip("Imagen anterior")
        self.buttonAnterior.setCursor(Qt.PointingHandCursor)
        self.buttonAnterior.setFixedSize(30, 30)
        self.buttonAnterior.move(607, 519)
        
        self.buttonSiguiente = QPushButton(">", self)
        self.buttonSiguiente.setObjectName("Siguiente")
        self.buttonSiguiente.setToolTip("Imagen siguiente")
        self.buttonSiguiente.setCursor(Qt.PointingHandCursor)
        self.buttonSiguiente.setFixedSize(30, 30)
        self.buttonSiguiente.move(642, 519)

      # ===================== CONECTAR SEÑALES =====================

        self.buttonCargar.clicked.connect(self.Cargar)
        self.buttonEliminar.clicked.connect(self.Eliminar)
        self.buttonAnterior.clicked.connect(self.anteriorSiguiente)
        self.buttonSiguiente.clicked.connect(self.anteriorSiguiente)

        # Establecer los valores predeterminados
        self.posicion = int
        self.estadoAnterior, self.estadoSiguiente = False, False
        self.carpetaActual = QDir()
        self.imagenesCarpeta = []

  # ======================= FUNCIONES ==============================

    def bloquearBotones(self, bool):
        self.buttonCargar.setEnabled(bool)
        self.buttonEliminar.setEnabled(bool)
        self.buttonAnterior.setEnabled(bool)
        self.buttonSiguiente.setEnabled(bool)

    def Mostrar (self, label, imagen, nombre, posicionX=650):
        imagen = QPixmap.fromImage(imagen)

        # Escalar imagen a 640x480 si el ancho es mayor a 640 o el alto mayor a 480
        if imagen.width() > 640 or imagen.height() > 480:
            imagen = imagen.scaled(640, 480, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Mostrar imagen
        label.setPixmap(imagen)

        # Animación (al finalizar la animación se muestra en la barra de estado el nombre y la extensión de la imagen
        # y se desbloquean los botones).       
        self.animacionMostar = QPropertyAnimation(label, b"geometry")
        self.animacionMostar.finished.connect(lambda: (self.parent.statusBar.showMessage(nombre),
                                                       self.bloquearBotones(True)))
        self.animacionMostar.setDuration(200)
        self.animacionMostar.setStartValue(QRect(posicionX, 0, 640, 480))
        self.animacionMostar.setEndValue(QRect(0, 0, 640, 480))
        self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

    def Limpiar(self, labelConImagen, labelMostrarImagen, imagen, nombre,
                posicionInternaX, posicionX=None):

        def Continuar(estado):
            if estado:
                if posicionX:
                    self.Mostrar(labelMostrarImagen, imagen, nombre, posicionX)
                else:
                    self.Mostrar(labelMostrarImagen, imagen, nombre)
            
        self.animacionLimpiar = QPropertyAnimation(labelConImagen, b"geometry")
        self.animacionLimpiar.finished.connect(lambda: labelConImagen.clear())
        self.animacionLimpiar.setDuration(200)
        # self.animacionLimpiar.valueChanged.connect(lambda x: print(x))
        self.animacionLimpiar.stateChanged.connect(Continuar)
        self.animacionLimpiar.setStartValue(QRect(0, 0, 640, 480))
        self.animacionLimpiar.setEndValue(QRect(posicionInternaX, 0, 640, 480))
        self.animacionLimpiar.start(QAbstractAnimation.DeleteWhenStopped)

    def Cargar(self):
        nombreImagen, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen",
                                                      QDir.currentPath(),
                                                      "Archivos de imagen (*.jpg *.png *.ico *.bmp)")

        if nombreImagen:
            # Verificar que QLabel tiene imagen
            labelConImagen = ""
            if self.labelImagen.pixmap():
                labelConImagen = self.labelImagen
            elif self.labelImagenUno.pixmap():
                labelConImagen = self.labelImagenUno
                
            imagen = QImage(nombreImagen)
            if imagen.isNull():
                if labelConImagen:
                    self.Eliminar()
                    
                QMessageBox.information(self, "Visor de imágenes",
                                        "No se puede cargar %s." % nombreImagen)
                return
            
            # Obtener ruta de la carpeta que contiene la imagen seleccionada
            self.carpetaActual = QDir(QFileInfo(nombreImagen).absoluteDir().path())

            # Obtener la ruta y el nombre de las imagenes que se encuentren en la carpeta de
            # la imagen seleccionada
            imagenes = self.carpetaActual.entryInfoList(["*.jpg", "*.png", "*.ico", "*.bmp"],
                                                        QDir.Files, QDir.Name)
            self.imagenesCarpeta = [imagen.absoluteFilePath() for imagen in imagenes]

            self.posicion = self.imagenesCarpeta.index(nombreImagen)
            self.estadoAnterior = True if self.posicion == 0 else False
            self.estadoSiguiente = True if self.posicion == len(self.imagenesCarpeta)-1 else False

            # Función encargada de bloquear o desbloquear los botones
            self.bloquearBotones(False)

            # Nombre y extensión de la imagen
            nombre = QFileInfo(nombreImagen).fileName()
            
            if labelConImagen:
                posicionInternaX = -650
                labelMostrarImagen = self.labelImagen if self.labelImagenUno.pixmap() else self.labelImagenUno
                self.Limpiar(labelConImagen, labelMostrarImagen, imagen, nombre, posicionInternaX)
            else:
                self.Mostrar(self.labelImagen, imagen, nombre)

    def Eliminar(self):
        def establecerValores():
            labelConImagen.clear()
            labelConImagen.move(0, 0)

            # Limpiar la barra de estado
            self.parent.statusBar.clearMessage()

            # Establecer los valores predeterminados
            self.posicion = int
            self.estadoAnterior, self.estadoSiguiente = False, False
            self.carpetaActual = QDir()
            self.imagenesCarpeta.clear()

            self.bloquearBotones(True)
            
        # Verificar que QLabel tiene imagen
        labelConImagen = ""
        if self.labelImagen.pixmap():
            labelConImagen = self.labelImagen
        elif self.labelImagenUno.pixmap():
            labelConImagen = self.labelImagenUno
                
        if labelConImagen:
            self.bloquearBotones(False)
            
            self.animacionEliminar = QPropertyAnimation(labelConImagen, b"geometry")
            self.animacionEliminar.finished.connect(establecerValores)
            self.animacionEliminar.setDuration(200)
            self.animacionEliminar.setStartValue(QRect(0, 0, 640, 480))
            self.animacionEliminar.setEndValue(QRect(-650, 0, 640, 480))
            self.animacionEliminar.start(QAbstractAnimation.DeleteWhenStopped)

    def anteriorSiguiente(self):
        if self.imagenesCarpeta:
            widget = self.sender().objectName()
            
            if widget == "Anterior":
                self.estadoAnterior = True if self.posicion == 0 else False
                self.estadoSiguiente = False
                    
                self.posicion -= 1 if self.posicion > 0 else 0
                posicionInternaX, posicionX = 650, -650 
            else:
                self.estadoSiguiente = True if self.posicion == len(self.imagenesCarpeta)-1 else False
                self.estadoAnterior = False
                    
                self.posicion += 1 if self.posicion < len(self.imagenesCarpeta)-1 else 0
                posicionInternaX, posicionX = -650, 650 

            if self.estadoAnterior or self.estadoSiguiente:
                return
            else:
                imagen = self.imagenesCarpeta[self.posicion]

                # Verificar que la carpeta que contiene la imagene exista
                if not QDir(self.carpetaActual).exists():
                    self.Eliminar()
                    return
                elif not QFile.exists(imagen):
                    # Obtener la ruta y el nombre de las imagenes que se encuentren en la
                    # carpeta de la imagen seleccionada
                    imagenes = self.carpetaActual.entryInfoList(["*.jpg", "*.png", "*.ico", "*.bmp"],
                                                                QDir.Files, QDir.Name)

                    if not imagenes:
                        self.Eliminar()
                        return
                    
                    self.imagenesCarpeta = [imagen.absoluteFilePath() for imagen in imagenes]

                    self.posicion = randint(0, len(self.imagenesCarpeta)-1)
                    self.estadoAnterior = True if self.posicion == 0 else False
                    self.estadoSiguiente = True if self.posicion == len(self.imagenesCarpeta)-1 else False
                elif QImage(imagen).isNull():
                    del self.imagenesCarpeta[self.posicion]

                    if not self.imagenesCarpeta:
                        self.Eliminar()
                        return

                    self.posicion = randint(0, len(self.imagenesCarpeta)-1)
                    self.estadoAnterior = True if self.posicion == 0 else False
                    self.estadoSiguiente = True if self.posicion == len(self.imagenesCarpeta)-1 else False

                imagen = self.imagenesCarpeta[self.posicion]

                if self.labelImagen.pixmap():
                    labelConImagen = self.labelImagen
                elif self.labelImagenUno.pixmap():
                    labelConImagen = self.labelImagenUno

                # Función encargada de bloquear o desbloquear los botones
                self.bloquearBotones(False)

                # Nombre y extensión de la imagen
                nombre = QFileInfo(imagen).fileName()

                # Label en el que se va a mostrar la imagen
                labelMostrarImagen = self.labelImagen if self.labelImagenUno.pixmap() else self.labelImagenUno

                # Quitar la imagen actual y mostrar la siguiente
                self.Limpiar(labelConImagen, labelMostrarImagen, QImage(imagen),
                             nombre, posicionInternaX, posicionX)


# ====================== CLASE visorImagenes =======================

class visorImagenes(QMainWindow):
    def __init__(self, parent=None):
        super(visorImagenes, self).__init__(parent)

        self.setWindowIcon(QIcon("Qt.png"))
        self.setWindowTitle("Visor de imagenes en PyQt5 por: ANDRES NIÑO")
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(682, 573)

        self.initUI()

    def initUI(self):

      # ===================== LLAMAR WIDGETS =======================
      
        widget = Widgets(self)
        self.setCentralWidget(widget)

      # =============== BARRA DE ESTADO (STATUSBAR) ================

        labelVersion = QLabel(self)
        labelVersion.setText(" Vima versión beta: 1.0  ")

        self.statusBar = self.statusBar()
        self.statusBar.addPermanentWidget(labelVersion, 0)
            

# ==================================================================

if __name__ == '__main__':
    
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
    
    ventana = visorImagenes()
    ventana.show()
    
    sys.exit(aplicacion.exec_())
