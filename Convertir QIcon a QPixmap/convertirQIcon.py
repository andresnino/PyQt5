# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       convertirQIcon.py
# Autor:        Miguel Andres Garcia Niño
# Creado:       04 de Junio 2018
# Modificado:   04 de Junio 2018
# Copyright:    (c) 2018 by Miguel Andres Garcia Niño, 2018
# License:      Apache License 2.0
# ----------------------------------------------------------------------------

__version__ = "1.0"

"""
El módulo *convertirQIcon* permite convertir un QIcon a QPixmap y luego guardarlo en el
computador.
"""

# Versión Python: 3.5.2
# Versión PyQt5: 5.10.1

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (QApplication, QDialog, QComboBox, QStyle, QLineEdit, QPushButton,
                             QSizePolicy, QVBoxLayout)


# ==================== CLASE ventanaPrincipal ======================

class ventanaPrincipal(QDialog):
    def __init__(self, parent=None):
        super(ventanaPrincipal, self).__init__()

        self.setWindowIcon(QIcon("Qt.png"))
        self.setWindowTitle("Convertir QIcon a QPixmap en PyQt5 por: ANDRES NIÑO")
        self.resize(350, 350)

        self.initUI()

    def initUI(self):

      # ================ LISTA DE ICONOS ESTÁNDAR ================

        iconos = [
            "SP_TitleBarMinButton",
            "SP_TitleBarMenuButton",
            "SP_TitleBarMaxButton",
            "SP_TitleBarCloseButton",
            "SP_TitleBarNormalButton",
            "SP_TitleBarShadeButton",
            "SP_TitleBarUnshadeButton",
            "SP_TitleBarContextHelpButton",
            "SP_MessageBoxInformation",
            "SP_MessageBoxWarning",
            "SP_MessageBoxCritical",
            "SP_MessageBoxQuestion",
            "SP_DesktopIcon",
            "SP_TrashIcon",
            "SP_ComputerIcon",
            "SP_DriveFDIcon",
            "SP_DriveHDIcon",
            "SP_DriveCDIcon",
            "SP_DriveDVDIcon",
            "SP_DriveNetIcon",
            "SP_DirHomeIcon",
            "SP_DirOpenIcon",
            "SP_DirClosedIcon",
            "SP_DirIcon",
            "SP_DirLinkIcon",
            "SP_FileIcon",
            "SP_FileLinkIcon",
            "SP_FileDialogStart",
            "SP_FileDialogEnd",
            "SP_FileDialogToParent",
            "SP_FileDialogNewFolder",
            "SP_FileDialogDetailedView",
            "SP_FileDialogInfoView",
            "SP_FileDialogContentsView",
            "SP_FileDialogListView",
            "SP_FileDialogBack",
            "SP_DockWidgetCloseButton",
            "SP_ToolBarHorizontalExtensionButton",
            "SP_ToolBarVerticalExtensionButton",
            "SP_DialogOkButton",
            "SP_DialogCancelButton",
            "SP_DialogHelpButton",
            "SP_DialogOpenButton",
            "SP_DialogSaveButton",
            "SP_DialogCloseButton",
            "SP_DialogApplyButton",
            "SP_DialogResetButton",
            "SP_DialogDiscardButton",
            "SP_DialogYesButton",
            "SP_DialogNoButton",
            "SP_ArrowUp",
            "SP_ArrowDown",
            "SP_ArrowLeft",
            "SP_ArrowRight",
            "SP_ArrowBack",
            "SP_ArrowForward",
            "SP_CommandLink",
            "SP_VistaShield",
            "SP_BrowserReload",
            "SP_BrowserStop",
            "SP_MediaPlay",
            "SP_MediaStop",
            "SP_MediaPause",
            "SP_MediaSkipForward",
            "SP_MediaSkipBackward",
            "SP_MediaSeekForward",
            "SP_MediaSeekBackward",
            "SP_MediaVolume",
            "SP_MediaVolumeMuted",
            "SP_LineEditClearButton"
            ]

      # ======================= QCOMBOBOX ========================

        self.comboBox = QComboBox()

        for i in iconos:
            self.comboBox.addItem(self.style().standardIcon(getattr(QStyle, i)), i)

        self.comboBox.setCurrentIndex(-1)

      # ======================= QLINEEDIT ========================

        self.lineEdit = QLineEdit()

      # ================= BOTONES (QPUSHBUTTON) ==================
        
        self.button = QPushButton()
        self.button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.button.setAutoDefault(False)

        buttonDescargar = QPushButton("Descargar icono")
        buttonDescargar.setAutoDefault(False)

      # ==================== DISEÑO (LAYOUT) =====================

        disenio = QVBoxLayout()
        disenio.addWidget(self.comboBox)
        disenio.addWidget(self.lineEdit)
        disenio.addWidget(self.button)
        disenio.addWidget(buttonDescargar)

        self.setLayout(disenio)

      # ======================== EVENTOS =========================

        self.comboBox.activated[str].connect(self.Activado)
        buttonDescargar.clicked.connect(self.descargarIcono)

  # ======================= FUNCIONES ============================

    def Activado(self, texto):
        self.lineEdit.setText(texto)

        # self.style().standardIcon(QStyle.SP_TitleBarMenuButton)
        self.button.setIcon(self.style().standardIcon(getattr(QStyle, texto)))
        self.button.setIconSize(QSize(200, 200))

    def descargarIcono(self):
        nombre = self.comboBox.currentText()

        if nombre:
            icono = self.button.icon()
            print(type(icono))
            
            pixmap = icono.pixmap(200, 200, QIcon.Normal, QIcon.On)
            pixmap.save("{}.png".format(nombre), quality = 100)

            print("Icono descargado...")
        
        
# ================================================================

if __name__ == '__main__':

    import sys
    
    aplicacion = QApplication(sys.argv)

    dialogo = ventanaPrincipal()
    dialogo.show()

    sys.exit(aplicacion.exec_())
