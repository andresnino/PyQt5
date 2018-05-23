# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       QLineEdit.py
# Autor:        Miguel Andres Garcia Niño
# Creado:       22 de Mayo 2018
# Modificado:   22 de Mayo 2018
# Copyright:    (c) 2018 by Miguel Andres Garcia Niño, 2018
# License:      Apache License 2.0
# ----------------------------------------------------------------------------

__versión__ = "1.0"

"""
El módulo *QLineEdit* permite probar varias funciones públicas de un QLineEdit
y las señales que este widget emite.
"""

from PyQt5.QtGui import QIcon, QRegExpValidator, QFont
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit


# =================== CLASE ventanaPrincipal =======================

class ventanaPrincipal(QMainWindow):
    def __init__(self, parent=None):
        super(ventanaPrincipal, self).__init__(parent)
        
        self.setWindowTitle("QLineEdit en PyQt5 por: ANDRES NIÑO")
        self.setWindowIcon(QIcon("icono.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(400, 400)

        self.initUI()

    def initUI(self):

      # =================== WIDGET QLINEEDIT =====================

        self.lineEdit = QLineEdit(self)

        # ================== FUNCIONES PÚBLICAS ==================

        self.lineEdit.setGeometry(20, 20, 360, 24)
        self.lineEdit.setText("Andres Niño")
        # self.lineEdit.setAlignment(Qt.AlignLeft)
        # self.lineEdit.setClearButtonEnabled(True)
        # self.lineEdit.setCursorPosition(6)
        # self.lineEdit.home(True)
        # self.lineEdit.end(True)
        # self.lineEdit.setEchoMode(QLineEdit.Password)
        # self.lineEdit.setFrame(False)
        # self.lineEdit.setMaxLength(2)
        # self.lineEdit.setPlaceholderText("Andres Niño")
        # self.lineEdit.setReadOnly(True)
        # self.lineEdit.setSelection(3, 2)
        # self.lineEdit.selectAll()
        # self.lineEdit.deselect()
        # self.lineEdit.setTextMargins(10, 0, 6, 1)
        # self.lineEdit.setInputMask(">AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#")
        # self.lineEdit.setValidator(QRegExpValidator(QRegExp("[0-9]+")))
        # print(self.lineEdit.text())

        fuente = QFont()
        fuente.setPointSize(10)
        fuente.setCapitalization(QFont.Capitalize)
        
        self.lineEdit.setFont(fuente)

        # ======================= SEÑALES ========================
        
        # self.lineEdit.returnPressed.connect(lambda: print("Se presiono la tecla Enter..."))
        # self.lineEdit.textChanged.connect(lambda: print("El texto cambio..."))
        # self.lineEdit.textEdited.connect(lambda: print("El texto cambio..."))


# ================================================================

if __name__ == '__main__':
    
    import sys
    
    aplicacion = QApplication(sys.argv)
    
    ventana = ventanaPrincipal()
    ventana.show()
    
    sys.exit(aplicacion.exec_())
