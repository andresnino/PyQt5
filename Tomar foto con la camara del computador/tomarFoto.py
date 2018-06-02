# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       tomarFoto.py
# Autor:        Miguel Andres Garcia Niño
# Creado:       01 de Junio 2018
# Modificado:   01 de Junio 2018
# Copyright:    (c) 2018 by Miguel Andres Garcia Niño, 2018
# License:      Apache License 2.0
# ----------------------------------------------------------------------------

__version__ = "1.0"

"""
El módulo *tomarFoto* permite seleccionar la camara que se va a utilizar, iniciarla,
detenerla, visualizar la interfaz, tomar fotos, guardarlas y/o eliminarlas.
"""

# Versión Python: 3.5.2
# Versión PyQt5: 5.10.1

from os import remove, getcwd

from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt, QByteArray, QFile, QByteArray, QIODevice, QBuffer
from PyQt5.QtMultimedia import QCamera, QCameraInfo, QCameraImageCapture
from PyQt5.QtMultimediaWidgets import QCameraViewfinder, QVideoWidget
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QWidget, QFileDialog,
                             QAction, QStyle, QActionGroup, QFrame, QLabel, QStackedWidget,
                             QMessageBox)


# ========================= CLASE Widgets ==========================

class Widgets(QWidget):
    def __init__(self, dispositivoCamara, parent=None):
        super(Widgets, self).__init__(parent)

        self.parent = parent

        self.estadoFoto = False
        self.byteArrayFoto = QByteArray()
        
      # ==========================================================

        frame = QFrame(self)
        frame.setFrameShape(QFrame.Box)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setFixedWidth(505)
        frame.setFixedHeight(380)
        frame.move(10, 10)

        # Instancias
        self.paginaVisor = QVideoWidget()
        self.paginaVisor.resize(500, 375)
        
        self.visor = QCameraViewfinder(self.paginaVisor)
        self.visor.resize(500, 375)

        self.labelFoto = QLabel()
        self.labelFoto.setAlignment(Qt.AlignCenter)
        self.labelFoto.resize(500, 375)

        # QStackedWidget
        self.stackedWidget = QStackedWidget(frame)
        self.stackedWidget.addWidget(self.paginaVisor)
        self.stackedWidget.addWidget(self.labelFoto)
        self.stackedWidget.resize(500, 375)
        self.stackedWidget.move(2, 2)

      # ======================== BOTONES =========================

        self.buttonTomarFoto = QPushButton("Tomar foto", self)
        self.buttonTomarFoto.resize(110, 26)
        self.buttonTomarFoto.move(525, 10)

        self.buttonEliminarFoto = QPushButton("Eliminar foto", self)
        self.buttonEliminarFoto.resize(110, 26)
        self.buttonEliminarFoto.move(525, 50)

        self.buttonGuardarFoto = QPushButton("Guardar foto", self)
        self.buttonGuardarFoto.resize(110, 26)
        self.buttonGuardarFoto.move(525, 82)

      # ======================== EVENTOS =========================
        
        self.buttonTomarFoto.clicked.connect(self.tomarFoto)
        self.buttonEliminarFoto.clicked.connect(self.eliminarFoto)
        self.buttonGuardarFoto.clicked.connect(self.guardarFoto)

      # ================== FUNCIONES AUTOMÁTICAS =================
      
        self.setCamara(dispositivoCamara)

  # ======================= FUNCIONES ============================

    def setCamara(self, dispositivoCamara):
        if dispositivoCamara.isEmpty():
            self.camara = QCamera()
        else:
            self.camara = QCamera(dispositivoCamara)

        self.camara.stateChanged.connect(self.actualizarEstadoCamara)

        self.capturaImagen = QCameraImageCapture(self.camara)

        self.camara.setViewfinder(self.visor)

        self.actualizarEstadoCamara(self.camara.state())
        
        self.capturaImagen.imageCaptured.connect(self.procesarImagenCapturada)
        self.capturaImagen.imageSaved.connect(self.imagenGuardada)

        self.camara.isCaptureModeSupported(QCamera.CaptureStillImage)

        self.camara.start()

        self.paginaVisor.update()

    def actualizarDispositivoCamara(self, action):
        self.setCamara(action.data())

    def actualizarEstadoCamara(self, estado):
        if estado == QCamera.ActiveState:
            self.parent.accionIniciarCamara.setEnabled(False)
            self.parent.accionDetenerCamara.setEnabled(True)

            if not self.estadoFoto:
                self.buttonTomarFoto.setEnabled(True)
                self.buttonEliminarFoto.setEnabled(False)
                self.buttonGuardarFoto.setEnabled(False)
        elif estado in (QCamera.UnloadedState, QCamera.LoadedState):
            self.parent.accionIniciarCamara.setEnabled(True)
            self.parent.accionDetenerCamara.setEnabled(False)

            if not self.estadoFoto:
                self.buttonTomarFoto.setEnabled(False)
                self.buttonEliminarFoto.setEnabled(False)
                self.buttonGuardarFoto.setEnabled(False)

    def iniciarCamara(self):
        self.camara.start()

    def detenerCamara(self):
        self.camara.stop()

    def tomarFoto(self):
        rutaFoto = "{}/fotoTemporal.jpg".format(getcwd())
        self.capturaImagen.capture(rutaFoto)

        self.estadoFoto = True

    def procesarImagenCapturada(self, requestId, imagen):
        foto = QPixmap.fromImage(imagen)
        
        buffer = QBuffer(self.byteArrayFoto)
        buffer.open(QIODevice.WriteOnly)
        buffer.close()
        foto.save(buffer, "PNG")
            
        fotoEscalada = foto.scaled(self.labelFoto.size())

        self.labelFoto.setPixmap(fotoEscalada)
        self.mostrarImagenCapturada()

    def visualizarVisor(self):
        self.stackedWidget.setCurrentIndex(0)

    def mostrarImagenCapturada(self):
        self.stackedWidget.setCurrentIndex(1)

        self.buttonTomarFoto.setEnabled(False)
        self.buttonEliminarFoto.setEnabled(True)
        self.buttonGuardarFoto.setEnabled(True)

    def imagenGuardada(self, id, nombreFoto):
        if QFile.exists(nombreFoto):
            remove(nombreFoto)

    def eliminarFoto(self):
        self.estadoFoto = False
        self.byteArrayFoto.clear()
        
        self.labelFoto.clear()

        self.actualizarEstadoCamara(self.camara.state())
        self.visualizarVisor()

    def guardarFoto(self):
        guardarComo, extension = QFileDialog.getSaveFileName(self, "Guardar como", "Foto",
                                                             "JPG (*.jpg);;PNG (*.png);;ICO (*.ico);;BMP (*.bmp)",
                                                             options=QFileDialog.Options())
                
        if guardarComo:
            foto = QPixmap()
            foto.loadFromData(self.byteArrayFoto, "PNG", Qt.AutoColor)
            foto.save(guardarComo, quality = 100)

            QMessageBox.information(self, "Guardar foto",
                                    "Foto guardada con éxito                                 ")

            self.eliminarFoto()


# ======================== CLASE tomarFoto =========================

class tomarFoto(QMainWindow):
    def __init__(self, parent = None):
        super(tomarFoto, self).__init__(parent)

        self.setWindowTitle("Tomar foto con PyQt5 por: ANDRES NIÑO")
        self.setWindowIcon(QIcon("Qt.png"))
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint |
                            Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(645, 420)

        self.initUI()

    def initUI(self):

      # ========================= MENÚ ===========================
        
        menu = self.menuBar()
        
        archivoMenu = menu.addMenu("&Archivo")
        self.accionIniciarCamara = archivoMenu.addAction(self.style().standardIcon(QStyle.SP_MediaPlay),
                                                         "Iniciar la camara", self.iniciarCamara)
        self.accionDetenerCamara = archivoMenu.addAction(self.style().standardIcon(QStyle.SP_MediaStop),
                                                         "Detener la camara", self.detenerCamara)
        archivoMenu.addAction(self.style().standardIcon(QStyle.SP_MessageBoxCritical), " Salir", self.close)

        dispositivosMenu = menu.addMenu("&Dispositivos")

        videoDevicesGroup = QActionGroup(self)
        videoDevicesGroup.setExclusive(True)

        dispositivoCamara = QByteArray()

        for nombreDispositivo in QCamera.availableDevices():
            descripcion = QCamera.deviceDescription(nombreDispositivo)
            videoDeviceAction = QAction(descripcion, videoDevicesGroup)
            videoDeviceAction.setCheckable(True)
            videoDeviceAction.setData(nombreDispositivo)

            if dispositivoCamara.isEmpty():
                dispositivoCamara = nombreDispositivo
                videoDeviceAction.setChecked(True)

            dispositivosMenu.addAction(videoDeviceAction)

        # Instancia del Widget central
        self.widgets = Widgets(dispositivoCamara, self)

        # Llamar función cuando se activa una Acción del Menú
        videoDevicesGroup.triggered.connect(self.widgets.actualizarDispositivoCamara)

        # Establecer el Widget central de la ventana
        self.setCentralWidget(self.widgets)

  # ======================= FUNCIONES ============================

    def iniciarCamara(self):
        self.widgets.iniciarCamara()

    def detenerCamara(self):
        self.widgets.detenerCamara()


# ===============================================================

if __name__ == '__main__':

    import sys
    
    aplicacion = QApplication(sys.argv)

    fuente = QFont("Bahnschrift Light")
    fuente.setPointSize(10)
    
    aplicacion.setFont(fuente)

    ventana = tomarFoto()
    ventana.show()

    sys.exit(aplicacion.exec_())
